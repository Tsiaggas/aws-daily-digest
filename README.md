# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-18 09:20 UTC_

- [AWS Transfer Family now supports source IP preservation for SFTP servers behind a Network Load Balancer (NLB)](https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-source-ip-nlb/)
- [AWS HealthOmics now supports IAM session policies](https://aws.amazon.com/about-aws/whats-new/2026/09/omics-iam-session-policy/)
- [AWS Batch now supports bulk job cancellation and termination](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-batch-bulk-cancellation/)
- [Introducing Amazon EC2 T8i instances](https://aws.amazon.com/about-aws/whats-new/2026/09/ec2-t8i-instances-ga/)
- [AWS Elastic Beanstalk introduces Cluster Mode to run multiple applications on shared infrastructure](https://aws.amazon.com/about-aws/whats-new/2026/09/elastic-beanstalk-cluster-mode/)
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
