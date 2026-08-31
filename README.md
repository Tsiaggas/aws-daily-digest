# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-31 11:17 UTC_

- [Amazon EC2 C8gn instances are now available in AWS Europe (Paris) region](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-c8gn-europe-paris/)
- [Amazon Bedrock AgentCore Memory now supports fine-grained access control](https://aws.amazon.com/about-aws/whats-new/2026/08/agentcorememory-fine-grained-access-control)
- [Amazon Bedrock AgentCore Memory now supports flexible namespace variables](https://aws.amazon.com/about-aws/whats-new/2026/08/agentcorememory-flexible-namespaces)
- [AWS Transform now in scope for FedRAMP Class C](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-transform-fedramp-class-c/)
- [Amazon EC2 P6-B300 instances are now available in additional AWS Regions](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-p6-b300-instances-available-additional-regions)
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
