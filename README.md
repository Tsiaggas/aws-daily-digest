# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-15 09:44 UTC_

- [Qwen3.6-35B-A3B-NVFP4 and Wan2.1-T2V-1.3B-Diffusers models now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/qwen3.6-35b-a3b-nvfp4-wan2.1-t2v-1.3B-diffusers-jumpstart/)
- [Ministral-3-3B-Instruct-2512 and Ministral-3-8B-Instruct-2512 models now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/ministral-3-3b-instruct-2512-ministral-3-8B-Instruct-2512-jumpstart/)
- [Gemma-4-31B-it-assistant and Gemma-4-31B-IT-NVFP4 models now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/gemma-4-31b-it-assistant-gemma-4-31b-it-nvfp4-jumpstart/)
- [granite-speech-4.1-2b, kanana-2-30b-a3b-instruct, and OpenFold3 models now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/granite-speech-4.1-2b-edge-kanana-2-30b-a3b-instruct-openfold3-jumpstart/)
- [AWS Glue zero-ETL adds target table property ownership and conflict detection](https://aws.amazon.com/about-aws/whats-new/2026/09/glue-zero-etl-ownership-conflicts/)
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
