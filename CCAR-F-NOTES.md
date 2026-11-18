# CCAR-F - Ghi chú ôn thi Claude Certified Architect - Foundations

> Cấu trúc: note chính + cheatsheet + nhật ký quiz.
> Nguồn chính: exam guide chính thức v1.0 (effective July 2026) bạn đã tải. Bắt đầu: 2026-10-31.
> ⚠️ Kiểm tra 2026-11-03: đợt đổi đề **07/12/2026** chỉ áp dụng cho CCAO-F, CCDV-F, CCAR-P (guide mới ra 17/11). **CCAR-F không có trong danh sách** => vẫn học guide v1.0 (2026-11-15: banner của 1 site học tiếng Việt (mục 9 #6) cũng ghi đợt đổi đề 07/12 "trừ CCAR-F"). Nguồn: [Pearson VUE - Anthropic](https://www.pearsonvue.com/us/en/anthropic.html). Sau 17/11 xem lại trang này + [Partner Academy](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification) 1 lần cho chắc.
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
💡 **Không** có câu ordering / matching, **không** có câu "unscored" được nhắc tới. Tất cả là câu chọn đáp án trong scenario.

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
- Embedding, vector DB. Computer use. Vision / ảnh. **Streaming / SSE**
- Rate limit, quota, **tính giá API**. Token counting / tokenizer
- **Prompt caching chi tiết** (chỉ cần biết nó tồn tại). Cấu hình cloud (AWS / GCP / Azure). Benchmark / so sánh model
- Chi tiết implementation của **ngôn ngữ / framework cụ thể** (chỉ cần đủ để cấu hình tool + schema)

### 🧠 10 luật vàng (rút ra từ 12 câu mẫu của guide) *(Claude)*

Mỗi luật: **dấu hiệu trong đề** => **chọn gì** => **vì sao**. Gặp từ khó => xem 📖 **Giải nghĩa từ khó** bên dưới.

**1. Cần đúng 100% => dùng code chặn, không dùng prompt** `[G 1.4, 1.5]` `[G Q1]`
- Dấu hiệu: tiền, xác minh danh tính, bước phải làm **theo thứ tự**, "guarantee", "must always", "agent bỏ qua bước X trong 12% case".
- Chọn: **gate / hook** (xem 2.4): code làm cho tool sau **không chạy được** tới khi bước trước xong.
- Vì sao: prompt, few-shot = model **thường** nghe theo, nhưng không phải **lúc nào** cũng nghe. Với tiền, sai 1 lần cũng không được.

**2. "First step" => cách rẻ nhất mà sửa đúng gốc lỗi** `[G Q2, Q3]`
- Dấu hiệu: "most effective **first step**", "proportionate first response".
- Chọn: sửa đúng **nguyên nhân gốc** (root cause) bằng việc **nhỏ nhất**: viết lại tool description, thêm tiêu chí rõ + ví dụ vào prompt.
- Loại: xây **hệ thống mới** (routing layer, classifier, model riêng, đổi sang model to hơn) khi cách rẻ **chưa thử**. Guide gọi là **over-engineered** (làm to hơn mức cần). Xem 🧭 Routing layer / classifier bên dưới.

**3. Lỗi nằm đúng chỗ log chỉ ra, đừng đổ cho agent phía sau** `[G Q7]`
- Dấu hiệu: đề cho log từng bước. Vd report về "AI trong creative industries" chỉ nói về visual art, log cho thấy coordinator chỉ giao 3 chủ đề con đều là visual art.
- Chọn: sửa ở **chỗ sai đầu tiên** trong log (vd coordinator **chia việc quá hẹp**).
- Loại: sửa agent phía sau (search, synthesis) khi nó **làm đúng** phần được giao. Đầu vào thiếu thì đầu ra thiếu, không phải lỗi của nó.

**4. Báo lỗi phải đủ thông tin: không im lặng, không dừng hết** `[G 2.2, 5.3]` `[G Q8]`
- Chọn: trả **structured error** (lỗi có các field rõ): loại lỗi (timeout? không có quyền?), đã thử gì, kết quả **có được một phần** (partial result), hướng khác có thể thử. Coordinator đọc rồi tự quyết: thử lại, đổi cách, hay đi tiếp với phần đã có.
- Loại: ❌ chỉ ghi "Operation failed" (coordinator không biết làm gì tiếp). ❌ trả **rỗng** như thể thành công (giấu lỗi). ❌ **dừng cả workflow** chỉ vì 1 subagent lỗi.

**5. Mỗi agent chỉ có tool cho việc của nó** `[G 2.3]` `[G Q9]`
- Tên gọi: **least privilege** (quyền tối thiểu).
- Dấu hiệu: agent dùng tool ngoài vai trò (synthesis agent tự đi search web). Hoặc 1 nhu cầu **hay gặp** (85% case chỉ cần check 1 fact đơn giản) phải vòng qua coordinator => chậm.
- Chọn: cho thêm **1 tool hẹp** chỉ làm đúng việc đó (vd `verify_fact`). Case khó (15%) vẫn đi qua coordinator.
- Loại: cho agent **cả bộ** tool của agent khác.

**6. Điểm tự tin do agent tự chấm + cảm xúc khách: không dùng để quyết định escalate** `[G 5.2]` `[G Q3]` `[G 4.6, 5.5]`
- Loại: "agent tự chấm 1-10, dưới ngưỡng thì chuyển người" (con số không khớp thực tế, agent **tự tin sai** đúng ở case khó). "Đo sentiment, khách bực thì escalate" (khách bực ≠ case khó).
- ⚠️ Khác: confidence cho **từng field / từng finding**, đã **calibrate** (so với bộ dữ liệu có đáp án đúng), dùng để chọn **cái nào đưa người xem lại** = ✅ (5.6, 6.5).

**7. Model to hơn / context dài hơn không sửa được việc review quá nhiều thứ 1 lần** `[G 1.6, 4.6]` `[G Q12]`
- Dấu hiệu: review 14 file trong 1 lượt => file kỹ file sơ sài, sót bug rõ, cùng 1 kiểu code chỗ khen chỗ chê.
- Nguyên nhân: **attention dilution** (sự chú ý bị chia mỏng, xem 5.6). Context lớn hơn = **chứa** được nhiều hơn, không = **chú ý** kỹ hơn.
- Chọn: **chia pass**: 1 lượt cho từng file + 1 lượt riêng xem liên kết giữa các file.

**8. Đáp án có flag / file / env var không tồn tại => loại ngay** `[G Q4, Q10]`
- Đồ bịa hay gặp: `CLAUDE_HEADLESS`, `--batch`, `.claude/config.json` có mảng commands.
- Đồ thật: `claude -p`, `--output-format json`, `--json-schema`, `.claude/commands/`, `.claude/rules/`, `.mcp.json`.

**9. Batch API chỉ dùng cho việc không ai ngồi chờ** `[G 4.5]` `[G Q11]`
- Batch = rẻ 50%, nhưng có thể **tới 24 giờ** mới xong, **không cam kết** thời gian.
- Hợp: report chạy đêm (overnight), audit hằng tuần (weekly). Chậm vài giờ không ai bị ảnh hưởng.
- Không hợp: **pre-merge check** (dev phải đợi check pass mới merge PR được, xem 5.5) => **sync API** (gọi bình thường, trả lời ngay).

**10. Lời dặn mơ hồ không làm bớt báo sai => viết tiêu chí cụ thể** `[G 4.1]`
- Loại: "be conservative", "only report high-confidence findings" (model không biết "cẩn thận" cụ thể là sao).
- Chọn: ghi rõ **báo gì / bỏ qua gì** cho từng loại lỗi + **ví dụ code** cho từng mức severity.
- Mục tiêu: tăng **precision** (trong số lỗi báo ra, bao nhiêu % là lỗi thật). Báo sai nhiều (**false positive**) => dev mất niềm tin cả những cảnh báo đúng.

🧭 **Routing layer / classifier là gì?** (luật 2) *(Claude)*
- **Routing layer** = code thường chạy **trước** model mỗi lượt, đọc message rồi quyết định đi đâu (tool / agent / prompt nào), thường bằng **keyword / regex**. Vd Q2 C: thấy "order #12345" => chọn sẵn `lookup_order`.
- **Classifier** = **model riêng** (ML hoặc thêm 1 LLM call) xếp input vào nhãn. Cần **labeled data**, train, host, monitor. Vd Q3 C: model train trên ticket cũ đoán "có cần escalate?". Q1 D "routing classifier" = đoán loại request => chỉ bật tool cho loại đó.
- Vì sao sai: tốn công (build, data, bảo trì) + thường **không chạm root cause**. Q1: giải quyết tool **có sẵn**, không phải **thứ tự**. Q2: over-engineered, **bỏ qua khả năng hiểu ngôn ngữ của LLM**, keyword dễ vỡ. Q3: cần data + hạ tầng ML khi **chưa thử prompt**.
- ⚠️ Chữ "routing" **không phải** lúc nào cũng sai: coordinator tự chọn subagent `[G 1.2]`, route extraction confidence thấp sang người review `[G 4.6, 5.5]`, case phức tạp đi qua coordinator `[G 2.3]` = ✅. Cờ đỏ = **hệ thống riêng mới** khi **cách rẻ chưa thử**. Đề nói "đã sửa prompt / description mà vẫn lỗi" => hạ tầng có thể thành đúng.
- Chữ bẫy: "trained on historical", "detected keywords", "pre-selects", "separate model", "sentiment analysis".

### 🔑 Từ điển "chữ trong đề => đáp án" *(Claude, gom từ guide)*

| Chữ trong đề | Nghĩa (tình huống là gì) | => Thường chọn (và vì sao) |
|---|---|---|
| **guaranteed / must always / compliance / financial** | phải đúng **100%**, sai 1 lần cũng không được | **code chặn**: hook / gate (programmatic prerequisite). ❌ prompt, few-shot (chỉ là xác suất) |
| agent **skips** a required step X% of the time | agent **bỏ qua** bước bắt buộc trong X% case (vd không gọi `get_customer` trước khi refund) | **gate**: code chặn tool sau (`process_refund`) tới khi tool trước (`get_customer`) trả kết quả |
| **most effective first step** | hỏi bước **đầu tiên** nên làm | việc **nhỏ nhất** mà sửa đúng gốc lỗi (vd **viết lại tool description**). ❌ xây hệ thống mới |
| picks the **wrong tool**, tools have **minimal / similar descriptions** | chọn nhầm tool vì description **sơ sài / giống nhau** | **viết description đầy đủ hơn**: input nhận gì, ví dụ câu hỏi, edge case, khi nào dùng tool kia |
| agent has **18 tools** / too many tools | agent có **quá nhiều** tool => chọn kém | **giảm còn 4-5** tool mỗi agent, chia tool theo vai trò |
| must call a tool, **not return conversational text** (vd extraction có **nhiều** extract tool, **không biết trước** loại tài liệu) | ở **request này**, câu trả lời **phải là 1 tool call** (để lấy JSON đúng schema), không được trả lời bằng chữ | `tool_choice: "any"` = **bắt buộc** gọi tool, nhưng model **tự chọn** tool nào (vd `extract_invoice` hay `extract_receipt` tùy tài liệu). ⚠️ Không có nghĩa "agent lượt nào cũng phải gọi tool": chat bình thường => `auto` (lab 2: đặt `any` thì "Thanks, bye!" cũng bị gọi `escalate_to_human`) (3.3) |
| tool X must run **first** (vd `extract_metadata` trước các bước enrichment) | biết rõ **request đầu** phải gọi **đúng tool X**, không phải tool khác | forced `tool_choice: {"type":"tool","name":"X"}` = **bắt buộc** gọi **đúng X**. Chỉ đặt cho **request đó**. Các bước sau chạy ở **request sau** (thường lại để `auto`) (3.3) |
| **job hangs** waiting for input in CI | Claude Code chạy trong CI mà job **đứng im** chờ người gõ | `claude -p` (`--print`) = chạy 1 lần không tương tác, in kết quả rồi thoát |
| **machine-parseable** findings, inline PR comments | kết quả phải để **code đọc** được (vd tự post comment vào PR) | `--output-format json` + `--json-schema` (output JSON đúng schema) |
| available to **every developer** who clones the repo | **ai clone repo** cũng phải có | đặt file **trong repo** (commit vào git): `.claude/commands/`, `.claude/skills/`, `.mcp.json`, `CLAUDE.md` |
| **personal / experimental** | chỉ **mình** dùng, đang thử | đặt trong **home**: `~/.claude/...`, `~/.claude.json` (không vào git) |
| **new team member** doesn't get the instructions | người mới **không nhận được** rule mà người cũ có | rule đang nằm ở `~/.claude/CLAUDE.md` (chỉ có trên máy người cũ) => chuyển vào `CLAUDE.md` **trong repo** |
| test files **spread throughout** the codebase | file cùng loại (test) nằm **rải rác** nhiều thư mục | `.claude/rules/*.md` + `paths:` glob (vd `**/*.test.tsx`): rule **tự load** khi sửa file khớp |
| skill output is **verbose**, **pollutes** main conversation | skill in ra **quá dài**, làm rối hội thoại chính | `context: fork` trong SKILL.md: skill chạy ở **context riêng**, chỉ trả kết quả gọn về |
| restructure / migrate **dozens of files**, **architectural** decisions | thay đổi **lớn**: nhiều file, quyết định kiến trúc | **plan mode**: điều tra + lên kế hoạch trước khi sửa |
| **single-file** fix, clear stack trace | sửa **nhỏ, rõ**: 1 file, có stack trace | **direct execution**: làm luôn |
| **cost** savings + **overnight / weekly** | muốn **rẻ**, kết quả **không gấp** | **Message Batches API**: rẻ 50%, có thể tới 24h mới xong |
| **blocking** / pre-merge / developer waits | có người **ngồi chờ** kết quả (dev đợi check pass mới merge được PR) | **sync API** (gọi bình thường, trả lời ngay). ❌ Batch |
| **correlate** batch requests and results | ghép **kết quả** batch với **request** tương ứng | `custom_id`: tự đặt ID cho mỗi request, kết quả trả về kèm ID đó (thứ tự trả về không quan trọng) |
| JSON **syntax** errors | JSON **hỏng cú pháp** (thiếu ngoặc, sai dấu phẩy) | **tool_use + JSON schema** (strict): output luôn đúng cú pháp |
| totals **don't sum**, value in **wrong field** | JSON đúng cú pháp nhưng **nội dung sai** (cộng các dòng không ra tổng, giá trị nằm nhầm field) | **code kiểm tra** + **retry kèm lỗi cụ thể** (schema không bắt được loại lỗi này) |
| model **fabricates** values for missing fields | model **bịa** giá trị cho field mà tài liệu không có | để field **optional / nullable**: được trả `null` thì model không cần bịa |
| info **only in another document** not provided | thông tin **không có** trong tài liệu được đưa vào | retry **vô ích** (thử mấy lần cũng không có) => đánh dấu thiếu / đưa người xem |
| **inconsistent format** of output | output lúc kiểu này lúc kiểu khác | **few-shot**: 2-4 ví dụ output mẫu |
| too many **false positives**, developers **lose trust** | **báo lỗi sai** nhiều => dev mất niềm tin | **tiêu chí cụ thể** báo gì / bỏ qua gì + **tạm tắt** loại cảnh báo hay báo sai trong lúc sửa prompt |
| **14 files**, superficial / **contradictory** review | review **nhiều file 1 lượt** => chỗ kỹ chỗ sơ sài, nhận xét mâu thuẫn | **1 lượt cho từng file** + **1 lượt** xem liên kết giữa các file |
| same session **reviews its own** code | phiên vừa **viết code** tự **review** code đó | **phiên mới, độc lập** review (không nhớ lý luận cũ nên dám nghi ngờ) |
| subagent **doesn't know** earlier findings | subagent **không biết** kết quả các bước trước | coordinator **chép thẳng findings vào prompt** giao việc (subagent không tự thấy hội thoại của coordinator) |
| report covers only **part of the topic** | report **thiếu mảng** của chủ đề | coordinator **chia việc quá hẹp** (lỗi ở coordinator, không phải subagent) |
| timeout in a subagent | 1 subagent **bị lỗi** (timeout) | subagent trả **structured error** (loại lỗi, đã thử gì, phần kết quả có được) về coordinator. ❌ trả rỗng, ❌ dừng hết |
| customer **asks for a human** | khách **đòi gặp người** | **escalate ngay**, không điều tra trước |
| policy is **silent / ambiguous** | chính sách **không nói tới** trường hợp này (vd đòi price-match giá **đối thủ**, policy chỉ nói giá của mình) | **escalate** |
| tool returns **multiple customers** | tìm khách ra **nhiều người** khớp | **hỏi thêm** thông tin (email, SĐT). ❌ tự đoán 1 người |
| summary **loses numbers / dates** | tóm tắt hội thoại dài làm **mất** số tiền, ngày | **case facts block**: khối dữ kiện giữ riêng, gửi kèm mọi prompt, không đem đi tóm tắt |
| findings in the **middle** get missed | thông tin ở **giữa** input dài bị sót | **lost in the middle** => đưa key findings lên **đầu**, chia section header |
| **97% overall** accuracy, ready to automate? | độ chính xác **tổng** cao, muốn bỏ bớt người kiểm tra | đo **riêng từng loại tài liệu + từng field** trước (con số tổng có thể che 1 loại kém), lấy mẫu kiểm tra **chia theo nhóm** (stratified sampling) |
| two credible sources **conflict** | 2 nguồn uy tín **nói khác nhau** | **giữ cả 2** + ghi nguồn + ngày. ❌ tự chọn 1 |
| long session, answers get **vague / "typical patterns"** | phiên dài, trả lời **chung chung** thay vì tên class cụ thể => context đã xuống cấp | ghi findings ra **scratchpad file**, giao câu hỏi cụ thể cho **subagent**, `/compact` |
| resume but **files changed** | resume phiên cũ nhưng **file đã bị sửa** | báo agent **file nào đổi** để xem lại đúng chỗ. Đổi quá nhiều (tool result cũ sai hết) => **session mới + summary** |

### 📖 Giải nghĩa từ khó *(Claude)*

| Từ | Nghĩa đơn giản | Ví dụ |
|---|---|---|
| **root cause** | nguyên nhân **gốc**, không phải triệu chứng | chọn nhầm tool vì description sơ sài => gốc là description |
| **over-engineered** | giải pháp **to / phức tạp hơn mức cần** | dựng classifier khi chưa thử sửa prompt |
| **deterministic** vs **probabilistic** | **chắc chắn** (code, lần nào cũng giống nhau) vs **xác suất** (model thường làm đúng, không phải luôn luôn) | hook vs prompt |
| **gate** / **programmatic prerequisite** | code **chặn** bước B tới khi bước A xong | chặn `process_refund` tới khi có verified customer ID |
| **upstream / downstream** | bước / agent **phía trước** / **phía sau** trong luồng | coordinator là upstream của search agent |
| **least privilege** | chỉ cho **vừa đủ** quyền / tool cần cho việc | synthesis agent không có web search |
| **scoped tool** | tool **hẹp**, chỉ làm 1 việc | `verify_fact` thay vì cả bộ search |
| **structured error** | lỗi trả về có field rõ (loại lỗi, retry được không, mô tả) | `{"errorCategory":"business","isRetryable":false}` |
| **transient error** | lỗi **tạm thời**, thử lại có thể được | timeout, service down |
| **partial result** | kết quả **có được một phần** trước khi lỗi | tìm được 3/5 nguồn |
| **hub-and-spoke** | mô hình **trục - nan hoa**: subagent chỉ nói chuyện với coordinator, không nói thẳng với nhau | |
| **provenance** | **nguồn gốc** của từng thông tin (URL, tài liệu, ngày) | câu nào lấy từ nguồn nào |
| **stale** | **cũ, lỗi thời**, không còn đúng | tool result từ trước khi file bị sửa |
| **inject** | **chèn** thông tin vào prompt / context | chèn summary vào session mới |
| **instance độc lập** | 1 phiên Claude **mới**, không thấy hội thoại / lý luận cũ | phiên mới review code mà phiên cũ viết |
| **pass** | **1 lượt** cho model xử lý dữ liệu | per-file pass = mỗi file 1 lượt |
| **false positive** / **precision** | báo lỗi mà **thật ra không lỗi** / % lỗi báo ra là lỗi thật | |
| **calibrate** + **labeled validation set** | so điểm confidence với **bộ dữ liệu đã có đáp án đúng**: mỗi mức điểm thật sự đúng bao nhiêu %, rồi đặt ngưỡng | model ghi 0.9 nhưng chỉ đúng 70% => điểm chưa đáng tin |
| **stratified sampling** | lấy mẫu kiểm tra **chia theo nhóm** (nhóm nào cũng có mẫu), không bốc ngẫu nhiên chung | loại viết tay chỉ 5% vẫn được lấy đủ mẫu |
| **progressive summarization** | tóm tắt hội thoại dài **dần dần**, mỗi lần tóm lại bản tóm cũ => dễ mất số liệu | |
| **case facts block** | khối **dữ kiện cố định** (số tiền, ngày, mã đơn), gửi kèm **mọi** prompt, **không** đem đi tóm tắt | |
| **scratchpad file** | file **nháp** agent ghi findings để đọc lại sau | |
| **manifest** | file ghi **trạng thái** công việc, dùng để chạy tiếp sau crash | |
| **SLA** | **cam kết thời gian** trả kết quả | "có kết quả trong 30 giờ" |
| **sync API** | gọi Messages API **bình thường**, chờ trả lời ngay | ngược với Batch |
| **escalate** | chuyển case cho **người thật** | |
| **first-contact resolution (FCR)** | % case xong **ngay lần liên hệ đầu**, không phải chuyển người / quay lại | |

**Từ tiếng Anh hay gặp trong đề** (bạn ghi lại khi làm mock M1)

| Từ | Nghĩa | Ví dụ trong đề |
|---|---|---|
| **dispute** / **billing dispute** | **tranh chấp, khiếu nại** / khách khiếu nại về **tiền bị tính** (trừ trùng, sai giá) | "complex billing disputes" |
| **curation** / **curate** | **tuyển chọn**, chọn lọc nội dung | "content curation agent" |
| **editorial** (judgment) | (quyết định) kiểu **biên tập viên**: chọn bài nào hợp chủ đề | "make editorial judgments" |
| **exemplify** | **là ví dụ mẫu** cho | "3 modules that exemplify these patterns" |
| **tangential** | **liên quan bên lề**: không phải chủ đề chính nhưng có ích | "valuable tangential sources" |
| **nuance** | **sắc thái**, chi tiết nhỏ nhưng quan trọng (vd "±$7B", "methodology varies") | "losing nuance" |
| **fabricated** | **bịa ra**, giả | "a fabricated order_id" |
| **synthesis agent** | agent **tổng hợp** kết quả các agent khác thành 1 bản | research scenario |
| **high-ambiguity** | **mơ hồ cao**: chưa rõ khách muốn gì | "high-ambiguity requests" |

💡 **Mẹo đọc đề**
1. **Đọc câu CUỐI trước**: "most effective **first step**", "most **maintainable**", "**guarantee**", "**reduce overhead while maintaining reliability**". Chữ đó quyết định đáp án.
2. **Đọc số liệu trong đề**: "12% of cases", "85% simple / 15% complex", "40% latency". Số liệu thường chỉ thẳng vào đáp án. Vd "85% chỉ cần check fact đơn giản, 15% cần điều tra sâu" => cho 1 tool hẹp lo 85% case dễ, 15% case khó vẫn đi qua coordinator (Q9).
3. **Đáp án sai thường là**: (a) **prompt** khi cần **đảm bảo 100%**, (b) **hệ thống mới** (classifier, routing layer, model to hơn) khi chưa thử cách đơn giản, (c) **đẩy việc cho developer** (vd "bắt dev chia PR nhỏ" thay vì sửa hệ thống), (d) **feature không tồn tại**.
4. **Multiple response**: đề ghi chọn mấy => chọn **đủ** số đó.
5. **Kiểm tra cả 2 yêu cầu** nếu đề có 2 ("reduce latency" **và** "maintain reliability").

---

## 1. Những chỗ đã sửa

Thông tin từ các site bên ngoài và từ câu trả lời đầu tiên của Claude **khác** guide chính thức. Theo guide.

| # | Thông tin cũ | Đúng theo guide | Nguồn |
|---|---|---|---|
| 1 | 🔴 Thứ tự domain: D2 = Claude Code, D3 = Prompt, D4 = Tool & MCP (nhiều site + câu trả lời trước của Claude) | **D2 = Tool Design & MCP (18%)**, **D3 = Claude Code (20%)**, **D4 = Prompt (20%)**. Mock test bên ngoài có thể đánh số khác => nhìn **tên** domain, đừng nhìn số | `[G §4]` |
| 2 | 🔴 "Domain 5: học kỹ số liệu prompt caching (TTL, min token)" (Claude nói trước đó) | **Prompt caching chi tiết = OUT OF SCOPE**, chỉ cần biết nó tồn tại. D5 thực tế là escalation, error propagation, provenance, human review | `[G §17]` |
| 3 | 🟡 Thứ tự ưu tiên settings (managed > CLI > local > project > user) | **Không** có trong task statement. Guide hỏi **CLAUDE.md hierarchy**, rules, commands, skills, `.mcp.json`. Ưu tiên thấp | `[G 3.1]` |
| 4 | 🟡 Tên tool tạo subagent | Guide gọi là **Task** tool (`allowedTools` phải có `"Task"`). Claude Code bản mới hiển thị tool này là **Agent**. **Thi theo guide: Task** *(Claude)* | `[G 1.3]` |
| 5 | 🟡 Slash command | Guide tách `.claude/commands/` và `.claude/skills/`. Claude Code bản mới đã gộp command vào skill. **Thi theo guide** *(Claude)* | `[G 3.2]` |

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

**Tất cả giá trị `stop_reason`** *(Claude, theo API docs)*. API gắn field này vào mỗi response, báo **vì sao Claude ngừng viết**. Thi chủ yếu hỏi 2 cái đầu.

| `stop_reason` | Nghĩa | Code làm gì |
|---|---|---|
| **`tool_use`** | Claude **xin** gọi tool. Nó **không tự chạy** tool | chạy tool, gửi `tool_result`, gọi lại |
| **`end_turn`** | Claude trả lời xong | dừng, trả kết quả |
| `max_tokens` | chạm `max_tokens` của bạn => câu trả lời **bị cắt** | tăng limit / cho viết tiếp. Không coi là xong |
| `stop_sequence` | gặp chuỗi dừng bạn đặt trong `stop_sequences` | tùy thiết kế |
| `pause_turn` | server tool chạy lâu (web search phía Anthropic) bị tạm dừng | gửi lại conversation để chạy tiếp |
| `refusal` | bộ lọc an toàn từ chối | không retry y nguyên, xử lý riêng |

`[W]` Site học tiếng Việt (mục 9 #6) bài 1.1 ghi thêm (ngoài phạm vi thi, đọc lướt): `stop_reason` `model_context_window_exceeded` (hết context window). Agent SDK: `max_turns` (mặc định không giới hạn) hết lượt => `ResultMessage` subtype `error_max_turns`; còn có `error_max_budget_usd`, `error_during_execution`. => `max_turns` = **lưới an toàn**, không phải cách dừng chính.

**`tool_use` đi từ đâu ra** *(Claude)*

1. **Danh sách tool do BẠN gửi**, trong param `tools=[...]` của **mỗi** request: `name` + `description` + `input_schema` (JSON schema). Claude chỉ biết những tool có trong list này. Code mẫu: `labs/common/support_tools.py`.
2. Định nghĩa tool nằm trong **prompt** => tốn input token **mỗi lần gọi**. Đo thật: 1 câu ngắn + 6 tool = **1.300 input token**.
3. Claude đọc system + messages + **description** của tool => tự quyết (model-driven): trả lời luôn, hay cần thêm dữ liệu => chọn tool hợp nhất. Description mơ hồ => chọn sai tool (lab 2, `[G 2.1]`).
4. Muốn gọi tool, Claude trả về block `tool_use` và API đặt `stop_reason = "tool_use"`:
   ```json
   {"type": "tool_use", "id": "toolu_016Y...", "name": "get_customer",
    "input": {"email": "alex.tran@example.com"}}
   ```
5. **Code của bạn** chạy hàm thật, gửi lại `{"type": "tool_result", "tool_use_id": "toolu_016Y...", "content": "..."}` trong **1** user message. Có lỗi => thêm `"is_error": true`. `tool_use_id` phải khớp `id`.
6. 1 response có thể có **nhiều** `tool_use` (gọi song song) => gửi **tất cả** `tool_result` trong **1** message.
7. `tool_choice` đổi quyền quyết định: `auto` (Claude tự chọn, mặc định) / `any` (phải gọi 1 tool nào đó) / `{"type":"tool","name":X}` (phải gọi X) / `none` (cấm gọi tool) `[G 2.3]`.

🧪 **Lab 1 (đã chạy 2026-11-13, Haiku 5.5)**

| Mode | Kết quả | Bài học |
|---|---|---|
| `wrong-text` (dừng khi có chữ) | **chạy đúng do may mắn** | Model mới không trả text chung response với `tool_use` (text giữa các tool nằm trong thinking ẩn). Điều kiện dừng sai có thể **pass test rồi hỏng khi đổi model / prompt** |
| `wrong-turns` (dừng sau 2 vòng) | cắt sau 2/4 bước, câu trả lời **rỗng** | `stop_reason` vẫn là `tool_use` mà code đã dừng => mất việc |
| `right` (theo `stop_reason`) | 4 bước, đủ câu trả lời | 2 `lookup_order` **song song** trong 1 response, gửi lại chung 1 message |

Thêm: agent nói "không thấy ngày hôm nay" => thiếu thông tin trong context (D5): đưa dữ kiện agent cần (ngày hiện tại) vào system prompt.

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
- Context phải **đưa thẳng vào prompt** của subagent (vd đưa kết quả web search + phân tích tài liệu cho synthesis agent). Subagent **không** share memory giữa các lần gọi.
- Truyền dữ liệu bằng **format có cấu trúc**, tách **nội dung** khỏi **metadata** (URL, tên tài liệu, số trang) => giữ được nguồn.
- **Chạy song song**: coordinator gọi **nhiều Task tool call trong 1 response** (không phải mỗi turn 1 cái).
- Prompt cho coordinator: nêu **mục tiêu + tiêu chí chất lượng**, **không** viết từng bước thủ tục => subagent linh hoạt hơn.
- **Fork session**: tách nhánh từ 1 bản phân tích chung để thử hướng khác nhau.
- **Tool của subagent** (`tools` trong AgentDefinition): bỏ trống => kế thừa **hết** tool trong session. Subagent dùng tool quá tay => thu hẹp `tools` (least privilege).

🧭 **Đề**: "coordinator **không gọi được** subagent" => thiếu `"Task"` trong `allowedTools`. "Subagent **làm quá tay**" => thu hẹp `AgentDefinition.tools`. Hub-and-spoke: mọi thứ đi qua coordinator.

⚙️ **SDK thật** (docs Agent SDK, kiểm tra 2026-11-15). Đề vẫn dùng mô hình đơn giản ở trên *(Claude)*:

| Lớp | Là gì |
|---|---|
| **Tool pool** | mọi tool có trong session: built-in + MCP server đã kết nối |
| `allowedTools` | list **auto-approve** (chạy không hỏi). Tool không có trong list **vẫn tồn tại**, ❌ không phải "hộp tool của coordinator" |
| `AgentDefinition.tools` | tool của **1 subagent**, lấy từ pool. Bỏ trống = lấy hết |

- Subagent **có thể** có tool mà coordinator không list. Ví dụ trong docs: coordinator `allowed_tools` = Read, Grep, Glob, Agent; subagent `test-runner` có `tools` = **Bash**, Read, Grep.
- Giới hạn: subagent chỉ chọn được tool **có trong session** (MCP server chưa kết nối => không dùng được).
- Thiết kế thường gặp: coordinator **ít tool** (chủ yếu Task để giao việc), worker giữ tool làm việc thật.
- Docs chưa nói rõ: Bash của subagent trong ví dụ trên chạy luôn hay phải xin phép (vì không nằm trong list auto-approve).
- Subagent **có thể** tạo subagent con (lồng nhau), sâu tối đa mặc định **3** (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, đặt `1` để chặn). Tên tool hiện tại là `Agent` (guide gọi `Task`).

### 2.4 Workflow nhiều bước: enforcement + handoff `[G 1.4]`

- **Programmatic enforcement** (hook, prerequisite gate) vs **prompt guidance**. Khi cần đúng tuyệt đối (xác minh danh tính trước giao dịch tiền) => prompt **luôn có tỉ lệ lỗi > 0**.
- Ví dụ chuẩn: **chặn** `lookup_order` / `process_refund` tới khi `get_customer` trả về **verified customer ID** `[G Q1]`.
- **Code vs gate vs hook** *(Claude)*: không phải 3 lựa chọn khác nhau, mà là 3 tầng:

| Từ | Là gì | Tầng |
|---|---|---|
| **Code** (deterministic) | mọi logic chạy **ngoài model** | cả họ |
| **Gate** (programmatic prerequisite) | 1 **luật**: "bước B **bị chặn** tới khi bước A xong" | **cái gì** cần ép |
| **Hook** (PreToolUse / PostToolUse) | tính năng của **framework** (Agent SDK, Claude Code): chạy hàm của bạn tại 1 thời điểm cố định cho mọi tool call khớp | **ở đâu / cách nào** gắn check |

- Cùng 1 gate, 3 chỗ build: (1) **trong tool** (`process_refund` tự check `verified_customer_id`), (2) **trong agent loop** (check trước khi chạy `tool_use`), (3) **PreToolUse hook** trả `permissionDecision: "deny"` + lý do. Cả 3: model nhận lỗi => tự gọi `get_customer` trước, **không lách được**.
- Hook hợp khi: check **tập trung** cho nhiều tool, hoặc tool **không sửa được** (MCP server bên thứ 3). PostToolUse hook **sửa kết quả** (chuẩn hóa ngày) = hook nhưng **không phải** gate.
- 🏦 Ngân hàng: luật "kiểm ID trước khi rút tiền" = **gate**. Phần mềm quầy không mở màn hình rút tới khi quét ID = gate **trong tool**. Bảo vệ ở cửa kiểm mọi người = **hook**. Quản lý dặn "nhớ kiểm ID" = **prompt** (đa số lần đúng, không 100%).
- 🧭 Thi: gate và hook đều **đúng** (cùng họ deterministic), không cần phân biệt. Sai = prompt, few-shot, routing classifier. Chữ báo hiệu: "guarantee", "must always", "X% skip a step", tiền, danh tính.
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

| `tool_choice` | Nghĩa | Dùng khi (theo guide) |
|---|---|---|
| `"auto"` (mặc định) | model **tự quyết**: gọi tool hoặc trả lời bằng chữ | chat / agent bình thường |
| `"any"` | **bắt buộc** gọi tool, model **tự chọn** tool nào | extraction có **nhiều** extract tool (mỗi loại tài liệu 1 schema), **không biết trước** tài liệu loại nào => model phải trả JSON qua 1 trong các tool, không được trả lời bằng chữ `[G 2.3, 4.3]` |
| `{"type":"tool","name":"X"}` (forced) | **bắt buộc** gọi **đúng** tool **X** | biết chắc bước đầu phải là X: ép `extract_metadata` chạy **trước**, các bước enrichment chạy ở **request sau** `[G 2.3, 4.3]` |

🧭 `tool_choice` đặt **cho từng request**, không phải cho cả agent. `any` / forced **chỉ khi request đó bắt buộc phải ra tool call** (vd lấy structured output: lab 5, lab 6). Hội thoại thường => `auto`. *(Claude)*

⚠️ **API thật** (claude-api reference, 2026-11): model mới nhất (Opus 5.5, Sonnet 5.5, Fable 5.1 / 5.2) **trả lỗi 400** với `any` / forced => dùng `auto` + `strict: true` hoặc structured outputs. Haiku 5.5 vẫn chạy (lab 2). **Thi theo guide**: `any` / forced vẫn là đáp án đúng trong scenario *(Claude)*.
- Với `any` / forced, Claude **không viết câu giải thích** trước tool call `[W]`.
- Bộ tool **rất lớn**: API có **tool search** (`defer_loading`). Site học tiếng Việt (mục 9 #6) nói độ chính xác giảm rõ khi > 30-50 tool `[W]`. Đề vẫn: 18 tool => **giảm còn 4-5, chia theo vai trò**.

🧪 **Lab 2 (2026-11-14, Haiku 5.5)**: user nói "Thanks, bye!" (không cần tool):
- `auto` => trả text ✅
- `any` => gọi **`escalate_to_human`** ❌ (bị ép gọi tool nào đó => chọn bừa 1 **hành động**)
- forced `get_customer` => gọi lookup khi không có gì để tra ❌

Thêm từ lab 2: tên tool rõ (`get_customer` vs `search_customers`) + câu hỏi rõ => description mơ hồ vẫn 8/8. Description dài hơn **lái hành vi**: "needs customer_id from get_customer" => thêm 1 bước gọi thừa, "ask, don't guess" => hỏi lại trước khi search (6/8). => Viết description xong phải **test bằng bộ case**, chạy nhiều lần.

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

💡 Ví dụ ngay trong máy bạn: `~/.claude/CLAUDE.md` có dòng `@<tên-file>.md` = **@import** đúng kiểu guide nói. Và vì nó là **user-level**, người khác clone repo sẽ **không** có các rule đó (đúng loại bẫy trong đề).

- **@import**: `@path/to/file.md` trong CLAUDE.md để tách nhỏ, mỗi package import chuẩn liên quan.
- **`/memory`**: xem file memory nào **đang được load** => debug khi hành vi khác nhau giữa các session.

### 4.2 Commands + Skills `[G 3.2]`

3 field này nằm **ngay trong file `SKILL.md`**, ở phần **frontmatter** (khối YAML giữa 2 dòng `---` ở **đầu file**). **Không** phải trong settings.json. Mỗi skill tự khai báo cho riêng nó *(Claude)*:

```markdown
<!-- .claude/skills/codebase-scan/SKILL.md -->
---
name: codebase-scan
description: Scan a folder and summarize its architecture
context: fork
allowed-tools: Read, Grep, Glob
argument-hint: "[folder to scan]"
---
Scan $ARGUMENTS, then return a 10-line summary of the main modules.
```

Kết quả: skill chạy trong **sub-agent riêng** (đọc 100 file cũng không làm đầy hội thoại chính), chỉ được dùng Read / Grep / Glob, và gợi ý "[folder to scan]" khi dev gõ `/codebase-scan` mà không ghi thư mục. Hội thoại chính chỉ nhận lại **bản tóm tắt 10 dòng**.

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
- ⚠️ `paths:` **không phải** để chỉ cho Claude "test nằm ở đâu" *(Claude)*. Nó là **điều kiện load rule**: "khi Claude đọc / sửa file nào khớp pattern này thì mới nạp rule này vào context". Ví dụ trên: Claude sửa `src/cart/Cart.test.tsx` hay `lib/x/y.test.tsx` (thư mục nào cũng được) => rule "dùng React Testing Library" **tự** được nạp. Sửa `Cart.tsx` => không nạp. `**/` = mọi thư mục, mọi độ sâu.
- Vì sao thắng CLAUDE.md thư mục: test nằm trong **50 thư mục** khác nhau => phải chép rule vào 50 file `CLAUDE.md`. 1 file rule + glob là phủ hết.

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
| **Test case cụ thể** (input + output mong muốn) | sửa 1 edge case (vd giá trị `null` trong migration script) |
| **Interview pattern**: để Claude **hỏi lại** trước khi làm | domain **lạ** (cache invalidation, failure mode) |
| Gửi **tất cả lỗi trong 1 message** | các lỗi **liên quan nhau** (sửa cái này ảnh hưởng cái kia) |
| Sửa **lần lượt** | các lỗi **độc lập** |

💡 Bạn đã dùng sẵn: skill **brainstorming** ≈ interview pattern, skill **TDD** ≈ test-driven iteration.

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
- Review code: few-shot **phân biệt pattern chấp nhận được vs lỗi thật** => **bớt false positive** mà model vẫn khái quát được.
- Few-shot cũng dùng cho **chọn tool khi request mơ hồ** và mẫu **format output** (location, issue, severity, suggested fix).

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
- Công cụ guide nhắc: **Pydantic** (schema validation, semantic validation error, validation-retry loop).

### 5.5 Batch processing `[G 4.5]`

| Message Batches API | |
|---|---|
| Giá | rẻ **50%** |
| Thời gian | **tới 24 giờ**, **không có SLA** độ trễ |
| Hạn chế | **không** hỗ trợ **multi-turn tool calling** trong 1 request |
| Ghép kết quả | **`custom_id`** |
| Lấy kết quả | **polling** tới khi batch xong |

- Hợp: overnight report, weekly audit, nightly test generation. Không hợp: **pre-merge check** (chặn dev).
- **"Blocking" / "chặn merge" nghĩa là gì** *(Claude)*: **pre-merge check** = bước kiểm tra tự động (CI review bằng Claude) chạy khi dev mở PR. Repo cấu hình "check phải **pass** thì nút **Merge** mới mở". Nên dev **bị chặn**, phải **ngồi chờ** kết quả. Gửi qua Batch => có thể chờ **tới 24 giờ** => không chấp nhận được. Report overnight thì khác: chạy đêm, sáng mới đọc, chậm vài giờ **không ai bị chặn** => Batch hợp.
- 🧭 Mẹo nhớ: hỏi "**có ai đang ngồi chờ kết quả không?**". Có => **sync API** (Messages API gọi thường). Không => **Batch** (rẻ 50%). ❌ "batch + polling" hay "batch + timeout fallback sang real-time" cho việc chặn: batch **không có SLA**, "thường nhanh" chưa đủ `[G Q11]`.
- **Tính tần suất gửi theo SLA**: SLA 30 giờ, batch tới 24 giờ => gửi theo **cửa sổ 4 giờ** (đợi tối đa 4h + xử lý 24h = 28h < 30h, còn dư) *(Claude giải thích số của guide)*.
- Lỗi: gửi lại **chỉ request lỗi** (theo `custom_id`), có chỉnh (vd **chia nhỏ** tài liệu vượt context).
- **Thử prompt trên sample nhỏ trước** khi chạy batch lớn => giảm chi phí gửi lại.

### 5.6 Multi-instance, multi-pass review `[G 4.6]`

- **Self-review yếu**: model còn giữ reasoning lúc sinh code => ít nghi ngờ quyết định của mình.
- **Instance độc lập** (không có context cũ) bắt lỗi tốt hơn self-review hoặc extended thinking.
- **Multi-pass**: per-file (lỗi local) + integration pass (data flow giữa file) => tránh **attention dilution** và feedback **mâu thuẫn**.
- **Attention dilution** (chú ý bị pha loãng) *(Claude)*: đưa **quá nhiều thứ cùng lúc** (14 file 1 pass) => sự chú ý của model **chia mỏng** => file này kỹ, file kia sơ sài, sót bug rõ, cùng 1 pattern chỗ khen chỗ chê. Context lớn hơn = **chứa được** nhiều hơn, **không** = chú ý kỹ hơn => model to / context dài **không sửa** `[G Q12]`. Khác **lost in the middle** (6.1): cái đó do **vị trí** (phần giữa input dài), cái này do **khối lượng**.
- Verification pass: model ghi **confidence cho từng finding** => routing review (con số phải được **calibrate**, xem 6.5).

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

**Case facts block: ví dụ cụ thể** *(Claude)*

- **Vấn đề**: chat support dài 40 lượt, context sắp đầy => app cho model **tóm tắt** các lượt cũ. Mỗi lần đầy lại tóm tắt tiếp, **gồm cả bản tóm tắt cũ** (= "progressive", giống photocopy của bản photocopy: mỗi lần mờ thêm). Model viết lại bằng lời của nó => số bị làm tròn hoặc mất:
  - Thật: đơn **#A123, $89.99, giao 03/11**. Đơn **#B456 giao trễ 5 ngày**. Khách muốn refund **về thẻ**, **không** lấy store credit.
  - Sau vài lần tóm tắt: "Khách không hài lòng về **vài đơn hàng** gần đây, muốn được **hoàn tiền**."
  - Hậu quả: agent refund sai số tiền, sai đơn, hoặc trả store credit => khách bực hơn.
- **Cách sửa**: ngay khi dữ kiện xuất hiện, **trích** nó ra (bằng code, hoặc 1 bước extraction của model) vào 1 khối riêng. Khối này **chép nguyên văn**, chỉ cập nhật khi có dữ kiện mới, **không bao giờ** đem đi tóm tắt, và **gửi kèm mọi request**. Chỉ phần nói chuyện mới bị tóm tắt:

```text
<case_facts>                      <- giữ nguyên văn, gửi mọi request
customer_id: C-1042 (verified)
order #A123: $89.99, delivered 2026-11-03, refund requested
order #B456: $45.00, delivered 5 days late
customer wants: refund to original card, NOT store credit
</case_facts>

<conversation_summary>            <- phần này được phép tóm tắt
Customer is frustrated about two delayed orders...
</conversation_summary>

[vài lượt chat gần nhất, giữ nguyên]
```

- **Agent đoán cái gì là case fact?** Không *(Claude)*. **Bạn (người thiết kế)** quyết định trước **loại** dữ kiện nào quan trọng cho domain, dạng schema cố định (support: customer ID, mã đơn, số tiền, ngày, status, mong muốn khách nói ra; guide gọi là "transactional facts"). Giá trị được điền từ 2 nguồn:
  1. **Tool result** (chắc nhất): `get_customer` trả `customer_id`, `lookup_order` trả số tiền / ngày / status => **code** chép thẳng field vào block, không có model, không đoán.
  2. **Lời khách nói** ("refund về thẻ nhé"): model điền vào **schema cố định** (tool_use + JSON schema, field nullable, khách không nói => `null`). Model chỉ điền ô có sẵn, không tự chọn "cái gì quan trọng" => hẹp hơn nhiều so với "tóm tắt mọi thứ".
  - Giống tờ khai ở bệnh viện có sẵn ô "Dị ứng: ___": **tờ khai** quyết định cái gì phải ghi, y tá chỉ điền.
  - Thi chỉ cần nhận ra pattern, không hỏi cách build.
- 🏥 Giống hồ sơ bệnh án: "**Dị ứng: penicillin**" ghi riêng ở đầu hồ sơ, không chôn trong phần ghi chú tóm tắt các lần khám. Bác sĩ nào mở hồ sơ cũng thấy ngay.
- 🧭 Đề: "summary làm mất số tiền / ngày / kỳ vọng của khách" => **case facts block**. ❌ "tóm tắt kỹ hơn", ❌ "dùng model context dài hơn".

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

- ❌ **Sentiment** và **self-reported confidence** = proxy **không đáng tin** cho độ phức tạp (để quyết định escalate). Khác 6.5: confidence đã **calibrate** để route review = ✅.
- Escalate vì **policy exception / gap**, không phải chỉ vì case "phức tạp".

### 6.3 Error propagation trong multi-agent `[G 5.3]`

- Structured error context: **failure type**, **query đã thử**, **partial result**, **hướng thay thế** => coordinator quyết định thông minh (retry query khác, đổi cách, hoặc đi tiếp với partial).
- 2 anti-pattern: ❌ **nuốt lỗi** (trả rỗng như thành công) · ❌ **dừng toàn bộ** workflow vì 1 lỗi.
- ❌ Status chung chung ("search unavailable") **giấu** thông tin coordinator cần. Phải tách **access failure** (timeout, cần quyết định retry) với **valid empty result** (tìm được, không có kết quả).
- Subagent **tự retry lỗi transient** tại chỗ, chỉ đẩy lên lỗi **không tự xử lý được** + đã thử gì + partial result.
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
- Sau khi bớt human review: **lấy mẫu stratified đều đặn** (vd hằng tuần `[W]`) các kết quả confidence cao để bắt lỗi kiểu mới.
- ❌ Đáp án nhiễu hay gặp `[W]`: chỉnh threshold theo **điểm tổng**, hoặc chạy thử rồi **chờ lỗi xuất hiện**. ✅ phân tích **theo loại tài liệu + field**.
- Ví dụ minh họa `[W]` (số giả định): 97% tổng = mẫu chuẩn 80% tài liệu (đúng 99%) + chủ nhà tự soạn 15% (93%) + **viết tay 5% (78%)** => con số tổng đẹp che loại viết tay kém.

🧭 Confidence: **tự báo thô** (1-10) để quyết định escalate ❌ `[G Q3]`. Confidence **từng field / finding** + **calibrate bằng labeled set** để route review ✅ `[G 4.6, 5.5]`. Calibrate = chạy trên bộ tài liệu đã có đáp án đúng, đo mỗi mức điểm đúng thật bao nhiêu %, rồi đặt ngưỡng **riêng cho từng field** *(Claude)*.


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

Cách làm: **làm mock => đưa câu sai cho Claude => Claude giải thích + kiểm tra với guide => ghi vào mục 10 => cập nhật bảng 🔁 điểm yếu => cuối cùng đọc cheatsheet**.

**Vòng lặp mỗi lần làm mock**
1. Làm **timed** (bấm giờ thật: 2 phút / câu). Không tra tài liệu.
2. Chép **câu sai + câu đoán mò** (đề + 4 đáp án + đáp án mock + đáp án bạn chọn) gửi Claude.
3. Claude: giải thích ✅ / ❌ từng đáp án, ghi nguồn `[G x.y]`, đánh dấu ⚠️ nếu **đáp án mock sai** so với guide.
4. Ghi vào mục 10. Chủ đề sai **lần 2** => thêm vào bảng 🔁 + cheatsheet.

**Lịch đề xuất** (hôm nay 2026-10-31, ~8-10 giờ / tuần) *(Claude)*

| Tuần | Ngày | Việc |
|---|---|---|
| 0 | 1-2/11 | Đọc mục 0 + 1 (30 phút). Làm **diagnostic** (bộ sampler free 20 câu, mục 9 #2). **Chưa học gì**. Ghi điểm từng domain |
| 1 | 3-9/11 | **D1** (mục 2) + bắt đầu **Ex 1** |
| 2 | 10-16/11 | **D2 + D3** (mục 3, 4). Ex 2 (nhanh, bạn đã quen) |
| 3 | 17-23/11 | **D4** (mục 5) + **Ex 3** |
| 4 | 24-30/11 | **D5** (mục 6) + Ex 4 (hoặc bỏ nếu thiếu giờ). **Mock full #1** |
| 5 | 1-7/12 | Mock full #2, #3. Ôn bảng 🔁. Mock **>= 80%** ổn định => **đặt lịch thi** |
| 6 | ~8-12/12 | **Thi lần 1**. Đọc cheatsheet sáng hôm thi |

**Ngày thi**
- Đọc `CCAR-F-CHEATSHEET.md` (10-15 phút).
- Thi online: dọn bàn, 1 màn hình, không điện thoại / đồng hồ thông minh `[G §13]`.
- 2 phút / câu. Câu dài (scenario) chậm hơn => đánh dấu, làm câu khác, quay lại.

---

## 9. Nguồn mock test

| # | Nguồn | Giá | Ghi chú |
|---|---|---|---|
| 1 | **Practice test chính thức trên Anthropic Partner Academy** | ? | Guide ghi 12 câu mẫu "drawn from the practice test" => có thể có bộ practice chính thức. **Kiểm tra trong Partner Academy trước** (Claude chưa xác minh được) |
| 2 | Bộ sampler free | free | 20 câu, timed + review mode. **Dùng làm diagnostic** |
| 3 | Site free (diagnostic + mock + bài học) | free | diagnostic 10 câu + mock + bài học. Không liên quan Anthropic |
| 4 | Bộ practice exam trả phí (cùng nhà với #2) | trả phí | 100+ câu scenario |
| 5 | Khóa luyện đề trên nền tảng khóa học online | trả phí, hay giảm giá | Rất nhiều bộ, chất lượng **không đều**. Chọn bộ **mới cập nhật theo guide v1.0**, rating cao, đọc review |
| 6 | Site học tiếng Việt (bài học + khóa luyện đề) | bài học: xem được không cần đăng nhập. Khóa luyện đề: **280.000đ**, có thử **10 câu** (giá 2026-11-03, trang index giờ không hiện giá) | Kiểm tra 2026-11-03 + **2026-11-15** (banner: đợt đổi đề 07/12 "**trừ CCAR-F**", khớp ⚠️ đầu file; bài học ghi đối chiếu docs 02/11/2026; chi tiết thêm của bài 1.1, 2.3, 5.5 đã ghi vào mục 2.1, 3.3, 6.5 với ký hiệu `[W]`). **30 bài = đúng 30 task statement**, **đúng thứ tự domain** của guide (D2 = Tool & MCP). Bài 1.1 khớp guide (stop_reason, 3 anti-pattern), có thêm chi tiết API **ngoài phạm vi thi** (các `stop_reason` khác, lỗi 400) => đọc lướt. ⚠️ **Không phải của Anthropic** dù tên trang có chữ "Anthropic". Không ghi tác giả. Quảng cáo "**bám sát đề thi thật**": nếu thấy câu hỏi giống **y nguyên** đề thật => dừng (NDA) |
| 7 | Bộ mock free online (mock 1) | free (cần đăng nhập) | Làm 2026-11-18: 39/60. Câu hỏi bám guide khá sát (nhiều đáp án = ví dụ nguyên văn của guide). ⚠️ **Lời giải thích hay bịa** (chương sách không có, tên MCP sai, flag không tồn tại) => chỉ dùng **đáp án**, tự kiểm với guide. 1 đáp án sai logic (Q46). Xem log mục 10 |

⚠️ **Tránh "dump"**: site ghi "**real exam questions**" = vi phạm **NDA** (`[G §14]`) => có thể bị **hủy kết quả + cấm thi** (`[G §13]`). **Đừng dùng** site kiểu đó.
⚠️ Mock bên ngoài **có thể sai đáp án**. Thấy mâu thuẫn với guide => **tin guide**, ghi ⚠️ vào mục 10.
⚠️ Mock bên ngoài có thể đánh **số domain khác** guide (xem mục 1 #1).

---

## 10. Quiz đã gặp + giải thích

### 🔁 Điểm yếu: câu sai nhiều lần (ôn cái này TRƯỚC khi thi)

| # | Chủ đề | Sai ở câu | Quy tắc 1 dòng | Ôn lại |
|---|---|---|---|---|
| 1 | **Hỏi / điều tra trước** khi làm theo yêu cầu của khách | M1 Q8, Q29 | Khách **đòi người rõ ràng** ("real person NOW") => escalate **ngay**, kèm history. Khách bực nhưng việc agent **làm được** => ghi nhận + đề nghị giải quyết **hoặc** escalate. Cả 2: ❌ hỏi thêm / điều tra trước | 6.2 |
| 2 | **Tóm tắt văn xuôi** làm mất dữ liệu | M1 Q18, Q56, Q37 | Dữ liệu phải giữ (ID, số tiền, status) => **structured**: chỉ giữ field cần, lớp context riêng, session mới + structured summary. ❌ prose summary, ❌ resume với tool result cũ | 6.1, 2.7 |
| 3 | **Thiết kế error** trả cho model | M1 Q14, Q49, Q51 | Lỗi phải có: **loại**, **retry được không**, **gợi ý bước tiếp**. ❌ retry ẩn trong tool, ❌ msg ngắn + tool riêng. Request hỏng (thiếu param) => **JSON-RPC protocol error**. Tool chạy mà lỗi => **isError** | 3.2, 6.3 |
| 4 | **Cấu hình Claude Code** (rules / @import / /memory) | M1 Q20, Q25, Q50 | File có **pattern tên** (`**/*.test.tsx`, `terraform/**`) => rules + `paths:`. **Không** có pattern, maintainer tự biết => **@import** trong CLAUDE.md từng package. Lúc theo lúc không => **/memory** trước | 4.1, 4.3 |
| 5 | **Gộp / tách tool** | M1 Q3, Q31, Q44 | 1 tool làm **nhiều việc** (output lộn xộn) => **tách**. 2 tool **trùng nghĩa** model không phân biệt => **gộp** (hoặc rename + description). Model cần **thấy hết** để tự chọn => tool gộp trả **dữ liệu**, hành động giữ riêng | 3.1 |
| 6 | Chọn **hook** khi có cách code **đầy đủ hơn** | M1 Q2, Q52 | Đề có nhiều đáp án deterministic => chọn cái **phủ mọi trường hợp**: kiểm tra **sau khi loop dừng** (Q2), **tool tự** tạo yêu cầu duyệt (Q52). ❌ ngưỡng tùy ý (80% max_turns), ❌ hook + flag truyền qua | 2.4 |
| 7 | Bị hút vào **prompt caching** | M1 Q6 (nghi), Q54 | Caching = **chi phí / tốc độ**, không sửa **gốc** (gọi subagent thừa, context quá dài làm kém chất lượng). Chi tiết caching **ngoài phạm vi thi** => thường là bẫy | 0, 6.1 |

### ⚠️ Đáp án mock đã kiểm tra là SAI

| Nguồn + câu | Mock ghi | Đúng theo guide |
|---|---|---|
| M1 Q46 (send_notification timeout, không biết đã gửi chưa => bị gửi trùng) | A: `retry_safe: true` cho timeout | ⚠️ **Sai logic**: báo "retry an toàn" => gửi trùng **thêm**. Nên là B: báo rõ "status unknown, có thể đã gửi, **đừng retry**" (instructive error) |
| M1 Q32 (update_user_profile thiếu `user_id`) | A: strict JSON schema | ⚠️ **Tranh cãi**: docs Anthropic nói description chi tiết là yếu tố **quan trọng nhất** (D). Mẹo: "bảo đảm / loại bỏ lỗi cấu trúc" => schema; "giúp model **hiểu** nên điền gì" => description |
| M1 Q16 (gap phát hiện sau analysis) | C: coordinator tự dò gap rồi search lại | ⚠️ **Sát nút**: B (analysis báo gap cho coordinator, search + analysis lại tới khi đủ) cũng khớp `[G 1.2]`. Điểm chung cần nhớ: vòng lặp đi **qua coordinator** |
| M1 Q8 (khách "want someone who can actually help") | B: đề nghị làm ngay **hoặc** escalate | ⚠️ **Xám** với `[G 5.2]` "đòi người rõ ràng => escalate ngay". Phân biệt: Q8 = bực + việc làm được; Q29 = "real person NOW" => escalate ngay |
| M1 (giải thích nói chung) | nhiều lời giải thích của site | ⚠️ Giải thích hay **bịa**: "Chapter 7 ... 2026 Edition", MCP = "Model-Control-Plane" / "Managed Claude Platform" (thật: **Model Context Protocol**), flag `--plan`/`--run`, `/add_memory`, hook nằm trong CLAUDE.md (thật: settings.json), "Claude không load CLAUDE.md thư mục con" (sai), "LLM bypass được hook" (sai). **Chỉ tin đáp án, đừng học theo giải thích** |

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

*(Mẫu ghi)*

```markdown
**[M2 Q5] <đề rút gọn>** 🔁 (nếu sai lần 2)
A / B / C / D
- ✅ **B**: vì ... `[G 2.1]`
- ❌ A: ...
- 🔑 Keyword: "..." => ...
```

#### [M1] Mock 1 - 60 câu (2026-11-18): **39/60 = 65%**

Site đặt đậu 72% (thi thật: 720/1000 thang điểm scaled). Câu sai: 2, 3, 7, 8, 14, 18, 20, 21, 25, 28, 29, 31, 33, 37, 44, 49, 50, 51, 52, 54, 56. Claude đã đọc **cả 60 câu** (cả câu đúng, vì có thể đúng nhờ may) và đối chiếu guide. Tóm tắt bằng lời của Claude, không chép nguyên đề.

**Câu sai (21)**

| Câu | Tình huống (rút gọn) | Bạn chọn | ✅ Đúng | Vì sao | Guide |
|---|---|---|---|---|---|
| Q2 | hết `max_turns` giữa chừng, phải **bảo đảm** mọi ca kết thúc = xong hoặc chuyển người | hook dừng ở 80% max_turns | **code kiểm tra kết quả SAU khi loop dừng**, chưa xong => code gọi `escalate_to_human` kèm context | 80% là ngưỡng tùy ý, không phủ các lý do dừng khác | 1.4 |
| Q3 | agent gom bài viết, 18+ tool call tuần tự, cần **thấy hết** ứng viên để chọn | preview + approve theo rule cố định | **tool gộp `discover_and_analyze`** trả hết ứng viên + điểm, `add_to_collection` để riêng | rule cố định lấy mất quyền chọn của model | 3.1 |
| Q7 | coordinator ra lệnh từng bước => subagent bỏ cuộc, kém với chủ đề mới | **classifier** "well-defined / exploratory" | **mục tiêu + tiêu chí chất lượng**, subagent tự chọn cách search | bẫy classifier; gốc là over-specification | 1.3 |
| Q8 | khách bực "muốn người giúp được", việc trả hàng **làm được ngay** | hỏi chuyện gì chưa ổn trước | **ghi nhận bực + nói làm được ngay + đề nghị làm hoặc escalate** | không điều tra trước khi đáp ứng | 5.2 |
| Q14 | `control_device` timeout, agent chỉ nói "không phản hồi" | msg ngắn "Device offline" + tool riêng lấy gợi ý | **isError + nguyên nhân có thể + bước khắc phục** để agent nói với user | thêm tool = thêm vòng gọi, msg vẫn thiếu thông tin | 2.2 |
| Q18 | `lookup_order` trả 40+ field, chiếm context, sắp tra thêm 2 đơn | model viết **tóm tắt văn xuôi** | **chỉ giữ field liên quan** (items, ngày mua, hạn trả, status) | văn xuôi làm mất giá trị chính xác | 5.1 |
| Q20 | monorepo 15 package, 3 standard, **không** có pattern tên, maintainer tự cấu hình | `.claude/rules/` + paths liệt kê từng thư mục | **`@import` đúng standard** trong CLAUDE.md từng package | không có pattern để glob; đề nói maintainer tự biết | 3.1 |
| Q21 | MCP server có **MCP prompts** (template) ngoài tools | vào tool registry, model tự gọi | **slash command** user tự chạy | MCP: tool = model gọi, resource = dữ liệu đọc, **prompt = template user chạy** | (MCP thật) |
| Q25 | repo IaC `/terraform` `/kubernetes`, CLAUDE.md 500 dòng, chỉ load rule hợp **loại file** | CLAUDE.md thư mục con | **`.claude/rules/` + `paths: ["terraform/**/*"]`** | = ví dụ nguyên văn của guide. (CLAUDE.md thư mục con vẫn chạy ngoài đời) | 3.3 |
| Q28 | sau `lookup_order` (mua 45 ngày), loop quyết refund hay escalate thế nào | decision tree cấu hình sẵn | **kết quả tool vào hội thoại, model tự suy luận** | model-driven, không phải cây quyết định | 1.1 |
| Q29 | "I want to talk to a real person **NOW**", chưa gọi tool nào | ghi nhận + hỏi 1 câu trước | **escalate ngay** kèm history | đòi người rõ ràng => không hỏi, không điều tra | 5.2 |
| Q31 | 4 => 10 tool, sai vì **tool trùng nghĩa** (credit vs refund) | tách 2 subagent tài chính / giao hàng | **gộp tool trùng** (`resolve_compensation` + action, `lookup_order` + include_tracking) | tách subagent vẫn để 2 tool trùng chung 1 agent | 3.1 |
| Q33 | lợi ích chính của JSON có field so với text | "model xử lý JSON **deterministic**" | **agent lấy giá trị chắc chắn, không phải parse text** | model không bao giờ deterministic (bẫy chữ) | 5.3 |
| Q37 | khách quay lại sau 4h, session cũ có tool result "PENDING" đã cũ | resume, bỏ tool_result cũ | **session mới + structured summary + gọi tool mới trước** | câu trả lời cũ của assistant vẫn nhắc data cũ | 2.7 |
| Q44 | 1 tool `analyze_document` + lệnh tự do => format output lung tung, 35% phải hỏi lại | description + ví dụ | **tách 3 tool có contract** (extract / summarize / verify) | = ví dụ nguyên văn guide; 1 tool nhiều việc => tách | 3.1 |
| Q49 | `track_shipment` ném Python exception => agent nói "có trục trặc" | retry backoff trong tool | **structured error**: loại, recoverable, gợi ý (kiểm tra mã, tìm bằng số đơn) | retry chỉ cứu lỗi tạm; ID sai / không có đơn vẫn không có hướng dẫn | 3.2 |
| Q50 | CLAUDE.md có convention nhưng lúc theo lúc không, **bước chẩn đoán đầu** | tìm rule xung đột ở `~/.claude` | **`/memory`** xem file nào đang load | `/memory` thấy luôn file user-level => bao luôn ý kia | 4.1 |
| Q51 | MCP: (1) thiếu param bắt buộc, (2) API 404, (3) API 503 | cả 3 là `isError` | **(1) JSON-RPC protocol error**, (2)+(3) tool result `isError` | request hỏng chưa tới logic tool; tool chạy mà lỗi thì model cần biết | (MCP thật) |
| Q52 | hoàn tiền > $500 cần quản lý duyệt, **không lách được** | PreToolUse hook thêm flag `requires_approval` | **tool tự enforce**: < $500 trả, > $500 tạo yêu cầu duyệt + trả "pending" | luật nằm ngay chỗ chi tiền, không phụ thuộc hook + flag | 2.4 |
| Q54 | 35 lượt, 50K token, chậm + kém; 94% chỉ cần 3-5 lượt gần, 6% dễ nhắc lại | **prompt caching** + giữ hết | **sliding window 8-10 lượt**, cũ thì nhờ user nhắc lại | số liệu đề chỉ thẳng đáp án; caching không giảm context | 6.1 |
| Q56 | 3 vấn đề trong 1 session, gần hết context, hỏi lại vấn đề đầu | **tóm tắt văn xuôi** lượt cũ | **trích issue data có cấu trúc** (ID, số tiền, status) vào lớp context riêng | = guide nguyên văn; văn xuôi mất số | 6.1 |

**Câu đúng nhưng bạn còn phân vân**

| Câu | Bạn nghi | Vì sao đáp án đúng thắng |
|---|---|---|
| Q5 (refund timeout giữa chừng) | C: retry backoff, giữ hội thoại tới khi xong | khách chờ vô hạn. ✅ A: giải thích + xác nhận đủ điều kiện + báo lỗi hệ thống + đề nghị escalate / thử lại sau |
| Q6 (tóm tắt follow-up mất 40s) | A: prompt caching cho subagent | vẫn spawn + đẩy 80K token mỗi lần. ✅ B: coordinator tự tóm tắt bằng context đang có `[G 1.2]` |
| Q13 (confidence của ML extraction) | A: điểm thô + few-shot dạy model đọc | vẫn để model đoán = đang hỏng. ✅ B: `request_review` boolean tính bằng **ngưỡng đã test** trong code + lý do (calibrate, 6.5) |
| Q22 (format code lúc đúng lúc sai) | D: Stop hook + prompt kiểm tra | model chấm = xác suất. ✅ A: **PostToolUse** hook, matcher `Edit|Write`, chạy Prettier |
| Q40 (mọi lỗi đều "Operation failed") | B: few-shot dạy đọc pattern lỗi | mọi lỗi **cùng 1 chữ** => không có pattern để học. ✅ C: thêm `errorCategory`, `isRetryable`, mô tả ở nguồn |
| Q24, Q45, Q55 | (phân vân) | Q24: lỗi riêng từng loại + gợi ý bước tiếp. Q45: mỗi agent export **manifest**, coordinator load khi resume (6.4). Q55: subagent trả **claim-source mapping**, synthesis giữ khi gộp (6.6) |

**Bài học thêm từ câu đúng**
- Q1 vs Q52: tool trả lỗi "please escalate" (Q1-A) vẫn để model tự escalate => ❌. Tool **tự tạo yêu cầu duyệt** (Q52-A) => ✅. Gate trong tool chỉ thắng khi nó làm **trọn** hành động an toàn.
- Q23: đề hỏi "**root cause**" agent bịa `order_id` => sửa **description** (order_id phải lấy từ `lookup_order`). Nếu đề hỏi "**guarantee**" => gate.
- Q27 vs Q31: tool chung có **bộ tham số khác nhau** => **tách**. 2 tool **cùng một việc** => **gộp**.
- Q59: 2 tool description 1 dòng (archive vs delete) => **mở rộng description** (giống câu mẫu Q2).
- Q60: tool B cần dữ liệu mà tool A trả => cho tool B **nhận ID và tự tra** bên trong, bỏ chuỗi phụ thuộc.

**Nhận xét chung**: sai nhiều nhất ở **D1 agent / multi-agent**, **D2 thiết kế tool + error**, **D3 cấu hình Claude Code**, **D5 context**. Kiểu sai lặp lại: chọn đáp án "**hỏi thêm / điều tra trước**", "**tóm tắt văn xuôi**", "**hook**" khi có thiết kế đầy đủ hơn, "**prompt caching**". Xem bảng 🔁.
