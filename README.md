# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-17 14:29 UTC_

- [Amazon ECR now replicates image deletions across regions and accounts](https://aws.amazon.com/about-aws/whats-new/2026/11/replication-deletes-amazon-ecr)
- [Amazon EBS now supports associating additional KMS keys with snapshots](https://aws.amazon.com/about-aws/whats-new/2026/11/ebs-snapshots-associate-kms-keys/)
- [Amazon S3 Vectors now supports hybrid search combining vector and full text for more relevant search results](https://aws.amazon.com/about-aws/whats-new/2026/11/s3-vectors-hybrid-search/)
- [Amazon Redshift now supports multi-statement transactions, conflict resolution, and time travel for Apache Iceberg](https://aws.amazon.com/about-aws/whats-new/2026/11/redshift-time-travel-multi-statement)
- [AWS DevOps Agent is now available in AWS GovCloud (US-West)](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-devops-agent-govcloud-west/)
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
