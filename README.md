# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-04 10:50 UTC_

- [Amazon ECS adds Amazon VPC Lattice support for blue/green, linear, and canary deployments](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ecs-vpc-lattice-blue-green-deployments)
- [AWS Health introduces the version catalog for software lifecycle management](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-health-introduces-version-catalog-software-lifecycle-management)
- [Amazon Aurora DSQL now supports partial indexes](https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-dsql-partial-indexes/)
- [Amazon EKS and Amazon EKS Distro now support Kubernetes version 1.37](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-eks-distro-kubernetes-version-1-37)
- [AWS Brazil automates distribution of non-Brazilian software product licenses to Brazilian customers](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-brazil-software-license-distribution/)
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
