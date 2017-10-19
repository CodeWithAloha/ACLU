output "public_ip" {
  value = "${aws_eip.aclu.public_ip}"
}

output "ecr_url" {
  value = "${aws_ecr_repository.aclu.repository_url}"
}

output "frontend_domain" {
  value = "${aws_s3_bucket.frontend.website_endpoint}"
}