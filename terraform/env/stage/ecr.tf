resource "aws_ecr_repository" "aclu" {
  name = "${var.APP_NAME}"
}