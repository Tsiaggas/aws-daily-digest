# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-17 09:25 UTC_

- [Amazon CloudWatch log centralization now available in AWS GovCloud and additional commercial Regions](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-cloudwatch-centralization-region-expansion)
- [AWS Lambda durable functions are now available in AWS GovCloud (US) Regions](https://aws.amazon.com/about-aws/whats-new/2026/10/durablefunctions-govcloud/)
- [Nemotron 3.5 Super VL model now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/nvidia-nemotron-3.5-super-vl-on-sagemaker-jumpstart/)
- [Beam model by Reflection is now available on Amazon SageMaker JumpStart and AWS Trainium](https://aws.amazon.com/about-aws/whats-new/2026/01/reflection-beam-on-sagemaker-jumpstart-and-aws-trainium/)
- [AWS Transform announces Azure-to-AWS cloud-native code conversion](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-transform-azure-to-aws-code-conversion/)
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
