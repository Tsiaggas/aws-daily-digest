# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-31 07:47 UTC_

- [Amazon SageMaker Unified Studio brings richer Git version control to all project tools](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-sagemaker-unified-studio-git/)
- [AWS Direct Connect now supports BGP route visibility on Virtual Interfaces](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-direct-connect-bgp-visibility/)
- [Amazon Redshift RG large and 12xlarge instances now available on the trailing track](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-redshift-rg-large-12xlarge-trailing-track)
- [IAM Policy Simulator moves to the IAM console and adds additional capabilities](https://aws.amazon.com/about-aws/whats-new/2026/07/iam-policy-simulator-iam-console/)
- [Amazon Bedrock announces up to 80% lower prices for OpenAI GPT‑5.6 models](https://aws.amazon.com/about-aws/whats-new/2026/07/openai-gpt-terra-luna-pricing-bedrock/)
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
