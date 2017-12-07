output "API_URL" {
  value = "${var.API_DOMAIN}"
}

output "ECR_URL" {
  value = "${aws_ecr_repository.aclu.repository_url}"
}

output "ECR_REPO_NAME" {
  value = "${aws_ecr_repository.aclu.name}"
}

output "FRONTEND_DOMAIN" {
  value = "${aws_cloudfront_distribution.frontend_distribution.domain_name}"
  }

