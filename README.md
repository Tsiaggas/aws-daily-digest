# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-23 09:41 UTC_

- [Amazon CloudWatch Omni: AI-first observability for agents and applications](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-cloudwatch-omni-ai/)
- [Billing Transfer now supports automatic billing group creation for two-level transfers](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-billing-transfer-supports-automatic-billing-group-creation/)
- [OpenAI GPT-6 Sol and GPT-6 Luna are now generally available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/09/openai-gpt-6-sol-luna-on-amazon-bedrock/)
- [Claude Opus 5.5 is now available on AWS GovCloud (US)](https://aws.amazon.com/about-aws/whats-new/2026/09/claude-opus-5-5-aws-govcloud/)
- [Claude Opus 5.5 is now available on AWS](https://aws.amazon.com/about-aws/whats-new/2026/09/claude-opus-5-5-aws/)
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
