# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-20 05:24 UTC_

- [Launching External Web Access for Web Search on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-web-access-web-search/)
- [Web Search in Amazon Bedrock AgentCore adds domain and published date filtering, expands to Europe and Asia Pacific](https://aws.amazon.com/about-aws/whats-new/2026/08/web-search-amazon-bedrock/)
- [Amazon CloudWatch log Centralization now supports log group tag propagation](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudwatch-centralization-tag-propogation/)
- [Amazon SageMaker notebooks now support trusted identity propagation](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-sagemaker/)
- [AWS Cost Anomaly Detection supports third-party models on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-cost-anomaly-detection-bedrock-3P/)
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
