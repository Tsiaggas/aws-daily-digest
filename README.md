# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-15 07:11 UTC_

- [AWS Elastic Disaster Recovery now supports Amazon EBS volume initialization rate](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-drs-fast-hydration/)
- [AWS Lambda console provides a one-click setup prompt for coding agents](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-lambda-prompt-coding-agents/)
- [AWS IAM Identity Center achieves FedRAMP Class C Certification](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-identity-center-fedramp/)
- [Introducing Amazon GuardDuty AI Protection for AWS AI workloads](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-guardduty-ai-protection-aws/)
- [Amazon Managed Service for Apache Flink now offers AI Agent Skills to simplify building and operating Flink applications](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-managed-service-flink-agent-skills/)
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
