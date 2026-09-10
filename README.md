# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-10 09:20 UTC_

- [Amazon Connect Customer now lets you set specific capacity limits for different types of Tasks and Emails](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-connect-capacity-limits/)
- [AWS Transform for .NET modernization is now generally available via CLI](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-transform-dotnet-cli)
- [AWS Lambda now supports 90-minute function timeout on Lambda Managed Instances](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-lambda-90-minute-function/)
- [AWS Lambda now supports Graviton5-powered EC2 instances on Lambda Managed Instances](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-lambda-graviton5-ec2/)
- [Amazon Bedrock Managed Knowledge Base adds APIs and console support for debugging document-level access control](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-knowledge-base-debugging-document-access-control/)
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
