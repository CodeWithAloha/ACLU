# Since leveraging ECS may be too cumbersome at this stage we will use an EC2 instance with docker installed for now

# Get latest ubuntu AMI for this region
data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

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
  cidr_blocks       = ["${element(var.admin_cidrs, count.index)}"]
  count             = "${length(var.admin_cidrs)}"
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

# TODO Add SG
# TODO Add Elastic IP and add it as ENV variable to codebuild
# TODO Add Role to call connect to CodeDeploy

# We use a template_file to create the user-data script for the ec2 instance
# this is because the instance behavior depends on TF outputs such us ECR URL
data "template_file" "bootstrap_script" {
  template = "${file("../../../scripts/aws-ec2/bootstrap.tpl")}"
  
  vars {
    ECR_REGION      = "${var.REGION}"
    IMAGES_REPO_URL = "${aws_ecr_repository.aclu.repository_url}"
  }
}

resource "aws_instance" "aclu" {
  ami                   = "${data.aws_ami.ubuntu.id}"
  instance_type         = "t2.micro"
  user_data             = "${data.template_file.bootstrap_script.rendered}"
  key_name              = "${var.KEY_PAIR}"
  iam_instance_profile  = "${aws_iam_instance_profile.instance_profile.id}"
  security_groups       = ["${aws_security_group.aclu_sg.name}", "${aws_security_group.aclu_admin_sg.name}"]
  tags {
    project = "${var.APP_NAME}"
  }
}