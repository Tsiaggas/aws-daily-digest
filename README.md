# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-07 08:18 UTC_

- [Amazon SageMaker HyperPod now supports disaggregated prefill and decode](https://aws.amazon.com/about-aws/whats-new/2026/7/amazon-sagemaker-hyperpod-dpd/)
- [Amazon Cognito now supports self-service provisioned API rate limits](https://aws.amazon.com/about-aws/whats-new/2026/07/cognito-provisioned-limits)
- [Amazon SageMaker Studio now integrates with Hugging Face for one-click model deployment and customization](https://aws.amazon.com/about-aws/whats-new/2026/07/sagemaker-studio-hugging-face-integration/)
- [Amazon EVS VCF 9.0 and 9.1 support](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-evs-vcf9)
- [AWS Certificate Manager now supports the ACME protocol for public certificates](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-certificate-manager-acme/)
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
