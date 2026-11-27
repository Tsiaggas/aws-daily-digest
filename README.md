# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-27 15:09 UTC_

- [Amazon RDS for PostgreSQL supports minor versions 18.7, 17.12, 16.16, 15.20, and 14.25](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-postgresql-18-7-17-12-16-16-15-20-14-25/)
- [AWS Lambda now supports orchestrating MicroVMs with Lambda durable functions](https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-microvm/)
- [Amazon CloudWatch Omni now integrates with PagerDuty](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-omni-pagerduty/)
- [Amazon EC2 M8g instances are now available in Israel (Tel Aviv)](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-m8g-instances-telaviv-region/)
- [Amazon EC2 M9gd instances are now available in Asia Pacific (Seoul)](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-m9gd-asiapacific-seoul/)
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

<!-- docs: add maintenance note 2026-10-09 -->

<!-- docs: update maintenance note 2026-10-09 -->
