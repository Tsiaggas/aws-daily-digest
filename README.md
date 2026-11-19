# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-19 14:28 UTC_

- [AWS Transform supports optimized storage for server migration](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-transform-optimized-storage/)
- [AWS Transform automates source and migration target actions to accelerate cutover](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-transform-automates-source-actions/)
- [AWS Systems Manager Parameter Store raises API throughput limits](https://aws.amazon.com/aws.amazon.com/about-aws/whats-new/2026/11/parameter-store-raises-api-throughput-limits/)
- [Amazon OpenSearch Memory is now generally available](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-memory-generally-available/)
- [Introducing the Apache Spark Optimization Agent for AWS Glue ETL](https://aws.amazon.com/about-aws/whats-new/2026/11/apache-spark-aws-glue-etl/)
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
