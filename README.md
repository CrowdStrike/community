# CrowdStrike Github Overview
Last updated 2022-04-19

## Falcon Sensor Installation
 - install scripts ([Bash](https://github.com/CrowdStrike/falcon-scripts/tree/main/bash/install), [Powershell](https://github.com/CrowdStrike/falcon-scripts/tree/main/powershell))
 - [Ansible module](https://github.com/CrowdStrike/ansible_collection_falcon) ([Ansible Galaxy](https://galaxy.ansible.com/crowdstrike/falcon))
 - [Puppet module](https://github.com/CrowdStrike/puppet-falcon)

## Cloud Integrations
 - [AWS](https://github.com/CrowdStrike/Cloud-AWS)
   - Sensor Automation
     - [AWS Autoscale Groups for Auto Register/Deregister](https://github.com/crowdstrike/cloud-aws/blob/main/Agent-Install-Examples/Cloudformation/autoscale/README.md)
     - [AWS Systems Manager Parameter Store with PowerShell Sensor Installation Script](https://github.com/crowdstrike/cloud-aws/blob/main/Agent-Install-Examples/powershell)
     - [AWS Systems Manager with Linux BASH Sensor Installation Script](https://github.com/crowdstrike/cloud-aws/blob/main/Agent-Install-Examples/bash)
     - [AWS Terraform Template for Sensor Installation](https://github.com/crowdstrike/cloud-aws/blob/main/Agent-Install-Examples/Terraform-bootstrap-s3)
   - Services Integrations
     - [AWS Control Tower with CrowdStrike Discover for Cloud and Containers](https://github.com/crowdstrike/cloud-aws/blob/main/Control-Tower/README.md)
     - [AWS Control Tower with CrowdStrike Horizon](https://github.com/crowdstrike/cloud-aws/blob/main/Control-Tower-For-Horizon/README.md)
     - [AWS Network Firewall with CrowdStrike Threat Intelligence](https://github.com/crowdstrike/cloud-aws/blob/main/Network-Firewall/README.md)
     - [AWS Private Link with CrowdStrike Sensor Proxy](https://github.com/crowdstrike/cloud-aws/blob/main/aws-privatelink/README.md)
     - [AWS Security Hub with CrowdStrike Event Streams API](https://github.com/crowdstrike/cloud-aws/blob/main/Falcon-Integration-Gateway/README.md)
     - [AWS S3 Protected Bucket with CrowdStrike Quick Scan API](https://github.com/crowdstrike/cloud-aws/blob/main/s3-bucket-protection)

 - [Azure](https://github.com/CrowdStrike/Cloud-Azure/)
   - Sensor Automation
     - [VM Extension](https://github.com/CrowdStrike/Cloud-Azure/tree/main/vm/vm-extensions)
     - [VM Run Command](https://github.com/CrowdStrike/Cloud-Azure/blob/main/vm/vmrun.md)
     - [VM Applications](https://github.com/CrowdStrike/Cloud-Azure/blob/main/vm/vmapp/README.md)
     - [VM Virtual Machine Scale Sets](https://github.com/CrowdStrike/Cloud-Azure/tree/main/vm/vmss)
   - Services Integrations
     - [Azure Log Analytics](https://github.com/CrowdStrike/falcon-integration-gateway/tree/main/fig/backends/azure)
 - [GCP](https://github.com/CrowdStrike/Cloud-GCP)
   - Sensor Automation
     - [OSConfig](https://console.cloud.google.com/marketplace/product/crowdstrike-saas/crowdstrike-falcon-endpoint-protection?project=solar-gcp-integration-lab)
   - Services Integrations
     - [Security Command Center](https://github.com/CrowdStrike/falcon-integration-gateway/blob/main/docs/listings/gke/UserGuide.md)
     - [Google Chronicle](https://github.com/CrowdStrike/falcon-integration-gateway/blob/main/docs/listings/gke-chronicle/UserGuide.md)

## Kubernetes Deployment
 - [Falcon Operator](https://github.com/CrowdStrike/falcon-operator)
 - [Falcon Helm](https://github.com/CrowdStrike/falcon-helm)
 - Containers
   - [CI container image scanning script](https://github.com/crowdstrike/container-image-scan)
      - [github action](https://github.com/CrowdStrike/container-image-scan-action)
   - helper tools
      - [cloud-tools-image](https://github.com/CrowdStrike/cloud-tools-image/)
      - [detection container](https://github.com/CrowdStrike/detection-container)

## API SDKs
 - [psfalcon](https://github.com/CrowdStrike/psfalcon)
 - [falconpy](https://github.com/CrowdStrike/falconpy)
 - [gofalcon](https://github.com/CrowdStrike/gofalcon)
 - [rusty-falcon](https://github.com/CrowdStrike/rusty-falcon)
 - [falconjs](https://github.com/CrowdStrike/falconjs)

## Other Integrations
 - [Falcon Integration Gateway](https://github.com/CrowdStrike/falcon-integration-gateway)
   - [AWS Security Hub](https://github.com/CrowdStrike/falcon-integration-gateway/tree/main/fig/backends/aws)
   - [Azure Log Analytics](https://github.com/CrowdStrike/falcon-integration-gateway/tree/main/fig/backends/azure)
   - [Chronicle](https://github.com/CrowdStrike/falcon-integration-gateway/tree/main/fig/backends/chronicle)
   - [GCP Security Command Center](https://github.com/CrowdStrike/falcon-integration-gateway/tree/main/fig/backends/gcp)
   - [Workspace ONE](https://github.com/CrowdStrike/falcon-integration-gateway/tree/main/fig/backends/workspaceone)
 - [Cloud-Benchmarks](https://github.com/CrowdStrike/Cloud-Benchmark)
 - [Falcon Data Replicator (FDR)](https://falcon.us-2.crowdstrike.com/documentation/9/falcon-data-replicator)
 - Various Humio integrations
