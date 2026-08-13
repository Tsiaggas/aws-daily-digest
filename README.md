# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-13 06:12 UTC_

- [AWS Global View now offers an interactive map view for AWS Regions and AWS Local Zones](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-global-view-map-view/)
- [AWS IAM now provides role manager to set up IAM roles automatically](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-iam-role-manager)
- [Amazon EKS now supports advanced Kubernetes control plane configuration parameters](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-control-plane-configuration-parameters)
- [Amazon Quick adds deny by default for custom permissions](https://aws.amazon.com/whats-new/2026/08/amazon-quick-deny-by-default-permissions/)
- [Amazon Connect Customer supports manual assignment of queued agent-first callbacks](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-connect-agent-callbacks/)
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
