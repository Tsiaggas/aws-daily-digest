# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-23 10:08 UTC_

- [Amazon Connect Customer now supports customizing the Customer Profiles app on the agent workspace](https://aws.amazon.com/about-aws/whats-new/2026/10/connect-customer-customize-cp)
- [AWS Continuum for code vulnerabilities is now generally available](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-continuum-for-code-vulnerabilities-is-now-generally-available)
- [Amazon OpenSearch Serverless now supports a 5-second default refresh interval](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-opensearch-serverless-supports-5-second-refresh-interval/)
- [AWS CloudFormation now simplifies stack update rollback operations](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-cloudformation-cdk/)
- [Amazon SageMaker AI announces training session APIs for serverless model customization](https://aws.amazon.com/about-aws/whats-new/2026/10/training-session-apis-on-sagemaker-ai)
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
