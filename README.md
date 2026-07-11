# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-11 07:08 UTC_

- [Amazon EC2 network/EBS instances now available in additional regions](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-r8in-r8ib-r8idn-r8idb)
- [Amazon EMR on EKS now supports Apache Spark troubleshooting agent](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-emr-eks-spark-troubleshooting/)
- [Amazon Location Service enhances Places APIs with new address and search options](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-location-service-enhanced-address-search)
- [Amazon SageMaker HyperPod now supports AMI-based node lifecycle configuration for Slurm clusters using continuous provisioning](https://aws.amazon.com/about-aws/whats-new/2025/06/ami-configuration-continuous-slurm/)
- [Amazon EC2 G7 instances are now available in the AWS US East (N. Virginia) Region](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-g7-available-North-Virginia)
<!-- LATEST:END -->

## How it works

```
GitHub Actions (daily cron, 05:00 UTC)
        │
        ▼
fetch_digest.py ──► AWS What's New RSS feed
        │
        ▼
digests/YYYY/MM/YYYY-MM-DD.md  +  README "Latest" section
        │
        ▼
auto commit & push
```

- **Python + feedparser** for RSS parsing with graceful failure handling
- **GitHub Actions** scheduled workflow, `workflow_dispatch` for manual runs
- Digests archived by year/month for easy browsing

## Why

I work with AWS daily (migrations, EC2, IAM) and I'm preparing for the **Solutions Architect Associate** cert — this keeps me on top of new AWS releases and doubles as a small, honest automation project.
