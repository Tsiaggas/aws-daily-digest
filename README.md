# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-10 08:17 UTC_

- [OAuth support for the AWS MCP Server](https://aws.amazon.com/about-aws/whats-new/2026/07/oauth-aws-mcp-server/)
- [Amazon Timestream for InfluxDB now publishes database state change events to Amazon EventBridge](https://aws.amazon.com/about-aws/whats-new/2026/07/timestream-influxdb-eventbridge/)
- [AWS Client VPN extends availability to four additional AWS Regions](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-client-vpn-four-additional-regions/)
- [Amazon SageMaker Unified Studio adds custom asset types to the catalog in IAM-based domains](https://aws.amazon.com/about-aws/whats-new/2026/07/smus-custom-asset-types-iam/)
- [Amazon SageMaker HyperPod now supports deep health checks for Slurm clusters with continuous provisioning](https://aws.amazon.com/about-aws/whats-new/2026/07/deep-health-check-continuous-slurm/)
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
