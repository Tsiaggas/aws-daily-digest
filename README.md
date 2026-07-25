# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-25 07:11 UTC_

- [Amazon Connect now supports audio optimization for Azure Virtual Desktop and Windows 365 Cloud PC](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-connect/)
- [Amazon MWAA now supports Apache Airflow version 2.11.2](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-mwaa-now-supports-apache-airflow-version-2-11-2)
- [Amazon EC2 Dedicated Hosts now support host resource groups without self-managed licenses](https://aws.amazon.com/about-aws/whats-new/2026/07/ec2-dedicated-hosts-hrg/)
- [Amazon Kinesis Data Streams now supports scaling down ingest capacity with warm throughput](https://aws.amazon.com/about-aws/whats-new/2026/07/kinesis/on-demand-scale-down)
- [AWS Lambda now publishes logs for Lambda Managed Instances capacity providers](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-lambda-managed-instances-logs/)
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
