# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-09 08:28 UTC_

- [AWS Builder Center Now Offers Free Sandbox Environments](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-builder-center-sandbox/)
- [AWS Security Hub now offers Network Scanning to identify publicly reachable resources](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-security-hub-network-scanning/)
- [Amazon Redshift RG instances now available on the trailing track](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-redshift-graviton-rg-instances-trailing-track)
- [Amazon Aurora DSQL change data capture (CDC) Is now generally available](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-aurora-dsql-cdc-ga/)
- [Amazon Connect Customer now supports forecasting, planning, and scheduling for Tasks and Emails](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-connect-customer-agent-scheduling-tasks/)
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
