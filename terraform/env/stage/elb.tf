resource "aws_elb" "aclu" {
  name               = "${var.APP_NAME}-elb"
  # TODO - Hack for AZs...use data instead
  availability_zones = ["${var.REGION}a", "${var.REGION}b", "${var.REGION}c"]

  listener {
    instance_port     = 50050
    instance_protocol = "http"
    lb_port           = 50050
    lb_protocol       = "https"
    ssl_certificate_id = "${var.ELB_CERTIFICATE_ARN}"
  }

  health_check {
    healthy_threshold   = 2
    unhealthy_threshold = 2
    timeout             = 20
    target              = "HTTP:50050/aloha"
    interval            = 30
  }

  instances                   = ["${aws_instance.aclu.id}"]
  cross_zone_load_balancing   = true
  idle_timeout                = 400
  connection_draining         = true
  connection_draining_timeout = 400

  tags = "${var.GLOBAL_TAGS}"
}