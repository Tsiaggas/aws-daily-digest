# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-10-16 09:53 UTC_

- [Web Search on Amazon Bedrock AgentCore expands to AWS GovCloud and 3 Regions](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-bedrock-agentcore/)
- [Amazon SageMaker Studio simplifies getting started for new AI/ML builders with new sign-in options](https://aws.amazon.com/about-aws/whats-new/2026/10/sagemaker-studio-new-sign-in-options/)
- [Amazon EC2 T8i instances are now available in South America (São Paulo)](https://aws.amazon.com/about-aws/whats-new/2026/10/ec2-t8i-instances-south-america/)
- [Amazon DynamoDB Streams now supports timestamp-based stream processing](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-dynamodb-streams-timestamp-processing)
- [AWS Lambda Durable Execution SDK for Go is now generally available](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-go-sdk-support/)
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
