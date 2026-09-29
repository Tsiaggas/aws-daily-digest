# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-29 11:01 UTC_

- [Amazon EC2 Future-dated Capacity Reservations Now Supports Postponing Start Dates](https://aws.amazon.com/about-aws/whats-new/2026/09/ec2-fcr-postpone-start-date/)
- [Amazon Rekognition Face Liveness now returns Feedback Codes](https://aws.amazon.com/about-aws/whats-new/2026/09/rekognition-liveness-feedback-codes/)
- [Grok 4.7 is now available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-grok-4-7/)
- [Claude Sonnet 5.5 now available on AWS](https://aws.amazon.com/about-aws/whats-new/2026/09/claude-sonnet-5-5-aws/)
- [Claude Sonnet 5.5 now available on AWS GovCloud (US)](https://aws.amazon.com/about-aws/whats-new/2026/09/claude-sonnet-5-5-aws-govcloud-us/)
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
