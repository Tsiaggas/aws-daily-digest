# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-14 12:14 UTC_

- [Aurora PostgreSQL with express configuration now supported in CloudFormation](https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-postgresql-cloudformation/)
- [Grok 4.7 now available on Kiro in AWS GovCloud (US)](https://aws.amazon.com/about-aws/whats-new/2026/11/kiro-grok-4-7-aws-govcloud-us/)
- [Amazon RDS for Oracle reduces downtime for automatic minor version upgrades and scheduled maintenance](https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-reduces-maintenance-downtime-for-amvu-scheduled-upgrades/)
- [AWS Security Hub CSPM now supports centralized configuration with AWS Organizations declarative policies](https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-cspm-org-policies/)
- [Amazon Bedrock AgentCore Identity now supports OAuth 2.0 discovery URLs](https://aws.amazon.com/about-aws/whats-new/2026/11/bedrock-agentcore-oauth2-discovery/)
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
