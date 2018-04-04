terraform {
  backend "s3" {
    bucket  = "aclu.terraform.state"
    key     = "aclu/envs/stage/terraform.tfstate"
    region  = "us-west-2"                         # This cannot be set using var because it is too early in the process
    profile = "aclu"
  }
}

provider "aws" {
  profile = "${var.PROFILE}"
  region  = "${var.REGION}"
}

data "terraform_remote_state" "network" {
  backend = "s3"

  config {
    bucket  = "aclu.terraform.state"
    key     = "aclu/envs/stage/terraform.tfstate"
    region  = "${var.REGION}"
    profile = "${var.PROFILE}"
  }
}
