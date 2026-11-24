# CCAR-F - Đọc nhanh trước giờ thi (10-15 phút)

> Bản rút gọn của `CCAR-F-NOTES.md`: chỉ giữ **luật, keyword, lỗi lặp lại**. Cần chi tiết => xem số mục trong ngoặc (vd "3.2"). Gặp từ khó => bảng 📖 **Giải nghĩa từ khó** ở mục 0 của notes.

---

## 1. Trước khi làm bài: 5 thói quen

1. **Đọc CUỐI câu trước**: "most effective **first step**", "most **maintainable**", "**guarantee**", "reduce overhead **while maintaining reliability**". Chữ đó quyết định đáp án.
2. **Đọc số liệu**: "12% skip", "85% simple / 15% complex", "18 tools", "14 files" => số liệu chỉ thẳng vào đáp án.
3. **Gạch 4 loại đáp án sai**:
   - **prompt / few-shot** khi đề cần **đảm bảo 100%**
   - **hệ thống mới** (classifier, routing layer, model to hơn) khi cách đơn giản **chưa thử**
   - **đẩy việc cho dev** (vd "bắt dev chia PR nhỏ" thay vì sửa hệ thống)
   - **flag / file không tồn tại**
4. **Multiple response**: đề ghi chọn mấy => chọn **đủ** số đó.
5. Đề có **2 yêu cầu** ("giảm latency" **và** "giữ độ tin cậy") => đáp án phải thỏa **cả 2**.

⚙️ **Luật thi**: 60 câu, 4/6 scenario, 120 phút (~2 phút / câu), đậu **>= 720/1000**. Trả lời **hết mọi câu**.

---

## 2. 🔁 Lỗi đã lặp lại (đọc kỹ nhất)

| # | Chủ đề | Quy tắc 1 dòng |
|---|---|---|
| 1 | Hỏi / điều tra trước (M1 Q8, Q29) | Khách **đòi người rõ ràng** => escalate **ngay**. Bực nhưng làm được => đề nghị làm **hoặc** escalate. ❌ hỏi thêm trước |
| 2 | Tóm tắt văn xuôi (Q18, Q56, Q37) | Giữ dữ liệu bằng **cấu trúc**: chỉ field cần, lớp context riêng, session mới + structured summary. ❌ prose, ❌ resume với tool result cũ |
| 3 | Error cho model (M1 Q14, Q49, Q51 · M4 Q60) | Có **loại + retry được không + bước tiếp**. Request hỏng => JSON-RPC protocol error. Tool chạy mà lỗi => `isError`. Lỗi để agent nói với user => **nguyên nhân + bước khắc phục**, ❌ mã lỗi kỹ thuật |
| 4 | Cấu hình Claude Code (M1 Q20, Q25, Q50 · M2 Q41, Q44 · M4 Q21, Q29 · M5 Q34) | Tự hỏi "**có pattern đường dẫn không?**". Có => rules + `paths:`. Không pattern, maintainer tự biết => **@import**. Lúc theo lúc không => **/memory** trước. "**Never** sửa X" => `permissions.deny`. Checklist chỉ dùng lúc review => slash command, ❌ CLAUDE.md (luôn load), ❌ subagent riêng |
| 5 | Gộp / tách tool (M1 Q3, Q31, Q44 · M2 Q7 · M4 Q32, Q54, Q56, Q57 · M5 Q26) | 1 tool **nhiều việc** hoặc **nhiều bộ tham số** => tách. 2 tool **trùng nghĩa** => gộp. Model cần **thấy hết** để chọn => tool trả dữ liệu, hành động để riêng. Tool **1 việc**, description sơ sài => **viết lại description**, ❌ tách, ❌ validation server. Tool B gọi tool A chỉ để lấy 1 field => **B nhận ID tự tra**, ❌ gộp |
| 6 | Hook khi có cách đầy đủ hơn (M1 Q2, Q52 · M4 Q18) | Nhiều đáp án là code => chọn cái **phủ mọi trường hợp** (kiểm tra sau khi loop dừng; tool tự tạo yêu cầu duyệt) |
| 7 | Prompt caching (Q6, Q54) | Caching chỉ là **chi phí / tốc độ**, không sửa gốc. Chi tiết ngoài phạm vi thi => thường là **bẫy** |
| 8 | Chia task (M2 Q5, Q12 · M5 Q6, Q42) | Bước **cố định, biết trước** => **prompt chaining**. Việc **mở**, chưa biết lỗi ở đâu => **dynamic** (vừa tìm vừa đổi kế hoạch). ❌ orchestrator-workers cho việc cố định, ❌ kế hoạch đầy đủ trước khi biết gì |
| 9 | Làm to hơn (M2 Q13, Q50 · M6 Q53) | Output không nhất quán / case lạ bị bịa => **few-shot**. ❌ model to hơn, ❌ fine-tune, ❌ temperature 0. Sliding window mất thông tin cũ => **hybrid summary**, ❌ window to hơn |
| 10 | Context xuống cấp khi khám phá lâu (M2 Q26, Q29 · M5 Q22, Q50) | **scratchpad file** + **subagent** cho câu hỏi cụ thể. Chuyển sang chủ đề liên quan => tóm tắt findings rồi spawn subagent **kèm summary**. ❌ clear hết + 1 report, ❌ tóm tắt mọi file trước, ❌ subagent độc lập rồi tự gộp |
| 11 | Chọn built-in tool + khám phá code (M2 Q6, Q17, Q38 · M3 Q11 · M5 Q21) | Grep = **nội dung** (import, error message). Glob / `find` = **tên** file. Edit không có text unique => **Read + Write**. Hiểu code: Grep **entry point** rồi theo **import / function call**. ❌ file to nhất trước, ❌ subagent chia theo service khi cần hiểu 1 luồng |
| 12 | Iterative refinement (M2 Q37, Q48 · M5 Q1, Q4) | 1 edge case => **test case** (input + output mong muốn). Domain **lạ** => **interview pattern**. Lỗi ảnh hưởng nhau => **1 message** |
| 13 | 1 prompt / 1 call ôm quá nhiều (M3 Q3, Q6) | Thêm cho mảng A thì mảng B tụt, hoặc output bị cắt ở `max_tokens` => **chia nhiều prompt / call nhỏ** rồi gộp. ❌ checklist trong cùng prompt, ❌ đổi sang markdown |
| 14 | MCP tool / resource / prompt (M1 Q21, M4 Q42 · M3 Q2) | **Tool** = model tự gọi. **Resource** = dữ liệu / catalog để đọc (`@`-mention, bớt call dò dẫm). **Prompt** = template user chạy => **slash command** |
| 15 | Bẫy "deterministic" (M1 Q33, M4 Q26) | Model **không bao giờ** deterministic. Lợi ích JSON có field = **không phải parse text** |
| 16 | Plan mode: cần / không cần (M4 Q46 · M5 Q1, Q12 · M6 Q22) | Plan mode chỉ khi việc **to, nhiều file, nhiều cách làm**. Thư viện đổi **breaking API** ở 45 file nhiều module => **plan mode**, ❌ bump rồi sửa test fail dần. Bug có **stack trace rõ** / sửa **1 hàm 1 file** => **direct**. Chưa biết **yêu cầu** (domain lạ) => **interview pattern** (plan mode đọc code, không hỏi bạn) |
| 17 | Chọn cái đưa người xem (M2 Q18 · M5 Q32, Q47 · M6 Q50) | **confidence thấp (từng field, calibrate) / tài liệu mơ hồ, mâu thuẫn**. ❌ random (random = để **đo**), ❌ heuristic theo layout |
| 18 | Lỗi extraction (M2 Q19, Q46, Q51 · M5 Q41, Q45, Q46 · M6 Q11 🔴 lần 3) | Input quá dài (`context_length_exceeded`) => **chunk + gửi lại chỉ cái lỗi**, ❌ `max_tokens` (= output). Lỗi format validation => **gửi lại kèm lỗi cụ thể**, ❌ tiền xử lý. Tool X phải chạy trước => forced X **request đầu**, ❌ forced **mọi** request |
| 19 | Multi-agent (M2 Q4, Q22 · M5 Q24, Q29, Q51, Q53 · M6 Q17 🔴 lần 3, Q27, Q30) | Song song => **coordinator** spawn / gọi **2 Task trong 1 response**, ❌ subagent tự spawn con, ❌ lớp async ngoài. Số khác năm => **ghi ngày**, ❌ tin số mới nhất. Nhiều loại nội dung => **render theo loại**, ❌ ép về 1 format (kể cả "văn xuôi hết") |
| 20 | Hội thoại quên thông tin cũ (M4 Q22 · M6 Q4, Q53) | Mới 2-3 lượt đã quên => app **không gửi lịch sử** trong `messages` (API stateless), ❌ "vượt context window". Hội thoại dài, sliding window bỏ lượt cũ => **hybrid**: tóm tắt cũ + giữ mới nguyên văn; số tiền / ngày / ID => **case facts block**. ❌ tăng window |
| 21 | Review sót bug xuyên file (M2 Q33 · M6 Q8) | Bug ở file **không có trong prompt** (caller ở file không đổi) => **review agentic giới hạn lượt** (model tự Read / Grep theo reference). ❌ chain-of-thought, ❌ pass song song + nhét dependents tĩnh. **Khác** 14 file đã có trong prompt mà review nông => chia pass (attention dilution) |

