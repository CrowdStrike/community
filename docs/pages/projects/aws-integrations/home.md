---
title: CRWD | AWS Integrations
description: Integrations between CrowdStrike and Amazon Web Services (AWS).
permalink: /aws-integrations/

layout: page
sidenav: aws-integrations
#subnav:
#  - text: Welcome
#    href: '#welcome'
#  - text: How do I make a contribution?
#    href: '#how-do-i-make-a-contribution'
#  - text: Where can I go for help?
#    href: '#where-can-i-go-for-help'
#  - text: What does the Code of Conduct mean for me?
#    href: '#what-does-the-code-of-conduct-mean-for-me'

hero:
  image: ../assets/img/crwd-banner-01.png
  callout:
    alt: "Watch the Demo"
    text: " "
  button:
    href: 
    text: Coming Soon
  link:
    text: 
    href:
  content: When CrowdStrike detects suspicious activity, threat actors can automatically be added to your domain block list in AWS Network Firewall.
---

## Integrated Solutions
Joint customers of CrowdStrike and AWS can gain operational benefits through the following
deep integrations between AWS services and the CrowdStrike Falcon platform.

<!-- Please help maintain readability/visual searchability by
     keeping the table sorted alphabetically 
     
     online free tool to help:
     https://wordcounter.net/alphabetize
-->
     
{: .usa-table-borderless}
| Integration / Use Case  | Description  | Links |
|---|---|---|
| [AWS Network Firewall with CrowdStrike Threat Intelligence](/aws-integrations/aws-network-firewall-with-crowdstrike-threat-intelligence/) | Add FQDN's from CrowdStrike detections to a domain block list in AWS Network Firewall. | [Code on GitHub](https://crowdstrike.github.io/aws-network-firewall) |
| AWS PrivateLink to Secure Connections to CrowdStrike Cloud | Utilize AWS PrivateLink to provide secure connectivity between your CrowdStrike protected workloads/endpoints and the CrowdStrike Cloud | [Code on GitHub](https://github.com/CrowdStrike/Cloud-AWS/tree/master/aws-privatelink) |
| AWS S3 Buckets to Archive Logs From Falcon Data Replicator | Replicate event data from your CrowdStrike environment to an AWS S3 bucket. | [Code on GitHub](https://github.com/CrowdStrike/FDR) |
| AWS Security Hub to Receive CrowdStrike Detections | Publish CrowdStrike detections to AWS Security Hub | [Code on GitHub](https://github.com/CrowdStrike/Cloud-AWS/tree/master/Security-Hub) |
| AWS Systems Manager Distributor to Automatically Install/Remove CrowdStrike Sensor | Automatically install and uninstall the CrowdStrike Falcon Sensor into AWS EC2 instances. This integration utilizes CloudFormation scripts executed via AWS Lambda functions, which are executed whenever AWS System Manager Distributor detects EC2 instance creation or termination. | [Code on GitHub](https://github.com/CrowdStrike/Cloud-AWS/tree/master/systems-manager) |