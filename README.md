# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-26 05:28 UTC_

- [AWS IoT Core now supports native InfluxDB routing for time-series data](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-iot-core-influxdb/)
- [AWS Batch now supports Amazon ECS Managed Instances](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-batch-on-ecs-managed-instances/)
- [Capacity Reservation Resource Groups now support Amazon EC2 Capacity Blocks and interruptible Capacity Reservations](https://aws.amazon.com/about-aws/whats-new/2026/08/capacity-reservation-resource-groups-ec2)
- [AWS Lambda MicroVMs now supports AWS PrivateLink](https://aws.amazon.com/about-aws/whats-new/2026/08/lambda-microvms-supports-privatelink)
- [Amazon RDS for PostgreSQL supports minor versions 18.6, 17.11, 16.15, 15.19, and 14.24](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-rds-postgresql-18-6-17-11-16-15-15-19-14-24/)
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
