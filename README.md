# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-22 07:31 UTC_

- [Amazon EC2 R6in and R6idn instances are now available in additional regions](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-r6in-r6idn/)
- [Amazon EC2 C6in instances are now available in Asia Pacific (Taipei) Region](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-c6in/)
- [Amazon EC2 M6in and M6idn instances are now available in additional regions](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-m6in-m6idn/)
- [Amazon ECS advanced deployment strategies now available in AWS European Sovereign Cloud](https://aws.amazon.com/about-aws/whats-new/2026/07/ecs-adv-deployments-eu-sovereign-cloud/)
- [Amazon SES introduces pricing plans](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ses-pricing-plans/)
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
