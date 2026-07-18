# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-18 06:57 UTC_

- [Amazon GameLift Streams now supports IAM role credentials for stream sessions](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-gamelift-streams-iam/)
- [Amazon OpenSearch UI now supports one-click dashboard migration](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-opensearch-ui-one-click-dashboard-migration)
- [Amazon SageMaker HyperPod now supports partition-level topology for Slurm orchestrated clusters](https://aws.amazon.com/about-aws/whats-new/2026/07/hyperpod-partition-topology-slurm/)
- [Amazon Managed Grafana achieves FedRAMP High authorization in AWS GovCloud (US)](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-managed-grafana-fedramp-high/)
- [Track cost efficiency trends directly in Billing and Cost Management Dashboards with the new Cost Efficiency widget](https://aws.amazon.com/about-aws/whats-new/2026/07/monitor-cost-efficiency-using-dashboards)
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
