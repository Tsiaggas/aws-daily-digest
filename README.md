# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-21 10:13 UTC_

- [Announcing Amazon ECS Gateway, a managed ingress solution for your ECS services](https://aws.amazon.com/about-aws/whats-new/2026/10/announcing-amazon-ecs-gateway/)
- [Amazon DynamoDB global tables now support disassociating replicas](https://aws.amazon.com/about-aws/whats-new/2026/10/dynamodb-global-tables-disassociate/)
- [Polly Generative engine upgraded with more natural speech, 14 new voices, and 2 new languages](https://aws.amazon.com/about-aws/whats-new/2026/10/polly-generative/)
- [AWS announces TorchNeuron: Native PyTorch Support for AWS Trainium (Public Beta)](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-announce-native-pytorch-support-trainium)
- [Structured outputs for Claude models available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/10/claude-structured-outputs-bedrock/)
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
