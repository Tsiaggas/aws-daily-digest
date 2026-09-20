# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-20 09:33 UTC_

- [AWS Continuum now supports credential testing and accessible domain suggestions](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-security-agent/)
- [Amazon ECS Express Mode now supports AWS Graviton (ARM64) workloads](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ecs-express-mode-arm-architecture/)
- [AWS Resilience Hub adds three new capabilities](https://aws.amazon.com/about-aws/whats-new/2026/09/resilience-hub-eks-dependency-policy/)
- [AWS RTB Fabric now supports configurable Availability Zone affinity](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-rtb-fabric-configurable-availability-zone-affinity/)
- [Kimi K3 by Moonshot AI is now generally available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/09/moonshot-ai-kimi-k3-on-amazon-bedrock/)
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
