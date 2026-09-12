# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-12 08:58 UTC_

- [Amazon EC2 X2idn instances are now available in Asia Pacific (Hong Kong)](https://aws.amazon.com/about-aws/whats-new/2026/09/ec2-x2idn-asia-pacific-hong-kong/)
- [Amazon SageMaker HyperPod now supports model caching for faster inference autoscaling and reduced cold starts](https://aws.amazon.com/about-aws/whats-new/2026/09/sgm-hyperpod-model-caching-inf/)
- [AWS Lambda now supports direct read configuration for Amazon S3 Files](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-lambda-direct-read-s3files/)
- [Amazon Bedrock Managed Knowledge Base now supports multimodal embeddings for video, audio, and image content with TwelveLabs Marengo 3.0](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-managed-knowledge-base-multimodal-embeddings-twelvelabs-marengo/)
- [AWS HealthOmics now publishes real-time run metrics to Amazon CloudWatch](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-healthomics-realtime-run-metrics/)
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
