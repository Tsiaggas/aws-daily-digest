# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-11 05:50 UTC_

- [FLUX.2-small-decoder and gemma-4-12B-it models now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/flux.2-small-decoder-gemma-4-12B-it-on-sagemaker-jumpstart/)
- [langcache-embed-v3-small, Mellum2-12B-A2.5B-Thinking, and LightOnOCR-2-1B models now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/langcache-embed-v3-small-mellum2-12B-A2.5B-thinking-lightOnOCR-2-1B-on-sagemaker-jumpstart/)
- [Amazon EC2 High Memory U7i instances now available in AWS South America (São Paulo) region](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-high-memory-u7i-south-america)
- [GLM-5.2 FP8, NVIDIA-Nemotron-Nano-12B-v2 and GLM-OCR models now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/glm-5.2-fp8-nemotron-nano-12b-v2-glm-ocr-on-sagemaker-jumpstart/)
- [Amazon GameLift Streams Now Offers Service-managed Shader Caching](https://aws.amazon.com/about-aws/whats-new/2026/08/Amazon-GameLift-Streams-Shader-Caching/)
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
