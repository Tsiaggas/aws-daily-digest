# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-01 07:24 UTC_

- [Amazon Aurora DSQL adds multi-Region cluster support in four more Regions](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-aurora-dsql-adds-multi-region-clusters-four-more-regions/)
- [Amazon RDS for Oracle now offers Reserved Instances for R8i and M8i instances](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-rds-oracle-r8i-m8i/)
- [AWS Lambda now supports Java 8, 11, and 17 on Amazon Linux 2023](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-lambda-java-amazon-linux/)
- [Amazon CloudWatch announces managed Prometheus collectors](https://aws.amazon.com/about-aws/whats-new/2026/07/cloudwatch-managed-collectors/)
- [AWS CodeDeploy now available in five additional AWS regions](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-codedeploy-five-additional-regions)
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
