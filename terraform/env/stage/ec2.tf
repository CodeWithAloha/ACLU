# Since leveraging ECS may be too cumbersome at this stage we will use an EC2 instance with docker installed for now

# Create an IAM role for the Web Servers.
resource "aws_iam_role" "instance_iam_role" {
  name = "${var.APP_NAME}-instance-role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowInstanceToAsumeRole",
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      }
    }
  ]
}
EOF
}

resource "aws_iam_instance_profile" "instance_profile" {
  name = "${var.APP_NAME}-instance-profile"
  role = "${aws_iam_role.instance_iam_role.id}"
}	

resource "aws_iam_role_policy" "instance_role_policy" {
  name = "${var.APP_NAME}-instance-role-policy"
  role = "${aws_iam_role.instance_iam_role.id}"
  # TODO - Restrict policy to specific ECR (receive ECR ARN from ecr.tf)
  # TODO - Restrict policy for cloudwatch writes
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowWriteLogsToCloudWatch",
      "Effect": "Allow",
      "Action": [
          "logs:*"
      ],
      "Resource": "*"
    }, {
      "Sid": "AllowPullDockerImageFromECR",
      "Effect": "Allow",
      "Action": [
        "ecr:*"
      ],
      "Resource": "*"
    }, {
      "Sid": "ManageArtifactsInBuildBucket",
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": [
        "${aws_s3_bucket.codepipeline_build_repository.arn}",
        "${aws_s3_bucket.codepipeline_build_repository.arn}/*"
      ]
    }, {
      "Sid": "AdminS3",
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": "*"
    }
  ]
}
EOF
}

# Admin Security Group
resource "aws_security_group" "aclu_admin_sg" {
  name        = "${var.APP_NAME}-admin-sg"
  description = "Admin SG for ACLU machines"

  lifecycle {
    create_before_destroy = true
  }

  # tags = "${merge(var.bastion_additional_tags,var.bastion_module_tags,map("Name","${var.bastion_resource_name_prepend}-${var.bastion_environment}"))}"
}

resource "aws_security_group_rule" "ssh_admin_sg_group_rule" {
  security_group_id = "${aws_security_group.aclu_admin_sg.id}"
  description       = "Allow SSH access from whitelisted ips"
  type              = "ingress"
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  
  # Create one rule per whitelisted ip
  cidr_blocks       = ["${element(var.ADMIN_CIDRS, count.index)}"]
  count             = "${length(var.ADMIN_CIDRS)}"
}

# Instance Security Group
resource "aws_security_group" "aclu_sg" {
  name        = "${var.APP_NAME}-sg"
  description = "SG for ACLU machines"

  lifecycle {
    create_before_destroy = true
  }

  # tags = "${merge(var.bastion_additional_tags,var.bastion_module_tags,map("Name","${var.bastion_resource_name_prepend}-${var.bastion_environment}"))}"
}

resource "aws_security_group_rule" "api_sg_group_rule" {
  security_group_id = "${aws_security_group.aclu_sg.id}"
  description       = "Allow all HTTP inbound for ACLU API"
  type              = "ingress"
  from_port         = 50050
  to_port           = 50050
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
}
resource "aws_security_group_rule" "ssl_sg_group_rule" {
  security_group_id = "${aws_security_group.aclu_sg.id}"
  description       = "Allow HTTPS for ACLU API"
  type              = "ingress"
  from_port         = 443
  to_port           = 443
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
}

# By default allow all outbound traffic...we can restrict this later

resource "aws_security_group_rule" "egress_sg_group_rule" {
  security_group_id = "${aws_security_group.aclu_sg.id}"
  description       = "Allow all outbound traffic from instance (for updates). We can restrict it later for PRDO if neccessary"
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks = ["0.0.0.0/0"]
  }

resource "aws_eip" "aclu" {
  instance = "${aws_instance.aclu.id}"
  vpc      = true
}

# TODO Refine CodeDeploy role
# TODO Add VPC (modularize stuff)
# We use a template_file to create the user-data script for the ec2 instance
# this is because the instance behavior depends on TF outputs such us ECR URL
data "template_file" "bootstrap_script" {
  template = "${file("../../../scripts/aws-ec2/bootstrap.tpl")}"
  
  vars {
    ECR_REGION        = "${var.REGION}"
    IMAGES_REPO_URL   = "${aws_ecr_repository.aclu.repository_url}"
    IMAGES_REPO_NAME  = "${aws_ecr_repository.aclu.name}"
  }
}

resource "aws_instance" "aclu" {
  ami                   = "ami-5dca1925" # Ubuntu 16.04 ami
  instance_type         = "t2.micro"
  user_data             = "${data.template_file.bootstrap_script.rendered}"
  key_name              = "${var.KEY_PAIR}"
  iam_instance_profile  = "${aws_iam_instance_profile.instance_profile.id}"
  security_groups       = ["${aws_security_group.aclu_sg.name}", "${aws_security_group.aclu_admin_sg.name}"]
  
  tags = "${var.GLOBAL_TAGS}"

  root_block_device = {
    volume_type = "gp2"
    volume_size = "30"
  }
}