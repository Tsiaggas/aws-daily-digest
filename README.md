# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-05 07:34 UTC_

- [[Preview Announcement] Re-introducing Forward Proxy as AWS Network Firewall Functionality](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-network-firewall-forward-proxy-preview/)
- [Amazon Connect Customer now lets you export cases to CSV from the agent workspace](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-connect-export-cases/)
- [Amazon Bedrock launches Web Search for OpenAI GPT models](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-web/)
- [Run interactive workloads on Amazon EMR on EC2 with Spark Connect](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-emr-ec2-spark-connect/)
- [AWS Security Hub Extended adds supply chain security as its 10th category](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-security-hub-extended-adds-supply-chain-security)
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