---

## 2b. 🎯 Đáp án đúng vs bẫy bạn đã chọn (câu sai >= 2 lần)

> Đáp án viết lại bằng lời Claude, giữ **keyword thật** của đề. Cách ôn: **che 2 cột ✅ / ❌**, đọc "Đề nói", tự nói đáp án, rồi mới mở. 🔴 = sai 3 lần.

**Agent + multi-agent (D1)**

| Đề nói | ✅ Chọn | ❌ Bẫy bạn đã chọn | Phân biệt |
|---|---|---|---|
| 🔴 `lookup_citations` chạy trước khi có DOI, muốn `extract_metadata` chạy trước (M2 Q51 · M5 Q46 · M6 Q11) | forced `tool_choice: {"type":"tool","name":"extract_metadata"}` + enrichment ở **subsequent turns** | cùng forced đó nhưng "**for every API call**" | 2 đáp án mở đầu **giống nhau** => đọc **đuôi**. Mọi call => enrichment không bao giờ chạy. Cũng ❌ `"any"` (ép 1 tool bất kỳ), ❌ xếp tool lên đầu mảng `tools` |
| 🔴 2024: 35% vs 2022: 18% bị coi là mâu thuẫn (M2 Q22 · M5 Q51 · M6 Q17) | subagent **include publication / collection dates** trong structured output | synthesis coi số **most recent** là **authoritative**, số cũ ra appendix | khác năm = **xu hướng**. Sửa ở **nguồn** (output subagent), không đặt luật cứng ở synthesis |
| 🔴 tài chính / tin tức / patent bị ép hết thành bullet (M5 Q53 · M6 Q27, Q30) | synthesis **render each content type**: tables / prose / structured lists | **standardize** hết thành prose (M6), **conversion layer** về 1 common format (M5) | thấy "standardize / uniform / common format" => loại: vẫn ép 1 format |
| phân tích tuần tự chậm, muốn song song mà coordinator **vẫn theo dõi / debug** được (M2 Q4 · M5 Q24) | **coordinator spawns** nhiều subagent song song, gộp kết quả | subagent **tự spawn** subagent con | mọi thứ đi **qua coordinator** (hub-and-spoke) |
| 2 subagent độc lập nhưng chạy tuần tự (M5 Q29) | coordinator gọi **2 `Task` trong 1 response** | **async orchestration layer** bên ngoài agent | song song có sẵn trong agent loop, không cần hạ tầng mới |
| lỗi 500 lúc có lúc không, 200+ file, **chưa biết** ở đâu (M2 Q12 · M5 Q6) | **dynamic**: tạo subtask theo cái vừa tìm ra, đổi kế hoạch | lập **full plan** mọi code path trước | chưa biết gì => không lập kế hoạch đầy đủ được |
| refund > $500 phải duyệt, **không lách được** (M1 Q52 · M4 Q18) | **tool tự enforce**: < $500 refund luôn, > $500 tạo approval request + trả "pending" | **PreToolUse hook** gắn flag `requires_approval`, tool đọc flag | code **1 chỗ, phủ hết** thắng hook + flag (2 mảnh phải khớp nhau) |

**Tool + MCP (D2)**

| Đề nói | ✅ Chọn | ❌ Bẫy bạn đã chọn | Phân biệt |
|---|---|---|---|
| agent dùng Grep thay vì `analyze_dependencies` (description: "Analyzes dependency graph") (M2 Q7 · M5 Q26) | **expand description**: làm gì, trả gì (direct imports, transitive deps, cycles) | **split** thành 3 tool (M2), **routing instructions** trong system prompt (M5) | tool làm **1 việc**, description sơ sài => sửa **description** |
| 1 tool `analyze_document` + instruction tự do, 35% phải hỏi lại (M1 Q44 · M4 Q32) | **split**: `extract_data_points`, `summarize_content`, `verify_claim_against_source`, có input / output contract | viết **description + examples** tốt hơn | tool làm **nhiều việc** => tách. Ngược với dòng trên |
| MCP server có **prompts** ngoài tools (M1 Q21 · M4 Q42) | thành **slash command** user tự chạy (`/mcp__<server>__<prompt>`) | vào **tool registry**, model tự gọi | tool = model gọi; resource = dữ liệu đọc; **prompt = user chạy** |
| `control_device` timeout, agent chỉ nói "không phản hồi" (M1 Q14 · M4 Q60) | `isError` + **likely causes + next steps** để agent nói với user | device ID + timeout + mã API (M4); "Device offline" + tool riêng (M1) | lỗi để **user** đọc => nguyên nhân + bước khắc phục, không phải thông tin debug |
| hiểu logic cache rải 15 file trước khi sửa (M2 Q6 · M5 Q21) | theo **imports + class hierarchy** => tìm **base class**, Read, trace từng chỗ invalidation | Glob + đọc file **to nhất** (M2); Grep "invalidate" rồi đọc vài dòng quanh (M5) | hiểu **interface chung** trước, chi tiết sau |

**Claude Code (D3)**

| Đề nói | ✅ Chọn | ❌ Bẫy bạn đã chọn | Phân biệt |
|---|---|---|---|
| `/terraform`, `/kubernetes`: chỉ load rule hợp **loại file** đang sửa (M1 Q25 · M4 Q21) | `.claude/rules/` + `paths: ["terraform/**/*"]` | CLAUDE.md thư mục con (M1); `@import` trong **root** CLAUDE.md (M4) | có **pattern đường dẫn** => rules + `paths:` |
| monorepo 15 package, **không** có pattern tên, maintainer tự biết (M1 Q20 · M4 Q29 bỏ trống) | `@import` chuẩn liên quan trong CLAUDE.md **từng package** | `.claude/rules/` + `paths:` **liệt kê từng thư mục** | **không** có pattern => `@import`. Cặp với dòng trên |
| checklist review 8 mục, team dùng Claude cho nhiều việc khác (M2 Q44 · M5 Q34) | slash command **`/review`** (`.claude/commands/review.md`) | **CLAUDE.md** (M2); **review subagent** riêng (M5) | chỉ cần **lúc review**. CLAUDE.md luôn load; subagent nặng hơn mức cần |
| làm cache Redis, **mới** với cache production (M2 Q48 · M5 Q1) | để Claude **interview** bạn trước (invalidation, consistency, failure modes) | **plan mode** đọc code `/products` | thiếu **yêu cầu**, không thiếu hiểu code. Plan mode đọc code, không hỏi bạn |
| migration script sai với `null` (M2 Q37 · M5 Q4) | đưa **test case**: input có null + **expected output** | mô tả bằng lời + **rewrite** cả script | test case rõ nhất, không phá phần đang đúng |
| plan mode 2 chiều (M4 Q46 · M5 Q12 · M6 Q22) | **direct**: stack trace rõ / 1 hàm 1 file. **plan mode**: breaking change thư viện ở 45 file nhiều module | plan mode cho việc nhỏ (M4, M5); bump version + sửa test fail dần cho việc to (M6) | hỏi: "to / nhiều module / breaking change?" |
| review sót caller ở file **không đổi** (M2 Q33 · M6 Q8) | **turn-limited agentic review**: model tự Read / Grep theo reference | **chain-of-thought** (M2); **parallel passes** + direct dependents + summary call (M6) | thiếu **context** => cho tool đi tìm. Đủ file mà review nông => chia pass |

**Structured output (D4)**

| Đề nói | ✅ Chọn | ❌ Bẫy bạn đã chọn | Phân biệt |
|---|---|---|---|
| lợi ích chính của JSON có field so với text (M1 Q33 · M4 Q26) | agent lấy giá trị **reliably**, không phải **parse text** | "model xử lý JSON **deterministically**" | model không bao giờ deterministic => loại |
| batch 10.000, 300 lỗi `context_length_exceeded` (M2 Q19 · M5 Q41) | **chunk** + resubmit **chỉ 300 cái lỗi** | tăng **`max_tokens`** | `max_tokens` = **output**; lỗi do **input** dài |
| 12% fail Pydantic ("got '2 to 3'"), retry y nguyên ra y lỗi (M2 Q46 · M5 Q45) | resubmit **kèm validation error cụ thể** | **preprocess** tài liệu nguồn | retry **kèm lỗi** sửa được lỗi format |
| format không nhất quán / số đo lạ bị bịa (M2 Q13, Q50) | **few-shot** 2-3 cặp input / output | **bigger model** (Q13); **fine-tune** (Q50) | "làm to hơn" = bẫy. Fine-tune không thi |

