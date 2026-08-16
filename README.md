# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-16 05:22 UTC_

- [Amazon RDS for Oracle now supports Oracle Application Express (APEX) version 26.1](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-rds-oracle-apex-26-1/)
- [Amazon SES click tracking now supports custom URL paths for mobile app deep linking](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ses-supports-customurl-deeplinking)
- [AWS Billing and Cost Management introduces Managed Dashboards](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-billing-and-cost-management-managed-dashboards/)
- [AWS Client VPN now supports CLI, administration controls, and faster connections](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-client-vpn-cli/)
- [Amazon Redshift adds rg.large and rg.12xlarge instance sizes in AWS GovCloud (US) Regions](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-redshift-adds-rg-large-12xlarge-aws-govcloud-regions/)
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
