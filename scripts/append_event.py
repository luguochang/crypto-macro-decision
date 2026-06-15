#!/usr/bin/env python3
import argparse
from datetime import datetime
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description="Append an event entry to event-pool.md.")
    p.add_argument("--file", default=str(Path(__file__).resolve().parents[1] / "references" / "event-pool.md"))
    p.add_argument("--title", required=True)
    p.add_argument("--body", required=True)
    p.add_argument("--time", default=datetime.now().strftime("%Y-%m-%d %H:%M"))
    args = p.parse_args()

    path = Path(args.file)
    entry = f"\n\n### {args.time} - {args.title}\n\n{args.body.strip()}\n"
    with path.open("a", encoding="utf-8") as f:
        f.write(entry)
    print(path)


if __name__ == "__main__":
    main()
