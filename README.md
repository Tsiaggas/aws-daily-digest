# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-09 09:21 UTC_

- [OpenAI GPT-6 Astra is now generally available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/09/openai-gpt-6-astra-on-amazon-bedrock/)
- [Amazon Timestream for InfluxDB 3 now supports custom plugins](https://aws.amazon.com/about-aws/whats-new/2026/09/timestream-influxdb-custom-plugins/)
- [Amazon SageMaker Feature Store now supports individual feature updates to lower write latency](https://aws.amazon.com/about-aws/whats-new/2026/08/sgm-feature-store-update-record/)
- [AWS Transform is now available in AWS GovCloud (US-West)](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-transform-govcloud-us-west/)
- [Amazon API Gateway now supports mutual TLS for backend integrations](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-api-gateway-mutual-tls-backend/)
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
