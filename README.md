# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-27 10:38 UTC_

- [OpenAI GPT-6.1 Terra is now generally available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/10/openai-gpt-6-1-terra-on-amazon-bedrock/)
- [Amazon WorkSpaces Core Managed Instances now supports ModifyVolume API](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-workspaces-cmi-modifyvolume/)
- [Amazon SageMaker Unified Studio adds light mode support for IDC-based domains](https://aws.amazon.com/about-aws/whats-new/2026/10/smus-light-mode)
- [Amazon Connect Customer expands testing and simulation to validate flow action outcomes](https://aws.amazon.com/about-aws/whats-new/2026/10/connect-customer-validate-flow-actions/)
- [Amazon Connect Customer now lets you view metrics by customer lifetime value and repeat-caller status](https://aws.amazon.com/about-aws/whats-new/2026/10/connect-customer-boma-segment/)
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

<!-- docs: add maintenance note 2026-10-09 -->

<!-- docs: update maintenance note 2026-10-09 -->
