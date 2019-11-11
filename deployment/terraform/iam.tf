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
resource "aws_iam_role_policy_attachment" "role-tagging-attach" {
  role       = aws_iam_role.AutoTaggingMachine.name
  policy_arn = aws_iam_policy.AllowTaggingAndLogging.arn
}