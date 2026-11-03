# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-03 12:50 UTC_

- [Amazon RDS for Oracle now supports M8i and R8i instances in additional AWS Regions](https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-m8i-r8i-instances-new-regions/)
- [Haiku 5.5 now available on Kiro in AWS GovCloud (US)](https://aws.amazon.com/about-aws/whats-new/2026/11/kiro-haiku-5-5-aws-govcloud-us/)
- [Amazon RDS now supports per snapshot billing](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-per-snapshot-billing/)
- [Amazon Quick on desktop now uses your organization's existing Amazon Quick sign-in](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-quick-desktop-organization-sign-in/)
- [Amazon Aurora MySQL 8.4.10 is now generally available](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-aurora-mysql-8410-available/)
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
