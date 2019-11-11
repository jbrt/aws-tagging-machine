# Archive Lambda files
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "../../src/"
  output_path = "lambda.zip"
}

# Declare the AWS Lambda function
resource "aws_lambda_function" "AutoTaggingMachineFunction" {
  filename         = "lambda.zip"
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  function_name    = "AutoTaggingMachineFunction"
  description      = "This function will applied tags on new AWS resources"
  handler          = "handler.auto_tagging"
  runtime          = "python3.7"
  memory_size      = 128
  timeout          = 60
  role             = aws_iam_role.AutoTaggingMachine.arn
}

# Finally, allow the lambda function to be called by the CloudWatch rule
resource "aws_lambda_permission" "allow_cloudwatch" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.AutoTaggingMachineFunction.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.AutoTaggingMachineRule.arn
}

