# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-28 07:34 UTC_

- [Amazon Neptune now supports tag-based access control for IAM](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-neptune-tbac/)
- [AWS Glue Data Quality now supports anomaly detection and writing results to the AWS Glue Data Catalog](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-glue-data-quality-catalog-anomaly-detection-write-results)
- [AWS Glue Data Quality now supports distribution statistics for data profiling](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-glue-data-quality-distribution-profiling)
- [Amazon GameLift Streams now supports Custom Aspect Ratio and Dynamic Resolution](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-gamelift-streams/)
- [AWS Security Hub MCP App brings exposure findings into your AI-assisted workflow (Preview)](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-security-hub-mcp-app/)
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