**Context + human review (D5)**

| Đề nói | ✅ Chọn | ❌ Bẫy bạn đã chọn | Phân biệt |
|---|---|---|---|
| reviewer chỉ xem được 5% / 20% (M2 Q18 · M5 Q32, Q47 · M6 Q50) | **low confidence** (field-level, **calibrated** với labeled set) + tài liệu **ambiguous / contradictory** | **random 5% sample** (M2, M5); tài liệu **formatting anomalies** / layout lạ (M5, M6) | random = để **đo**, không để chọn. Layout không báo trước field nào sai |
| đọc 8/45 file thì quên dần pattern (M2 Q26 · M5 Q50) | **subagents** cho câu hỏi cụ thể ("find all test files"), main agent giữ bức tranh lớn | summary + **clear** hết (M2); **Grep tên hàm** thay vì đọc (M5) | guide 5.4 nguyên văn |
| mới vài lượt đã hỏi lại thứ user vừa nói (M4 Q22 · M6 Q4) | app **không gửi prior messages** trong `messages` (API stateless) | tool **xóa state** (M4); **context window exceeded** (M6) | 2-3 lượt không thể đầy context |
| sliding window 2 chiều (M1 Q54 · M4 Q35 bỏ trống · M6 Q53) | 94% câu chỉ cần 3-5 lượt gần => **sliding window** 8-10 lượt. User mất sở thích cũ => **hybrid**: summary cũ + giữ mới nguyên văn | **prompt caching** (M1); **window to hơn** 25 => 50 (M6) | caching không làm context nhỏ đi; window to chỉ mất muộn hơn |

---

## 2c. 📚 Story index: câu đã gặp => đáp án (theo 6 scenario thi)

> Đọc cột **Story** như đang đọc đề, **tự nói đáp án trước**, rồi mới nhìn ✅. Cột **Clue** = chữ trong đề chỉ ra đáp án. Trong mỗi scenario, câu yếu nhất đứng đầu. Tổng: 114 câu (mock M1-M6 + 12 câu mẫu guide). Flashcard dùng cùng dữ liệu này.

> 🔴 sai 3 lần · 🔁 sai 2 lần · ❌ sai 1 lần (đã sửa) · ⚠️ key site sai, bạn đúng · 🟡 đúng nhưng không chắc / bỏ trống · 📘 câu mẫu guide

**1. Customer Support Resolution Agent** (26 câu)

| | Story | Clue | ✅ Chọn | ❌ Bẫy (mock bạn đã chọn) | Câu |
|---|---|---|---|---|---|
| 🔁 | Refunds over $500 need manager approval and must not be bypassable | cannot be bypassed | **The refund tool enforces it: under $500 refunds, over $500 creates an approval request and returns pending** | PreToolUse hook sets a requires_approval flag that the tool reads (M1, M4) | M1 Q52 · M4 Q18 |
| 🔁 | control_device times out; the agent only says the device is not responding | help the user take the next step | **isError + likely causes + next steps the agent can tell the user** | Device ID + timeout + API code for debugging (M4); Device offline + a separate tool (M1) | M1 Q14 · M4 Q60 |
| 🔁 | 35 turns (about 50K tokens), slow and worse; 94% of questions need only the last 3-5 turns | 94%, customers easily restate old details | **Sliding window: send only the last 8-10 turns** | Prompt caching while still sending everything (M1); left blank (M4) | M1 Q54 · M4 Q35 |
| 🔁 | Only 2-3 turns later the agent asks again for info the user just gave (their name, loves jazz) | only a few turns | **The app is not sending prior messages in the messages array (the API is stateless)** | The tool cleared the state (M4); context window exceeded (M6) | M4 Q22 · M6 Q4 |
| ❌ | Angry customer wants someone who can actually help; the return is something the agent can do right now | frustrated, but the task is doable | **Acknowledge, say it can be done now, offer to do it OR escalate** | Ask what went wrong / investigate first (M1) | M1 Q8 · M4 Q19 ✅ |
| ❌ | Customer: I want to talk to a real person NOW (no tools called yet) | explicit request for a human | **Escalate immediately with the conversation history** | Acknowledge and ask one question first (M1) | M1 Q29 · M4 Q20 ✅ |
| ❌ | Agent hits max_turns mid-case; every case must end resolved or escalated | guarantee | **Code checks the result after the loop stops; if not resolved, code calls escalate_to_human with context** | Hook that stops at 80% of max_turns (M1) | M1 Q2 · M4 Q6 ✅ |
| ❌ | After lookup_order (bought 45 days ago), how should the loop decide refund vs escalate? | agentic loop | **The tool result goes into the conversation and the model reasons about the next step** | Preconfigured decision tree (M1) | M1 Q28 · M4 Q8 ✅ |
| ❌ | Tools grew from 4 to 10 (or 1 to 7); accuracy drops; agent confuses issue_credit and process_refund | semantically overlapping tools | **Merge the overlapping tools (one tool + action param; lookup_order + include_tracking flag)** | Split into finance and delivery subagents (M1) | M1 Q31 · M4 Q11 ✅ · M6 Q19 ✅ |
| ❌ | track_shipment throws a Python exception; the agent can only say something went wrong | agent has no next step | **Structured error: category, recoverable or not, suggestion (check the ID, search by order number)** | Retry with backoff inside the tool (M1) | M1 Q49 |
| ❌ | MCP: (1) missing required param, (2) API returns 404, (3) API returns 503 | which error type for each | **(1) JSON-RPC protocol error; (2) and (3) tool result with isError** | All three as isError (M1) | M1 Q51 · M4 Q28 ✅ |
| ❌ | lookup_order returns 40+ fields and fills context; 2 more orders to check | verbose tool output | **Keep only the relevant fields (items, purchase date, return deadline, status)** | Model writes a prose summary (M1) | M1 Q18 · M4 Q49 ✅ |
| ❌ | 3 issues in one session, near the context limit; customer asks about the first issue again | exact IDs, amounts, status needed | **Extract structured issue data (ID, amount, status) into a separate context layer** | Prose summary of older turns (M1) | M1 Q56 · M4 Q4 ✅ |
| ❌ | Sliding window keeps 25 message pairs; users say it forgets earlier topics and preferences | earlier preferences lost | **Hybrid: summarize older messages, keep recent ones verbatim** | Grow the window to 50 pairs (M6) | M6 Q53 |
| ❌ | Customer returns after 4 hours; old session has lookup_order PENDING; agent keeps citing it | even after fresh tool calls | **New session + structured summary of the old one + fresh tool calls before replying** | Resume and strip the old tool_results (M1) | M1 Q37 · M4 Q33 ✅ · M6 Q2 ✅ |
| ❌ | Confirm? dialog: 98% click within 2 seconds and still post to the wrong account / time / content | 2 seconds | **Show the full details (content, account, time, platform) in the confirmation** | Make the user type a confirmation phrase (M4) | M4 Q52 |
| ⚠️ | send_notification times out; unknown if it was sent; retries cause duplicates | status unknown | **By logic: report status unknown, may already be sent, do NOT retry** | Site key: retry_safe true (wrong by logic, see ⚠️ table) | M1 Q46 = M4 Q40 |
| 🟡 | Every tool error comes back as Operation failed | same message for every error | **Add errorCategory, isRetryable and a description at the source** | Few-shot to teach the model error patterns | M1 Q40 |
| 🟡 | 90-minute billing session; the summary turned a $184.60 credit (Mar 3, promised by May 10) into vague text | amounts, dates, promises lost | **Case facts block (amounts, dates, IDs) sent with every prompt, never summarized** | Better summarizer / bigger window / summarize later | M6 Q40 |
| 🟡 | The refund call times out midway while the customer waits | customer is waiting | **Explain, confirm eligibility, say it is a system error, offer escalation or retry later** | Keep retrying with backoff while the customer waits | M1 Q5 |
| 🟡 | Agent invents an order_id; the question asks for the root cause | root cause | **Fix the description: order_id must come from lookup_order (if it asked to guarantee: a gate)** | Gate / validation when the question asks for the root cause | M1 Q23 |
| 🟡 | remove_team_member(dry_run) preview is skipped in 15% of calls | ensure every, user explicitly confirms | **Two tools: preview_remove_member returns a single-use token; execute_remove_member requires it** | Prompt to always dry_run first / default dry_run=true | M6 Q28 |
| 🟡 | Asking 3 clarifying questions makes 40% of users give up | too many questions | **Make a reasonable assumption, state it, invite correction** | One question per turn / classifier / silent lookup table | M4 Q31 |
| 📘 | Agent skips get_customer in 12% of cases and refunds without a verified customer | 12%, skips a required step | **Gate in code: block process_refund until a verified customer ID exists** | Stronger system prompt / few-shot / routing classifier | Guide Q1 |
| 📘 | Agent mixes up two tools whose descriptions are one line each | first step, minimal descriptions | **Expand the tool descriptions (what it does, when to use it, inputs, examples)** | Few-shot examples / routing layer / merge the tools | Guide Q2 |
| 📘 | FCR 55%: agent escalates easy cases and handles hard ones alone | escalation is miscalibrated | **Explicit escalation criteria + few-shot examples in the system prompt** | Self-reported confidence score / separate classifier / sentiment analysis | Guide Q3 |

