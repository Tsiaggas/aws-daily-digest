# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-24 07:28 UTC_

- [Amazon ECS Service Connect now supports Zone-Aware routing](https://aws.amazon.com/about-aws/whats-new/2026/07/ecs-service-connect-zone-aware/)
- [AWS now supports automatic credit memo application preferences](https://aws.amazon.com/about-aws/whats-new/2026/07/credit-memo-applications/)
- [Amazon RDS for MySQL supports MySQL 9.7 in Amazon RDS Database Preview Environment](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-rds-mysql-long-term-9-7-rds-database-preview/)
- [AWS Lambda durable execution SDK for .NET is now generally available](https://aws.amazon.com/about-aws/whats-new/2026/07/lambdadf-dotnet/)
- [Amazon Bedrock AgentCore now delivers unified observability with traces and logs in a single log group](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-bedrock-agentcore-unified-observability-single-log-group/)
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
