# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-16 09:38 UTC_

- [Monitor cost anomalies directly in Billing and Cost Management Dashboards with the new Detected Anomalies widget](https://aws.amazon.com/about-aws/whats-new/2026/09/monitor-detected-anomalies-using-dashboards)
- [AWS Direct Connect announces flat-rate pricing for dedicated connections](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-direct-connect-announces-flat-rate-pricing/)
- [AWS Billing Conductor now supports custom rates and usage tier pricing configurations](https://aws.amazon.com/about-aws/whats-new/2026/09/AWS-Billing-Conductor-custom-rates-usage-tier)
- [Amazon SageMaker AI now supports instance preference lists for training and processing jobs](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-sagemaker-training-processing-instance-pref-lists/)
- [Analyze your CloudTrail events using natural language in Amazon Q Console](https://aws.amazon.com/about-aws/whats-new/2026/09/cloudtrail-amazon-q-console/)
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
