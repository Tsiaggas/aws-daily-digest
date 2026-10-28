# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-28 11:22 UTC_

- [Amazon ECS now supports GPU sharing with NVIDIA Multi-Process Service (MPS)](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ecs-gpu-sharing-nvidia-mps/)
- [SageMaker MLflow Apps now support MLflow 3.16](https://aws.amazon.com/about-aws/whats-new/2026/10/mflow-version-3-16/)
- [Amazon Aurora serverless now supports up to 384 ACUs](https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-serverless-supports-384-acu/)
- [Amazon ElastiCache for Valkey now supports changing durability on existing clusters](https://aws.amazon.com/about-aws/whats-new/2026/10/elasticache-changing-durability/)
- [Amazon Corretto October 2026 Patch Updates](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-corretto-oct-2026-patch-updates)
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
