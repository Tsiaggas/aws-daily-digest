# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-18 14:05 UTC_

- [Amazon WorkSpaces Applications adds support for smart card redirection](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-workspaces-applications-smart-card-redirection/)
- [Amazon EMR 8.2 is now available](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-emr-8.2/)
- [Introducing the Apache Spark Optimization Agent for Amazon EMR Serverless](https://aws.amazon.com/about-aws/whats-new/2026/11/apache-spark-optimization-agent/)
- [AWS Transform now accelerates migration deals for Migration Acceleration Program (MAP) benefits](https://aws.amazon.com/about-aws/whats-new/2026/11/map-integration-with-aws-transform/)
- [Amazon EC2 C8gn instances are now available in AWS Israel (Tel Aviv) region](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-c8gn/)
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
