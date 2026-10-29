# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-29 11:33 UTC_

- [Amazon RDS for Oracle now supports September 2026 Monthly Recommended Patch](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-rds-oracle-september-mrp)
- [Amazon Bedrock AgentCore CLI version 1.0 is now available](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-bedrock-agentcore-cli-version-1-0-available/)
- [AWS Lambda supports Seekable OCI (SOCI) lazy loading for Lambda Managed Instances](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-seekable-oci-soci/)
- [Introducing time series collections for the next generation of Amazon OpenSearch Serverless](https://aws.amazon.com/about-aws/whats-new/2026/10/time-series-collection-next-generation-opensearch-serverless/)
- [Quick now supports smart approvals for agentic actions](https://aws.amazon.com/about-aws/whats-new/2026/10/quick-smart-approvals-agentic-actions/)
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
