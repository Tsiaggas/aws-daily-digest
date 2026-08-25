# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-08-25 05:26 UTC_

- [Amazon ECS now automatically detects and repairs container instances with impaired agent connectivity](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ecs-agent-connectivity-health)
- [SageMaker MLflow now supports customer managed keys](https://aws.amazon.com/about-aws/whats-new/2026/08/sagemaker-mlflow-custom-keys)
- [Amazon EKS now supports multiple external OIDC identity providers per cluster](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-multiple-oidc-providers)
- [Amazon Aurora now supports PostgreSQL 18.4, 17.10, 16.14, 15.18, and 14.23](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-aurora-postgresql-18-4-17-10-16-14-15-18-14-23/)
- [Amazon SageMaker HyperPod enhances support for Ray](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-sagemaker-hyperpod-ray)
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
