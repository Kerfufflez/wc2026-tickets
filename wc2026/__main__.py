"""CLI: python -m wc2026 <command>"""

from __future__ import annotations

import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="wc2026",
        description="WC2026 Semi-Final ticket inventory dashboard",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("fetch", help="Fetch latest listings from SeatSidekick API")
    sub.add_parser("overlap", help="Run G4 pair-derivation overlap analysis")
    sub.add_parser("build", help="Build dashboard HTML, deal log, and publish docs")
    sub.add_parser(
        "refresh",
        help="Full pipeline: fetch → overlap → build",
    )

    args = parser.parse_args(argv)

    if args.command == "fetch":
        from wc2026.fetch import main as run
    elif args.command == "overlap":
        from wc2026.overlap import main as run
    elif args.command == "build":
        from wc2026.build import main as run
    elif args.command == "refresh":
        from wc2026.fetch import main as fetch_run
        from wc2026.overlap import main as overlap_run
        from wc2026.build import main as build_run

        if fetch_run() != 0:
            return 1
        if overlap_run() != 0:
            return 1
        return build_run()
    else:
        parser.print_help()
        return 1

    return run()


if __name__ == "__main__":
    raise SystemExit(main())
