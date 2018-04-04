# Bucket to host front end site
resource "aws_s3_bucket" "frontend" {
  bucket = "${var.FRONT_END_BUCKET_NAME}"
  acl    = "public-read"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["PUT", "POST"]

    # TODO - This will change when we get a domain for website
    allowed_origins = ["https://hawaii.aclu.com"]
    expose_headers  = ["ETag"]
    max_age_seconds = 3000
  }

  tags = "${var.GLOBAL_TAGS}"
}

# Bucket to store builds
resource "aws_s3_bucket" "codepipeline_build_repository" {
  bucket = "aclu-builds"
  acl    = "private"

  tags = "${var.GLOBAL_TAGS}"
}