**2. Code Generation with Claude Code** (18 câu)

| | Story | Clue | ✅ Chọn | ❌ Bẫy (mock bạn đã chọn) | Câu |
|---|---|---|---|---|---|
| 🔁 | IaC repo with /terraform and /kubernetes: load only the rules for the file type being edited | a path pattern exists | **.claude/rules/ + paths: ["terraform/**/*"]** | Subfolder CLAUDE.md (M1); @import in the root CLAUDE.md (M4) | M1 Q25 · M4 Q21 |
| 🔁 | Monorepo with 15 packages and 3 standards; no naming pattern; maintainers know what each package needs | no pattern, maintainers decide | **@import the right standard in each package's CLAUDE.md** | .claude/rules/ with paths: listing each folder (M1); left blank (M4) | M1 Q20 · M4 Q29 |
| 🔁 | 8-item review checklist; the team also uses Claude for many other tasks | only needed when reviewing | **/review slash command (.claude/commands/review.md)** | Put it in CLAUDE.md (M2); dedicated review subagent (M5) | M2 Q44 · M5 Q34 |
| 🔁 | Add a Redis cache with 5-minute TTL; you are new to production caching | unfamiliar domain | **Have Claude interview you first (invalidation, consistency, failure modes)** | Plan mode reading the /products code (M2, M5) | M2 Q48 · M5 Q1 |
| 🔁 | Migration script mishandles records that contain null | one edge case | **Give a test case: input with null + expected output** | Describe the bug in words and rewrite the whole script (M2, M5) | M2 Q37 · M5 Q4 |
| 🔁 | Intermittent 500 errors, 200+ files, unknown which component is involved | unknown where | **Dynamic decomposition: create subtasks from findings, adapt the plan** | Full plan of every code path before reading code (M2, M5) | M2 Q12 · M5 Q6 |
| ❌ | CLAUDE.md conventions are followed only sometimes; first diagnostic step? | first step, inconsistent | **/memory to see which memory files are loaded** | Search ~/.claude for conflicting rules (M1) | M1 Q50 · M4 Q15 ✅ |
| ❌ | 3 rules in CLAUDE.md, but Claude still edits db/migrations | never / prefer / after every edit | **permissions.deny for migrations + logging rule stays in CLAUDE.md + PostToolUse hook for Prettier** | Move everything to .claude/rules/ (M2) | M2 Q41 · M5 Q55 ✅ |
| ❌ | Production bug with a clear stack trace to one function, in a module you do not know | clear stack trace | **Direct execution: read the trace and the code, fix it** | Plan mode to list possible root causes (M5) | M2 Q10 ✅ · M5 Q12 · M6 Q26 ✅ |
| ❌ | Add one date check inside one function in one file | one file, small | **Direct execution** | Plan mode to analyze impact on the booking flow (M4) | M4 Q46 |
| ❌ | Auth library v2 to v3: callback to Promise, User type changed, 3 methods removed, imported in 45 files | breaking changes, several modules | **Plan mode: explore usage, map code paths, make a migration strategy, then implement** | Bump the version, run the tests, fix each failure (M6) | M6 Q22 |
| ❌ | Every PR gets the same 3 steps: style, security, docs | fixed, known steps | **Prompt chaining** | Orchestrator-workers (M2) | M2 Q5 · M5 Q5 ✅ |
| ⚠️ | PDF report: narrow columns, date format, page breaks; the three issues affect each other | issues interact | **All three in one detailed message (guide 3.5) - your pick, correct** | Site key: fix one at a time and test each (wrong by guide, see ⚠️ table) | M2 Q42 · M5 Q23 · M6 Q20 |
| 🟡 | Code format is right only some of the time | every time | **PostToolUse hook, matcher Edit\|Write, runs Prettier** | Stop hook + prompt asking the model to check | M1 Q22 · M4 Q9 ✅ |
| 🟡 | Add tests to a 200-file legacy codebase; no priorities given | open-ended | **Glob/Grep to map the structure, prioritize key modules, adapt the plan** | Read all 200 files first / fixed schedule | M2 Q53 ✅ · M5 Q42 blank |
| 📘 | Create a /review command that the whole team gets | team-wide | **.claude/commands/ in the repo** | ~/.claude/commands/ (personal) / CLAUDE.md / .claude/config.json (does not exist) | Guide Q4 |
| 📘 | Split a monolith into microservices | large, architectural | **Plan mode** | Direct execution, fix as you go | Guide Q5 |
| 📘 | Conventions depend on file type; test files are scattered across folders | scattered files of the same type | **.claude/rules/ with glob paths:** | Root CLAUDE.md / skills / per-folder CLAUDE.md | Guide Q6 |

**3. Multi-Agent Research System** (15 câu)

| | Story | Clue | ✅ Chọn | ❌ Bẫy (mock bạn đã chọn) | Câu |
|---|---|---|---|---|---|
| 🔴 | Web data says 35% (2024), an internal report says 18% (2022); synthesis flags a contradiction | different years | **Subagents include publication / collection dates in their structured output** | Treat the most recent data as authoritative, older data to an appendix (M2, M5, M6) | M2 Q22 · M5 Q51 · M6 Q17 |
| 🔴 | Financial JSON, news prose and patent lists all get rendered as bullet points | tabular clarity, narrative flow, hard to scan | **Synthesis renders each type: financial = tables, news = prose, technical = structured lists** | Standardize all to prose (M6 twice); conversion layer to one common format (M5) | M2 Q27 ✅ · M5 Q53 · M6 Q27, Q30 |
| 🔁 | 12 precedents analyzed one by one (3 minutes); make it faster, but the coordinator must still track and debug | coordinator visibility | **Coordinator spawns several subagents in parallel and merges the results** | The analysis subagent spawns its own child subagents (M2, M5) | M2 Q4 · M5 Q24 |
| 🔁 | One analyze_document tool with a free-text instruction; 35% of results need re-requests | one tool, many jobs | **Split into extract_data_points, summarize_content, verify_claim_against_source, each with a contract** | Better description + examples (M1, M4) | M1 Q44 · M4 Q32 · M6 Q44 ✅ |
| ❌ | Coordinator calls web search, waits, then calls document analysis; the two are independent | independent but sequential | **Coordinator emits 2 Task calls in one response** | Async orchestration layer outside the agent (M5) | M2 Q35 ✅ · M5 Q29 |
| ❌ | Coordinator gives step-by-step orders; subagents fail on new topics | over-specified | **Give goals + quality criteria; the subagent chooses how to search** | Classifier for well-defined vs exploratory tasks (M1) | M1 Q7 · M4 Q13 ✅ |
| ❌ | Curation agent makes 18+ sequential calls; it must see all candidates to choose | see everything to choose | **Combined discover_and_analyze returns all candidates + scores; add_to_collection stays separate** | Preview + approve by a fixed rule (M1) | M1 Q3 · M4 Q37 ✅ |
| 🟡 | Summarizing a follow-up takes 40 seconds through a subagent | the coordinator already has the context | **The coordinator summarizes from its own context** | Prompt caching for the subagent | M1 Q6 |
| 🟡 | The final report loses which source each fact came from | source metadata lost | **Subagents return a claim-source mapping (claim, URL/doc, quote, date); synthesis keeps it** | Inline citations in prose summaries | M1 Q55 · M4 Q45 |
| 🟡 | A multi-agent job crashes; resume without redoing the work | resume after a crash | **Each agent writes a manifest file; the coordinator reads it on resume** | Restart from scratch / rely on chat history | M1 Q45 |
| 🟡 | Query types are diverse and evolving | diverse and evolving | **The coordinator (LLM) decides how to route each query** | Fast-path rules / pattern routing / trained classifier | M2 Q16 |
| 🟡 | A contract amendment changes 30 days to 45 days | two values, both real | **Schema keeps multiple values + source + effective date** | Pick one value | M2 Q32 |
| 📘 | Report about creative industries is missing music, writing and film | each subagent did its own part well | **The coordinator decomposed the topic too narrowly** | Blame the search or synthesis subagents | Guide Q7 |
| 📘 | Web search subagent times out | what the coordinator should receive | **Structured error context: what was tried, partial results, alternatives** | Generic status / empty result as success / stop the whole workflow | Guide Q8 |
| 📘 | Synthesis needs to verify facts; 85% are simple checks | 85% simple | **Give synthesis one narrow verify_fact tool; complex checks go via the coordinator** | Give synthesis all search tools / batch verify / pre-cache | Guide Q9 |

