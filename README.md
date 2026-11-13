# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-13 13:10 UTC_

- [Amazon Cognito now supports OAuth 2.0 token exchange](https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-token-exchange/)
- [Amazon Aurora and RDS now support Graviton5-based R9g database instances](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-aurora-rds-postgresql-mysql-mariadb-r9g-instances/)
- [Amazon MWAA now supports fine-grained access control with IAM Identity Center and multi-team environments](https://aws.amazon.com/about-aws/whats-new/2026/11/mwaa-fine-grained-access-control/)
- [Amazon Connect Customer supports merging and linking related cases in the agent workspace](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-connect-cases-merge-link/)
- [Amazon SNS now supports push notifications in four additional AWS Regions](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-sns-push-four-regions/)
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
