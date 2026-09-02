# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-02 09:15 UTC_

- [Amazon Quick now lets you build custom apps with natural language  -](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-quick-custom-apps-natural-language/)
- [AWS Deadline Cloud now supports sharing job bundles](https://aws.amazon.com/about-aws/whats-new/2026/09/deadline-cloud/job-bundle-sharing)
- [Amazon CloudWatch Database Insights now supports self-managed PostgreSQL](https://aws.amazon.com/about-aws/whats-new/2026/08/database-insights-self-managed-postgresql/)
- [Amazon Kinesis Data Streams now supports a dry run feature to validate API requests](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-kinesis-data-streams-api/)
- [AWS Backup now supports protecting more than 1,000 Amazon S3 buckets per account](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-backup-more-than-1000-s3-buckets/)
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
