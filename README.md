# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-04 07:33 UTC_

- [AWS Transform continuous modernization is now generally available](https://aws.amazon.com/about-aws/whats-new/2026/7/aws-transform-continuous-general-available)
- [OpenAI GPT-5.6 Sol, Terra, and Luna now support 1 million token context windows on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/08/gpt-sol-terra-luna-long-context-bedrock)
- [Amazon GameLift Streams now supports sharing streams with stream URLs](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-gamelift-streams/)
- [AWS Resilience Hub now provides recommended resilience tests](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-resilience-hub/)
- [AWS Organizations now provides maximum account quota visibility in Service Quotas](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-organizations/)
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
