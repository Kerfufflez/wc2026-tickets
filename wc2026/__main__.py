"""CLI: python -m wc2026 <command>"""

from __future__ import annotations

import argparse
import sys


def _resolve_game(pid_arg: str) -> tuple[dict, str]:
    """Look up a match by pid or event code. Returns (match, pid_str)."""
    from wc2026.games import get_game
    match = get_game(pid_arg)
    pid = str(match["pid"])
    return match, pid


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="wc2026",
        description="WC2026 ticket inventory dashboard",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("fetch-games", help="Fetch match list from SeatSidekick → data/matches.json")

    p_fetch = sub.add_parser("fetch", help="Fetch seat listings for a game")
    p_fetch.add_argument("--game", required=True, metavar="PID", help="Performance ID or event code (e.g. M102)")

    p_overlap = sub.add_parser("overlap", help="G4 pair-derivation overlap analysis")
    p_overlap.add_argument("--game", required=True, metavar="PID")

    p_build = sub.add_parser("build", help="Build dashboard HTML, deal log, and publish docs")
    p_build.add_argument("--game", required=True, metavar="PID")

    p_refresh = sub.add_parser("refresh", help="Full pipeline: fetch → overlap → build")
    p_refresh.add_argument("--game", required=True, metavar="PID")

    sub.add_parser("refresh-all", help="Run full pipeline for every game in data/matches.json")

    args = parser.parse_args(argv)

    if args.command == "fetch-games":
        from wc2026.games import fetch_matches
        try:
            count = fetch_matches()
            print(f"Done: {count} matches cached.")
            return 0
        except Exception as e:
            print(f"Error fetching matches: {e}")
            return 1

    if args.command == "fetch":
        from wc2026.fetch import main as fetch_run
        from wc2026.games import game_categories
        match, pid = _resolve_game(args.game)
        cats = game_categories(match)
        print(f"Fetching {match['matchup']} (pid={pid}, {len(cats)} categories)...")
        return fetch_run(pid, cats)

    if args.command == "overlap":
        from wc2026.overlap import main as overlap_run
        from wc2026.games import game_categories
        match, pid = _resolve_game(args.game)
        cats = game_categories(match)
        return overlap_run(pid, cats)

    if args.command == "build":
        from wc2026.build import main as build_run
        match, _ = _resolve_game(args.game)
        return build_run(match)

    if args.command == "refresh":
        from wc2026.fetch import main as fetch_run
        from wc2026.overlap import main as overlap_run
        from wc2026.build import main as build_run
        from wc2026.games import game_categories

        match, pid = _resolve_game(args.game)
        cats = game_categories(match)
        print(f"\n=== {match['matchup']} (pid={pid}) ===")
        if fetch_run(pid, cats) != 0:
            return 1
        if overlap_run(pid, cats) != 0:
            return 1
        return build_run(match)

    if args.command == "refresh-all":
        from wc2026.fetch import main as fetch_run
        from wc2026.overlap import main as overlap_run
        from wc2026.build import main as build_run
        from wc2026.games import game_categories, load_matches

        matches = load_matches()
        print(f"Refreshing {len(matches)} games...")
        errors = []
        for match in matches:
            pid = str(match["pid"])
            cats = game_categories(match)
            print(f"\n=== {match.get('matchup', pid)} (pid={pid}) ===")
            try:
                if fetch_run(pid, cats) != 0:
                    errors.append(pid)
                    print(f"  FETCH FAILED — skipping build")
                    continue
                overlap_run(pid, cats)
                if build_run(match) != 0:
                    errors.append(pid)
            except Exception as exc:
                errors.append(pid)
                print(f"  ERROR: {exc}")
        built = len(matches) - len(errors)
        if errors:
            print(f"\nSkipped {len(errors)} games (no data or build error): {', '.join(errors)}")
        print(f"\n{built}/{len(matches)} games refreshed successfully.")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
