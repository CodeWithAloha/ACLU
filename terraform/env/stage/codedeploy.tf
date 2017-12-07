resource "aws_iam_role" "codedeploy_role" {
  name = "${var.APP_NAME}-codedeploy-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "codedeploy.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy" "codedeploy_policy" {
  name = "${var.APP_NAME}-codedeploy-policy"
  role = "${aws_iam_role.codedeploy_role.id}"
  # TODO  - Restrict s3 access to build bucket
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCodeDeployBasics",
      "Effect": "Allow",
      "Action": [
        "autoscaling:CompleteLifecycleAction",
        "autoscaling:DeleteLifecycleHook",
        "autoscaling:DescribeAutoScalingGroups",
        "autoscaling:DescribeLifecycleHooks",
        "autoscaling:PutLifecycleHook",
        "autoscaling:RecordLifecycleActionHeartbeat",
        "codedeploy:*",
        "ec2:DescribeInstances",
        "ec2:DescribeInstanceStatus",
        "tag:GetTags",
        "tag:GetResources",
        "sns:Publish"
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
      "Action": [
        "elasticbeanstalk:*",
        "ec2:*",
        "elasticloadbalancing:*",
        "autoscaling:*",
        "cloudwatch:*",
        "s3:*",
        "sns:*",
        "cloudformation:*",
        "rds:*",  
        "sqs:*",
        "ecs:*",
        "iam:PassRole"
        ],
      "Resource": "*",
      "Effect": "Allow"
    }
  ]
}
EOF
}

resource "aws_codedeploy_app" "aclu" {
  name = "${var.APP_NAME}-codedeploy"
}

resource "aws_sns_topic" "codedeploy_sns" {
  name = "${var.APP_NAME}-codedeploy-sns"
}

resource "aws_codedeploy_deployment_group" "aclu" {
  app_name              = "${aws_codedeploy_app.aclu.name}"
  deployment_group_name = "${var.APP_NAME}-deployment-group"
  service_role_arn      = "${aws_iam_role.codedeploy_role.arn}"

  ec2_tag_filter {
    key   = "project"
    type  = "KEY_AND_VALUE"
    value = "${var.APP_NAME}"
  }

  trigger_configuration {
    trigger_events     = ["DeploymentFailure", "DeploymentSuccess"]
    trigger_name       = "${var.APP_NAME}-codedeploy-trigger"
    trigger_target_arn = "${aws_sns_topic.codedeploy_sns.arn}"
  }

  auto_rollback_configuration {
    enabled = true
    events  = ["DEPLOYMENT_FAILURE"]
  }

}