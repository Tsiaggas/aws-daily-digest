# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-04 09:16 UTC_

- [Amazon ECS Managed Daemons now support non-critical daemons](https://aws.amazon.com/about-aws/whats-new/2026/09/ecs-managed-daemons-non-critical/)
- [Amazon EC2 P6-B200 instances are now available in the AWS Asia Pacific (Hyderabad) Region](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ec2-p6-b200-instances-available-asia-pacific-hyderabad)
- [Amazon EC2 P6-B300 instances are now available in the AWS Asia Pacific (Jakarta) Region](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ec2-p6-b300-instances-available-asia-pacific-jakarta)
- [Amazon CloudFront announces API support for flat-rate pricing plans](https://aws.amazon.com/about-aws/whats-new/2026/09/cloudfront-flat-rate-pricing-plans-api/)
- [Introducing Amazon Quick Max: 5x the usage for power users who want the most out of Quick](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-quick-max-5x-usage-power-users/)
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
