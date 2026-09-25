# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-25 09:57 UTC_

- [AWS Billing and Cost Management now provides billing context for your account through a new API](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-billing-and-cost-management-billing-context-api/)
- [Amazon EventBridge relaunches event buses for enterprise scale](https://aws.amazon.com/about-aws/whats-new/2026/09/eventbridge-relaunches-custom-event-buses/)
- [AWS Lambda durable functions are now available in AWS European Sovereign Cloud region](https://aws.amazon.com/about-aws/whats-new/2026/09/durablefunctions-european-sovereign-cloud/)
- [Amazon RDS for MySQL announces Extended Support minor versions 5.7.44-rds.20260902 and 8.0.46-rds.20260908](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-rds-mysql-extended-support-minor-5744-8046-rds/)
- [Amazon RDS for PostgreSQL now supports PostgreSQL 19 Beta 4 in the Amazon RDS Database Preview Environment](https://aws.amazon.com/about-aws/whats-new/2026/09/postgresql-19-beta-4-amazon-rds-database-preview-environment/)
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
