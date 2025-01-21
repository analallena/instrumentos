data "aws_iam_policy_document" "s3-editor-policy-document" {

  statement {
    actions   = ["s3:GetObject", "s3:PutObject"]
    resources = [var.s3-bucket-arn]
    effect = "Allow"
  }
}

resource "aws_iam_policy" "s3EditorPolicy" {
  name        = "s3-editor-policy"
  description = "S3 Editor policy"

  policy = data.aws_iam_policy_document.s3-editor-policy-document.json
}

resource "aws_iam_group_policy_attachment" "aws_config_attach" {
  group      = var.s3-bucket-editor-group
  policy_arn = aws_iam_policy.s3EditorPolicy.arn
}
