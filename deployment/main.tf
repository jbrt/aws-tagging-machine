# Define the AWS region
# By default, eu-west-1 but you can/must update this value
provider "aws" {
  region = "${var.aws_region}"
}

variable "aws_region" {
  description = "The AWS region to create the resources"
  default     = "eu-west-1"
}

# Declare the AWS Lambda function
resource "aws_lambda_function" "AutoTaggingMachineFunction" {
  function_name    = "AutoTaggingMachineFunction"
  description      = "This function will applied tags on new AWS resources"
  handler          = "handler.auto_tagging"
  runtime          = "python3.6"
  memory_size      = 128
  timeout          = 60
  role             = "${aws_iam_role.AutoTaggingMachine.arn}"
  filename         = "code.zip"
  source_code_hash = "${base64sha256(file("code.zip"))}"
}

# Create a new IAM Role for this function
resource "aws_iam_role" "AutoTaggingMachine" {
  name        = "AutoTaggingMachine"
  description = "Role used by the Auto Tagging Machine to apply tags"

  assume_role_policy = <<EOF
{
"Version": "2012-10-17",
"Statement": [
    {
    "Effect": "Allow",
    "Principal": {
        "Service": "lambda.amazonaws.com"
    },
    "Action": "sts:AssumeRole"
    }
]
}
EOF
}

# Define the policies that will be used for that role
resource "aws_iam_policy" "AllowTaggingAndLogging" {
  name        = "AllowTaggingAndLogging"
  description = "Policy used for the Lambda function AutoTaggingMachine"

  policy = <<EOF
{
"Version": "2012-10-17",
"Statement": [
    {
        "Action": [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
        ],
        "Resource": "arn:aws:logs:*:*:*",
        "Effect": "Allow"
    },
    {
        "Action": [
            "tag:TagResources",
            "dynamodb:TagResource",
            "ec2:CreateTags",
            "s3:PutBucketTagging",
            "s3:GetBucketTagging",
            "sqs:TagQueue"
        ],
        "Resource": "*",
        "Effect": "Allow"
    }
]
}
EOF
}

# Attach the policies to the IAM role
resource "aws_iam_role_policy_attachment" "test-attach" {
  role       = "${aws_iam_role.AutoTaggingMachine.name}"
  policy_arn = "${aws_iam_policy.AllowTaggingAndLogging.arn}"
}

# Declare a CloudWatch Event rule
resource "aws_cloudwatch_event_rule" "AutoTaggingMachineRule" {
  name        = "AutoTaggingMachineRule"
  description = "Send events to AutoTaggingMachine Lambda function"

  event_pattern = <<PATTERN
{
  "detail-type": [
    "AWS API Call via CloudTrail"
  ],
  "detail": {
    "eventSource": [
      "ec2.amazonaws.com",
      "dynamodb.amazonaws.com",
      "s3.amazonaws.com",
      "sqs.amazonaws.com"
    ],
    "eventName": [
      "RunInstances",
      "CreateBucket",
      "CreateImage",
      "CreateDhcpOptions",
      "CreateNetworkAcl",
      "CreateNetworkInterface",
      "CreateQueue",
      "CreateRouteTable",
      "CreateSecurityGroup",
      "CreateSnapshot",
      "CreateSubnet",
      "CreateTable",
      "CreateVolume",
      "CreateVpc",
      "CreateInternetGateway"
    ]
  },
  "source": [
    "aws.ec2",
    "aws.dynamodb",
    "aws.s3",
    "aws.sqs"
  ]
}
PATTERN
}

# Define a target for that rule (here, the lambda function previously created)
resource "aws_cloudwatch_event_target" "lambda_target" {
  rule      = "${aws_cloudwatch_event_rule.AutoTaggingMachineRule.name}"
  target_id = "SendEventToLambda"
  arn       = "${aws_lambda_function.AutoTaggingMachineFunction.arn}"
}

# Finally, allow the lambda function to be called by the CloudWatch rule
resource "aws_lambda_permission" "allow_cloudwatch" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.AutoTaggingMachineFunction.function_name}"
  principal     = "events.amazonaws.com"
  source_arn    = "${aws_cloudwatch_event_rule.AutoTaggingMachineRule.arn}"
}
