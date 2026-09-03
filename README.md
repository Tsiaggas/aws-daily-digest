# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-09-03 09:23 UTC_

- [Web Search on Amazon Bedrock is now available in AWS GovCloud (US-West)](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-web-aws-govcloud/)
- [Amazon Connect Customer expands automated performance evaluations to Malay](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-connect-customer-automated-evaluations-malay/)
- [Amazon Quick adds new tool settings and Model Context Protocol (MCP) sync support for connectors](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-quick-adds-tool-settings-mcp-sync/)
- [Amazon Connect Customer announces general availability of agentic CX designer](https://aws.amazon.com/about-aws/whats-new/2026/09/agentic-cx-designer/)
- [Second-generation AWS Outposts racks now in the AWS GovCloud (US) Regions](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-outposts-govcloud-us-regions/)
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
