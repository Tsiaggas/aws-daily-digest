# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-07-29 07:39 UTC_

- [Amazon EKS Provisioned Control Plane now delivers faster pod autoscaling](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-provisioned-control/)
- [Second-generation AWS Outposts racks now supported in the AWS Asia Pacific (Mumbai) Region](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-outposts-asia-pacific-mumbai/)
- [AWS Console Home now supports the Cost and Usage widget in the AWS European Sovereign Cloud (Germany) Region](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-console-home-cost-and-usage-eu-sovereign-cloud)
- [AWS DataSync Enhanced mode now supports Amazon EFS and Amazon FSx for Lustre](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-datasync-amazon-efs-fsx-lustre/)
- [AWS DataSync Enhanced mode adds HDFS, Azure Blob, and object storage locations with Hyper-V agent support](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-datasync-hdfs-azure-blob-hyper-v/)
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
