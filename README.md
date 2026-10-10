# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-10 11:12 UTC_

- [AWS Security Hub now exports findings to S3 in CSV or JSON format](https://aws.amazon.com/about-aws/whats-new/2026/10/security-hub-exports-s3-csv-json/)
- [Amazon EC2 R8gd instances are now available in additional regions](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ec2-r8gd-thf/)
- [Amazon EC2 R8g instances now available in additional regions](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ec2-r8g-instances-thf/)
- [Amazon Bedrock now supports reasoning summaries for OpenAI models](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-bedrock-reasoning-summaries-openai/)
- [Anthropic Claude Sonnet 5.5 and Claude Opus 5.5 are now available on Kiro in AWS GovCloud (US)](https://aws.amazon.com/about-aws/whats-new/2026/06/kiro-claude-5-5-aws-govcloud-us/)
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
