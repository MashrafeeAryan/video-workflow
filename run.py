"""Trigger one video-workflow cycle using Codex's existing ChatGPT login.

Run from any directory: python path/to/video-workflow/run.py
Preview without starting Codex: python run.py --dry-run

Requires Python 3.10+ and Codex CLI, signed in via `codex login` with ChatGPT.
Uses the ChatGPT plan allowance, subject to its limits. Does not install or
connect production tools, create a schedule, or buy additional credits.
"""

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run", action="store_true", help="Print the task without running Codex."
    )
    parser.add_argument(
        "--credit-budget", type=int,
        help="Total Flow credits authorized for this trial, including revisions."
    )
    args = parser.parse_args(argv)
    if args.credit_budget is not None and args.credit_budget <= 0:
        parser.error("--credit-budget must be a positive whole number")
    repo = Path(__file__).resolve().parent
    instructions = next(
        (name for name in ("AGENTS.md", "instructions.md") if (repo / name).is_file()),
        None,
    )
    if instructions is None:
        print("Missing AGENTS.md or instructions.md beside run.py.", file=sys.stderr)
        return 1

    prompt = f"""Run one production cycle for this repository.

Read {instructions} and follow its workflow instructions. Read the game
resources, schedule or game-selection files, existing story folders, saved
progress, and insights before acting. Resume unfinished work before creating
another story. Keep each story's assets and continuity separate. Save progress,
outputs, job IDs, review results, and any blockers so the next run can resume.

Temporary override for this run: create only ONE 10-second test reel, including
the gghuman.ai ending. This overrides conflicting instructions about duration,
timing, release schedules, producing ten reels, or writing the full ten-part
story before generation. Do not produce additional reels during this run.
Keep the applicable game, character-consistency, quality-review, and failure-
handling instructions. Save the result locally; do not publish to Instagram
or collect insights. If the generation tool cannot output exactly 10 seconds,
assemble or trim the footage locally to a 10-second final export.

Use Google Flow's website through the existing signed-in Chrome browser MCP
connection for now. Video API integration is planned for the future; do not
use a separately billed video API for this trial.

Total Flow credit budget supplied for this trial: {args.credit_budget if args.credit_budget is not None else 'NOT SET; stop before generation and report the missing budget'}.
Include every generated output and paid retry in this total. Check the actual
displayed cost and output count before submitting. Allow one initial production
attempt and at most three targeted revision rounds; stop earlier if the next
submission would exceed the total budget. Preserve spending and revision counts
across restarts; this argument does not reset the budget for an unfinished trial.

Save video_stories/story1/reels/part-01/final.mp4 and review.md in the same folder,
with the script, references, source clips, job IDs, and progress. Record credits
used, failures, and corrections. Complete the trial only after generation,
download, local assembly and website ending, and all required quality checks.

Use only available, configured tools and already authorized budgets. Do not
use separately billed OpenAI API keys or purchase credits. If a required tool,
permission, budget, or input is missing, save the blocker and report it; never
invent a successful generation, review, schedule, or publication. Do not retry
an uncertain external action until you check whether it already succeeded.

Execute the workflow rather than rewriting it or implementing new integrations.
Do not edit the existing root README, change the workflow instructions, or
commit or push files. Finish with completed work, saved progress, and blockers.
"""

    if args.dry_run:
        print(f"Repository: {repo}\nAuthentication: ChatGPT plan\n\n{prompt}")
        return 0

    codex = shutil.which("codex.exe") or shutil.which("codex")
    if not codex:
        print("Codex CLI not found on PATH. Install it, then run codex login.", file=sys.stderr)
        return 1

    # Restrict only this child process; never change the user's environment.
    env = os.environ.copy()
    for name in ("OPENAI_API_KEY", "CODEX_API_KEY", "CODEX_ACCESS_TOKEN", "OPENAI_BASE_URL"):
        env.pop(name, None)
    command = [
        codex,
        "-c", 'forced_login_method="chatgpt"',
        "-c", 'model_provider="openai"',
    ]
    try:
        login = subprocess.run(
            command + ["login", "status"], cwd=repo, env=env,
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=30,
        )
        if login.returncode != 0 or "logged in using chatgpt" not in (
            login.stdout + login.stderr
        ).lower():
            print(
                "A ChatGPT login is required. Run codex login and choose ChatGPT. "
                "No production cycle was started.", file=sys.stderr,
            )
            return 1

        print("Starting one workflow cycle using ChatGPT plan usage.", flush=True)
        result = subprocess.run(
            command + ["exec", "--sandbox", "workspace-write", "--cd", str(repo), "-"],
            input=prompt, cwd=repo, env=env, text=True, encoding="utf-8",
        )
        if result.returncode:
            print(
                "Codex exited with an error. Check its output and saved progress "
                "before rerunning; external actions may already have occurred.",
                file=sys.stderr,
            )
        return result.returncode
    except subprocess.TimeoutExpired:
        print("Login check timed out; no production cycle was started.", file=sys.stderr)
        return 1
    except OSError as error:
        print(f"Could not launch Codex: {error}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nInterrupted. Check saved progress before rerunning.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
