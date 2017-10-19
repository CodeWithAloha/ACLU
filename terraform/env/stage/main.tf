terraform {
  backend "s3" {
    bucket     = "aclu.terraform"
    key        = "aclu/envs/stage/terraform.tfstate"
    region     = "us-west-1"
    profile    = "aclu"
  }
}

provider "aws" {
  profile    = "${var.PROFILE}"
}

data "terraform_remote_state" "network" {
  backend = "s3"

  config {
    bucket     = "felimartina.terraform"
    key        = "aclu/envs/stage/terraform.tfstate"
    region     = "${var.REGION}"
    profile    = "aclu"
  }
}