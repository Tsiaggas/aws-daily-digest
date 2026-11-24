# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-24 15:55 UTC_

- [Amazon EC2 X8i instances are now available in the Asia Pacific (New Zealand) Region](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-x8i-new-zealand/)
- [AWS Sign-In introduces configurable Sign-in duration of up to 90 days](https://aws.amazon.com/about-aws/whats-new/2026/11/configurable-aws-sign-in-duration/)
- [Amazon SageMaker HyperPod now supports managed observability and user management extensions for Slurm clusters](https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-hyperpod-extensions/)
- [Amazon OpenSearch Service now supports OpenSearch version 3.9](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-opensearch-3-9)
- [AWS WAF introduces simplified pricing](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-waf-introduces-simplified-pricing/)
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
