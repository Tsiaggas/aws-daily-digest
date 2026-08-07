# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-07 06:06 UTC_

- [Amazon ECS now supports fractional GPU scheduling with Amazon EC2 G6f instances](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ecs-fractional-gpu/)
- [AWS Lambda console extends console-to-IDE integration to Kiro and Cursor](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-lambda-ide-kiro-cursor/)
- [Amazon EC2 G7 instances are now available in the AWS Europe (Spain) Region](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-g7-available-spain)
- [AgentCore runtime instances are now generally available](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/)
- [Amazon ElastiCache now supports Graviton4-based M8g, R8g, and C8gn nodes](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-elasticache-graviton4-m8g-r8g-c8gn/)
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
