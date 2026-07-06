# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-06 12:14 UTC_

- [Amazon SageMaker Unified Studio now supports Terraform for provisioning](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-sagemaker-unified-studio-terraform/)
- [Amazon EC2 X8i instances are now available in additional regions](https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-ec2-x8i-instances-ICN-KUL-NRT-region/)
- [Amazon EC2 Dedicated Hosts now support AMD SEV-SNP](https://aws.amazon.com/about-aws/whats-new/2026/07/ec2-amd-sev-snp-dedicated-hosts)
- [Amazon SageMaker HyperPod now supports AMI versioning and auto-patching](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-sagemaker-hyperpod-ami-version-auto-patch)
- [AWS Config now supports 8 new resource types](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-config-new-resource-types)
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
