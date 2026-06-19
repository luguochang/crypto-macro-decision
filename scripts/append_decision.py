#!/usr/bin/env python3
import argparse
import re
from datetime import datetime, timezone
from pathlib import Path

ACTION_ENUM = {
    "open long",
    "open short",
    "hold long",
    "hold short",
    "close long",
    "close short",
    "flip long to short",
    "flip short to long",
    "trigger long",
    "trigger short",
    "no trade",
}

REQUIRED_FIELDS = [
    "Main action:",
    "EV / RR gate:",
    "Subjective probability:",
    "Why not the opposite:",
    "Next review time:",
]


def validate_body(body):
    missing = [field for field in REQUIRED_FIELDS if field not in body]
    if missing:
        raise SystemExit(f"Missing required decision fields: {', '.join(missing)}")

    matches = re.findall(r"(?im)^-?\s*Main action:\s*(.+?)\s*$", body)
    if len(matches) != 1:
        raise SystemExit("Decision body must contain exactly one Main action line.")

    action = matches[0].strip().strip("`")
    if action not in ACTION_ENUM:
        allowed = ", ".join(sorted(ACTION_ENUM))
        raise SystemExit(f"Main action must be exact enum. Got {action!r}. Allowed: {allowed}")


def main():
    p = argparse.ArgumentParser(description="Append a decision entry to decision-pool.md.")
    p.add_argument("--file", default=str(Path(__file__).resolve().parents[1] / "references" / "decision-pool.md"))
    p.add_argument("--title", required=True)
    p.add_argument("--body", required=True)
    p.add_argument("--time", default=datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M %Z"))
    p.add_argument("--no-validate", action="store_true", help="Append without enum/template validation for legacy imports.")
    args = p.parse_args()

    if not args.no_validate:
        validate_body(args.body)

    path = Path(args.file)
    entry = f"\n\n### {args.time} - {args.title}\n\n{args.body.strip()}\n"
    with path.open("a", encoding="utf-8") as f:
        f.write(entry)
    print(path)


if __name__ == "__main__":
    main()
