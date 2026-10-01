# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-01 11:18 UTC_

- [Amazon WorkSpaces Core Managed Instances adds support for NVIDIA Blackwell GPU](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-workspaces-cmi-g7/)
- [AWS CLI now supports bulk skill updates and version checks for the Agent Toolkit for AWS](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-cli-agent-toolkit-update-skill/)
- [Amazon S3 Vectors introduces metadata pre-filtering for up to 5x higher recall on filtered search](https://aws.amazon.com/about-aws/whats-new/2026/09/s3-vectors-introduces-metadata-pre-filtering/)
- [Amazon Managed Grafana now supports creating Grafana 13.2 workspaces](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-managed-grafana-now-supports-creating-grafana-13-2-workspaces)
- [OpenAI GPT-6 Astra now supports UltraFast mode on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/09/openai-gpt-6-astra-ultrafast-on-amazon-bedrock/)
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
