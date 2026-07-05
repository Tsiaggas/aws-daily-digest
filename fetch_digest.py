#!/usr/bin/env python3
"""Fetch the latest AWS "What's New" announcements and write a daily digest.

Runs via GitHub Actions cron (see .github/workflows/daily.yml).
Writes digests/YYYY/MM/YYYY-MM-DD.md and refreshes the "Latest" section in README.md.
"""
from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import feedparser

FEED_URL = "https://aws.amazon.com/about-aws/whats-new/recent/feed/"
MAX_ITEMS = 15
ROOT = Path(__file__).parent


def fetch_items() -> list[dict]:
    feed = feedparser.parse(FEED_URL)
    items = []
    for entry in feed.entries[:MAX_ITEMS]:
        items.append({
            "title": entry.get("title", "(no title)").strip(),
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
        })
    return items


def write_digest(items: list[dict], today: datetime) -> Path:
    day = today.strftime("%Y-%m-%d")
    path = ROOT / "digests" / today.strftime("%Y") / today.strftime("%m") / f"{day}.md"
    path.parent.mkdir(parents=True, exist_ok=True)

    lines = [f"# AWS What's New — {day}", ""]
    if items:
        for it in items:
            lines.append(f"- [{it['title']}]({it['link']})")
    else:
        lines.append("_No new announcements captured today (feed empty or unreachable)._")
    lines.append("")
    lines.append(f"_Generated automatically at {today.strftime('%Y-%m-%d %H:%M UTC')}._")
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def update_readme(items: list[dict], today: datetime) -> None:
    readme = ROOT / "README.md"
    if not readme.exists():
        return
    content = readme.read_text(encoding="utf-8")
    top = items[:5]
    block = [f"_Last update: {today.strftime('%Y-%m-%d %H:%M UTC')}_", ""]
    block += [f"- [{it['title']}]({it['link']})" for it in top] or ["_Nothing yet._"]
    new_section = "<!-- LATEST:START -->\n" + "\n".join(block) + "\n<!-- LATEST:END -->"
    content = re.sub(r"<!-- LATEST:START -->.*?<!-- LATEST:END -->", new_section,
                     content, flags=re.DOTALL)
    readme.write_text(content, encoding="utf-8")


def main() -> int:
    today = datetime.now(timezone.utc)
    try:
        items = fetch_items()
    except Exception as exc:  # noqa: BLE001 — digest must still be written
        print(f"WARN: feed fetch failed: {exc}", file=sys.stderr)
        items = []
    path = write_digest(items, today)
    update_readme(items, today)
    print(f"Wrote {path} ({len(items)} items)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
