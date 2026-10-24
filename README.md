# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-24 09:35 UTC_

- [Web Search on AWS Bedrock now supports domain filtering and user location controls](https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-web-search-domain-user-location/)
- [Amazon Connect Customer Global Resiliency now supports persistent chat across linked AWS Regions](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-connect-global-resiliency-persistent-chat)
- [AWS Transit Gateway and AWS Cloud WAN now support 1:1 NAT](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-transit-gateway-cloud-wan-1-1-nat/)
- [Amazon Corretto October 2026 Quarterly Updates](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-corretto-october-2026-quarterly-updates)
- [Amazon MWAA now available in Mexico (Central) Region](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-mwaa-mexico-central/)
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
