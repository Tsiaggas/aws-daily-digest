# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-08 07:25 UTC_

- [Amazon GameLift Streams introduces secure terminal access for stream sessions](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-gamelift-streams-terminal-access/)
- [Amazon S3 Vectors is now available in AWS GovCloud (US) Regions](https://aws.amazon.com/about-aws/whats-new/2026/07/s3-vectors-available-aws-govcloud-regions/)
- [AWS Security Hub extends unified security management to Microsoft Azure](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-security-hub-supports-monitoring-microsoft-azure/)
- [Amazon ECS Managed Instances reduces GPU management fees by up to 60%](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ecs-managed-instances-gpu-price/)
- [Amazon EMR Serverless now supports larger worker sizes to run more compute and memory intensive workloads](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-emr-serverless/)
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
