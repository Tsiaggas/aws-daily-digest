# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-07 11:45 UTC_

- [Kimi K3.1 Pro (Highspeed) now available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/11/moonshot-ai-kimi-k3-1-pro-on-amazon-bedrock)
- [Agent Registry is now generally available in AWS GovCloud (US-West) Region](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-agent-registry-govcloud-us-west/)
- [Amazon MSK Replicator is now available in AWS GovCloud (US-East, US-West) Regions](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-msk-replicator-additional-aws-regions)
- [Amazon Redshift expands SUPER data type to store strings up to 16 million bytes](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-redshift-expands-super-to-16-million-bytes/)
- [AWS launches support for amortization of EC2 Capacity Blocks for ML](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-ec2-capacity-blocks-ml/)
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

<!-- docs: add maintenance note 2026-10-09 -->

<!-- docs: update maintenance note 2026-10-09 -->
