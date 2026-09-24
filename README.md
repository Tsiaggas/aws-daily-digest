# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-24 09:40 UTC_

- [Amazon Kinesis Data Streams announces Service-Managed Partition Keys for simplified data ingestion](https://aws.amazon.com/about-aws/whats-new/2026/09/kinesis/service-managed-partition-keys)
- [Amazon Bedrock Managed Knowledge Base now supports Salesforce and Zendesk as native data source connectors](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-managed-knowledge-base-salesforce-zendesk-native-data-source-connectors/)
- [Amazon Connect Customer now provides routing step data in the analytics data lake](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-connect-routing-step-data/)
- [Amazon EMR on EKS now supports IPv6 Amazon EKS clusters](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-emr-eks-ipv6-support)
- [Amazon DynamoDB global tables with multi-Region strong consistency now supports additional AWS Regions and cross-continent configurations](https://aws.amazon.com/about-aws/whats-new/2026/09/dynamodb-mrsc-additional-regions/)
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
