variable "credentials" {
  description = "Credential key access"
  default     = "./keys/gcp_terraform_runner_key.json"
}

variable "project" {
  description = "Project name"
  default     = "de-zoomcamp-411908"
}

variable "location" {
  description = "Project location"
  default     = "asia-southeast2"
}

variable "bq_dataset_name" {
  description = "Big Query Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "Google Cloud Storage Bucket name"
  default     = "de-zoomcamp-411908"
}

variable "gcs_storage_class" {
  description = "Bucket Google Cloud Storage Class"
  default     = "STANDARD"
}