# CCAR-F - Ghi chú ôn thi Claude Certified Architect - Foundations

> Làm giống bộ AIF-C01 (`springboot-rag/docs/AIF-C01-NOTES.md`): note chính + cheatsheet + nhật ký quiz.
> Nguồn chính: exam guide chính thức v1.0 (effective July 2026) bạn đã tải. Bắt đầu: 2026-10-31.
> ⚠️ Kiểm tra 2026-11-03: đợt đổi đề **07/12/2026** chỉ áp dụng cho CCAO-F, CCDV-F, CCAR-P (guide mới ra 17/11). **CCAR-F không có trong danh sách** => vẫn học guide v1.0. Nguồn: [Pearson VUE - Anthropic](https://www.pearsonvue.com/us/en/anthropic.html). Sau 17/11 xem lại trang này + [Partner Academy](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification) 1 lần cho chắc.
> Bản đọc nhanh trước giờ thi: `CCAR-F-CHEATSHEET.md`.

**Ký hiệu nguồn**

| Ký hiệu | Nghĩa |
|---|---|
| `[G 1.1]` | Exam guide v1.0, Task Statement 1.1 |
| `[G Q3]` | Exam guide v1.0, mục 9, Sample Question 3 |
| `[G §17]` | Exam guide v1.0, mục 17 (Appendix: in-scope / out-of-scope) |
| `[W]` | Trang web bên ngoài (không phải Anthropic), kiểm tra 2026-10-31 |
| ✏️ **Sửa** | Thông tin cũ (của Claude hoặc site khác) bị sai, đã sửa theo guide |
| 💡 **Mẹo** | Mẹo do Claude tự đặt, KHÔNG phải tài liệu chính thức |
| 🔑 **Exam keywords** | Chữ hay gặp trong đề => đáp án |
| 🧭 **Cách chọn nhanh** | Cách phân biệt các đáp án dễ nhầm (Claude tự đặt) |
| *(Claude)* | Giải thích của Claude, guide không ghi |

## Mục lục

0. [Thông tin kỳ thi + mẹo làm bài](#0-thông-tin-kỳ-thi--mẹo-làm-bài)
1. [Những chỗ đã sửa](#1-những-chỗ-đã-sửa)
2. [Domain 1 - Agentic Architecture & Orchestration (27%)](#2-domain-1---agentic-architecture--orchestration-27)
3. [Domain 2 - Tool Design & MCP Integration (18%)](#3-domain-2---tool-design--mcp-integration-18)
4. [Domain 3 - Claude Code Configuration & Workflows (20%)](#4-domain-3---claude-code-configuration--workflows-20)
5. [Domain 4 - Prompt Engineering & Structured Output (20%)](#5-domain-4---prompt-engineering--structured-output-20)
6. [Domain 5 - Context Management & Reliability (15%)](#6-domain-5---context-management--reliability-15)
7. [Bài tập thực hành (build để nhớ)](#7-bài-tập-thực-hành-build-để-nhớ)
8. [Kế hoạch học: thi thử trước, học sau](#8-kế-hoạch-học-thi-thử-trước-học-sau)
9. [Nguồn mock test](#9-nguồn-mock-test)
10. [Quiz đã gặp + giải thích](#10-quiz-đã-gặp--giải-thích)

---

## 0. Thông tin kỳ thi + mẹo làm bài

**Format** `[G §3, §11, §12, §15]`

| Mục | Giá trị |
|---|---|
| Mã thi | **CCAR-F** (nhiều site ghi CCA-F, cùng 1 bài) |
| Số câu | **60**. Multiple choice + multiple response (đề **ghi rõ chọn mấy đáp án**) |
| Cấu trúc | **4 scenario** random trong **6** scenario. Câu hỏi bám theo scenario |
| Thời gian | **120 phút** => khoảng **2 phút / câu** |
| Đậu | scaled **720 / 1000** (thang 100-1000). Không cần đậu từng domain, chỉ cần tổng |
| Phí | $125. Giá lúc checkout đã trừ giảm giá theo **partner tier** của công ty |
| Thi ở đâu | Pearson VUE: online (webcam) hoặc test center. Closed book, chỉ có tiếng Anh `[W]` |
| Đổi lịch | Hủy / đổi lịch **trước 24 giờ**. Trong 24 giờ => **mất phí** |
| Thi lại | chờ **14 ngày** (lần 1 trượt), 30 ngày (lần 2), 90 ngày (lần 3). Tối đa **4 lần / 12 tháng**. Mỗi lần **trả phí** |
| Hiệu lực | **12 tháng**. Gia hạn đúng hạn = bài **online miễn phí, không giám sát**. Để hết hạn => thi lại full giá |
| Kết quả | Pass / fail + điểm + **% đúng theo từng domain** (dùng để biết domain yếu) |
| Giấy tờ | CMND / passport còn hạn, **tên phải khớp y hệt** tên đăng ký |

💡 Guide **không** nói sai có bị trừ điểm hay không. Không có lý do bỏ trống => **trả lời hết mọi câu** *(Claude)*.
💡 Khác AIF: **không** có câu ordering / matching, **không** có câu "unscored" được nhắc tới. Tất cả là câu chọn đáp án trong scenario.

**Trọng số** `[G §4]` (thứ tự domain theo guide chính thức)

| Domain | % | ~ số câu / 60 | Ghi chú cho bạn *(Claude)* |
|---|---|---|---|
| 1. Agentic Architecture & Orchestration | **27%** | ~16 | Nặng nhất. Agent SDK, subagent, hook. Bạn ít làm SDK => **học kỹ** |
| 2. Tool Design & MCP Integration | 18% | ~11 | Tool description, error MCP, `.mcp.json` |
| 3. Claude Code Configuration & Workflows | 20% | ~12 | Bạn dùng hằng ngày (CLAUDE.md, skills, hooks) => **lợi thế**, chỉ cần học đúng tên file |
| 4. Prompt Engineering & Structured Output | 20% | ~12 | tool_use + JSON schema, few-shot, batch |
| 5. Context Management & Reliability | 15% | ~9 | escalation, error propagation, provenance |

**6 scenario** `[G §5]` (thi gặp 4)

| # | Scenario | Domain chính | Bài tập liên quan (mục 7) |
|---|---|---|---|
| 1 | Customer Support Resolution Agent (Agent SDK + MCP tools: `get_customer`, `lookup_order`, `process_refund`, `escalate_to_human`, mục tiêu 80% first-contact resolution) | D1, D2, D5 | Ex 1 |
| 2 | Code Generation with Claude Code (slash commands, CLAUDE.md, plan mode) | D3, D5 | Ex 2 |
| 3 | Multi-Agent Research System (coordinator + search / analysis / synthesis / report subagents) | D1, D2, D5 | Ex 4 |
| 4 | Developer Productivity (Agent SDK + built-in tools Read / Write / Bash / Grep / Glob + MCP) | D2, D3, D1 | Ex 2 |
| 5 | Claude Code for CI (review PR, sinh test, giảm false positive) | D3, D4 | Ex 2 + 3 |
| 6 | Structured Data Extraction (JSON schema, validation, edge case) | D4, D5 | Ex 3 |

**❌ KHÔNG thi (đừng mất thời gian)** `[G §17]`
- Fine-tuning, training model. Kiến trúc bên trong Claude, RLHF, Constitutional AI
- Authentication, billing, account, OAuth, API key rotation
- Deploy / host MCP server (hạ tầng, network, container)
- Embedding, vector DB (khác AIF!). Computer use. Vision / ảnh. **Streaming / SSE**
- Rate limit, quota, **tính giá API**. Token counting / tokenizer
- **Prompt caching chi tiết** (chỉ cần biết nó tồn tại). Cấu hình cloud (AWS / GCP / Azure). Benchmark / so sánh model

### 🧠 10 luật vàng (rút ra từ 12 câu mẫu của guide) *(Claude)*

| # | Luật | Nguồn |
|---|---|---|
| 1 | Cần **đảm bảo 100%** (tiền, xác minh danh tính, thứ tự bắt buộc) => **code / hook / gate**. Prompt và few-shot chỉ là **xác suất** | `[G 1.4, 1.5]` `[G Q1]` |
| 2 | Đề hỏi "**first step**" / "most effective" => sửa **root cause** bằng cách **rẻ nhất, ít hạ tầng nhất**. Routing layer, classifier, model riêng = **over-engineered** | `[G Q2, Q3]` |
| 3 | Root cause nằm **đúng chỗ log chỉ ra**. Agent downstream làm đúng việc được giao thì đừng đổ lỗi cho nó | `[G Q7]` |
| 4 | Lỗi => trả **structured error** (loại lỗi, đã thử gì, partial result, hướng khác). ❌ "Operation failed" chung chung, ❌ trả rỗng như thành công, ❌ dừng cả workflow | `[G 2.2, 5.3]` `[G Q8]` |
| 5 | **Least privilege**: mỗi agent chỉ có tool của vai trò nó. Cần thêm cho case phổ biến => cho **1 tool hẹp** (vd `verify_fact`), không cho cả bộ | `[G 2.3]` `[G Q9]` |
| 6 | **Self-reported confidence** (1-10) và **sentiment** = **không đáng tin** để quyết định escalate | `[G 5.2]` `[G Q3]` |
| 7 | Model **to hơn** / context **dài hơn** **không** sửa được attention dilution => **chia nhỏ pass** | `[G 1.6, 4.6]` `[G Q12]` |
| 8 | Đáp án nhắc tới **flag / file / env var không tồn tại** => loại ngay (`CLAUDE_HEADLESS`, `--batch`, `.claude/config.json` với commands array) | `[G Q4, Q10]` |
| 9 | **Batch API** chỉ cho việc **không chặn** (overnight, weekly). Việc **chặn merge** => sync API | `[G 4.5]` `[G Q11]` |
| 10 | Lời dặn mơ hồ ("be conservative", "only high-confidence") **không** tăng precision => **tiêu chí cụ thể theo loại** + ví dụ | `[G 4.1]` |

### 🔑 Từ điển "chữ trong đề => đáp án" *(Claude, gom từ guide)*

| Chữ trong đề | Nghĩa | => Thường là |
|---|---|---|
| **guaranteed / must always / compliance / financial** | phải đúng 100% | **hook / programmatic prerequisite** (không phải prompt) |
| agent **skips** a required step X% of the time | bỏ qua bước bắt buộc | **gate chặn tool sau** tới khi tool trước trả kết quả |
| **most effective first step** | bước đầu hiệu quả nhất | sửa nhỏ nhất đúng root cause (vd **viết lại tool description**) |
| picks the **wrong tool**, tools have **minimal / similar descriptions** | chọn nhầm tool | **mở rộng description**: input format, ví dụ query, edge case, khi nào dùng tool khác |
| agent has **18 tools** / too many tools | quá nhiều tool | **giảm còn 4-5**, chia theo vai trò |
| must call a tool, **not return text** | bắt buộc gọi tool | `tool_choice: "any"` |
| tool X must run **first** | phải chạy trước | forced `tool_choice: {"type":"tool","name":"X"}` |
| **job hangs** waiting for input in CI | treo chờ input | `claude -p` (`--print`) |
| **machine-parseable** findings, inline PR comments | output máy đọc được | `--output-format json` + `--json-schema` |
| available to **every developer** who clones the repo | dùng chung cả team | file trong **repo**: `.claude/commands/`, `.claude/skills/`, `.mcp.json`, `CLAUDE.md` |
| **personal / experimental** | của riêng mình | `~/.claude/...`, `~/.claude.json` |
| **new team member** doesn't get the instructions | người mới không nhận rule | rule đang nằm ở **user-level** `~/.claude/CLAUDE.md` => chuyển lên **project-level** |
| test files **spread throughout** the codebase | file nằm rải rác | `.claude/rules/*.md` + `paths:` glob (vd `**/*.test.tsx`) |
| skill output is **verbose**, **pollutes** main conversation | output dài làm bẩn context | `context: fork` |
| restructure / migrate **dozens of files**, **architectural** decisions | thay đổi lớn | **plan mode** |
| **single-file** fix, clear stack trace | sửa nhỏ rõ ràng | **direct execution** |
| **cost** savings + **overnight / weekly** | rẻ + không gấp | **Message Batches API** (50% rẻ hơn, tới 24h) |
| **blocking** / pre-merge / developer waits | phải chờ | **sync API** (không batch) |
| **correlate** batch requests and results | ghép request - response | `custom_id` |
| JSON **syntax** errors | lỗi cú pháp JSON | **tool_use + JSON schema** (strict) |
| totals **don't sum**, value in **wrong field** | lỗi **ngữ nghĩa** | validation + **retry kèm lỗi cụ thể** (schema không bắt được) |
| model **fabricates** values for missing fields | bịa giá trị | field **optional / nullable** |
| info **only in another document** not provided | thông tin không có trong input | retry **vô ích** => đánh dấu thiếu / người xem |
| **inconsistent format** of output | format lúc thế này lúc thế khác | **few-shot** (2-4 ví dụ) |
| too many **false positives**, developers **lose trust** | báo sai nhiều | **tiêu chí cụ thể** + **tạm tắt category báo sai nhiều** |
| **14 files**, superficial / **contradictory** review | review nhiều file kém | **per-file pass + cross-file integration pass** |
| same session **reviews its own** code | tự review | **instance độc lập** (không có reasoning context cũ) |
| subagent **doesn't know** earlier findings | subagent thiếu context | **đưa thẳng findings vào prompt** của subagent (không tự kế thừa) |
| report covers only **part of the topic** | thiếu mảng | coordinator **chia task quá hẹp** |
| timeout in a subagent | subagent lỗi | **structured error context** về coordinator |
| customer **asks for a human** | khách đòi người | **escalate ngay**, không điều tra trước |
| policy is **silent / ambiguous** (vd price match **đối thủ**) | chính sách không nói tới | **escalate** |
| tool returns **multiple customers** | nhiều kết quả trùng | **hỏi thêm identifier**, không đoán |
| summary **loses numbers / dates** | tóm tắt mất số liệu | **"case facts" block** giữ riêng, ngoài phần tóm tắt |
| findings in the **middle** get missed | bỏ sót phần giữa | **lost in the middle** => đưa tóm tắt lên **đầu**, có section header |
| **97% overall** accuracy, ready to automate? | tổng thể cao | **chia theo loại tài liệu / field**, **stratified sampling** |
| two credible sources **conflict** | 2 nguồn mâu thuẫn | **giữ cả 2 + ghi nguồn**, không tự chọn 1 |
| long session, answers get **vague / "typical patterns"** | context xuống cấp | **scratchpad file**, subagent, `/compact` |
| resume but **files changed** | file đã đổi | báo cho agent **file nào đổi**; nếu tool result cũ quá => **session mới + summary** |

💡 **Mẹo đọc đề** (giống AIF, chỉnh cho bài này)
1. **Đọc câu CUỐI trước**: "most effective **first step**", "most **maintainable**", "**guarantee**", "**reduce overhead while maintaining reliability**". Chữ đó quyết định đáp án.
2. **Đọc số liệu trong đề**: "12% of cases", "85% simple / 15% complex", "40% latency". Số liệu thường chỉ thẳng vào đáp án (vd 85/15 => tool hẹp cho 85%, case khó vẫn qua coordinator).
3. **Đáp án sai thường là**: (a) **prompt** khi cần **đảm bảo**, (b) **hạ tầng mới** (classifier, routing layer, model to hơn) khi chưa thử cách đơn giản, (c) **đổ việc cho developer** ("bắt dev chia PR nhỏ"), (d) **feature không tồn tại**.
4. **Multiple response**: đề ghi chọn mấy => chọn **đủ** số đó.
5. **Kiểm tra cả 2 yêu cầu** nếu đề có 2 ("reduce latency" **và** "maintain reliability").

---

## 1. Những chỗ đã sửa

Thông tin từ các site bên ngoài và từ câu trả lời đầu tiên của Claude **khác** guide chính thức. Theo guide.

| # | Thông tin cũ | Đúng theo guide | Nguồn |
|---|---|---|---|
| 1 | 🔴 Thứ tự domain: D2 = Claude Code, D3 = Prompt, D4 = Tool & MCP (nhiều site + câu trả lời trước của Claude) | **D2 = Tool Design & MCP (18%)**, **D3 = Claude Code (20%)**, **D4 = Prompt (20%)**. Mock test bên ngoài có thể đánh số khác => nhìn **tên** domain, đừng nhìn số | `[G §4]` |
| 2 | 🔴 "Domain 5: học kỹ số liệu prompt caching (TTL, min token)" (Claude nói trước đó) | **Prompt caching chi tiết = OUT OF SCOPE**, chỉ cần biết nó tồn tại. D5 thực tế là escalation, error propagation, provenance, human review | `[G §17]` |
| 3 | 🟡 "Global Premier partner miễn phí tới 31/12/2026" (site bên ngoài) | Guide chỉ nói: giá lúc checkout **đã gồm giảm giá theo partner tier**. Xem giá thật lúc checkout bằng account công ty | `[G §11]` |
| 4 | 🟡 Thứ tự ưu tiên settings (managed > CLI > local > project > user) | **Không** có trong task statement. Guide hỏi **CLAUDE.md hierarchy**, rules, commands, skills, `.mcp.json`. Ưu tiên thấp | `[G 3.1]` |
| 5 | 🟡 Tên tool tạo subagent | Guide gọi là **Task** tool (`allowedTools` phải có `"Task"`). Claude Code bản mới hiển thị tool này là **Agent**. **Thi theo guide: Task** *(Claude)* | `[G 1.3]` |
| 6 | 🟡 Slash command | Guide tách `.claude/commands/` và `.claude/skills/`. Claude Code bản mới đã gộp command vào skill. **Thi theo guide** *(Claude)* | `[G 3.2]` |

---

## 2. Domain 1 - Agentic Architecture & Orchestration (27%)

### 2.1 Agentic loop `[G 1.1]`

Vòng lặp: gửi request => xem `stop_reason` => nếu `"tool_use"` thì chạy tool, **append `tool_result` vào messages**, gửi lại => nếu `"end_turn"` thì dừng, trả kết quả.

```python
messages = [{"role": "user", "content": task}]
while True:
    resp = client.messages.create(model=MODEL, max_tokens=4096,
                                  tools=TOOLS, messages=messages)
    messages.append({"role": "assistant", "content": resp.content})
    if resp.stop_reason != "tool_use":        # "end_turn" => xong
        break
    results = [{"type": "tool_result", "tool_use_id": b.id,
                "content": run_tool(b.name, b.input)}
               for b in resp.content if b.type == "tool_use"]
    messages.append({"role": "user", "content": results})
```

- **Model-driven**: Claude tự chọn tool tiếp theo dựa trên context. Khác với **decision tree / chuỗi tool cố định** do code quy định.
- ❌ **Anti-pattern** (đề hay cho làm đáp án sai):
  - đọc chữ trong câu trả lời ("I'm done", "task complete") để quyết định dừng
  - dùng **giới hạn số vòng** (iteration cap) làm cách dừng **chính** (làm lưới an toàn thì được *(Claude)*)
  - thấy có **text** trong response là coi như xong (response có thể vừa có text vừa có tool_use)

🧭 Dừng loop dựa vào **`stop_reason`**, không dựa vào **nội dung chữ**.

### 2.2 Multi-agent: coordinator - subagent `[G 1.2]`

- **Hub-and-spoke**: mọi giao tiếp giữa subagent **đi qua coordinator** (dễ quan sát, xử lý lỗi thống nhất, kiểm soát luồng thông tin).
- Subagent có **context riêng**: **không** tự thấy lịch sử hội thoại của coordinator.
- Coordinator làm: chia task, giao việc, gom kết quả, **chọn subagent nào cần gọi theo độ phức tạp** (không phải lúc nào cũng chạy cả pipeline).
- Rủi ro: coordinator **chia quá hẹp** => thiếu mảng (sample Q7: "creative industries" chỉ chia ra 3 mảng visual art => thiếu music, writing, film).
- Chia phạm vi để **không trùng**: mỗi subagent 1 subtopic hoặc 1 loại nguồn.
- **Iterative refinement**: coordinator xem bản synthesis còn thiếu gì => giao lại search / analysis với query cụ thể => synthesis lại, tới khi đủ.

### 2.3 Gọi subagent, truyền context `[G 1.3]`

- Tạo subagent bằng **Task tool**. Coordinator phải có `"Task"` trong `allowedTools`.
- **AgentDefinition**: description, system prompt, tool restrictions cho từng loại subagent.
- Context phải **đưa thẳng vào prompt** của subagent (vd đưa kết quả web search + phân tích tài liệu cho synthesis agent).
- Truyền dữ liệu bằng **format có cấu trúc**, tách **nội dung** khỏi **metadata** (URL, tên tài liệu, số trang) => giữ được nguồn.
- **Chạy song song**: coordinator gọi **nhiều Task tool call trong 1 response** (không phải mỗi turn 1 cái).
- Prompt cho coordinator: nêu **mục tiêu + tiêu chí chất lượng**, **không** viết từng bước thủ tục => subagent linh hoạt hơn.
- **Fork session**: tách nhánh từ 1 bản phân tích chung để thử hướng khác nhau.

### 2.4 Workflow nhiều bước: enforcement + handoff `[G 1.4]`

- **Programmatic enforcement** (hook, prerequisite gate) vs **prompt guidance**. Khi cần đúng tuyệt đối (xác minh danh tính trước giao dịch tiền) => prompt **luôn có tỉ lệ lỗi > 0**.
- Ví dụ chuẩn: **chặn** `lookup_order` / `process_refund` tới khi `get_customer` trả về **verified customer ID** `[G Q1]`.
- Request nhiều vấn đề => **tách thành từng item**, điều tra **song song** với context chung, rồi **gộp** thành 1 câu trả lời.
- **Handoff khi escalate**: người nhận **không đọc được transcript** => gửi summary có cấu trúc: customer ID, root cause, số tiền refund, đề xuất hành động.

### 2.5 Hooks trong Agent SDK `[G 1.5]`

| Hook | Làm gì | Ví dụ |
|---|---|---|
| **PostToolUse** | sửa **kết quả tool** trước khi model đọc | chuẩn hóa thời gian (Unix timestamp, ISO 8601), status code dạng số từ nhiều MCP tool khác nhau |
| Chặn **tool call đi ra** (PreToolUse) | chặn hành động vi phạm policy | refund **> $500** => chặn + chuyển sang **escalate cho người** |

🧭 Hook = **chắc chắn (deterministic)**. Prompt = **xác suất**. Business rule bắt buộc => hook.

### 2.6 Chia task (decomposition) `[G 1.6]`

| Loại | Khi nào | Ví dụ |
|---|---|---|
| **Prompt chaining** (pipeline cố định, tuần tự) | việc **đoán trước được**, nhiều khía cạnh | review: phân tích **từng file** => 1 pass **cross-file** |
| **Dynamic decomposition** (thích ứng) | việc **mở**, chưa biết sẽ gặp gì | "thêm test cho codebase cũ": map cấu trúc => tìm vùng quan trọng => kế hoạch ưu tiên, **đổi theo** dependency phát hiện ra |

### 2.7 Session: resume, fork `[G 1.7]`

| Tình huống | Chọn |
|---|---|
| Context cũ **phần lớn còn đúng** | `--resume <session-name>` |
| Context cũ đã **stale** (tool result cũ, file đổi nhiều) | **session mới** + **inject structured summary** (đáng tin hơn resume) |
| Resume sau khi **sửa vài file** | **báo agent đúng file nào đã đổi** để phân tích lại có mục tiêu, không bắt khám phá lại toàn bộ |
| So sánh **2 hướng** (2 chiến lược test, 2 cách refactor) từ 1 bản phân tích chung | `fork_session` |

---

## 3. Domain 2 - Tool Design & MCP Integration (18%)

### 3.1 Thiết kế tool interface `[G 2.1]`

- **Tool description** = cách **chính** để model chọn tool. Description sơ sài => chọn nhầm giữa các tool giống nhau.
- Description tốt có: **input format**, **ví dụ query**, **edge case**, **ranh giới** (khi nào dùng tool này, khi nào dùng tool kia).
- Tool trùng chức năng (`analyze_content` vs `analyze_document`) => **đổi tên + viết lại description** (vd thành `extract_web_results`).
- Tool chung chung => **tách** thành tool có mục đích rõ (`analyze_document` => `extract_data_points`, `summarize_content`, `verify_claim_against_source`).
- ⚠️ **System prompt** có từ khóa có thể **lấn át** description tốt (vd prompt nói "always analyze content..." làm model nghiêng về tool có chữ "content") => rà system prompt.

🧭 Sample Q2 `[G Q2]`: chọn nhầm `get_customer` / `lookup_order` => **mở rộng description** (✅ rẻ, đúng root cause). Few-shot = tốn token, không sửa gốc. Routing layer = over-engineered. Gộp tool = được nhưng tốn công hơn mức "first step".

### 3.2 Structured error cho MCP tool `[G 2.2]`

- MCP báo lỗi bằng flag **`isError`**.
- 4 loại lỗi:

| Loại | Ví dụ | Retry? |
|---|---|---|
| **transient** | timeout, service down | ✅ có |
| **validation** | input sai | ❌ (sửa input rồi gọi lại) |
| **business** | vi phạm policy | ❌ `retriable: false` + **lời giải thích thân thiện** cho khách |
| **permission** | không có quyền | ❌ |

- Trả metadata: `errorCategory`, `isRetryable`, mô tả dễ đọc. ❌ "Operation failed" chung chung => agent không biết xử lý.
- Subagent **tự retry** lỗi transient ở local. Chỉ đẩy lên coordinator lỗi **không tự xử lý được**, kèm **partial result + đã thử gì**.
- ⚠️ **Access failure** (gọi không được) ≠ **valid empty result** (gọi được, không có kết quả). Đừng trộn 2 cái.

```json
{ "isError": true,
  "content": [{ "type": "text", "text": "{\"errorCategory\":\"business\",\"isRetryable\":false,\"message\":\"Refunds over $500 need a human agent.\"}" }] }
```

### 3.3 Chia tool cho agent + tool_choice `[G 2.3]`

- **Quá nhiều tool** (18 thay vì 4-5) => chọn kém. Agent có tool **ngoài chuyên môn** => dùng sai (synthesis agent đi search web).
- **Scoped access**: mỗi agent chỉ có tool cho vai trò của nó. Cho thêm **1 tool hẹp** cho nhu cầu **hay gặp** (`verify_fact` cho synthesis), case phức tạp vẫn qua coordinator `[G Q9]`.
- Thay tool chung bằng tool **có ràng buộc**: `fetch_url` => `load_document` (kiểm tra URL là tài liệu hợp lệ).

| `tool_choice` | Nghĩa |
|---|---|
| `"auto"` | model **có thể** trả text thay vì gọi tool |
| `"any"` | **bắt buộc** gọi tool, model tự chọn tool nào |
| `{"type":"tool","name":"X"}` | **bắt buộc** gọi đúng tool **X** (vd ép `extract_metadata` chạy trước, các bước sau xử lý ở turn sau) |

### 3.4 MCP server trong Claude Code / agent `[G 2.4]`

| File | Scope | Dùng cho |
|---|---|---|
| **`.mcp.json`** (trong repo) | project | tool **dùng chung cả team** (commit vào git) |
| **`~/.claude.json`** | user | server **cá nhân / thử nghiệm** |

- **Env var expansion** trong `.mcp.json`: `"${GITHUB_TOKEN}"` => không commit secret.
- Tool của **tất cả** MCP server được discover lúc connect và dùng **cùng lúc**.
- **MCP resources** = đưa **catalog nội dung** (danh sách issue, cây tài liệu, DB schema) cho agent thấy => **bớt tool call dò dẫm**.
- Agent cứ dùng Grep thay vì MCP tool mạnh hơn => **viết description MCP tool chi tiết hơn**.
- Tích hợp chuẩn (Jira...) => dùng **community MCP server** có sẵn. Tự viết server chỉ cho workflow **riêng của team**.

🧭 **Resource** = dữ liệu để **đọc / xem** (catalog). **Tool** = **hành động**.

### 3.5 Built-in tools `[G 2.5]`

| Tool | Dùng khi |
|---|---|
| **Grep** | tìm **nội dung** trong file (tên hàm, error message, import) |
| **Glob** | tìm **tên / đường dẫn file** theo pattern (`**/*.test.tsx`) |
| **Read / Write** | đọc / ghi **cả file** |
| **Edit** | sửa 1 đoạn bằng **text duy nhất (unique)**. Text không unique => Edit lỗi => **Read + Write** |

- Hiểu codebase **từ từ**: Grep tìm entry point => Read theo import. ❌ đọc hết mọi file từ đầu.
- Trace hàm qua wrapper module: tìm **mọi tên được export** trước, rồi grep từng tên.

💡 Grep = **G**iữa nội dung. Glob = **G**lob tên file (đều chữ G, nhớ: grep **bên trong**, glob **bên ngoài**).

---

## 4. Domain 3 - Claude Code Configuration & Workflows (20%)

### 4.1 Bản đồ file (học thuộc bảng này) `[G 3.1-3.3, 2.4]`

| File / thư mục | Scope | Chia sẻ qua git? | Dùng cho |
|---|---|---|---|
| `~/.claude/CLAUDE.md` | user | ❌ | rule **cá nhân**. Teammate **không** nhận được |
| `CLAUDE.md` hoặc `.claude/CLAUDE.md` (gốc repo) | project | ✅ | chuẩn chung cả team, **luôn load** |
| `<subdir>/CLAUDE.md` | directory | ✅ | rule cho **1 thư mục** |
| `.claude/rules/*.md` | project | ✅ | rule theo **chủ đề** (testing.md, api-conventions.md...). Có `paths:` => chỉ load khi sửa file khớp |
| `.claude/commands/` | project | ✅ | slash command **cả team** `[G Q4]` |
| `~/.claude/commands/` | user | ❌ | slash command cá nhân |
| `.claude/skills/<name>/SKILL.md` | project | ✅ | skill gọi **khi cần** |
| `~/.claude/skills/` | user | ❌ | skill cá nhân (đặt **tên khác** để không đè của team) |
| `.mcp.json` | project | ✅ | MCP server team |
| `~/.claude.json` | user | ❌ | MCP server cá nhân |

💡 Ví dụ ngay trong máy bạn: `~/.claude/CLAUDE.md` có dòng `@RTK.md` = **@import** đúng kiểu guide nói. Và vì nó là **user-level**, người khác clone repo sẽ **không** có các rule đó (đúng loại bẫy trong đề).

- **@import**: `@path/to/file.md` trong CLAUDE.md để tách nhỏ, mỗi package import chuẩn liên quan.
- **`/memory`**: xem file memory nào **đang được load** => debug khi hành vi khác nhau giữa các session.

### 4.2 Commands + Skills `[G 3.2]`

Frontmatter của SKILL.md:

| Field | Làm gì |
|---|---|
| `context: fork` | chạy skill trong **sub-agent riêng** => output dài / brainstorm **không làm bẩn** hội thoại chính |
| `allowed-tools` | **giới hạn tool** khi chạy skill (vd chỉ cho ghi file, chặn lệnh nguy hiểm) |
| `argument-hint` | **gợi ý tham số** khi dev gọi skill mà không truyền argument |

🧭 **Skill** = gọi **khi cần**, cho task cụ thể. **CLAUDE.md** = **luôn load**, cho chuẩn chung.

### 4.3 Path-specific rules `[G 3.3]`

```markdown
---
paths: ["**/*.test.tsx"]
---
Test files: use React Testing Library, no snapshot tests.
```

- Chỉ load khi sửa file khớp glob => **bớt context thừa, bớt token**.
- File cùng loại nằm **rải rác nhiều thư mục** => rules + glob **tốt hơn** CLAUDE.md theo thư mục `[G Q6]`.

🧭 Sample Q6: ❌ gộp hết vào root CLAUDE.md (dựa vào model tự đoán), ❌ skills (phải gọi thủ công, không tự động), ❌ CLAUDE.md mỗi thư mục (không phủ được file rải rác) => ✅ `.claude/rules/` + glob.

### 4.4 Plan mode vs direct execution `[G 3.4]`

| Plan mode | Direct execution |
|---|---|
| thay đổi **lớn**, **nhiều file** (migration 45+ file, monolith => microservices) | sửa **nhỏ, rõ** (1 file, có stack trace, thêm 1 điều kiện validate) |
| **nhiều cách** làm đúng, quyết định **kiến trúc** | đã biết rõ cách làm |

- Kết hợp: **plan mode để điều tra + thiết kế**, rồi **direct execution để làm** theo plan.
- **Explore subagent**: tách phần khám phá dài dòng, trả **tóm tắt** => giữ context chính.
- ❌ Bẫy `[G Q5]`: "làm trước, gặp phức tạp mới chuyển plan mode" => sai vì **độ phức tạp đã ghi sẵn trong đề**.

### 4.5 Iterative refinement `[G 3.5]`

| Kỹ thuật | Khi nào |
|---|---|
| **2-3 ví dụ input / output** cụ thể | mô tả bằng lời bị hiểu **không nhất quán** |
| **Test-driven**: viết test trước, đưa **test fail** cho Claude sửa dần | cần đúng edge case, performance |
| **Interview pattern**: để Claude **hỏi lại** trước khi làm | domain **lạ** (cache invalidation, failure mode) |
| Gửi **tất cả lỗi trong 1 message** | các lỗi **liên quan nhau** (sửa cái này ảnh hưởng cái kia) |
| Sửa **lần lượt** | các lỗi **độc lập** |

💡 Bạn đã dùng sẵn: superpowers **brainstorming** ≈ interview pattern, **TDD** skill ≈ test-driven iteration.

### 4.6 Claude Code trong CI/CD `[G 3.6]`

```bash
claude -p "Review this PR for bugs and security issues" \
  --output-format json --json-schema ./review-schema.json
```

- `-p` / `--print` = non-interactive => **không treo** chờ input `[G Q10]`.
- `--output-format json` + `--json-schema` => output **máy đọc được** để post **inline PR comment**.
- **CLAUDE.md** = nơi đưa context cho CI: chuẩn test, fixture có sẵn, tiêu chí review.
- Session vừa **sinh code** review code đó **kém hơn** 1 instance **độc lập**.
- Review lại sau commit mới: đưa **findings cũ** vào context, dặn chỉ báo lỗi **mới / chưa sửa** => không comment trùng.
- Sinh test: đưa **file test có sẵn** vào context => không đề xuất test trùng.

---

## 5. Domain 4 - Prompt Engineering & Structured Output (20%)

### 5.1 Tiêu chí rõ ràng => giảm false positive `[G 4.1]`

- ✅ "flag comment **chỉ khi** hành vi được mô tả **mâu thuẫn** với code thật". ❌ "check comments are accurate".
- ❌ "be conservative", "only report high-confidence findings" => **không** tăng precision.
- False positive cao ở 1 category => developer **mất niềm tin cả những category đúng**.
- Cách sửa: định nghĩa rõ **báo gì** (bug, security) / **bỏ qua gì** (style nhỏ, pattern local) · **tạm tắt** category báo sai nhiều trong lúc sửa prompt · mỗi **mức severity** có **ví dụ code** cụ thể.

### 5.2 Few-shot `[G 4.2]`

- Cách **hiệu quả nhất** để output **nhất quán format** khi hướng dẫn chi tiết vẫn không đủ.
- **2-4 ví dụ**, nhắm vào **case mơ hồ**, có **lý do** vì sao chọn hành động này mà không chọn cái khác.
- Giúp model **khái quát** sang pattern mới (không chỉ khớp case có sẵn).
- Extraction: few-shot với **tài liệu nhiều dạng** (citation inline vs bibliography, bảng vs văn xuôi) => **giảm hallucination** và giảm field rỗng.

### 5.3 Structured output bằng tool_use + JSON schema `[G 4.3]`

- **tool_use + JSON schema** = cách **chắc nhất** để output đúng schema => **hết lỗi cú pháp JSON**.
- ⚠️ Nhưng **không** chặn được lỗi **ngữ nghĩa** (line item cộng không ra total, giá trị nằm sai field).
- Thiết kế schema:
  - field **có thể không có** trong tài liệu => **optional / nullable** => model **không bịa** để lấp field required
  - enum mở rộng: thêm `"other"` + field `detail` (string); thêm `"unclear"` cho case mơ hồ
  - kèm **luật chuẩn hóa format** trong prompt (ngày, đơn vị) cùng với schema
- Nhiều loại tài liệu, không biết trước loại nào => `tool_choice: "any"` (nhiều extraction tool). Bắt 1 bước chạy trước => forced tool.

```json
{ "name": "extract_invoice",
  "input_schema": { "type": "object",
    "properties": {
      "invoice_no":     { "type": "string" },
      "due_date":       { "type": ["string", "null"] },
      "category":       { "type": "string", "enum": ["hardware", "software", "other", "unclear"] },
      "category_detail":{ "type": ["string", "null"] },
      "stated_total":   { "type": "number" },
      "calculated_total": { "type": "number" },
      "conflict_detected": { "type": "boolean" } },
    "required": ["invoice_no", "category", "stated_total"] } }
```

### 5.4 Validation + retry + feedback loop `[G 4.4]`

- **Retry kèm lỗi**: gửi lại **tài liệu gốc + extraction bị lỗi + lỗi validation cụ thể** => model tự sửa.
- Retry **có ích**: lỗi format, lỗi cấu trúc. Retry **vô ích**: thông tin **không có** trong tài liệu (nằm ở tài liệu khác không được đưa vào).
- **Self-check field**: lấy cả `calculated_total` và `stated_total` để bắt lệch; thêm `conflict_detected`.
- **`detected_pattern`** trong mỗi finding => khi dev bỏ qua (dismiss) finding, phân tích được **pattern nào hay báo sai**.

### 5.5 Batch processing `[G 4.5]`

| Message Batches API | |
|---|---|
| Giá | rẻ **50%** |
| Thời gian | **tới 24 giờ**, **không có SLA** độ trễ |
| Hạn chế | **không** hỗ trợ **multi-turn tool calling** trong 1 request |
| Ghép kết quả | **`custom_id`** |

- Hợp: overnight report, weekly audit, nightly test generation. Không hợp: **pre-merge check** (chặn dev).
- **Tính tần suất gửi theo SLA**: SLA 30 giờ, batch tới 24 giờ => gửi theo **cửa sổ 4 giờ** (đợi tối đa 4h + xử lý 24h = 28h < 30h, còn dư) *(Claude giải thích số của guide)*.
- Lỗi: gửi lại **chỉ request lỗi** (theo `custom_id`), có chỉnh (vd **chia nhỏ** tài liệu vượt context).
- **Thử prompt trên sample nhỏ trước** khi chạy batch lớn => giảm chi phí gửi lại.

### 5.6 Multi-instance, multi-pass review `[G 4.6]`

- **Self-review yếu**: model còn giữ reasoning lúc sinh code => ít nghi ngờ quyết định của mình.
- **Instance độc lập** (không có context cũ) bắt lỗi tốt hơn self-review hoặc extended thinking.
- **Multi-pass**: per-file (lỗi local) + integration pass (data flow giữa file) => tránh **attention dilution** và feedback **mâu thuẫn**.
- Verification pass: model ghi **confidence cho từng finding** => routing review.

🧭 Sample Q12 `[G Q12]`: 14 file review kém => ✅ chia pass. ❌ bắt dev chia PR (đẩy việc cho người). ❌ model context lớn hơn (không sửa attention). ❌ chạy 3 lần lấy đa số (**bỏ sót** bug thật chỉ thấy thỉnh thoảng).

---

## 6. Domain 5 - Context Management & Reliability (15%)

### 6.1 Giữ thông tin quan trọng trong hội thoại dài `[G 5.1]`

| Vấn đề | Cách sửa |
|---|---|
| **Progressive summarization** làm mất số tiền, %, ngày, kỳ vọng của khách | giữ **"case facts" block** riêng (số tiền, ngày, mã đơn, trạng thái), đưa vào **mọi prompt**, nằm **ngoài** phần tóm tắt |
| **Lost in the middle**: model nhớ đầu + cuối, sót phần giữa | **tóm tắt key findings ở đầu**, phần chi tiết chia **section header** rõ |
| Tool result **dài** (40+ field, chỉ cần 5) chiếm token | **cắt bớt**, chỉ giữ field liên quan **trước khi** đưa vào context |
| Multi-issue session | lưu dữ liệu từng issue (order ID, số tiền, status) vào **lớp context riêng** |
| Agent sau có ít context | agent trước trả **structured data** (key facts, citation, relevance score), không trả văn dài + reasoning |

- API là **stateless**: mỗi request phải gửi **đủ lịch sử hội thoại** *(Claude: đây là ý "passing complete conversation history")*.

### 6.2 Escalation + xử lý mơ hồ `[G 5.2]`

| Tình huống | Làm gì |
|---|---|
| Khách **đòi gặp người** | **escalate ngay**, **không** điều tra trước |
| Khách bực nhưng vấn đề **agent làm được** | ghi nhận cảm xúc + **đề nghị giải quyết**. Khách **nhắc lại** muốn gặp người => escalate |
| **Policy không nói tới / mơ hồ** (vd đòi price-match **đối thủ**, policy chỉ nói giá **của mình**) | **escalate** |
| **Không tiến triển** được | escalate |
| Tool trả **nhiều khách trùng tên** | **hỏi thêm thông tin** (email, SĐT), ❌ tự chọn theo heuristic |
| Escalate **sai nhiều** (case dễ thì escalate, case khó thì tự làm) | thêm **tiêu chí escalate rõ ràng + few-shot** vào system prompt `[G Q3]` |

- ❌ **Sentiment** và **self-reported confidence** = proxy **không đáng tin** cho độ phức tạp.
- Escalate vì **policy exception / gap**, không phải chỉ vì case "phức tạp".

### 6.3 Error propagation trong multi-agent `[G 5.3]`

- Structured error context: **failure type**, **query đã thử**, **partial result**, **hướng thay thế** => coordinator quyết định thông minh (retry query khác, đổi cách, hoặc đi tiếp với partial).
- 2 anti-pattern: ❌ **nuốt lỗi** (trả rỗng như thành công) · ❌ **dừng toàn bộ** workflow vì 1 lỗi.
- Synthesis output có **coverage annotation**: phần nào có nguồn chắc, phần nào **thiếu** vì nguồn không truy cập được.

### 6.4 Context khi khám phá codebase lớn `[G 5.4]`

- Dấu hiệu context xuống cấp: trả lời **không nhất quán**, nói về "**typical patterns**" thay vì class cụ thể đã tìm thấy.
- Cách chống:
  - **Scratchpad file** ghi key findings, các câu hỏi sau đọc lại file đó
  - **Subagent** cho câu hỏi cụ thể ("find all test files", "trace refund flow") => main agent chỉ giữ bức tranh lớn
  - **Tóm tắt** kết quả phase trước rồi **inject** vào context đầu của subagent phase sau
  - **`/compact`** khi context đầy output khám phá dài
- **Crash recovery**: mỗi agent export state ra **chỗ cố định** (manifest), coordinator **load manifest** khi resume và đưa vào prompt.

💡 Bạn đã dùng sẵn: memory files + MEMORY.md index của Claude Code ≈ scratchpad / manifest pattern.

### 6.5 Human review + confidence calibration `[G 5.5]`

- **97% tổng thể** có thể che giấu **kém** ở 1 loại tài liệu / 1 field => **đo accuracy theo loại tài liệu + theo field** trước khi giảm human review.
- **Stratified random sampling** các extraction **confidence cao** => đo error rate liên tục + bắt lỗi kiểu mới.
- **Field-level confidence** do model ghi, nhưng phải **calibrate bằng labeled validation set** (không tin con số thô).
- Đưa người xem: confidence **thấp**, tài liệu **mơ hồ / mâu thuẫn** => ưu tiên dùng reviewer có hạn.

💡 Liên hệ springboot-rag: golden set + baseline gate của bạn ≈ "labeled validation set". Chia kết quả eval theo loại câu hỏi ≈ "accuracy by segment".

### 6.6 Provenance + nguồn mâu thuẫn `[G 5.6]`

- Tóm tắt làm **mất nguồn** nếu không giữ **claim - source mapping** (URL, tên tài liệu, đoạn trích).
- 2 nguồn uy tín **mâu thuẫn** => **giữ cả 2 + ghi nguồn**, ❌ tự chọn 1. Document analysis để nguyên mâu thuẫn + annotate, **coordinator** quyết định.
- **Ngày xuất bản / thu thập** bắt buộc trong output => khác biệt **do thời gian** không bị hiểu nhầm là mâu thuẫn.
- Report tách **well-established** vs **contested**.
- Mỗi loại nội dung **format riêng**: tài chính => bảng, tin tức => văn xuôi, kỹ thuật => list. ❌ ép tất cả về 1 format.

---

## 7. Bài tập thực hành (build để nhớ) `[G §8]`

Guide khuyên làm 4 bài. Mỗi bài phủ 2-3 domain. Agent SDK có Python + TypeScript (chưa có Java) => làm bằng **Python** cho nhanh *(Claude)*.

🧪 **Code sẵn:** [labs/README.md](labs/README.md) - 7 lab (làm sai trước, xem lỗi, rồi làm đúng). Lab 1-4 + 5 = Ex 1, lab 0 = Ex 2, lab 6 = Ex 3, lab 7 = Ex 4.

**Ex 1 - Support agent có escalation** (D1, D2, D5) => Scenario 1
- [ ] 3-4 MCP tool, có **2 tool gần giống nhau** cần description kỹ
- [ ] Agentic loop theo `stop_reason`
- [ ] Error có `errorCategory` + `isRetryable`; thử từng loại lỗi
- [ ] Hook chặn refund > ngưỡng => escalate
- [ ] Thử message **nhiều vấn đề** => tách, xử lý, gộp

**Ex 2 - Claude Code cho team** (D3, D2) => Scenario 2, 4, 5
- [ ] CLAUDE.md project-level
- [ ] `.claude/rules/` với `paths:` (vd `src/api/**/*`, `**/*.test.*`), kiểm tra chỉ load khi sửa file khớp
- [ ] Skill có `context: fork` + `allowed-tools`
- [ ] `.mcp.json` có `${ENV_VAR}` + 1 server cá nhân trong `~/.claude.json`, kiểm tra cả 2 cùng chạy
- [ ] So plan mode vs direct trên 3 việc: sửa 1 file / migration nhiều file / feature nhiều cách làm
- [ ] (thêm) chạy `claude -p ... --output-format json --json-schema` trong GitHub Action

**Ex 3 - Extraction pipeline** (D4, D5) => Scenario 6
- [ ] Tool có schema: required + optional, enum `other` + detail, nullable; kiểm tra model trả `null` thay vì bịa
- [ ] Validation-retry loop (Pydantic); ghi lại lỗi nào retry sửa được, lỗi nào không
- [ ] Few-shot với tài liệu nhiều format
- [ ] Batch 100 tài liệu, xử lý lỗi theo `custom_id`, chia nhỏ tài liệu quá dài, tính thời gian so với SLA
- [ ] Field-level confidence + route sang người + đo accuracy theo loại tài liệu

**Ex 4 - Multi-agent research** (D1, D2, D5) => Scenario 3
- [ ] Coordinator có `"Task"` trong `allowedTools` + 2 subagent; đưa findings **vào prompt**
- [ ] Gọi song song (nhiều Task call trong 1 response), đo latency so với tuần tự
- [ ] Output subagent: claim, evidence, source, date; kiểm tra synthesis giữ nguồn
- [ ] Giả lập timeout => coordinator nhận structured error, đi tiếp với partial + ghi coverage gap
- [ ] Đưa 2 nguồn mâu thuẫn => report giữ cả 2 + ghi nguồn

💡 Không có thời gian làm cả 4? Ưu tiên **Ex 1** (Scenario 1 là nặng nhất về D1) và **Ex 3**. Ex 2 bạn gần như đã làm hằng ngày.

---

## 8. Kế hoạch học: thi thử trước, học sau

Giống cách làm AIF-C01: **làm mock => đưa câu sai cho Claude => Claude giải thích + kiểm tra với guide => ghi vào mục 10 => cập nhật bảng 🔁 điểm yếu => cuối cùng đọc cheatsheet**.

**Vòng lặp mỗi lần làm mock**
1. Làm **timed** (bấm giờ thật: 2 phút / câu). Không tra tài liệu.
2. Chép **câu sai + câu đoán mò** (đề + 4 đáp án + đáp án mock + đáp án bạn chọn) gửi Claude.
3. Claude: giải thích ✅ / ❌ từng đáp án, ghi nguồn `[G x.y]`, đánh dấu ⚠️ nếu **đáp án mock sai** so với guide.
4. Ghi vào mục 10. Chủ đề sai **lần 2** => thêm vào bảng 🔁 + cheatsheet.

**Lịch đề xuất** (hôm nay 2026-10-31, ~8-10 giờ / tuần) *(Claude)*

| Tuần | Ngày | Việc |
|---|---|---|
| 0 | 1-2/11 | Đọc mục 0 + 1 (30 phút). Làm **diagnostic** (Tutorials Dojo free sampler 20 câu). **Chưa học gì**. Ghi điểm từng domain |
| 1 | 3-9/11 | **D1** (mục 2) + bắt đầu **Ex 1** |
| 2 | 10-16/11 | **D2 + D3** (mục 3, 4). Ex 2 (nhanh, bạn đã quen) |
| 3 | 17-23/11 | **D4** (mục 5) + **Ex 3** |
| 4 | 24-30/11 | **D5** (mục 6) + Ex 4 (hoặc bỏ nếu thiếu giờ). **Mock full #1** |
| 5 | 1-7/12 | Mock full #2, #3. Ôn bảng 🔁. Mock **>= 80%** ổn định => **đặt lịch thi** |
| 6 | ~8-12/12 | **Thi lần 1**. Đọc cheatsheet sáng hôm thi |

⚠️ **Đặt lịch sớm**: nếu giá miễn phí / giảm giá của công ty có **hạn chót** (vd 31/12), thi lần 1 trước **~12/12** => trượt vẫn còn **14 ngày chờ** để thi lại trong năm. Kiểm tra giá thật lúc checkout trên Partner Academy.

**Ngày thi** (giống AIF)
- Đọc `CCAR-F-CHEATSHEET.md` (10-15 phút).
- Thi online: dọn bàn, 1 màn hình, không điện thoại / đồng hồ thông minh `[G §13]`.
- 2 phút / câu. Câu dài (scenario) chậm hơn => đánh dấu, làm câu khác, quay lại.

---

## 9. Nguồn mock test

| # | Nguồn | Giá | Ghi chú |
|---|---|---|---|
| 1 | **Practice test chính thức trên Anthropic Partner Academy** | ? | Guide ghi 12 câu mẫu "drawn from the practice test" => có thể có bộ practice chính thức. **Kiểm tra trong Partner Academy trước** (Claude chưa xác minh được) |
| 2 | [Tutorials Dojo - FREE CCAR-F sampler](https://portal.tutorialsdojo.com/product/free-claude-certified-architect-foundations-ccar-f-practice-exams-sampler/) | free | 20 câu, timed + review mode. **Dùng làm diagnostic** |
| 3 | [claudecertificationguide.com](https://claudecertificationguide.com/ccar-f) | free | diagnostic 10 câu + mock + bài học. Không liên quan Anthropic |
| 4 | [Tutorials Dojo - CCAR-F practice exams](https://portal.tutorialsdojo.com/product/claude-certified-architect-foundations-ccar-f-practice-exams/) | trả phí | 100+ câu scenario. TD có tiếng ở mảng AWS |
| 5 | Udemy (vd [bộ này](https://www.udemy.com/course/ccar-f-claude-certified-architect-foundations-practice-test/)) | trả phí, hay giảm giá | Rất nhiều bộ, chất lượng **không đều**. Chọn bộ **mới cập nhật theo guide v1.0**, rating cao, đọc review |
| 6 | [Anthropic Exam Pro - Kiến thức CCAR-F](https://anthropic.cloudexam.pro/kien-thuc/ccar-f) (tiếng Việt) | bài học: xem được không cần đăng nhập. Khóa luyện đề: **280.000đ**, có thử **10 câu** | Kiểm tra 2026-11-03. **30 bài = đúng 30 task statement**, **đúng thứ tự domain** của guide (D2 = Tool & MCP). Bài 1.1 khớp guide (stop_reason, 3 anti-pattern), có thêm chi tiết API **ngoài phạm vi thi** (các `stop_reason` khác, lỗi 400) => đọc lướt. ⚠️ **Không phải của Anthropic** dù tên có chữ "Anthropic". Không ghi tác giả, chỉ có Facebook. Quảng cáo "**bám sát đề thi thật**": nếu thấy câu hỏi giống **y nguyên** đề thật => dừng (NDA) |

⚠️ **Tránh "dump"**: site ghi "**real exam questions**" = vi phạm **NDA** (`[G §14]`) => có thể bị **hủy kết quả + cấm thi** (`[G §13]`). Bộ AIF dùng ExamTopics, nhưng với bài này **đừng dùng** site kiểu đó.
⚠️ Mock bên ngoài **có thể sai đáp án** (bài học từ AIF: Q6, Q71). Thấy mâu thuẫn với guide => **tin guide**, ghi ⚠️ vào mục 10.
⚠️ Mock bên ngoài có thể đánh **số domain khác** guide (xem mục 1 #1).

---

## 10. Quiz đã gặp + giải thích

### 🔁 Điểm yếu: câu sai nhiều lần (ôn cái này TRƯỚC khi thi)

| # | Chủ đề | Sai ở câu | Quy tắc 1 dòng | Ôn lại |
|---|---|---|---|---|
| | *(điền sau mock đầu tiên)* | | | |

### ⚠️ Đáp án mock đã kiểm tra là SAI

| Nguồn + câu | Mock ghi | Đúng theo guide |
|---|---|---|
| | *(điền khi gặp)* | |

### 12 câu mẫu trong guide (tóm tắt bài học, đề đầy đủ xem PDF mục 9)

| Câu | Scenario | Tình huống (rút gọn) | ✅ Đáp án | Vì sao các đáp án khác sai | Luật |
|---|---|---|---|---|---|
| Q1 | Support | 12% case agent bỏ qua `get_customer` | **gate trong code** chặn tool sau tới khi có verified ID | prompt, few-shot = xác suất. Routing classifier = sai vấn đề (tool **có sẵn** vs **thứ tự**) | #1 |
| Q2 | Support | chọn nhầm 2 tool có description sơ sài | **mở rộng description** | few-shot tốn token. Routing layer over-engineered. Gộp tool tốn công hơn "first step" | #2 |
| Q3 | Support | FCR 55%, escalate sai | **tiêu chí escalate + few-shot** trong system prompt | self-confidence không calibrate. Classifier riêng over-engineered. Sentiment ≠ độ phức tạp | #2, #6 |
| Q4 | Code gen | `/review` cho cả team | **`.claude/commands/`** trong repo | `~/.claude/commands/` = cá nhân. CLAUDE.md không định nghĩa command. `.claude/config.json` không tồn tại | #8 |
| Q5 | Code gen | monolith => microservices | **plan mode** | đề đã nói rõ phức tạp => không "làm rồi tính" | |
| Q6 | Code gen | convention theo loại file, test rải rác | **`.claude/rules/` + glob** | root CLAUDE.md dựa đoán. Skills phải gọi tay. CLAUDE.md theo thư mục không phủ file rải rác | |
| Q7 | Research | report thiếu music / writing / film | **coordinator chia quá hẹp** | các subagent làm đúng phần được giao | #3 |
| Q8 | Research | web search subagent timeout | **structured error context** | generic status giấu thông tin. Rỗng = thành công là nuốt lỗi. Dừng cả workflow là thừa | #4 |
| Q9 | Research | synthesis cần verify, 85% đơn giản | **tool `verify_fact` hẹp** cho synthesis | batch verify = phụ thuộc chặn. Cho cả bộ search = vượt quyền. Cache trước = đoán mò | #5 |
| Q10 | CI | job treo chờ input | **`claude -p`** | `CLAUDE_HEADLESS`, `--batch` không tồn tại. `< /dev/null` là mẹo Unix không đúng cách | #8 |
| Q11 | CI | đổi cả 2 workflow sang batch | **batch chỉ cho report overnight** | pre-merge cần nhanh. Thứ tự kết quả không phải vấn đề (có `custom_id`). Timeout fallback = phức tạp thừa | #9 |
| Q12 | CI | review 14 file kém, mâu thuẫn | **per-file pass + integration pass** | đẩy việc cho dev. Context lớn không sửa attention. Đa số 2/3 bỏ sót bug thật | #7 |

### Mock đã làm

*(Mẫu ghi: giống AIF)*

```markdown
**[TD-1 Q5] <đề rút gọn>** 🔁 (nếu sai lần 2)
A / B / C / D
- ✅ **B**: vì ... `[G 2.1]`
- ❌ A: ...
- 🔑 Keyword: "..." => ...
```
