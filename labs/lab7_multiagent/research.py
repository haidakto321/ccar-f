"""Lab 7 - Coordinator + subagents (guide 1.2, 1.3, 5.3, 5.6; notes 2.2, 2.3, 6.3, 6.6).

Uses the Claude Agent SDK. Run from the labs folder:
    python -m lab7_multiagent.research wrong   # coordinator thinks subagents can see its context
    python -m lab7_multiagent.research right   # your prompts (fill the TODOs first)
"""
import asyncio
import json
import sys

from claude_agent_sdk import AgentDefinition, AssistantMessage, ClaudeAgentOptions, ResultMessage, ToolUseBlock, query

from common.config import DATA_DIR, MODEL

KB_DIR = DATA_DIR / "kb"
QUESTION = "Should we extend our refund window from 30 to 45 days? Give a recommendation with evidence."

READ_ONLY = ["Read", "Grep", "Glob"]

# WRONG: the coordinator believes subagents share its context, so it sends them almost nothing.
WRONG_COORDINATOR = (
    "You coordinate a research team. Your subagents can see this whole conversation, "
    "so send each of them a very short task like 'do your part'. Then write the final report."
)
WRONG_AGENTS = {
    "policy-researcher": AgentDefinition(
        description="Researches our internal policy and support data.",
        prompt="You are a researcher. Do the task you are given.",
        tools=READ_ONLY,
        model=MODEL,
    ),
    "market-researcher": AgentDefinition(
        description="Researches competitors.",
        prompt="You are a researcher. Do the task you are given.",
        tools=READ_ONLY,
        model=MODEL,
    ),
}

# TODO 1: coordinator prompt. Subagents see ONLY the prompt you pass in the Agent call, so tell the
#   coordinator to include: the question, which files to read, and the output format.
#   Ask it to start both subagents in ONE response (parallel), and to keep conflicting
#   numbers side by side with their source and date instead of picking one.
RIGHT_COORDINATOR = WRONG_COORDINATOR

# TODO 2: subagent prompts. Ask for findings as a list of
#   {"claim", "evidence", "source_file", "source_date"}. Say: report conflicts, don't resolve them.
RIGHT_AGENTS = WRONG_AGENTS


def make_options(coordinator: str, agents: dict) -> ClaudeAgentOptions:
    return ClaudeAgentOptions(
        model=MODEL,
        system_prompt=coordinator,
        agents=agents,
        # "Agent" is the tool that starts subagents. The exam guide calls it "Task" (old name).
        allowed_tools=["Agent", *READ_ONLY],
        cwd=str(KB_DIR),  # agents only see the knowledge base files
        setting_sources=[],  # don't load your own ~/.claude settings, hooks or plugins
        max_turns=20,
        max_budget_usd=1.0,
    )


def check_report(report: str) -> None:
    """Did the report keep both competitor numbers with their dates (provenance)?"""
    checks = {
        "mentions 45 days (2025 note)": "45" in report,
        "mentions 60 days (2026 help page)": "60" in report,
        "dates the sources": "2025" in report and "2026" in report,
        "uses the 12% late-request stat": "12%" in report or "149" in report,
    }
    for label, ok in checks.items():
        print(f"  {'OK  ' if ok else 'MISS'} {label}")


async def run(mode: str) -> None:
    coordinator, agents = (WRONG_COORDINATOR, WRONG_AGENTS) if mode == "wrong" else (RIGHT_COORDINATOR, RIGHT_AGENTS)
    report = ""
    try:
        async for message in query(prompt=QUESTION, options=make_options(coordinator, agents)):
            if isinstance(message, AssistantMessage):
                starts = [b for b in message.content if isinstance(b, ToolUseBlock) and b.name in ("Agent", "Task")]
                if starts and not message.parent_tool_use_id:
                    print(f"\n[coordinator starts {len(starts)} subagent(s) in one response]")
                    for block in starts:
                        print(f"  -> {block.input.get('subagent_type')}: {json.dumps(block.input.get('prompt', ''))[:300]}")
            elif isinstance(message, ResultMessage):
                report = message.result or ""
                print(f"\nresult: {message.subtype}, cost ${message.total_cost_usd}")
    except Exception as err:  # query() raises after an error result
        print(f"run ended with an error: {err}")
    print(f"\nREPORT:\n{report}\n")
    check_report(report)


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode not in ("wrong", "right"):
        sys.exit("usage: python -m lab7_multiagent.research [wrong|right]")
    asyncio.run(run(mode))


if __name__ == "__main__":
    main()
