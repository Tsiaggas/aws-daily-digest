# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-06 12:58 UTC_

- [AWS Security Hub now provides an SBOM inventory for your compute resources](https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-sbom-inventory/)
- [AWS Interconnect - last mile announces new metro in Northern Virginia, USA](https://aws.amazon.com/about-aws/whats-new/2026/11/interconnect-last-mile-northern-virginia/)
- [Announcing Web Answer on Amazon Bedrock AgentCore](https://aws.amazon.com/about-aws/whats-new/2026/11/web-answer-amazon-bedrock/)
- [AWS Network Load Balancer is now available in the AWS Phoenix Local Zone](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-nlb-available-phx-local-zone/)
- [Amazon DynamoDB now supports bulk put items](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-dynamodb-now-supports-bulk-put-items/)
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
