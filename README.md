# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-21 05:26 UTC_

- [AWS announces the general availability of a new AWS Local Zone in Las Vegas, Nevada](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-local-zones-las-vegas-nevada/)
- [Amazon Timestream for InfluxDB now supports customer managed keys](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-timestream-influxdb-cmk/)
- [Amazon EC2 P6-B300 instances are now available in the Asia Pacific (Seoul) Region](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-p6-b300/)
- [Amazon EKS now supports certificate authority (CA) rotation with automated lifecycle management](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-certificate-authority-ca-rotation-automated-lifecycle-management)
- [Amazon CloudFront now supports Origin Access Control (OAC) for Amazon S3 Multi-Region Access Points](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudfront-oac-s3-mrap)
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
