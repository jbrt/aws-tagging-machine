variable "aws_region" {
  description = "The AWS region to create the resources"
  default     = "eu-west-1"
}

variable "log_retention" {
  description = "How many days logs will be retained"
  default     = 7
}