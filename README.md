# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-14 07:08 UTC_

- [OpenAI GPT-5.6 Sol, Terra, and Luna now generally available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/07/openai-gpt-sol-terra/)
- [Amazon Managed Service for Prometheus is now available in Asia Pacific (New Zealand) Region](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-managed-service-prometheus-new-zealand/)
- [Amazon DocumentDB (with MongoDB compatibility) now available as a skill in the Agent Toolkit for AWS](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-documentdb-agent-skill)
- [Amazon DocumentDB (with MongoDB compatibility) adds support for 46 new MongoDB operators in version 8.0.1](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-documentdb-mongodb-8-0-1-mongo-api)
- [Gemma-4-E2B-it for is now available in Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/07/gemma-4-e2b-on-sagemaker-jumpstart/)
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
