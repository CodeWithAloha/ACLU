# Infrastructure

API
  Current setup has an ec2 instance running docker on it locally.
  Docker images are beeing stored in AWS ECR containers repository. Ideal state would be to run app on a cluster in ECS.
Website
  To ease the load in the server and reduce the maintenance effort, s3 is used as web hosting for the static Vue.js website. Downside is that s3 does not allow for apex routing, but we can work around that with redirects. If needed we can create an nginx/httpd docker container and deploy it as the api.

Provisioning
  Infrastructure is provisioned using Terraform.
  Terraform Gotchas:
    - You must have a profile named `aclu` setup in your aws shared credentials file with the following format
    ```
      [default]
      aws_access_key_id = 'SOME_OTHER_CREDS_HERE'
      aws_secret_access_key = 'SOME_OTHER_CREDS_HERE'
      region=us-west-2
      [aclu]
      aws_access_key_id = 'ACLU_ACCESS_KEY' // <- YOUR ACLU AWS CREDS HERE
      aws_secret_access_key = 'ACLU_SECRET_KEY' // <- YOUR ACLU AWS CREDS HERE
      region=us-west-1
    ```
    - You need to create a `terraform.tfvars` with your secret keys in the specifc env folder (ie. `terraform/env/stage') before being able to maintain and provision.
    - Terraform state is stored in an s3 bucket so that all developers can work seamless without state conflicts across different envs.
    - First time you are using terraform for a given env you will need to run `terraform init`.
    - Running `terraform plan` will tell you what is the execution plan based upon your modifications. After that you can run `terraform apply` and changes will be propagated to aws.

Deplloyment | CI/CD

    - CodePipeline is used as orchestrator for CI/CD, taking care of fetcing the code from github and passing it over to CodeBuild and CodeDeploy.
    - CodeBuild is used for building front end and creating the API docker containers.
    - CodeDeploy is used for deploying docker containers in the EC2 instance. It runds `docker-compose` to run api and mongodb containers in the ec2 instance. Future state: Ideally we will be deploying to an ECS Cluster.

