# ☁️ AWS Daily Digest

Automated pipeline that tracks the [AWS "What's New"](https://aws.amazon.com/new/) feed and commits a daily Markdown digest — fully hands-off via **GitHub Actions cron**.

## Latest announcements

<!-- LATEST:START -->
_Last update: 2026-11-23 16:02 UTC_

- [Amazon CloudWatch Query Studio now supports saved queries](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-query-studio-saved-queries)
- [AWS Quick now supports plugins to bundle agents, skills, connectors and flows](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-quick-plugins-bundle-agents-skills-connectors-flows/)
- [Amazon CloudWatch Omni now supports Microsoft Azure platform logs, metrics and traces](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-omni-microsoft-azure)
- [AWS Quick launches a new web experience with updated browser extension and Microsoft 365 add-ins](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-quick-launches-new-web-experience-updated-browser-extension-microsoft-365-add-ins/)
- [Web Search on Amazon Bedrock expands language support and country-aware search](https://aws.amazon.com/about-aws/whats-new/2026/11/web-search-amazon-bedrock/)
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
