# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-30 10:51 UTC_

- [Amazon Bedrock Managed Agents, powered by OpenAI, is now available in preview](https://aws.amazon.com/about-aws/whats-new/2026/09/bedrock-managed-agents-preview/)
- [Amazon RDS now adds full snapshot size information to the Console and API](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-rds-full-snapshot-size-available/)
- [OpenAI GPT-6.1 Sol is now generally available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/09/openai-gpt-6-1-sol-on-amazon-bedrock/)
- [Amazon Connect Customer now lets business users manage more reference data to adjust contact center configurations in real time](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-connect-manage-data-tables/)
- [Amazon WorkSpaces Applications introduces unified graphics images](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-workspaces-applications-unified-graphics-images/)
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
