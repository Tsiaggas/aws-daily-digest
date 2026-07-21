# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-21 07:29 UTC_

- [AWS Data Exports now provides standardized Amazon Bedrock product metadata](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-data-exports-amazon-bedrock-product-metadata/)
- [Amazon EC2 R8i and R8i-flex instances are now available in additional regions](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-r8i-r8i-flex-instances-in-stockholm-zurich-regions/)
- [Selectively log network activity events by identity in AWS CloudTrail](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-cloudtrail-filter-useridentity-advance-selectors/)
- [Amazon Connect delivers more natural agentic voice experiences with expanded language support and speech controls](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-connect-agentic-voice/)
- [Amazon EC2 I8ge instances are now available in AWS GovCloud (US) Regions](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-i8ge-instances-aws-govcloud-us-regions/)
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
