# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-22 05:21 UTC_

- [Amazon Bedrock announces reduced pricing for OpenAI GPT-5.6 Sol](https://aws.amazon.com/about-aws/whats-new/2026/08/bedrock-openai-gpt-56-sol-reduced-pricing/)
- [Amazon Connect Customer now lets managers chat with their data](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-connect-customer-ai-data-analytics)
- [AWS Deadline Cloud now tracks automatic download status in the Deadline Cloud Monitor](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-deadline-cloud-auto-download-status-tracking/)
- [Amazon EKS Capability for Argo CD now supports custom configuration](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-argo-cd-configuration)
- [AWS Glue 6.0 delivers 30% price reduction and Iceberg v3 support](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-glue-6-0-price-reduction-iceberg-v3)
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
