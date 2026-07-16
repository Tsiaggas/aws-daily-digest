# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-16 07:19 UTC_

- [Amazon CloudWatch Logs announces intelligent tiering for storage](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-intelligent-tiering/)
- [Amazon MQ now supports configurable storage for RabbitMQ brokers](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-mq-rabbitmq-configurable-storage/)
- [Amazon EC2 G7e instances now available in additional regions](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-g7e-additional-regions/)
- [Amazon Cognito now supports importing users with password hashes](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cognito-password-hash-import/)
- [Amazon RDS and Aurora now support R8g and M8g database instances in additional AWS Regions](https://aws.amazon.com/about-aws/whats-new/2026/7/amazon-rds-aurora-r8g-m8g-regions/)
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
