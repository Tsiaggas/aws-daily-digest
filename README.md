# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-31 10:56 UTC_

- [Amazon Bedrock expands API support and introduces Cross-Region Inferencing for OpenAI models in AWS GovCloud (US)](https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-openai-runtime-govcloud/)
- [Web Search now available on Kiro in AWS GovCloud (US)](https://aws.amazon.com/about-aws/whats-new/2026/10/kiro-web-search-aws-govcloud-us/)
- [Amazon Connect Customer automatically saves in-progress emails as drafts](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-connect-email-draft-save/)
- [Daybreak Red from OpenAI now available to eligible customers on Amazon Bedrock in AWS GovCloud (US-East)](https://aws.amazon.com/about-aws/whats-new/2026/10/openai-daybreak-red-govcloud-east/)
- [Amazon CloudFront now provides viewer ISP and post-quantum TLS details](https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-viewer-isp-post-quantum-visbility/)
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
