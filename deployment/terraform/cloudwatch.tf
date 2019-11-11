# Declare a CloudWatch LogGroup
resource "aws_cloudwatch_log_group" "lg_take_snapshot" {
  name              = "/aws/lambda/${aws_lambda_function.AutoTaggingMachineFunction.function_name}"
  retention_in_days = var.log_retention
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
  rule      = aws_cloudwatch_event_rule.AutoTaggingMachineRule.name
  target_id = "SendEventToLambda"
  arn       = aws_lambda_function.AutoTaggingMachineFunction.arn
}