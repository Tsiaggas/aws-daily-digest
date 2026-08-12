# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-12 06:09 UTC_

- [Amazon EC2 R8a instances are now available in Canada (Central) region](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-r8a-instances-canada-central/)
- [Amazon Bedrock expands IAM principal cost allocation to the bedrock-mantle endpoint](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-expands-iam-principal-cost-allocation-bedrock-mantle/)
- [LocateAnything-3B, Qwen-AgentWorld-35B-A3B, and Qwen3.5-122B-A10B models now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/locateAnything-3B-qwen-agentworld-35B-A3B-qwen3.5-122B-A10B-on-sagemaker-jumpstart/)
- [NVIDIA Nemotron 3.5 Lightning model is now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/nvidia-nemotron-3.5-lightning-on-sagemaker-jumpstart/)
- [AWS Glue adds one-click access to SageMaker Unified Studio from the AWS console](https://aws.amazon.com/about-aws/whats-new/2026/08/smus-glue-access)
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
