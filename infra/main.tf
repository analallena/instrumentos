provider "aws" {
  region = "eu-west-1"
}

resource "aws_s3_bucket" "instruments-raffle" {
  bucket = "instruments-raffle"

  tags = {
    Name        = "My instruments bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_object" "instrument-list" {
  bucket = "${aws_s3_bucket.instruments-raffle.id}"
  key    = "general-data/instruments.csv"
  source = "../s3_bucket_data/instruments.csv"

  # The filemd5() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the md5() function and the file() function:
  # etag = "${md5(file("path/to/file"))}"
  etag = filemd5("../s3_bucket_data/instruments.csv")
}

resource "aws_s3_object" "students-1eso-A" {
  bucket = "${aws_s3_bucket.instruments-raffle.id}"
  key    = "general-data/students_1ESO_A.csv"
  source = "../s3_bucket_data/students_1ESO_A.csv"

  # The filemd5() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the md5() function and the file() function:
  # etag = "${md5(file("path/to/file"))}"
  etag = filemd5("../s3_bucket_data/students_1ESO_A.csv")
}

# IAM role for Lambda execution
resource "aws_iam_role" "lambda_exec_role" {
  name = "lambda_execution_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# Attach AWSLambdaBasicExecutionRole policy for CloudWatch logging
resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = aws_iam_role.lambda_exec_role.name
}

# Attach AmazonS3ReadOnlyAccess policy for S3 read-only access
resource "aws_iam_role_policy_attachment" "lambda_s3_readonly" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
  role       = aws_iam_role.lambda_exec_role.name
}

# Create a zip file of the Lambda function
data "archive_file" "lambda" {
  type        = "zip"
  source_file = "../lambda.py"
  output_path = "lambda_function.zip"
}

# Lambda function resource
resource "aws_lambda_function" "example_lambda" {
  filename      = data.archive_file.lambda.output_path
  function_name = "example_lambda_function"
  role          = aws_iam_role.lambda_exec_role.arn
  handler       = "lambda.lambda_handler"
  runtime       = "python3.9"

  source_code_hash = data.archive_file.lambda.output_base64sha256
}

# CloudWatch Log Group for Lambda
resource "aws_cloudwatch_log_group" "lambda_log_group" {
  name              = "/aws/lambda/${aws_lambda_function.example_lambda.function_name}"
  retention_in_days = 14
}

