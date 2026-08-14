# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-14 06:09 UTC_

- [AWS Billing and Cost Management introduces Managed Dashboards](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-billing-and-cost-management-managed-dashboards/)
- [AWS Client VPN now supports CLI, administration controls, and faster connections](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-client-vpn-cli/)
- [Claude Opus 5 is now available in AWS GovCloud (US)](https://aws.amazon.com/about-aws/whats-new/2026/07/claude-opus-5-aws-govcloud/)
- [Amazon Quick Microsoft 365 extensions are now generally available](https://aws.amazon.com/amazon-quick-microsoft-365-extensions-generally-available)
- [Spot Placement Score now includes Local Zones](https://aws.amazon.com/about-aws/whats-new/2026/08/spot-placement-score-local-zones/)
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
