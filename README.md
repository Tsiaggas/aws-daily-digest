# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-10 06:07 UTC_

- [Amazon EC2 R8i and R8i-Flex instances are now available in Europe (Milan) region](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-r8i-r8i-flex/)
- [Amazon Timestream for InfluxDB now supports backup and restore](https://aws.amazon.com/about-aws/whats-new/2026/07/timestream-influxdb-backup-restore/)
- [Amazon Cognito now available as a skill in the Agent Toolkit for AWS](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-auth-agent-skill/)
- [AWS IAM Identity Center supports one-click multi-Region option for new organization instances](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-iam-identity-center-supports-one-click-multi-region-option-new-organization-instances)
- [Amazon VPC IPAM now supports BGP route protection monitoring and delegated RPKI for BYOIP prefixes](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-vpc-ipam-bgp-rpki-byoip/)
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
