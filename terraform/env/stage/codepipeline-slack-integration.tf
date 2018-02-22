module "codepipeline_slack_integration" {
  source            = "git::https://github.com/felimartina/aws-codepipeline-slack-integration-terraform-module.git"
  SLACK_WEBHOOK_URL = "${var.SLACK_WEBHOOK_URL}"
  SLACK_CHANNEL     = "${var.SLACK_CHANNEL}"
  APP_NAME          = "${var.APP_NAME}"
  PIPELINE_NAME     = "${aws_codepipeline.aclu.name}"
}
