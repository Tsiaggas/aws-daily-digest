# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-21 13:30 UTC_

- [Amazon CloudWatch Omni now supports Microsoft Azure platform logs, metrics and traces](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-omni-microsoft-azure)
- [Web Search on Amazon Bedrock expands language support and country-aware search](https://aws.amazon.com/about-aws/whats-new/2026/11/web-search-amazon-bedrock/)
- [Amazon RDS for Oracle now supports Primary Endpoint](https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-primary-endpoint-v2/)
- [AWS Lambda now publishes Event Function state change events to Amazon EventBridge](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-function-state-events/)
- [AWS Network Firewall introduces automated Internet firewall in public preview](https://aws.amazon.com/about-aws/whats-new/2026/11/network-firewall-automated-internet/)
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
