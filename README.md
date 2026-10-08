# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-08 12:04 UTC_

- [AWS Capabilities by Region now offers availability notifications for individual features and advanced filters](https://aws.amazon.com/about-aws/whats-new/2026/10/awscapabilities-enhancements/)
- [AWS Config now supports 77 new resource types](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-config-new-resource-types)
- [Claude Haiku 5.5 is now available on AWS](https://aws.amazon.com/about-aws/whats-new/2026/10/claude-haiku-5-5-aws/)
- [Claude Haiku 5.5 is now available on AWS GovCloud (US)](https://aws.amazon.com/about-aws/whats-new/2026/10/claude-haiku-5-5-aws-govcloud/)
- [AWS Batch now publishes job metrics to Amazon CloudWatch](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-batch-job-cloudwatch-metrics/)
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
