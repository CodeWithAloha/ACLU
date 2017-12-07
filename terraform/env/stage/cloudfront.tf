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

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 30 // Short TTL since we are using it for STAGE and CI/CD
    max_ttl                = 60 // Short TTL since we are using it for STAGE and CI/CD
  }

  price_class = "PriceClass_100" // Only availbale in US

  restrictions {
    geo_restriction {
      restriction_type = "whitelist"
      locations        = ["US"] // Only availbale in US
    }
  }

  viewer_certificate {
    acm_certificate_arn       = "${var.DOMAIN_CERTIFICATE_ARN}"
    ssl_support_method        = "sni-only"
    minimum_protocol_version  = "TLSv1"
  }
}

resource "aws_cloudfront_distribution" "backend_distribution" {
  origin {
    domain_name = "${aws_elb.aclu.dns_name}"
    origin_id   = "elb_backend_origin"

    custom_origin_config = {
      http_port               = 50050
      https_port              = 50050
      origin_protocol_policy  = "http-only"
      origin_ssl_protocols    = ["TLSv1", "TLSv1.1", "TLSv1.2"]
      origin_keepalive_timeout= 60
      origin_read_timeout     = 60
    }
  }

  enabled             = true
  is_ipv6_enabled     = true
  comment             = "CloudFront distribution with default SSL for backend"

  aliases = ["${var.API_DOMAIN}"]

  default_cache_behavior {
    allowed_methods  = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "elb_backend_origin"

    forwarded_values {
      query_string = true

      cookies {
        forward = "none"
      }

      headers = ["origin"]
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 10 // Short TTL since we are using it for STAGE and CI/CD
    max_ttl                = 30 // Short TTL since we are using it for STAGE and CI/CD
  }

  price_class = "PriceClass_100" // Only availbale in US

  restrictions {
    geo_restriction {
      restriction_type = "whitelist"
      locations        = ["US"] // Only availbale in US
    }
  }

  viewer_certificate {
    acm_certificate_arn       = "${var.DOMAIN_CERTIFICATE_ARN}"
    ssl_support_method        = "sni-only"
    minimum_protocol_version  = "TLSv1"
  }
}

