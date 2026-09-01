# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-01 09:42 UTC_

- [Amazon DocumentDB now supports direct major version upgrades to version 8.0](https://aws.amazon.com/about-aws/whats-new/2026/08/documentdb-major-version-upgrade-8-0/)
- [Partner Revenue Measurement expands service coverage for User Agent string capability](https://aws.amazon.com/about-aws/whats-new/2026/08/partner-revenue-measurement-user-agent-expansion/)
- [AWS Agent Registry agents and MCP servers now available in Amazon Quick](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-agent-registry-agents-mcp-servers-quick/)
- [Amazon Redshift now supports AWS IAM Identity Center authentication with enhanced VPC routing](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-redshift-supports-idc-evr)
- [Amazon Timestream for InfluxDB is now available in 8 additional AWS Regions](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-timestream-influxdb-regions/)
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
