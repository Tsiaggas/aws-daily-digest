# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-06 12:03 UTC_

- [Amazon Redshift adds support for creating and refreshing Apache Iceberg materialized views](https://aws.amazon.com/about-aws/whats-new/2026/10/redshift-iceberg-materialized-views)
- [GLM 5.3 by Z.ai is now generally available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-bedrock-glm-5-3/)
- [AWS IAM Identity Center now supports network access controls for Identity Store](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-identity-store-network-controls/)
- [AWS Continuum for Penetration Testing now supports continuous penetration testing integrated directly into your CI/CD pipeline](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-continuum-penetration-testing/)
- [AWS Advanced Ruby Driver Wrapper is generally available](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-ruby-driver-wrapper-available/)
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
