# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-13 12:44 UTC_

- [Amazon CloudFront now supports AWS Lambda Web Functions as an origin](https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-lambda-web-functions-origin/)
- [Amazon EC2 G7 instances now available in Europe (Frankfurt) and Europe (Stockholm) Regions](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-g7-european-regions/)
- [Amazon Connect Customer now prefills step-by-step guides for after contact work](https://aws.amazon.com/about-aws/whats-new/2026/10/connect-customer-prefills-guides-acw)
- [AWS Lambda announces Lambda Web Functions](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-web-functions/)
- [Announcing consumption-based pricing for short-term memory in Amazon Bedrock AgentCore](https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-memory-consumption-based-pricing)
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
