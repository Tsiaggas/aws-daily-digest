# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-11 12:45 UTC_

- [AWS Billing and Cost Management now supports AWS Billing Conductor and AWS Billing Transfer views as source views for custom billing views](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-billing-and-cost-management-multi-source-custom-billing-views)
- [Amazon EC2 G7 instances now available in additional regions](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-g7-additional-regions/)
- [Amazon OpenSearch Service announces managed cross-Region disaster recovery](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-service-managed-cross-region-disaster-recovery/)
- [Amazon RDS for MySQL 26.10 is now available in Amazon RDS Database Preview Environment](https://aws.amazon.com/about-aws/whats-new/2026/11/rds-mysql-26-10-preview-environment/)
- [Amazon RDS for PostgreSQL announces Extended Support minor versions 13.23-rds.20260819, 12.22-rds.20260820 and 11.22-rds.20260822](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-postgresql-extended-support/)
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
