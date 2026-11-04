# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-04 13:01 UTC_

- [Amazon Connect Customer lets agents pause and resume emails](https://aws.amazon.com/about-aws/whats-new/2026/11/connect-pause-resume-email/)
- [Amazon WorkSpaces for AI agents now supports Linux and Windows 11 cloud desktops](https://aws.amazon.com/about-aws/whats-new/2026/11/workspaces-ai-agents-linux-windows-11)
- [Amazon Connect Customer prefills the email address for new threads started from cases](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-connect-cases-email-addresses/)
- [AWS Config now supports 10 new resource types](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-config-new-resource-types)
- [Amazon RDS now supports the latest Cumulative Update and GDR updates for Microsoft SQL Server](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-supports-latest-cumulative-update-gdr-microsoft-sql-server/)
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
