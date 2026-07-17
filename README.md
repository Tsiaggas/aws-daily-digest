# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-17 07:13 UTC_

- [Amazon Managed Grafana achieves FedRAMP High authorization in AWS GovCloud (US)](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-managed-grafana-fedramp-high/)
- [Track cost efficiency trends directly in Billing and Cost Management Dashboards with the new Cost Efficiency widget](https://aws.amazon.com/about-aws/whats-new/2026/07/monitor-cost-efficiency-using-dashboards)
- [Amazon EC2 now surfaces the public SSM parameters associated with public AMIs](https://aws.amazon.com/about-aws/whats-new/2026/07/ec2-public-images-ssm-parameters)
- [Amazon S3 Event Notifications now include system-generated tags](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-s3-event-notifications-system-generated-tags/)
- [PostgreSQL 19 Beta 2 is now available in Amazon RDS Database Preview Environment](https://aws.amazon.com/about-aws/whats-new/2026/07/postgresql-19-beta-2-amazon-rds-database-preview-environment/)
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