**4. Developer Productivity** (20 câu)

| | Story | Clue | ✅ Chọn | ❌ Bẫy (mock bạn đã chọn) | Câu |
|---|---|---|---|---|---|
| 🔁 | Cache logic is spread over 15 files; understand it before adding a trigger | understand before changing | **Follow imports + class hierarchy, find the base class, Read it, trace each invalidation** | Glob + read the largest file (M2); Grep invalidate and read nearby lines (M5) | M2 Q6 · M5 Q21 |
| 🔁 | After reading 8 of 45 files, answers get worse and earlier patterns are forgotten | context degrading, same task | **Subagents for specific questions (find all test files); the main agent keeps the big picture** | Summary + clear everything (M2); Grep function names instead of reading (M5) | M2 Q26 · M5 Q50 |
| 🔁 | Agent uses Grep instead of analyze_dependencies (description: Analyzes dependency graph) | one job, vague description | **Expand the description: what it returns (direct imports, transitive deps, cycles)** | Split into 3 tools (M2); routing instructions in the system prompt (M5) | M2 Q7 · M5 Q26 |
| 🔁 | An MCP server exposes prompts (templates) besides tools | MCP prompts | **They show up as slash commands that users run** | Added to the tool registry for the model to call (M1, M4) | M1 Q21 · M4 Q42 |
| ❌ | Find every file that imports @company/auth | text inside the files | **Grep the import line (content search)** | find -type d -name *auth* (M2) | M2 Q17 · M5 Q31 ✅ |
| ❌ | Insert a function in the middle of a file; Edit fails because no anchor text is unique | not unique | **Read the whole file, insert, Write it back** | Edit with replace_all (M2) | M2 Q38 · M5 Q16 ✅ |
| ❌ | A new dev must understand auth across 800+ files and many services | one flow across services | **Grep the auth entry point, Read it, follow imports and calls** | Parallel subagent per service (M3) | M3 Q11 |
| ❌ | 30+ minutes of exploration; answers are inconsistent; the dev has to repeat things | long session | **Scratchpad file with key findings, re-read when needed** | Summarize every file before exploring (M2) | M2 Q29 · M5 Q2 ✅ |
| ❌ | 25 minutes on rendering; answers now say typical rendering patterns; next question is how physics integrates with rendering | typical patterns, integrates with | **Summarize the rendering findings, spawn a physics subagent with that summary** | Independent physics subagent, merge yourself (M5); /clear | M2 Q8 ✅ · M5 Q22 |
| ❌ | 3 MCP servers (git, Jira, docs); one request needs all three | how the tools become available | **Every server's tools are discovered at connect and usable together** | Agent picks one server and loads only its tools (M5) | M2 Q14 ✅ · M5 Q9 |
| ❌ | 3 MCP servers (issues, wiki, DB); the agent makes 8-10 blind calls because it does not know what each has | blind exploratory calls | **Expose each server's catalog as MCP resources** | Orchestrator routes by keyword to one server (M3) | M3 Q2 |
| ❌ | User says delete old backups; agent calls delete_file although policy says archive | most directly improve tool selection | **Expand both descriptions (when to use each, not for backups)** | Server-side validation that blocks deletes (M4) | M1 Q59 ✅ · M4 Q56 |
| ❌ | get_neighborhood_info(address) always needs get_property_details first, only to get the address | a call made only to fetch one field | **get_neighborhood_info takes property_id and looks up the address itself** | Merge both into one tool (M4) | M1 Q60 ✅ · M4 Q57 |
| ❌ | One tool for refund / cancel / reship, each with different params; missing or extra params | different param sets | **Split into 3 tools, each with only its own params** | if-then-else schema / nested object / all optional + few-shot; left blank (M4) | M1 Q27 ✅ · M4 Q54 |
| ❌ | Document of 175-190K tokens, last third missed, 200K context, tool definitions take 2,500 tokens | add up the numbers | **Tool definitions + system prompt + document nearly fill the 200K** | Exceeds the effective attention span (M5) | M2 Q43 ✅ · M5 Q35 |
| 🟡 | Find every eval( call, or the SYNC_CONFLICT error string across 12 services | text inside files | **Grep** | Glob *eval* / ls -R (file names only) | M3 Q5 · M2 Q45 |
| 🟡 | Subagent read 47 files, the connection dropped, a teammate renamed 2 functions | most context still valid | **Resume the subagent + tell it about the renamed functions** | New session / paste the whole transcript / ignore the rename | M5 Q58 · M6 Q46 |
| 🟡 | Yesterday's session is still useful; 3 of the 12 analyzed files were modified | small, known change | **Resume + tell it which 3 files changed so it re-reads them** | New session / re-read all 12 / say nothing | M2 Q49 ✅ · M5 Q11 blank |
| 🟡 | Try 2 refactor approaches from the same analysis | two branches from one point | **fork_session** | Redo the analysis twice | M2 Q40, Q54 |
| 🟡 | Need standard access to Jira data | standard integration | **Use an existing community MCP server for Jira** | Write a custom server / curl / export to markdown | M3 Q4 |

**5. Claude Code for CI/CD** (15 câu)

| | Story | Clue | ✅ Chọn | ❌ Bẫy (mock bạn đã chọn) | Câu |
|---|---|---|---|---|---|
| 🔁 | Review misses callers in unchanged files that use the old argument order; reviews run async | unchanged files not included | **Turn-limited agentic review: the model reads files and searches via tools** | Chain-of-thought (M2); parallel per-file passes + dependents + summary call (M6) | M2 Q33 · M5 Q19 ✅ · M6 Q8 |
| ❌ | CI test generation: trivial asserts, hand-built records instead of fixture factories | in the first place | **CLAUDE.md: test standards + good vs trivial examples + list of fixture factories** | Second Claude pass that scores and deletes weak tests (M6) | M3 Q9 ✅ · M6 Q15 |
| ❌ | One prompt reviews security + API + logic; few-shot raises logic 34% to 41% but API drops 82% to 68% | one area up, another down | **Separate prompts per area, each with its own examples, then merge findings** | Replace the few-shot with a checklist in the same prompt (M3) | M3 Q3 |
| ❌ | 30+ file PR; report_findings JSON is cut off at max_tokens | truncated output | **Split into several calls by file group, merge the findings arrays** | Return a markdown list instead (M3) | M3 Q6 |
| 🟡 | Managed Code Review (GitHub App) posts 18 noisy findings per PR | GitHub App review | **REVIEW.md at the repo root (paths to skip, required checks)** | Edit the workflow file / put the rules in CLAUDE.md | M3 Q1 |
| 🟡 | 30% false positives come from team-specific conventions | persistent context on every review | **Write the conventions in CLAUDE.md** | Filter afterwards / remove the surrounding context | M3 Q13 |
| 🟡 | Cap turns and spend, enforced by Claude Code itself | Claude Code stops by itself | **--max-turns 10 --max-budget-usd 2.00** | timeout-minutes (the runner) / cheaper model / dontAsk | M3 Q8 |
| 🟡 | CI startup takes 18 seconds from auto-discovery; root CLAUDE.md standards are still needed | keep the defaults, add the standards | **--bare + --append-system-prompt-file ./CLAUDE.md** | --system-prompt-file (replaces the default prompt) | M3 Q14 |
| 🟡 | The review only processes the diff; Claude stopped using its file tools | replaced vs added | **--append-system-prompt (keeps the default prompt)** | --system-prompt (replaces the default and loses the tool guidance) | M2 Q47 |
| 🟡 | Prompt says only report issues you are sure of; real bugs get hidden | the hedging instruction hides bugs | **Report everything with confidence + severity, filter later** | Second pass with the same prompt / more thinking | M3 Q7 |
| 🟡 | Half of the findings are ignored as trivial; fix it before adding infrastructure | before adding infrastructure | **Explicit criteria: what to report, what to skip** | Self-score 1-10 / highly confident only / classifier | M3 Q12 |
| 🟡 | 35% false positives; the model must generalize to code it has not seen | generalize | **Annotated few-shot examples** | Long spec / be conservative / keyword filter | M3 Q10 |
| 📘 | CI job hangs waiting for input | non-interactive | **claude -p** | CLAUDE_HEADLESS / --batch (do not exist) / < /dev/null | Guide Q10 |
| 📘 | Move both the pre-merge check and the overnight report to the Batch API | someone waits on the pre-merge check | **Batch only the overnight report; the pre-merge check stays on the sync API** | Batch both / batch + timeout fallback | Guide Q11 |
| 📘 | 14-file PR review is shallow and contradicts itself | the files are in the prompt, just too many | **Per-file passes + one integration pass** | Bigger context / make devs split PRs / majority vote of 3 runs | Guide Q12 |

**6. Structured Data Extraction** (20 câu)

| | Story | Clue | ✅ Chọn | ❌ Bẫy (mock bạn đã chọn) | Câu |
|---|---|---|---|---|---|
| 🔴 | lookup_citations runs before the DOI exists; extract_metadata must run first | two options start the same, read the end | **Forced tool_choice {"type":"tool","name":"extract_metadata"}, enrichment in subsequent turns** | The same forced choice for every API call (M2, M5, M6) | M2 Q51 · M5 Q46 · M6 Q11 |
| 🔁 | Batch of 10,000 documents; 300 fail with context_length_exceeded | input too long | **Chunk and resubmit only the 300 failed documents** | Raise max_tokens (M2, M5) | M2 Q19 · M5 Q41 |
| 🔁 | 12% fail Pydantic (expected float, got 2 to 3); a plain retry fails the same way | unchanged retry fails | **Resubmit with the specific validation error** | Preprocess the source documents (M2, M5) | M2 Q46 · M5 Q45 |
| 🔁 | Main benefit of JSON fields over free text for downstream agents | the word deterministic is a trap | **The agent reads exact values without parsing text** | The model processes JSON deterministically (M1, M4) | M1 Q33 · M4 Q26 |
| 🔁 | Reviewers can check only 5% of extractions; which ones should they get? | limited capacity | **Low-confidence extractions + ambiguous or contradictory documents** | A random 5% sample (M2, M5) | M2 Q18 · M5 Q32 |
| 🔁 | 12% semantic errors pass the schema; reviewers can check 20% | semantic errors | **Field-level confidence + calibrate thresholds on a labeled set** | Documents with formatting anomalies / unusual layouts (M5, M6) | M2 Q57 ✅ · M5 Q47 · M6 Q50 |
| ❌ | materials field: cotton blend vs Cotton/Polyester mix vs empty | inconsistent format | **Few-shot with 2-3 input/output pairs** | Bigger model (M2) | M2 Q13 · M5 Q49 ✅ |
| ❌ | 23% of corrections are measures like a handful or a splash: invented numbers or blanks | a repeated pattern | **Few-shot showing how to keep the original measure text** | Fine-tune on the 847 corrections (M2) | M2 Q50 · M5 Q43 ✅ |
| ❌ | property_type enum fails 8%: studio, loft, duplex... and new types keep appearing | long-term, new types | **Enum + other + a property_type_detail field** | Free string + normalize later (M2) | M2 Q55 · M5 Q14 ✅ |
| ⚠️ | Batch API (50% off, up to 24h); SLA 30 hours with 99.9% reliability | 99.9%, worst case | **Submit every 4 hours (4 + 24 = 28h) - your pick, correct** | Site key: every 6 hours (exactly 30h, no margin, see ⚠️ table) | M6 Q32 |
| 🟡 | Retry-with-error fixes most failures in 2-3 tries; when is it LEAST effective? | the info is not in the input | **Co-authors shown as et al. when the full list exists only in another document** | Format errors (retries fix those) | M6 Q37 |
| 🟡 | Calendar JSON is often invalid and downstream rejects it | syntax errors | **Tool use with an input schema** | Prompt + parse the text | M2 Q3, Q59 |
| 🟡 | skills string[]: Python and SQL sometimes joined, unstated skills added, length 5-10 vs 40+ | all three are inconsistency | **Few-shot showing how to split, what counts as stated, level of detail** | Limit to 10-20 skills | M2 Q20 ✅ · M5 Q15 blank |
| 🟡 | The field is nullable but the model still invents 500 | the schema is already nullable | **Instruct it to return null when the info is absent** | Make the field required | M2 Q36 |
| 🟡 | 5% of fields are empty although the document has the info (inline citations vs bibliography) | different document structures | **Few-shot with varied document structures** | Retry unchanged / make the fields optional | M2 Q58 |
| 🟡 | 12% errors hide in high-confidence results; you need ongoing measurement | measure | **Stratified random sampling every week** | Re-extract / lower the threshold / heuristics | M2 Q15 · M5 Q13 |
| 🟡 | 97% overall accuracy; is it ready to automate? | an aggregate can hide a weak type | **Measure per document type and per field first** | Trust the overall number / pilot and wait for errors | M2 Q52 |
| 🟡 | ML extraction confidence: 23% of wrong ones still pass, 31% of right ones still go to review | routing by confidence | **Return field + confidence + request_review set by a tested threshold in code + reason** | Raw score + few-shot so the model reads it | M1 Q13 · M4 Q55 |
| 🟡 | Prices come as $12 vs 12.00, icons vs text | normalization | **Strict schema + normalization rules in the prompt** | Post-processing script / second call | M2 Q28 · M5 Q8 |
| 🟡 | 50,000 contracts, 2-week deadline, 82% pass the schema on the first try | cost-efficient + deadline | **Batch all, then resubmit only the failures in new batches, refining the prompt between them** | Real-time API for everything / resubmit everything | M6 Q25 |

---

## 3. ⚠️ Đáp án mock đã kiểm tra là SAI (đừng học theo)

| Câu | Mock ghi | Đúng theo guide |
|---|---|---|
| M1 Q46 = M4 Q40 (timeout, không biết đã gửi chưa) | `retry_safe: true` | báo "**status unknown, đừng retry**" (retry => gửi trùng) |
| M1 Q32 (thiếu `user_id`) | strict schema | ⚠️ tranh cãi: "bảo đảm cấu trúc" => schema; "giúp **hiểu**" => description |
| M2 Q42 = M5 Q23 = M6 Q20 (3 lỗi format PDF **ảnh hưởng nhau**) | sửa **lần lượt**, test từng bước (2 site khác nhau đều ghi vậy) | gửi **cả 3 trong 1 message** (guide 3.5). Lần lượt = cho lỗi **độc lập** |
| M6 Q32 (SLA 30h, batch tới 24h) | gửi mỗi **6h** | mỗi **4h** (guide 4.5 nguyên văn). 6h + 24h = đúng 30h, không dư cho retry |
| Cheatsheet site M6 (luật 21) | "few-shot sửa được thông tin thiếu" | thông tin **không có** trong nguồn => **null / đưa người xem** (retry, few-shot đều vô ích). Few-shot chỉ giúp khi thông tin **có** nhưng ở dạng lạ. (Luật 17 "tách find / filter" là **đúng**, xem cặp precision / recall ở mục 5 D4) |
| M1 (giải thích) | chương sách, flag, tên MCP bịa | chỉ tin **đáp án**, kiểm với guide (notes mục 10) |

---

## 4. 10 luật vàng (mục 0)

1. Cần **đúng 100%** (tiền, danh tính, bước bắt buộc theo thứ tự) => **code chặn** (gate / hook). ❌ prompt, few-shot: model **thường** nghe, không phải **luôn** nghe.
2. "**First step**" => việc **nhỏ nhất** mà sửa đúng **gốc lỗi** (vd viết lại tool description). ❌ xây hệ thống mới khi cách rẻ chưa thử.
3. Sửa ở **chỗ sai đầu tiên** mà log chỉ ra (vd coordinator chia việc quá hẹp). Agent phía sau làm đúng phần được giao => **không phải lỗi nó**.
4. Lỗi => trả **structured error** (loại lỗi, đã thử gì, phần kết quả có được, hướng khác). ❌ "Operation failed" chung chung · ❌ trả rỗng như thành công · ❌ dừng cả workflow.
5. Mỗi agent chỉ có tool cho **việc của nó** (least privilege). Nhu cầu **hay gặp** => thêm **1 tool hẹp** (`verify_fact`), không cho cả bộ.
6. Agent **tự chấm** 1-10 + **cảm xúc khách** => ❌ không dùng để quyết định escalate (Q3). Confidence **từng field**, đã **calibrate** với dữ liệu có đáp án đúng => ✅ chọn cái nào đưa người xem (5.6, 6.5).
7. Model to / context dài **không** sửa **attention dilution** (quá nhiều file 1 lần => chú ý **chia mỏng**: file nông, sót bug, nhận xét mâu thuẫn) => **chia pass** (5.6).
8. `CLAUDE_HEADLESS`, `--batch`, `.claude/config.json` có commands = **không tồn tại** => loại.
9. **Batch** (rẻ 50%, có thể tới 24h) chỉ cho việc **không ai ngồi chờ** (report overnight). **Pre-merge check** (dev đợi check pass mới merge được) => **sync API** (5.5).
10. "be conservative" / "high-confidence only" **vô dụng** (model không biết "cẩn thận" là sao) => **tiêu chí cụ thể**: báo gì / bỏ qua gì + ví dụ code.

---

## 5. Các cặp dễ nhầm

**Agent + tool (D1, D2)**

| Cặp | Phân biệt |
|---|---|
| `stop_reason` **tool_use** vs **end_turn** | `tool_use` = Claude **xin** gọi tool => code chạy tool, gửi `tool_result` lại, gọi tiếp. `end_turn` = Claude trả lời **xong** => dừng. ❌ dừng khi thấy chữ "done" / khi đủ N vòng / khi response có text (2.1) |
| **Hook** vs **prompt** | hook = code chạy **mỗi lần** => **chắc chắn**. Prompt = lời dặn, model **thường** nghe => **xác suất** (2.4, 2.5) |
| **Code** vs **gate** vs **hook** | code = **cả họ** chắc chắn (deterministic). Gate = **luật** "B bị chặn tới khi A xong" (Q1). Hook = **chỗ gắn** check do framework cung cấp (PreToolUse / PostToolUse). Gate build được trong tool / agent loop / PreToolUse hook. Thi: gate + hook đều ✅. Prompt / few-shot / routing classifier ❌ (2.4) |
| **Routing layer** vs **classifier** | routing layer = code chạy **trước** model, dò keyword / regex để **chọn sẵn** tool (Q2 C). Classifier = **model riêng**, train trên dữ liệu có nhãn (Q3 C, Q1 D). "First step" => ❌ làm quá mức cần. ✅ khi Claude tự route (coordinator chọn subagent) hoặc route confidence thấp sang người (0, 2.2, 6.5) |
| **PostToolUse** vs **PreToolUse** (chặn tool call) | PostToolUse = chạy **sau** tool, **sửa kết quả** trước khi model đọc (vd đổi mọi ngày về 1 format). PreToolUse = chạy **trước** tool, **chặn hành động** (refund > $500 => chặn, chuyển người) (2.5) |
| **Prompt chaining** vs **dynamic decomposition** | chaining = các bước **cố định, biết trước** (review từng file => 1 lượt cross-file). Dynamic = **chưa biết trước** gặp gì, vừa làm vừa lập kế hoạch (thêm test cho code cũ) (2.6) |
| **Resume** vs **session mới + summary** | `--resume <name>` = mở lại phiên cũ, khi thông tin cũ **còn đúng**. Kết quả tool cũ **đã lỗi thời** (file đổi nhiều) => session mới + chèn bản tóm tắt (2.7) |
| **fork_session** | tách 1 phiên thành **2 nhánh** từ cùng 1 điểm => thử **2 hướng** (2 cách refactor) mà không phân tích lại từ đầu (2.7) |
| Subagent **context** | subagent **không thấy** hội thoại của coordinator => coordinator phải **chép** findings cần thiết **vào prompt** giao việc. Coordinator cần `"Task"` trong `allowedTools` (2.3) |
| `allowedTools` vs `AgentDefinition.tools` | Coordinator **không gọi được** subagent => thiếu `"Task"` trong `allowedTools`. Subagent **dùng tool quá tay** => thu hẹp `tools` trong `AgentDefinition` (bỏ trống = lấy **hết** tool). SDK thật: `allowedTools` = list tool **chạy không cần hỏi**, không xóa tool khác => subagent **có thể** có tool coordinator không list (vd Bash) (2.3) |
| Chạy subagent **song song** | coordinator gọi **nhiều Task trong 1 response** (không phải mỗi lượt 1 cái) (2.3) |
| `tool_choice` **auto / any / forced** | đặt **cho từng request**. auto = model tự quyết gọi tool hay trả chữ (chat thường). any = **phải** gọi tool, model **tự chọn** tool nào (extraction nhiều loại tài liệu, chưa biết loại nào => phải trả JSON qua 1 extract tool). forced = **phải** gọi **đúng** tool X (ép `extract_metadata` chạy **trước**, bước sau ở request sau). ⚠️ API thật: Opus 5.5 / Sonnet 5.5 / Fable 5.1+ trả **400** với any / forced, **thi theo guide** (3.3) |
| 4 loại lỗi: **transient / validation / business / permission** | transient = lỗi **tạm** (timeout, service down) => **retry được**. validation (input sai), business (vi phạm policy), permission (không có quyền) => retry **vô ích**. Business => `retriable: false` + câu giải thích cho khách (3.2) |
| **Access failure** vs **empty result** | access failure = gọi **không được** (timeout) => cần quyết định retry. Empty result = gọi được, chỉ là **không có** dữ liệu => vẫn là thành công (3.2, 6.3) |
| MCP **resource** vs **tool** | resource = **danh mục để xem** (danh sách issue, DB schema) => agent bớt gọi tool dò dẫm. Tool = **hành động** (3.4) |
| **Grep** vs **Glob** | Grep = tìm **nội dung bên trong** file. Glob = tìm **tên file** (`**/*.test.tsx`) (3.5) |
| **Edit** lỗi | Edit cần 1 đoạn text **chỉ xuất hiện 1 lần** trong file. Xuất hiện nhiều lần => Edit lỗi => **Read** cả file + **Write** lại (3.5) |
| Confirm bị **bấm bừa** | 98% user bấm "Confirm?" trong 2 giây mà vẫn đăng sai => **hiện đủ chi tiết** (nội dung, tài khoản, giờ, nền tảng) trong câu xác nhận. ❌ bắt gõ chữ, ❌ chờ thêm, ❌ tự duyệt (M4 Q52) |

**Claude Code (D3)**

| Cặp | Phân biệt |
|---|---|
| `~/.claude/CLAUDE.md` vs `CLAUDE.md` repo | `~/.claude/` = **chỉ máy mình**, teammate không nhận. Trong repo = **cả team** nhận qua git (4.1) |
| `.claude/rules/` + `paths:` vs **CLAUDE.md thư mục** | file cùng loại nằm **rải rác** nhiều thư mục => rules + glob. CLAUDE.md thư mục chỉ áp cho **1 thư mục** (4.3) |
| `.claude/rules/` + `paths:` vs **@import** | Tự hỏi: "**glob pattern có chọn đúng file không?**". **Có** (file Terraform đều nằm dưới `terraform/`) => rules + `paths: ["terraform/**/*"]`, tự load khi sửa file khớp (M4 Q21). **Không**, chỉ người phụ trách biết (package `billing` có xử lý dữ liệu user không?) => `@import` đúng chuẩn cần dùng trong CLAUDE.md **từng package** (M4 Q29). ❌ `@import` trong **root** CLAUDE.md (root luôn load => không tiết kiệm token). ❌ rule liệt kê tay từng thư mục package (không phải pattern, thêm package là phải sửa) (4.1, 4.3) |
| `.claude/commands/` vs `~/.claude/commands/` | trong repo = **cả team** / trong home = **cá nhân** (4.2) |
| `.mcp.json` vs `~/.claude.json` | `.mcp.json` = MCP server **team**, secret để dạng `${ENV}` / `~/.claude.json` = MCP **cá nhân, thử nghiệm** (3.4) |
| **Skill** vs **CLAUDE.md** | skill = chỉ load **khi cần** / CLAUDE.md = **luôn load** (4.2) |
| **Tool** vs **Skill** vs **MCP** | tool = **làm** (hàm, code bạn chạy, trả dữ liệu, D2) / skill = **biết cách làm** (`SKILL.md` load vào context, **dùng** tool, `allowed-tools` giới hạn tool, D3) / MCP server = **gói tool** từ bên ngoài (2.1, 3.4, 4.2) |
| Rule **tự áp dụng** cho file rải rác | `.claude/rules/` + `paths:`. ❌ skill (guide: skill phải **gọi khi cần**, không tự áp) (Q6, 4.3) |
| `context: fork` / `allowed-tools` / `argument-hint` | 3 field ở **frontmatter đầu file `SKILL.md`** (không phải settings.json). Chạy skill ở **context riêng**, chỉ trả kết quả gọn (output dài không làm bẩn hội thoại chính) / **giới hạn tool** skill được dùng / **gợi ý tham số** khi gọi skill thiếu argument (4.2) |
| **Plan mode** vs **direct** | plan = việc **lớn**, nhiều file, quyết định kiến trúc / direct = việc **nhỏ, rõ**, 1 file. Kết hợp: plan trước rồi direct (4.4) |
| **Explore subagent** | giao phần khám phá dài cho subagent, nó trả **tóm tắt** => context chính gọn (4.4) |
| `/memory` vs `/compact` | `/memory` = xem **file memory nào đang load** / `/compact` = **nén context** khi đầy (4.1, 6.4) |
| Lỗi **liên quan** vs **độc lập** | liên quan (sửa cái này ảnh hưởng cái kia) => gửi **1 message** tất cả / độc lập => sửa **lần lượt** (4.5) |
| `permissions.deny` vs CLAUDE.md vs hook | "**never** sửa `db/migrations/`" => `permissions.deny` (chặn cứng) / "**prefer** module logging" => CLAUDE.md (lời dặn) / "**sau mỗi lần** edit chạy Prettier" => PostToolUse hook. `.claude/rules/` vẫn chỉ là lời dặn (M2 Q41) |
| `--system-prompt` vs `--append-system-prompt` | `--system-prompt` = **thay toàn bộ** system prompt mặc định của Claude Code (mất phần hướng dẫn dùng tool đọc file) / `--append-system-prompt` = **thêm** vào cuối, giữ mặc định (M2 Q47) |
| CI | `-p` (không treo chờ input) + `--output-format json` + `--json-schema` (output máy đọc được). `--max-turns` + `--max-budget-usd` = Claude Code **tự dừng** khi đủ lượt / tiền (≠ timeout của job). `--bare` = bỏ auto-discovery => khởi động nhanh, kèm `--append-system-prompt-file ./CLAUDE.md` để giữ chuẩn team (4.6, M3 Q8, Q14) |
| **REVIEW.md** vs **CLAUDE.md** | REVIEW.md = rule **chỉ cho** Code Review managed (GitHub App): path bỏ qua, check bắt buộc. CLAUDE.md = convention cho **mọi** việc, cả `/code-review` local (4.6, M3 Q1, Q13) |
| Tự review vs **phiên độc lập** | phiên vừa viết code tự review = **kém** (còn nhớ lý luận cũ, ít nghi ngờ). Phiên **mới** review = **tốt hơn** (4.6, 5.6) |

**Prompt + output (D4)**

| Cặp | Phân biệt |
|---|---|
| Lỗi **syntax** vs **semantic** | syntax = JSON **hỏng cú pháp** (thiếu ngoặc) => **tool_use + schema** là hết. Semantic = JSON đúng cú pháp nhưng **nội dung sai** (cộng các dòng không ra tổng, giá trị nằm nhầm field) => schema không bắt được => code kiểm tra + **retry kèm lỗi** (5.3) |
| Báo **sai nhiều** vs **sót** bug | báo sai nhiều (precision) => **tiêu chí cụ thể** báo gì / bỏ gì, ❌ "be conservative" / "only high-confidence". Sót bug vì prompt dặn "chỉ báo cái chắc chắn" (recall) => bước tìm **báo hết** kèm confidence + severity, bước sau **lọc theo ngưỡng** (5.1, M3 Q7) |
| `calculated_total` vs `stated_total` | tổng tự cộng từ các dòng **khác** tổng ghi trên hóa đơn => **flag** cho người xem (+ `conflict_detected`). ❌ để model / pass 2 **tự sửa cho khớp** (che mất lỗi) (5.4) |
| Retry **có ích** vs **vô ích** | có ích: lỗi **format, cấu trúc** (model tự sửa được). Vô ích: thông tin **không có** trong tài liệu (retry mấy lần cũng không có) => đánh dấu thiếu / đưa người xem (5.4) |
| Field **required** vs **nullable** | field có thể **không có** trong tài liệu => để **nullable**. Để required => model **bịa** cho đủ (5.3) |
| enum mở rộng | thêm `"other"` + field `detail` ghi giá trị thật, thêm `"unclear"` khi mơ hồ => model không bị ép chọn sai (5.3) |
| **Few-shot** | 2-4 ví dụ, chọn case **mơ hồ**, có **lý do** vì sao chọn vậy. Dùng để: format nhất quán, extraction bớt bịa, phân biệt code OK vs lỗi thật => **bớt báo sai** (5.2) |
| **Batch** | rẻ 50%, có thể tới 24h, **không cam kết thời gian**, **không** gọi tool nhiều lượt trong 1 request, ghép kết quả bằng `custom_id`, **polling** để lấy kết quả, lỗi thì gửi lại **chỉ request lỗi**. Chỉ cho việc **không ai ngồi chờ** (5.5) |
| 1 lượt vs **nhiều lượt** (multi-pass) | review nhiều file => **1 lượt / file + 1 lượt xem liên kết giữa file** (5.6) |

**Context + reliability (D5)**

| Cặp | Phân biệt |
|---|---|
| Tóm tắt làm mất số liệu | tóm tắt nhiều lần => "đơn #A123, $89.99" thành "vài đơn hàng". Sửa: trích số tiền, ngày, mã đơn, mong muốn của khách vào **case facts block**: chép **nguyên văn**, gửi kèm **mọi** request, **không** đem đi tóm tắt. Chỉ phần nói chuyện được tóm tắt (6.1) |
| **Lost in the middle** | model nhớ đầu + cuối, sót phần **giữa** input dài => đưa key findings lên **đầu** + chia section header. ≠ attention dilution: cái này do **vị trí**, kia do **khối lượng** (6.1) |
| Tool trả về quá dài | **cắt** còn field cần dùng **trước khi** đưa vào context (6.1) |
| Agent **hỏi lại** thông tin user vừa nói | API **stateless** => app **không gửi lịch sử hội thoại** ở request sau. ❌ "tool xóa state", ❌ "Claude chỉ nhớ 2 lượt" (6.1, M4 Q22) |
| Context xuống cấp (trả lời chung chung "typical patterns") | ghi findings ra **scratchpad file** (file nháp), giao câu hỏi cụ thể cho subagent, `/compact` (6.4) |
| Crash recovery | mỗi agent ghi trạng thái ra file cố định (**manifest**), coordinator đọc file đó khi chạy lại (6.4) |
| 97% tổng thể, đã tự động hóa được chưa? | con số tổng có thể che 1 loại tài liệu kém => đo **riêng từng loại tài liệu + từng field**, lấy mẫu kiểm tra **chia theo nhóm** (stratified sampling) (6.5) |
| Confidence | confidence **từng field**, calibrate với **dữ liệu có đáp án đúng** => chọn cái đưa người xem. ❌ agent tự chấm 1-10 thô để escalate (Q3). ❌ chỉnh ngưỡng theo điểm tổng (6.5) |
| **Random sampling** vs **route theo confidence** | random / stratified sampling = để **đo** error rate, bắt lỗi kiểu mới (M2 Q15). Sức người có hạn, chọn cái đưa người xem => **confidence thấp / tài liệu mơ hồ** (M2 Q18, Q57) (6.5) |
| 2 nguồn **mâu thuẫn** | giữ **cả 2** + ghi nguồn + **ngày** (khác nhau có thể do thời gian). ❌ tự chọn 1 (6.6) |

---

## 6. Escalate hay không? (6.2)

| Tình huống | => |
|---|---|
| Khách **đòi gặp người** | **escalate NGAY**, không điều tra trước |
| Khách bực, nhưng agent làm được | đề nghị giải quyết. Khách **nhắc lại** đòi người => escalate |
| Policy **không nói tới / mơ hồ** (vd đòi price-match giá **đối thủ**) | **escalate** |
| Không tiến triển được | escalate |
| Tool trả **nhiều khách** khớp | **hỏi thêm** thông tin (email, SĐT), không đoán |
| Escalate lệch (case dễ thì chuyển người, case khó thì tự làm) | thêm **tiêu chí rõ + few-shot** vào system prompt |
| Handoff (bàn giao cho người) | gửi summary: customer ID, nguyên nhân, số tiền, đề xuất. Người nhận **không đọc được** transcript |

---

## 7. ❌ Không thi (thấy đáp án nói về mấy cái này thì cảnh giác)

Fine-tuning · RLHF / Constitutional AI · auth / billing / OAuth · host MCP server · embedding / vector DB · computer use · vision · **streaming** · rate limit / tính giá · tokenizer · **prompt caching chi tiết** · cấu hình AWS / GCP / Azure · benchmark model · chi tiết ngôn ngữ / framework cụ thể
