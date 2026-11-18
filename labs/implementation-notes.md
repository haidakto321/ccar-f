# Implementation notes - CCAR-F labs

Decisions I made while building `labs/` that were not in the request, things I changed, trade-offs,
and what is **not verified yet**. Written 2026-11-03.

## Not verified yet (read this first)

- **No lab has been run against the API.** There is no API key in this session. I checked: every file
  compiles, the fake backend gives the expected answers (refund window, errors, failure injection), the JSON
  files load, and the receipt numbers add up. The first real run may show small API mismatches.
- **Forced `tool_choice` + `thinking: disabled` on Haiku 5.5** (labs 2, 5, 6): the docs say forced tool use is
  rejected only on Opus 5.5 / Sonnet 5.5 / Fable 5.1 / Mythos 5.1, and that Haiku 5.5 can disable thinking at
  effort `high` or below (default is `medium`). I expect it to work, but it is untested. Labs 2 and 5 catch the
  400 and explain; lab 6 exits with a hint.
- **Agent SDK labs (4, 7)**: `setting_sources=[]` is meant to stop your own `~/.claude` hooks and plugins
  (user-level plugins and skills) from loading into the lab agent. The docs say settings load by default; I read that an
  empty list loads none, but did not test it. If you see your own plugin's answer style in lab 4, that is why.
- `tools=[]` in lab 4 removes the built-in tools so the agent only has the 4 support tools. Tool search is
  turned off there (`ENABLE_TOOL_SEARCH=false`) so the MCP tools load up front.

## Decisions

| Decision | Why | Trade-off |
|---|---|---|
| Python, not Java | The Agent SDK is Python / TypeScript only. One language for all labs. | Your CLAUDE.md prefers Java, but that is for Spring Boot work. |
| Default model `claude-haiku-5-5`, set by `CCAR_MODEL` | You agreed to "use Haiku to keep cost low". | Haiku may follow the system prompt better or worse than Opus; lab 4's prompt-only run may hold the rule. The README says that doesn't prove anything. |
| Raw Messages API for labs 1-3, 5, 6 | The exam tests the loop itself (`stop_reason`, `tool_result`). The SDK's Tool Runner would hide it. | More code than the Tool Runner. |
| Agent SDK for labs 4 and 7 | Hooks and subagents are Agent SDK features, and the exam scenarios use them. | Needs `claude-agent-sdk` and runs Claude Code under the hood. |
| Forced `tool_choice` + JSON schema for structured output (labs 5, 6) | That is what guide v1.0 tests. | The current API also has structured outputs (`output_config.format`); mentioned in lab 5's README, not used. |
| `common/` holds reference answers | Later labs need a working loop and error format even if your lab 1 / lab 3 is unfinished. | You can peek. Each README says: try first, then open `common/`. |
| No `python-dotenv`, tiny `.env` reader in `common/config.py` | Your CLAUDE.md: don't add dependencies without asking. | Very simple parser (KEY=VALUE only). |
| No version pins in `requirements.txt` | I don't know the exact current versions without installing. | A future SDK release could change an API. Pin after your first working install (`pip freeze`). |
| Fake data with a fixed `TODAY = 2026-11-03` | Refund-window answers stay the same on every run. | Dates in the data are relative to that day. |
| 10 receipts, not 20 | Each one has a known trap; ground truth stays easy to check by hand. | Smaller sample for accuracy numbers. Add more if you want. |
| Lab 7 marked optional | Matches my earlier suggestion: labs 1-6 cover the most exam weight. | Scenario 3 gets less practice. |

## Differences between the exam guide and the current SDK (good to know for the exam)

- Subagent tool: the guide says `Task`; the Agent SDK now emits `Agent` in `tool_use` blocks (`Task` still shows
  in the `system:init` tool list). Lab 7 matches both names. On the exam, think `Task`.
- Forced `tool_choice` (`any` / `tool`) returns a 400 on the newest Opus / Sonnet. The guide still tests it.
- MCP error flag: `isError` in MCP / TypeScript, `"is_error": True` in the Python SDK tool result dict,
  `is_error` on a Messages API `tool_result` block. Same idea.

## Other changes in this session

- `CCAR-F-NOTES.md`: added a line under the guide source: the Dec 7, 2026 exam update covers CCAO-F, CCDV-F
  and CCAR-P only, not CCAR-F (source: Pearson VUE Anthropic page). Plus a link from section 7 to these labs.
- Repo root `.gitignore`: `.env`, `labs/.env`, `.venv/`, `__pycache__/`.
- Nothing committed (your CLAUDE.md rule).
