resource "aws_cloudfront_distribution" "frontend_distribution" {
  origin {
    domain_name = "${aws_s3_bucket.frontend.bucket_domain_name}"
    origin_id   = "s3_frontend_origin"

    # s3_origin_config {
    #   origin_access_identity = "origin-access-identity/cloudfront/ABCDEFG1234567"
    # }
  }

  enabled             = true
  is_ipv6_enabled     = true
  comment             = "CloudFront distribution with default SSL for frontend"
  default_root_object = "index.html"

  aliases = ["${var.DOMAIN}"]

  default_cache_behavior {
    allowed_methods  = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "s3_frontend_origin"

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "allow-all"
    min_ttl                = 0
    default_ttl            = 300 // Short TTL since we are using it for STAGE and CI/CD
    max_ttl                = 600 // Short TTL since we are using it for STAGE and CI/CD
  }

  price_class = "PriceClass_100" // Only availbale in US

  restrictions {
    geo_restriction {
      restriction_type = "whitelist"
      locations        = ["US"] // Only availbale in US
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }
}