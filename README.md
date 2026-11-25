# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-25 15:40 UTC_

- [Amazon Bedrock adds bedrock-runtime endpoint support for OpenAI Daybreak Red in AWS GovCloud (US)](https://aws.amazon.com/about-aws/whats-new/2026/11/gpt-daybreak-red-runtime-govcloud/)
- [Amazon OpenSearch Serverless is now available in the Africa (Cape Town) Region](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-serverless-available-cape-town-region/)
- [AWS CloudFormation makes resource coverage comprehensive with 206 new types](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudformation-coverage-expansion/)
- [Amazon Connect Customer dashboards now support grouping historical metrics by time interval](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-connect-time-interval/)
- [Amazon RDS for SQL Server now supports up to 500 databases per instance](https://aws.amazon.com/about-aws/whats-new/2026/11/rds-sqlserver-supports-500-databases-per-instance)
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
