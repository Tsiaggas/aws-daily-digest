# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-06 07:35 UTC_

- [AWS Lambda announces scalable network bandwidth up to 3,000 Mbps for functions outside a VPC](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-lambda-network-bandwidth/)
- [Amazon Keyspaces (for Apache Cassandra) is now available in the Canada West (Calgary) Region (ca-west-1)](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-keyspaces-apache-cassandra-canada-west/)
- [AWS Glue Data Quality makes ETL anomaly detection free and improves anomaly predictions](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-glue-data-quality-anomaly-detection-free)
- [AWS Marketplace adds AI Insights so buyers can understand pricing before they buy](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-marketplace-ai-insights/)
- [Amazon DynamoDB now supports real-time vector search](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-dynamodb-vector-search)
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
