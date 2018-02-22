resource "aws_sns_topic" "codepipeline_events" {
  name = "${var.APP_NAME}-codepipeline-event"
}

resource "aws_cloudwatch_event_rule" "console" {
  name        = "${var.APP_NAME}-capture-codepipeline-state-change"
  description = "Capture state changes in CodePipeline"

  event_pattern = <<PATTERN
{
  "source": [
    "aws.codepipeline"
  ],
  "detail-type": [
    "CodePipeline Pipeline Execution State Change"
  ],
  "detail": {
    "pipeline": [
      "${aws_codepipeline.aclu.id}"
    ]
  }
}
PATTERN
}

resource "aws_cloudwatch_event_target" "sns" {
  rule      = "${aws_cloudwatch_event_rule.console.name}"
  target_id = "${var.APP_NAME}-codepipeline-event"
  arn       = "${aws_sns_topic.codepipeline_events.arn}"
}
