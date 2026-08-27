# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-27 16:02 UTC_

- [Amazon Cognito adds admin API operation to reset user TOTP configurations](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cognito-totp-reset/)
- [Amazon Connect Customer now supports unplanned shrinkage in agent schedules](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-connect-customer-unplanned-shrinkage/)
- [Mountpoint for Amazon S3 adds memory usage controls](https://aws.amazon.com/about-aws/whats-new/2026/08/mountpoint-for-S3-adds-memory-usage-controls)
- [Amazon Connect Customer now supports points-based scoring in performance evaluations](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-connect-customer-points-based-scoring-evaluations/)
- [AWS Glue 5.1 is now available in AWS European Sovereign Cloud Region](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-glue-5-1-european-sovereign-cloud)
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
