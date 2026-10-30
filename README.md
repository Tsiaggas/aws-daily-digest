# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-30 11:25 UTC_

- [AWS Marketplace now enables partners to list once and sell through multiple subsidiary accounts](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-marketplace-subsidiary-account-authorization)
- [Amazon RDS for Oracle and SQL Server now support storage autoscaling on additional storage volumes](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-rds-oracle-sqlserver-autoscaling-additional-storage-volumes)
- [Amazon Aurora now supports post-quantum TLS key exchange](https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-postgresql-post-quantum-tls-key-exchange/)
- [Amazon MSK Connect now supports updating connector plugins and worker configurations](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-msk-connect-update-plugin-worker-configurations)
- [AWS Step Functions workflows now available as AI agent tools](https://aws.amazon.com/about-aws/whats-new/2026/10/step-functions-workflows-ai-agent-tools/)
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
