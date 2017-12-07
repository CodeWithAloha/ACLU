# You  will need to create a 'terraform.tfvars' file providing your secret keys and credentials
variable "PROFILE" {
  description = "You must have an aws profile in your local credentials files that has ACCESS_KEY, SECRET_KEY, and REGION set. Check README.md for details"
  default     = "aclu"
}

variable "REGION" {
  default = "us-west-2"
}

variable "ENV" {
  default = "staging"
}

variable "APP_NAME" {
  default = "aclu"
}

variable "KEY_PAIR" {
  description = "Key Pair file name to ssh into instances."
  default     = "aclu"
}

variable "FRONT_END_BUCKET_NAME" {
  default = "hi.aclu.com"
}

variable "GITHUB_OWNER" {
  description = "Gtihub account. Also needs to provide GITHUB_TOKEN valid for this user. Should be in terraform.tfvars file."
}

variable "GITHUB_REPO" {
  default = "ACLU"
}

variable "GITHUB_BRANCH" {
  default = "master"
}

variable "GITHUB_TOKEN" {
  description = "OAuth token from github to grant CodePipeline access to your github repo. Should be in terraform.tfvars file."
}

variable "ADMIN_CIDRS" {
  type = "list"

  default = [
    "50.113.42.119/32", # Pipe's IP
    "199.68.252.130/32", # Boxjelly
    "167.216.21.125/32" # Manoa Innovation Center
  ]
}

variable "GLOBAL_TAGS" {
  type = "map"

  default = {
    "project"     = "aclu"
    "createdBy"   = "terraform"
    "environment" = "stage"
  }
}

variable "DOMAIN" {
  description = "Website Domian (ie. hawaii.aclu.com)"
  default     = "aclu.codeforhawaii.org"
}

variable "API_DOMAIN" {
  description = "API Domain (ie. api.aclu.codeforhawaii.org)"
  default     = "api.aclu.codeforhawaii.org"
}

variable "DOMAIN_CERTIFICATE_ARN" {
  description = "SSL Certificate should be in AWS Certificate Manager in region us-east-1"
  default     = "arn:aws:acm:us-east-1:705750910119:certificate/b079df26-2c6b-4c06-a6bd-5bfe8852f3c0"
}

variable "ELB_CERTIFICATE_ARN" {
  description = "SSL Certificate should be in AWS Certificate Manager in the same region where we are gonna provision"
  default     = "arn:aws:acm:us-west-2:705750910119:certificate/9a7aeb93-0e09-4504-9125-1af33cff6e44"
}
