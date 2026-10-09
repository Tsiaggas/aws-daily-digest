# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-09 11:56 UTC_

- [OpenAI GPT-6.1 Sol now supports Ultrafast mode on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/10/openai-gpt-sol-ultrafast-amazon/)
- [AWS Cost Explorer, Budgets, and Dashboards now support Amazon Bedrock product attributes](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-bedrock-attributes-in-cost-explorer/)
- [Amazon RDS for Oracle now supports minor version upgrade prechecks and a new RDS event to help reduce patching downtime](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-rds-oracle-minor-version-upgrade-precheck-new-patching-rds-event/)
- [AWS Network Firewall adds wildcard support for container attribute filters](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-network-firewall-container-attributes-wildcard)
- [Amazon GameLift Servers adds CPU burstability for container fleets](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-gamelift-servers-cpu-burstability)
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
