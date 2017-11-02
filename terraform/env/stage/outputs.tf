output "API_IP" {
  value = "${aws_eip.aclu.public_ip}"
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

