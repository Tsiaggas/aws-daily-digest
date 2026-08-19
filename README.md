# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-19 05:23 UTC_

- [Amazon Bedrock now supports OpenAI models in India](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-openai-india-v1/)
- [AWS IAM identity federation to external services is now available in AWS European Sovereign Cloud Region](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-iam-european-sovereign-cloud/)
- [Amazon Corretto August 2026 Critical Security Patch Updates](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-corretto-august-2026-security-updates)
- [AgentCore payments is now generally available in Amazon Bedrock AgentCore](https://aws.amazon.com/about-aws/whats-new/2026/08/bedrock-agentcore-payments-ga/)
- [Amazon SageMaker Unified Studio now supports data profiling and anomaly detection](https://aws.amazon.com/about-aws/whats-new/2026/05/smus-data-profiling)
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
