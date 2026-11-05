# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-05 13:15 UTC_

- [Amazon ECS Managed Daemons can now collect json-file logs from application containers on Amazon ECS Managed Instances](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ecs-managed-instances-json-file-log-driver/)
- [Amazon DocumentDB (with MongoDB compatibility) is now available in the Asia Pacific (Taipei) and Asia Pacific (New Zealand) Regions](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-documentdb-mongodb-compatibility-asia-pacific-taipei-new-zealand-regions/)
- [Amazon RDS for Oracle now supports copying option groups during cross-Region snapshot copy](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-oracle-cross-region-snapshot-copy-option-group/)
- [AWS announces AWS Interconnect - last mile preview with Equinix](https://aws.amazon.com/about-aws/whats-new/2026/11/interconnect-last-mile-preview-equinix/)
- [Amazon Connect Customer now shows associated cases in contact records](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-connect-cases-contact-records/)
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
