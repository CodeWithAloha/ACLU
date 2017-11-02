output "public_ip" {
  value = "${aws_eip.aclu.public_ip}"
}

output "ecr_url" {
  value = "${aws_ecr_repository.aclu.repository_url}"
}

output "ecr_repo_name" {
  value = "${aws_ecr_repository.aclu.name}"
}

output "frontend_domain" {
  value = "${aws_cloudfront_distribution.frontend_distribution.domain_name}"
  }

