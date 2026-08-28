# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-28 17:06 UTC_

- [Amazon Aurora MySQL 3.13 (compatible with MySQL 8.0.45) is generally available](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-aurora-mysql-313-available/)
- [Cosmos3-Edge, Cosmos3-Nano, and Cosmos3-Super models now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/cosmos3-edge-cosmos3-nano-cosmos3-super-on-sagemaker-jumpstart/)
- [Muse-Glimmer-30B and Qwen 3.8-27B models now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/muse-glimmer-30b-qwen-3.8-27b-on-sagemaker-jumpstart/)
- [Amazon Redshift streaming can now ingest 10MiB records from Amazon Kinesis Data Streams](https://aws.amazon.com/about-aws/whats-new/2026/08/redshift-streaming-supports-kds-10mib-records)
- [Amazon Redshift integrates with Agent Toolkit for AWS for AI-assisted data warehouse management](https://aws.amazon.com/about-aws/whats-new/2026/08/redshift-agenttoolkit-for-ai-assisted-datawarehouse-mgmt)
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
