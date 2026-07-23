# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-23 07:28 UTC_

- [Amazon EC2 C7a instances are now available in the US West (N. California) Region](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-c7a-instances-us-west-ncalifornia-region/)
- [Amazon EC2 M8a instances now available in the Asia Pacific (Hyderabad) region](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-m8a-instances-asia-pacific-hyderabad-region/)
- [AWS Network Load Balancer now supports Listener Rules for custom traffic routing](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-network-load-balancer-supports-listener-rules/)
- [AWS Entity Resolution now supports advanced real-time matching](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-entity-resolution/)
- [AWS Lambda durable functions now supports customer managed key encryption](https://aws.amazon.com/about-aws/whats-new/2026/07/durablefunctions-cmk/)
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
