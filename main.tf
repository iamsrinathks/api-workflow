module "bucket" {
  source  = "terraform-google-modules/cloud-storage/google//modules/simple_bucket"
  version = "~> 1.3"

  name       = "example-bucket"
  project_id = "example-project"
  location   = "us-east1"
}
