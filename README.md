# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-26 09:39 UTC_

- [Amazon Transcribe adds customer-managed KMS keys for custom resources](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-transcribe/)
- [Amazon EC2 M8i and M8i-flex instances are now available in additional regions](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ec2-m8i-m8i-flex-thf/)
- [Amazon EC2 R8i and R8i-flex instances are now available in additional regions](https://aws.amazon.com/about-aws/whats-new/2026/09/ec2-r8i-r8i-flex-thf/)
- [Amazon EC2 C8i and C8i-flex instances are now available in additional regions](https://aws.amazon.com/about-aws/whats-new/2026/09/c8i-c8i-flex-thf-september-2026/)
- [AWS IAM outbound identity federation now supports interface VPC endpoints for OIDC discovery](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-sts-vpc-oidc/)
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
