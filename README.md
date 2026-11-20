# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-20 14:03 UTC_

- [Announcing the general availability of a new AWS Local Zone in Bogotá, Colombia](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-local-zone-bogota-colombia/)
- [AWS DevOps Agent now supports Slack code channels and Microsoft Teams two-way conversations](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-devops-agent-slack-code-channels-teams-two-way/)
- [AWS Marketplace now supports agentic payments with AgentCore](https://aws.amazon.com/about-aws/whats-new/2026/11/marketplace-agentic-payments-agentcore/)
- [Amazon Cognito now supports client ID metadata documents](https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-client-id-metadata-documents/)
- [Amazon Aurora DSQL now delivers up to 50% higher write throughput](https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-dsql-higher-write-throughput/)
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
