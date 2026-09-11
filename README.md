# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-11 09:19 UTC_

- [AWS Lambda recursive loop detection is now available in Europe Sovereign Cloud](https://aws.amazon.com/about-aws/whats-new/2026/09/lambda-recursion-europe-sovereign-cloud)
- [AWS Transform for .NET now generates unit tests for modernized code](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-transform-net-unit-tests)
- [Amazon API Gateway now supports 1 MB execution logs with configurable delivery destinations](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-api-gateway-1-mb-execution-logs/)
- [AWS Lambda durable functions integrates with Pydantic AI](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-lambda-durable-pydantic-ai/)
- [Amazon MQ now supports RabbitMQ 4.3](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-mq-rabbitmq-43/)
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
