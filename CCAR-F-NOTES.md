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
| **sliding window** | chỉ gửi **N lượt chat mới nhất**, bỏ lượt cũ; do **code app** làm, không phải setting (xem 6.1) | chat 35 lượt nhưng mỗi request chỉ gửi 10 lượt cuối |
| **scratchpad file** | file **nháp** agent ghi findings để đọc lại sau | |
| **manifest** | file ghi **trạng thái** công việc, dùng để chạy tiếp sau crash | |
| **SLA** | **cam kết thời gian** trả kết quả | "có kết quả trong 30 giờ" |
| **sync API** | gọi Messages API **bình thường**, chờ trả lời ngay | ngược với Batch |
| **escalate** | chuyển case cho **người thật** | |
| **first-contact resolution (FCR)** | % case xong **ngay lần liên hệ đầu**, không phải chuyển người / quay lại | |

**Từ tiếng Anh hay gặp trong đề** (bạn ghi lại khi làm mock M1; thêm từ glossary của nguồn #8 mục 9, 2026-11-24)

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
| **superseded** | **bị thay thế** bởi bản mới hơn (không còn hiệu lực) | "policy v2 superseded v1" |
| **corroborate** | **xác nhận thêm** bằng nguồn thứ 2 | "claims corroborated by 2 sources" |
| **cadence** | **nhịp, tần suất** làm việc gì đó | "batch submission cadence" (M6 Q32) |
| **reconcile** | **đối chiếu** cho khớp (2 số liệu, 2 hệ thống) | "reconcile_delivery" (M6 Q19) |
| **propagate** | **lan truyền** (lỗi / thay đổi đi sang chỗ khác) | "errors propagate to the coordinator" |
| **brittle** | **dễ vỡ**: đổi nhỏ là hỏng | "brittle keyword routing" |
| **prescriptive** | **áp đặt cứng**, chỉ cách làm từng bước | "overly prescriptive prompt" |
| **consolidate** | **gộp** nhiều cái thành 1 | "consolidate overlapping tools" (M6 Q19) |
| **accumulated** | **tích lũy, dồn lại** qua thời gian | "30 minutes of accumulated context" (M6 Q46) |
| **unilaterally** | **tự ý**, không hỏi ai | "agent unilaterally issued a refund" |
| **worst-case** / **safety margin** | **trường hợp xấu nhất** / **khoảng dư an toàn** | 4h chờ + 24h batch = 28h, dư 2h so với SLA 30h |

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

**Ví dụ cụ thể: lỗi 500 lúc có lúc không => dynamic** *(Claude, M2 Q12 · M5 Q6 · M9 Q15)*
- Tình huống: `/api/orders` **thỉnh thoảng** trả 500, 200+ file, không ai biết phần nào hỏng.
- ✅ **Dynamic** = mỗi file vừa đọc chỉ ra file đọc tiếp:

| Bước | Agent đọc | Thấy gì | => bước tiếp |
|---|---|---|---|
| 1 | `routes/orders.js` | route gọi `OrderService.create()` | đọc `OrderService` |
| 2 | `OrderService.js` | **chỉ khi trả bằng thẻ** mới gọi `PaymentClient` | đọc `PaymentClient` |
| 3 | `PaymentClient.js` | **không xử lý timeout**: payment chậm => throw => **500** | tìm ra ✅ |

- 3 file là xong. Lỗi "lúc có lúc không" vì chỉ xảy ra khi payment chậm. Lúc đầu **không thể** lên kế hoạch "đọc `PaymentClient.js`" vì chưa biết nó tồn tại (tới bước 2 mới biết).
- ❌ Kế hoạch đầy đủ trước: "đọc hết routing (40 file), middleware (30), business logic (100), DB (30)" => 200 file, đầy context trước khi tới `PaymentClient`. ❌ Pipeline cố định từng tầng: cùng vấn đề. ❌ 4 worker song song, mỗi tầng 1 con: tốn x4, 3 con tìm nhầm chỗ.
- 🔑 Chữ trong đề: "**intermittent**", "**doesn't know which components**", "**investigate why**".
- 🧭 Hỏi "**biết Ở ĐÂU chưa?**": biết đúng chỗ (stack trace) => **direct**. Biết phạm vi, việc to (migration 45 file) => **plan mode**. **Không biết** => **dynamic**.
- Câu nhớ: "**Mỗi file đọc xong chỉ ra file đọc tiếp.**"

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
- Flag CI khác *(Claude, đã kiểm docs Claude Code 2026-11-21; mock M3 có hỏi)*:
  - `--max-turns N` + `--max-budget-usd X` (chỉ ở `-p`) => **Claude Code tự dừng** khi đủ số lượt / đủ tiền ước tính. ≠ `timeout-minutes` của job CI (runner chặn, không giới hạn tiền) (M3 Q8).
  - `--bare` => bỏ auto-discovery (hooks, skills, plugins, MCP, CLAUDE.md) => khởi động **nhanh**. Vẫn cần chuẩn team => thêm `--append-system-prompt-file ./CLAUDE.md` (M3 Q14).
  - `--system-prompt` / `--system-prompt-file` = **thay** prompt mặc định của Claude Code (mất phần hướng dẫn dùng tool đọc file). `--append-system-prompt` / `--append-system-prompt-file` = **thêm** vào cuối, giữ mặc định (M2 Q47, M3 Q14).
- **REVIEW.md** (gốc repo) = rule **chỉ cho** Code Review managed (chạy qua Claude GitHub App, không cần workflow file): path bỏ qua, check bắt buộc, yêu cầu bằng chứng. Đọc từ **base branch**, không từ PR. `/code-review` chạy local **không** đọc REVIEW.md, chỉ theo CLAUDE.md => rule cần cho cả 2 nơi để ở CLAUDE.md (M3 Q1) *(Claude, đã kiểm docs 2026-11-21)*.

---

## 5. Domain 4 - Prompt Engineering & Structured Output (20%)

### 5.1 Tiêu chí rõ ràng => giảm false positive `[G 4.1]`

- ✅ "flag comment **chỉ khi** hành vi được mô tả **mâu thuẫn** với code thật". ❌ "check comments are accurate".
- ❌ "be conservative", "only report high-confidence findings" => **không** tăng precision.
- 🧭 **2 bệnh khác nhau, 2 cách sửa** *(Claude, guide 4.1 + 4.6)*:
  - Báo **sai nhiều** (false positive = bệnh **precision**) => **tiêu chí cụ thể**: báo gì / bỏ gì + ví dụ. ❌ "be conservative", ❌ "only high-confidence".
  - **Sót** bug thật vì prompt dặn "chỉ báo cái chắc chắn" (bệnh **recall**) => **tách 2 bước**: bước tìm **báo hết**, mỗi finding kèm **confidence + severity**; bước sau mới **lọc theo ngưỡng** (M3 Q7; guide 4.6: "self-reports confidence alongside each finding to enable calibrated review routing").
  - Ví dụ: review báo 40 lỗi mà 25 là style vặt => tiêu chí. Review bỏ sót SQL injection vì "không chắc lắm" => báo hết + confidence, lọc sau.
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
| Hội thoại dài => chậm + kém, lượt cũ **hiếm khi cần** + khách dễ nói lại | **sliding window**: chỉ gửi **N lượt mới nhất** (xem **Sliding window** bên dưới). Lượt cũ có số quan trọng => case facts block, không bỏ |

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

**Sliding window: cách hoạt động** *(Claude)*

- **Không phải setting** của API hay của agent. Là pattern do **code app của bạn** làm. (Vài framework bên thứ 3 gói sẵn thành option "giữ k message cuối", bên trong vẫn là đoạn code như dưới.)
- Vì API **stateless** (dòng trên): mỗi request app tự gửi cả list `messages` => app tự quyết gửi gì.
  - Bình thường: gửi **hết** các lượt => list dài ra mỗi lượt (35 lượt = 50K token).
  - Sliding window: app vẫn **lưu đủ** lịch sử ở chỗ của nó (DB, memory), nhưng trước mỗi request chỉ **chọn N lượt mới nhất** để gửi.
- Hình dung (window = 3), cửa sổ "trượt" lên 1 lượt mỗi lần:

```text
Lịch sử đầy đủ (trong DB):  T1 T2 T3 T4 T5 T6  + câu hỏi mới
Gửi cho Claude:                      T4 T5 T6  + câu hỏi mới
Request sau:                            T5 T6 T7  + câu hỏi mới
```

- Phác thảo code (đơn giản hóa):

```python
WINDOW = 10   # keep the last 10 turns

def build_request(system_prompt, case_facts, turns, new_question):
    messages = []
    for user_msg, reply in turns[-WINDOW:]:      # only the last N turns
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": reply})
    messages.append({"role": "user", "content": new_question})
    return {
        "system": system_prompt + "\n" + case_facts,   # always sent, never cut
        "messages": messages,
    }
```

- 2 luật khi build:
  - Chỉ cắt ở **ranh giới lượt**: không tách message của khách khỏi câu trả lời, không tách tool call khỏi tool result (API từ chối `tool_result` mà thiếu `tool_use` đi kèm).
  - Thứ **không được mất** (system prompt, case facts) nằm **ngoài** window => lần nào cũng gửi.
- Dễ nhầm với tính năng có sẵn (không cái nào là "giữ N lượt cuối"):

| Cách | Nằm ở đâu | Context cũ bị làm gì |
|---|---|---|
| **Sliding window** | code của bạn | **bỏ hẳn** lượt cũ, giữ N lượt mới nhất |
| **Compaction** | Claude API (beta); Claude Code / Agent SDK: auto-compact + `/compact` | **tóm tắt** khi context to |
| **Context editing** | Claude API (beta) | **xóa** tool result cũ (hoặc thinking block); chữ chat vẫn giữ |
| **Case facts block** | code của bạn | **chép riêng** dữ kiện quan trọng, gửi mọi lần |

- 🧭 Thi: không hỏi cách build, chỉ cần nhận ra. ✅ khi đề nói lượt cũ **hiếm khi cần** + **dễ lấy lại** (M1 Q54). ❌ khi lượt cũ có **số phải giữ** (M1 Q56 => case facts block).

**Ví dụ cụ thể: nhiều vấn đề trong 1 session => bảng, không phải câu chuyện** *(Claude, M1 Q56 · M4 Q4 · M9 Q17)*
- Tình huống: 1 cuộc chat có 3 vấn đề: refund (lượt 1-15), subscription (16-30), đổi thẻ (31-45). Lượt 48 khách hỏi: "**Refund của tôi sao rồi?**" Context gần đầy.
- Muốn trả lời phải có **số chính xác**: đơn **#A123**, **$89.99**, trạng thái **approved ngày 20/11**.

| Lưu lượt cũ dưới dạng | Agent còn lại gì | Trả lời được không? |
|---|---|---|
| ❌ **Tóm tắt văn xuôi** (key M9 của site) | "Khách đã hỏi về refund trước đó, đã được xử lý." | **Không**: đơn nào? bao nhiêu? trạng thái gì? Số đã mất |
| ✅ **Structured data, lớp context riêng** (guide 5.1) | `refund: order A123, $89.99, approved 20/11` | **Có, chính xác** |

- Giống **bệnh án**: bệnh nhân quay lại, bác sĩ đọc bảng chỉ số ("huyết áp 120/80, thuốc X 50mg"), không đọc câu chuyện "bệnh nhân thấy hơi ổn".
- 🔑 Chữ trong đề: "**multiple issues**", "**order IDs, amounts, statuses**", khách **hỏi lại** vấn đề cũ.
- Câu nhớ: "**Sau này cần số chính xác => lưu bảng, không lưu câu chuyện.**"

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
| 7 | Bộ mock free online (mock 1, 2, 3) | free (cần đăng nhập) | M1 2026-11-18: 39/60. M2 (bộ thứ 2 cùng site) 2026-11-21: 37/60. M3 (bộ thứ 3, chỉ **14 câu**) 2026-11-21: 10/14. M4 (**làm lại bộ 1**) 2026-11-22: 46/60. M5 (**làm lại bộ 2**) 2026-11-24: 36/60. Câu hỏi bám guide khá sát (nhiều đáp án = ví dụ nguyên văn của guide). ⚠️ **Lời giải thích hay bịa** (chương sách không có, tên MCP sai, flag không tồn tại) => chỉ dùng **đáp án**, tự kiểm với guide. Đáp án sai: M1 Q46, M2 Q42. Xem log mục 10 |
| 8 | Site luyện thi free khác (bài học theo task statement + cheatsheet 22 luật + glossary Anh-Việt + mock) | free | M6 2026-11-24: **48/60 = 80%**. M7 2026-11-24: 49/60 = 81.7% (chi tiết mất: đã đóng tab kết quả). M8 2026-11-25: **53/60 = 88%** (làm trong tab group của Claude => đọc được đủ câu + giải thích). M9 2026-11-25: **54/60 = 90%** (56/60 theo guide). Ngân hàng 287 câu => từ M8 **trùng nhiều**. Đã đối chiếu **67 nguyên tắc** của trang bài học với mọi câu đã gặp: 11 nguyên tắc chưa gặp => thêm flashcard 📗 (xem M9 log). Kết quả chỉ lưu **trong trình duyệt** (không cần tài khoản). **Nhiều câu trùng** bộ mock #7 (bộ 1, 2) => có thể chung nguồn câu hỏi. Nhiều câu **chưa có giải thích**. ⚠️ Đáp án sai theo guide: M6 Q20 (lỗi ảnh hưởng nhau), Q32 (cửa sổ batch). Cheatsheet của site: luật 21 ("few-shot sửa được thông tin thiếu") **sai**, xem ⚠️ mục 10 (luật 17 đúng, khớp guide 4.6). Trang bài học D4 (12 nguyên tắc) đã đối chiếu 2026-11-24: notes phủ đủ, thêm cặp precision / recall ở 5.1 |

⚠️ **Tránh "dump"**: site ghi "**real exam questions**" = vi phạm **NDA** (`[G §14]`) => có thể bị **hủy kết quả + cấm thi** (`[G §13]`). **Đừng dùng** site kiểu đó.
⚠️ Mock bên ngoài **có thể sai đáp án**. Thấy mâu thuẫn với guide => **tin guide**, ghi ⚠️ vào mục 10.
⚠️ Mock bên ngoài có thể đánh **số domain khác** guide (xem mục 1 #1).

---

## 10. Quiz đã gặp + giải thích

### 🔁 Điểm yếu: câu sai nhiều lần (ôn cái này TRƯỚC khi thi)

> Bảng này = **luật**. Đáp án **cụ thể** từng câu sai >= 2 lần (✅ đáp án đúng vs ❌ đáp án bạn đã chọn, keyword thật): xem bảng **🎯 ngay dưới** (giống cheatsheet mục 2b). **Mọi câu đã gặp**, xếp theo 6 scenario thi (đọc như đọc đề): bảng **📚 Story index** dưới 🎯 (giống cheatsheet mục 2c).

| # | Chủ đề | Sai ở câu | Quy tắc 1 dòng | Ôn lại |
|---|---|---|---|---|
| 1 | **Hỏi / điều tra trước** khi làm theo yêu cầu của khách | M1 Q8, Q29 | Khách **đòi người rõ ràng** ("real person NOW") => escalate **ngay**, kèm history. Khách bực nhưng việc agent **làm được** => ghi nhận + đề nghị giải quyết **hoặc** escalate. Cả 2: ❌ hỏi thêm / điều tra trước | 6.2 |
| 2 | **Tóm tắt văn xuôi** làm mất dữ liệu | M1 Q18, Q56, Q37 · M9 Q22 (nguồn bị mất: chọn **prefix trong text**; đúng = **claim-source mapping có cấu trúc**) · M9 Q17 ⚠️ (bạn đúng, key site sai) | Dữ liệu phải giữ (ID, số tiền, status) => **structured**: chỉ giữ field cần, lớp context riêng, session mới + structured summary. ❌ prose summary, ❌ resume với tool result cũ | 6.1, 2.7 |
| 3 | **Thiết kế error** trả cho model | M1 Q14, Q49, Q51 · M4 Q60 (= M1 Q14 sai lần 2) · M8 Q16 (tool `analyze_error` riêng = cùng bẫy "tool riêng") · M9 Q10 (lỗi **tạm** retry ngay là được => **tool tự retry** bên trong; lỗi không bao giờ retry được => trả ngay kèm chi tiết. Khác M1 Q49: lỗi "không tìm thấy" **không** tạm => ❌ retry trong tool) | Lỗi phải có: **loại**, **retry được không**, **gợi ý bước tiếp**. ❌ retry ẩn trong tool, ❌ msg ngắn + tool riêng. Request hỏng (thiếu param) => **JSON-RPC protocol error**. Tool chạy mà lỗi => **isError**. Lỗi để agent **nói với user** (thiết bị không phản hồi) => **nguyên nhân có thể + bước khắc phục**, ❌ device ID + mã lỗi API (chỉ dev đọc được) | 3.2, 6.3 |
| 4 | **Cấu hình Claude Code** (rules / @import / /memory / permissions / command) | M1 Q20, Q25, Q50 · M2 Q41, Q44 · M4 Q21 (= M1 Q25 sai lần 2), Q29 bỏ trống (= M1 Q20) · M5 Q34 (= M2 Q44 sai lần 2) | Tự hỏi: **có pattern đường dẫn không?** Có (`**/*.test.tsx`, `terraform/**`) => rules + `paths:`. **Không** có pattern, maintainer tự biết => **@import** trong CLAUDE.md từng package. Lúc theo lúc không => **/memory** trước. "**Never** sửa thư mục X" => `permissions.deny` (rules vẫn chỉ là lời dặn). Checklist chỉ dùng **lúc review** => slash command / skill, ❌ CLAUDE.md (luôn load, tốn context mọi task), ❌ subagent riêng cho review (nặng hơn mức cần) | 4.1, 4.2, 4.3 |
| 5 | **Gộp / tách tool** | M1 Q3, Q31, Q44 · M2 Q7 · M4 Q32 (= M1 Q44 sai lần 2), Q56, Q57, Q54 bỏ trống · M5 Q26 (= M2 Q7 sai lần 2) | 1 tool làm **nhiều việc** (output lộn xộn) => **tách**. 2 tool **trùng nghĩa** model không phân biệt => **gộp** (hoặc rename + description). Model cần **thấy hết** để tự chọn => tool gộp trả **dữ liệu**, hành động giữ riêng. Tool làm **1 việc** mà description sơ sài (model dùng Grep thay vì nó, gọi delete thay vì archive) => **viết lại description**, ❌ tách nhỏ, ❌ validation phía server (đề hỏi "cải thiện **chọn tool**"). 1 tool có **bộ tham số khác nhau** theo thao tác => tách. Tool B gọi tool A **chỉ để lấy 1 field** (address) => cho B **nhận ID, tự tra bên trong**, ❌ gộp 2 tool làm 1 | 3.1, 3.4 |
| 6 | Chọn **hook** khi có cách code **đầy đủ hơn** | M1 Q2, Q52 · M4 Q18 (= M1 Q52 sai lần 2) | Đề có nhiều đáp án deterministic => chọn cái **phủ mọi trường hợp**: kiểm tra **sau khi loop dừng** (Q2), **tool tự** tạo yêu cầu duyệt (Q52). ❌ ngưỡng tùy ý (80% max_turns), ❌ hook + flag truyền qua | 2.4 |
| 7 | Bị hút vào **prompt caching** | M1 Q6 (nghi), Q54 | Caching = **chi phí / tốc độ**, không sửa **gốc** (gọi subagent thừa, context quá dài làm kém chất lượng). Chi tiết caching **ngoài phạm vi thi** => thường là bẫy | 0, 6.1 |
| 8 | **Chia task**: chaining / dynamic / orchestrator | M2 Q5, Q12 · M5 Q6 (= M2 Q12, **cùng đáp án sai**), Q42 bỏ trống · M9 Q15 (= M2 Q12, **bỏ trống**, lần 3 🔴) | Các bước **cố định, biết trước** (mọi PR đều review style => security => docs) => **prompt chaining**. Việc **mở**, chưa biết lỗi ở đâu (lỗi 500 lúc có lúc không, 200 file) => **dynamic**: vừa tìm vừa đổi kế hoạch. ❌ orchestrator-workers cho việc cố định (LLM "tự quyết cần check gì" là thừa), ❌ lập kế hoạch đầy đủ trước khi biết gì | 2.6 |
| 9 | **Làm to hơn** khi output không nhất quán / mất thông tin | M2 Q13, Q50 · M6 Q53 (tăng sliding window 25 => 50) | Format lúc thế này lúc thế kia, case lạ bị bịa / bỏ trống => **few-shot** 2-3 ví dụ đúng cách. ❌ model to hơn, ❌ fine-tune (không thi), ❌ temperature 0 (không dạy được format). Sliding window làm mất thông tin cũ => **hybrid** (tóm tắt cũ + giữ mới nguyên văn), ❌ **window to hơn** (chỉ mất muộn hơn) | 5.2, 6.1 |
| 10 | **Context xuống cấp** khi khám phá lâu | M2 Q26, Q29 · M5 Q22, Q50 (= M2 Q26 sai lần 2) · M8 Q15 (= M2 Q26, **cùng đáp án sai** "report + clear", lần 3) | Dấu hiệu: trả lời không nhất quán, "typical patterns", dev phải nhắc lại => **scratchpad file** ghi findings, **subagent** cho câu hỏi cụ thể ("tìm mọi test file"), summary **inject** vào subagent mới (M2 Q8 ✅). ❌ clear hết context + chỉ giữ 1 report, ❌ tóm tắt mọi file **trước** khi biết cái gì quan trọng | 6.4 |
| 11 | **Chọn built-in tool** + khám phá code | M2 Q6, Q17, Q38 · M3 Q11 · M5 Q21 (= M2 Q6 sai lần 2) · M8 Q38 (hàm bị wrapper đổi tên) · M9 Q34 (Edit không unique: chọn `old_string` **dài 30+ dòng**; đúng = **Read + Write**, sai lần 2) | Grep = tìm **nội dung** (import, error message). Glob / `find` = tìm **tên** file. Edit không tìm được text unique => **Read + Write** (❌ `replace_all`: chèn vào **mọi** chỗ khớp). Hiểu code lạ: Grep tìm **entry point**, rồi đi theo **import / function call / class gốc**. ❌ đọc file **to nhất** trước, ❌ subagent chia theo **service** khi cần hiểu **1 luồng** (auth) xuyên service. Hàm bị wrapper **đổi tên** (`calculateTax` => `computeOrderTax`) => **đọc library + wrapper lấy mọi tên**, rồi Grep từng tên (guide 2.5 nguyên văn); ❌ Grep file import rồi đọc từng file | 3.5 |
| 12 | **Iterative refinement** (sửa dần với Claude Code) | M2 Q37, Q48 (+ Q42 ⚠️) · M5 Q1, Q4 (= M2 Q48, Q37, **cùng đáp án sai**) | Sửa 1 edge case => đưa **test case** (input + output mong muốn). Domain **lạ** (lần đầu làm cache production) => **interview pattern**: để Claude hỏi bạn trước. Lỗi **ảnh hưởng nhau** => gửi **1 message**. ❌ mô tả bằng lời rồi bắt viết lại cả file | 4.5 |
| 13 | **1 prompt / 1 call ôm quá nhiều** | M3 Q3, Q6 | Dấu hiệu: thêm ví dụ cho mảng A thì mảng B **tụt**, hoặc output dài bị **cắt** ở `max_tokens` => **chia thành nhiều prompt / call nhỏ** (theo loại vấn đề, theo nhóm file), rồi **gộp** kết quả. ❌ thêm checklist vào **cùng** prompt, ❌ đổi sang markdown, ❌ model to hơn | 5.6 |
| 14 | **MCP: tool / resource / prompt** | M1 Q21, M4 Q42 (cùng 1 câu, sai 2 lần) · M3 Q2 | **Tool** = model **tự gọi** để làm việc. **Resource** = dữ liệu / catalog để **đọc** (trong Claude Code: `@`-mention được; cho agent thấy trước có gì => bớt call dò dẫm). **Prompt** = template **user tự chạy** => hiện thành **slash command**. ❌ "prompt vào tool registry, model tự gọi" | 3.4 |
| 15 | Bẫy chữ "**deterministic**" | M1 Q33, M4 Q26 (cùng 1 câu, sai 2 lần) | Model **không bao giờ** deterministic, kể cả khi đọc JSON. Lợi ích của JSON có field = agent **lấy giá trị chắc chắn, không phải parse text**. Đáp án có chữ "model xử lý deterministic" => loại | 5.3 |
| 16 | **Plan mode: khi nào cần / không cần** | M4 Q46 · M5 Q1, Q12 · M6 Q22 (**chiều ngược**: cần plan mode mà chọn bump version rồi sửa test fail dần) | Plan mode chỉ khi việc **to, nhiều file, nhiều cách làm** (migration 45 file, chọn WebSockets / SSE / polling). Thư viện đổi **breaking API** (callback => Promise, đổi type, bỏ method) dùng ở **45 file nhiều module** => **plan mode**, ❌ "update rồi sửa từng test fail". Bug có **stack trace rõ** / sửa **1 hàm 1 file** => **direct execution**. Chưa biết **yêu cầu** (lần đầu làm cache) => **interview pattern**, không phải plan mode (plan mode đọc **code**, không hỏi **bạn**) | 4.4, 4.5 |
| 17 | **Chọn cái đưa người xem** (sức người có hạn) | M2 Q18 · M5 Q32 (= M2 Q18, **cùng đáp án sai**), Q47 · M6 Q50 (= M5 Q47, **cùng đáp án sai**: layout lạ) · M8 Q50 (lần 3, **cùng đáp án sai**, không đánh dấu; cùng luật bạn làm **đúng** ở M8 Q9, Q37) | Chọn = **confidence thấp (từng field, đã calibrate) / tài liệu mơ hồ, mâu thuẫn**. ❌ random sample (random = để **đo** error rate), ❌ heuristic theo layout / loại entity | 6.5 |
| 18 | **Lỗi extraction: sửa đúng chỗ** | M2 Q19, Q46, Q51 · M5 Q41, Q45, Q46 (cả 3 **cùng đáp án sai** như M2) · M6 Q11 (forced **mọi** call, **sai lần 3**) | `context_length_exceeded` (input dài) => **chunk + gửi lại chỉ request lỗi**; ❌ `max_tokens` (là giới hạn **output**). Validation fail format ("2 to 3") => **gửi lại kèm lỗi cụ thể**; ❌ tiền xử lý tài liệu. Muốn tool X chạy **trước** => forced X **ở request đầu**, enrichment ở lượt sau; ❌ forced X **mọi** request (không bao giờ gọi được tool khác) | 5.3, 5.4, 5.5 |
| 19 | **Multi-agent: giữ thông tin + đi qua coordinator** | M2 Q4, Q22 · M5 Q24, Q51 (cả 2 **cùng đáp án sai**), Q29, Q53 · M6 Q17 (tin số mới nhất, **sai lần 3**), Q27 + Q30 (ép hết về văn xuôi, 1 câu xuất hiện 2 lần) · M8 Q52 (gap: chỉ search lại, thiếu vòng analysis) | Song song => **coordinator** spawn nhiều subagent / gọi **2 Task trong 1 response**; ❌ subagent tự spawn con, ❌ lớp async ngoài agent. Số liệu khác năm => subagent **ghi ngày**; ❌ tin số mới nhất. Nhiều loại nội dung => synthesis **render theo loại** (bảng / văn xuôi); ❌ lớp chuyển đổi về 1 format chung, ❌ chuẩn hóa hết thành văn xuôi (cũng là 1 format chung). Analysis thấy **gap** => analysis **báo gap** cho coordinator, coordinator search **và chạy lại analysis tới khi đủ** (guide 1.2); ❌ coordinator tự dò rồi **chỉ** search lại | 2.2, 2.3, 6.6 |
| 20 | **Hội thoại quên thông tin cũ** | M4 Q22 · M6 Q4, Q53 · M8 Q14 (= M6 Q53, **cùng đáp án sai**) | Mới **2-3 lượt** đã quên (user nói thích jazz, 2 lượt sau Claude hỏi lại) => app **không gửi lịch sử** trong `messages` (API **stateless**); ❌ vượt context window (2 lượt không thể đầy), ❌ tool xóa state. Hội thoại **dài**, sliding window bỏ lượt cũ => **hybrid**: tóm tắt lượt cũ + giữ lượt mới nguyên văn; số tiền / ngày / ID => **case facts block** (M6 Q40 ✅). ❌ tăng window (chỉ mất muộn hơn) | 6.1 |
| 21 | **Review sót bug xuyên file** | M2 Q33 · M6 Q8 (cùng 1 câu, sai 2 lần, đáp án sai khác nhau; M5 Q19 làm đúng) | Bug nằm ở file **không có trong prompt** (caller ở file không đổi vẫn dùng tham số cũ) => **review agentic có giới hạn lượt**: model tự Read / Grep, đi theo reference. ❌ chain-of-thought (không thấy file thì nghĩ mấy cũng không thấy), ❌ pass song song từng file + nhét dependents (danh sách tĩnh, sót reference nhiều tầng). **Khác** guide Q12: 14 file **đã có** trong prompt mà review nông => **attention dilution** => chia pass | 3.6, 4.6 |

### 🎯 Đáp án đúng vs bẫy bạn đã chọn (câu sai >= 2 lần)

> Đáp án viết lại bằng lời Claude, giữ **keyword thật** của đề. Cách ôn: **che 2 cột ✅ / ❌**, đọc "Đề nói", tự nói đáp án, rồi mới mở. 🔴 = sai 3 lần.

**Agent + multi-agent (D1)**

| Đề nói | ✅ Chọn | ❌ Bẫy bạn đã chọn | Phân biệt |
|---|---|---|---|
| 🔴 `lookup_citations` chạy trước khi có DOI, muốn `extract_metadata` chạy trước (M2 Q51 · M5 Q46 · M6 Q11) | forced `tool_choice: {"type":"tool","name":"extract_metadata"}` + enrichment ở **subsequent turns** | cùng forced đó nhưng "**for every API call**" | 2 đáp án mở đầu **giống nhau** => đọc **đuôi**. Mọi call => enrichment không bao giờ chạy. Cũng ❌ `"any"` (ép 1 tool bất kỳ), ❌ xếp tool lên đầu mảng `tools` |
| 🔴 2024: 35% vs 2022: 18% bị coi là mâu thuẫn (M2 Q22 · M5 Q51 · M6 Q17) | subagent **include publication / collection dates** trong structured output | synthesis coi số **most recent** là **authoritative**, số cũ ra appendix | khác năm = **xu hướng**. Sửa ở **nguồn** (output subagent), không đặt luật cứng ở synthesis |
| 🔴 tài chính / tin tức / patent bị ép hết thành bullet (M5 Q53 · M6 Q27, Q30) | synthesis **render each content type**: tables / prose / structured lists | **standardize** hết thành prose (M6), **conversion layer** về 1 common format (M5) | thấy "standardize / uniform / common format" => loại: vẫn ép 1 format |
| phân tích tuần tự chậm, muốn song song mà coordinator **vẫn theo dõi / debug** được (M2 Q4 · M5 Q24) | **coordinator spawns** nhiều subagent song song, gộp kết quả | subagent **tự spawn** subagent con | mọi thứ đi **qua coordinator** (hub-and-spoke) |
| 2 subagent độc lập nhưng chạy tuần tự (M5 Q29) | coordinator gọi **2 `Task` trong 1 response** | **async orchestration layer** bên ngoài agent | song song có sẵn trong agent loop, không cần hạ tầng mới |
| 🔴 lỗi 500 lúc có lúc không, 200+ file, **chưa biết** ở đâu (M2 Q12 · M5 Q6 · M9 Q15 bỏ trống) | **dynamic**: tạo subtask theo cái vừa tìm ra, đổi kế hoạch | lập **full plan** mọi code path trước | chưa biết **Ở ĐÂU** => **mỗi file đọc xong chỉ ra file đọc tiếp** (route => `OrderService` => `PaymentClient`: 3 file là ra, xem 2.6) |
| chèn hàm giữa file, `Edit` không tìm được text unique (M2 Q38 · M9 Q34) | **Read** cả file, chèn, **Write** lại | `replace_all` (M2); `old_string` **dài 30+ dòng** (M9) | `replace_all` sửa **mọi** chỗ khớp; chuỗi dài vẫn dễ lệch khoảng trắng |
| refund > $500 phải duyệt, **không lách được** (M1 Q52 · M4 Q18) | **tool tự enforce**: < $500 refund luôn, > $500 tạo approval request + trả "pending" | **PreToolUse hook** gắn flag `requires_approval`, tool đọc flag | code **1 chỗ, phủ hết** thắng hook + flag (2 mảnh phải khớp nhau) |

**Tool + MCP (D2)**

| Đề nói | ✅ Chọn | ❌ Bẫy bạn đã chọn | Phân biệt |
|---|---|---|---|
| agent dùng Grep thay vì `analyze_dependencies` (description: "Analyzes dependency graph") (M2 Q7 · M5 Q26) | **expand description**: làm gì, trả gì (direct imports, transitive deps, cycles) | **split** thành 3 tool (M2), **routing instructions** trong system prompt (M5) | tool làm **1 việc**, description sơ sài => sửa **description** |
| 1 tool `analyze_document` + instruction tự do, 35% phải hỏi lại (M1 Q44 · M4 Q32) | **split**: `extract_data_points`, `summarize_content`, `verify_claim_against_source`, có input / output contract | viết **description + examples** tốt hơn | tool làm **nhiều việc** => tách. Ngược với dòng trên |
| MCP server có **prompts** ngoài tools (M1 Q21 · M4 Q42) | thành **slash command** user tự chạy (`/mcp__<server>__<prompt>`) | vào **tool registry**, model tự gọi | tool = model gọi; resource = dữ liệu đọc; **prompt = user chạy** |
| `control_device` timeout, agent chỉ nói "không phản hồi" (M1 Q14 · M4 Q60) | `isError` + **likely causes + next steps** để agent nói với user | device ID + timeout + mã API (M4); "Device offline" + tool riêng (M1) | lỗi để **user** đọc => nguyên nhân + bước khắc phục, không phải thông tin debug |
| MCP error luôn là `isError` + "Operation failed", agent retry / escalate / hỏi user lung tung (M1 Q40 ✅ · M8 Q16) | trả **structured error metadata** ngay trong response: `errorCategory`, `isRetryable`, mô tả | tool mới **`analyze_error`** gọi sau mỗi lỗi (M8) | sửa lỗi **ở nguồn** (guide 2.2). Thêm tool = thêm call, mà tool đó cũng không biết lỗi gì. Cùng bẫy "tool riêng" như M1 Q14 |
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
| 🔴 reviewer chỉ xem được 5% / 20% (M2 Q18 · M5 Q32, Q47 · M6 Q50 · M8 Q50) | **low confidence** (field-level, **calibrated** với labeled set) + tài liệu **ambiguous / contradictory** | **random 5% sample** (M2, M5); tài liệu **formatting anomalies** / layout lạ (M5, M6, M8, cả 3 lần **không đánh dấu**) | random = để **đo**, không để chọn. Layout không báo trước field nào sai. Cùng luật bạn làm **đúng** ở M8 Q9, Q37: chỉ câu "30 minutes trong ingredient field" lừa được bạn |
| 🔴 đọc 8/45 file thì quên dần pattern (M2 Q26 · M5 Q50 · M8 Q15) | **subagents** cho câu hỏi cụ thể ("find all test files"), main agent giữ bức tranh lớn | summary report + **clear** hết (M2, M8); **Grep tên hàm** thay vì đọc (M5) | guide 5.4 nguyên văn. Clear = mất hiểu biết đã có từ 8 file |
| mới vài lượt đã hỏi lại thứ user vừa nói (M4 Q22 · M6 Q4) | app **không gửi prior messages** trong `messages` (API stateless) | tool **xóa state** (M4); **context window exceeded** (M6) | 2-3 lượt không thể đầy context |
| sliding window 2 chiều (M1 Q54 · M4 Q35 bỏ trống · M6 Q53 · M8 Q14) | 94% câu chỉ cần 3-5 lượt gần => **sliding window** 8-10 lượt. User mất sở thích cũ => **hybrid**: summary cũ + giữ mới nguyên văn | **prompt caching** (M1); **window to hơn** 25 => 50 (M6, M8) | caching không làm context nhỏ đi; window to chỉ mất muộn hơn |

### 📚 Story index: câu đã gặp => đáp án (theo 6 scenario thi)

> Đọc cột **Story** như đang đọc đề, **tự nói đáp án trước**, rồi mới nhìn ✅. Cột **Clue** = chữ trong đề chỉ ra đáp án. Trong mỗi scenario, câu yếu nhất đứng đầu. Tổng: 146 câu (mock M1-M9 + 12 câu mẫu guide + chủ đề chưa gặp). Flashcard dùng cùng dữ liệu này.

> 🔴 sai 3 lần · 🔁 sai 2 lần · ❌ sai 1 lần (đã sửa) · ⚠️ key site sai, bạn đúng · 📗 **chủ đề mới**: chưa gặp trong mock (nguyên tắc của site / guide) · 🟡 đúng nhưng không chắc / bỏ trống · 📘 câu mẫu guide

**1. Customer Support Resolution Agent** (34 câu)

| | Story | Clue | ✅ Chọn | ❌ Bẫy (mock bạn đã chọn) | Câu |
|---|---|---|---|---|---|
| 🔁 | Refunds over $500 need manager approval and must not be bypassable | cannot be bypassed | **The refund tool enforces it: under $500 refunds, over $500 creates an approval request and returns pending** | PreToolUse hook sets a requires_approval flag that the tool reads (M1, M4) | M1 Q52 · M4 Q18 · M9 Q36 ✅ |
| 🔁 | control_device times out; the agent only says the device is not responding | help the user take the next step | **isError + likely causes + next steps the agent can tell the user** | Device ID + timeout + API code for debugging (M4); Device offline + a separate tool (M1) | M1 Q14 · M4 Q60 |
| 🔁 | 35 turns (about 50K tokens), slow and worse; 94% of questions need only the last 3-5 turns | 94%, customers easily restate old details | **Sliding window: send only the last 8-10 turns** | Prompt caching while still sending everything (M1); left blank (M4) | M1 Q54 · M4 Q35 |
| 🔁 | Sliding window keeps 25 message pairs; users say it forgets earlier topics and preferences | earlier preferences lost | **Hybrid: summarize older messages, keep recent ones verbatim** | Grow the window to 50 pairs (M6, M8) | M6 Q53 · M8 Q14 |
| 🔁 | Only 2-3 turns later the agent asks again for info the user just gave (their name, loves jazz) | only a few turns | **The app is not sending prior messages in the messages array (the API is stateless)** | The tool cleared the state (M4); context window exceeded (M6) | M4 Q22 · M6 Q4 |
| ❌ | Angry customer wants someone who can actually help; the return is something the agent can do right now | frustrated, but the task is doable | **Acknowledge, say it can be done now, offer to do it OR escalate** | Ask what went wrong / investigate first (M1) | M1 Q8 · M4 Q19 ✅ · M8 Q3 ✅ |
| ❌ | Customer: I want to talk to a real person NOW (no tools called yet) | explicit request for a human | **Escalate immediately with the conversation history** | Acknowledge and ask one question first (M1) | M1 Q29 · M4 Q20 ✅ |
| ❌ | Agent hits max_turns mid-case; every case must end resolved or escalated | guarantee | **Code checks the result after the loop stops; if not resolved, code calls escalate_to_human with context** | Hook that stops at 80% of max_turns (M1) | M1 Q2 · M4 Q6 ✅ |
| ❌ | After lookup_order (bought 45 days ago), how should the loop decide refund vs escalate? | agentic loop | **The tool result goes into the conversation and the model reasons about the next step** | Preconfigured decision tree (M1) | M1 Q28 · M4 Q8 ✅ |
| ❌ | Tools grew from 4 to 10 (or 1 to 7); accuracy drops; agent confuses issue_credit and process_refund | semantically overlapping tools | **Merge the overlapping tools (one tool + action param; lookup_order + include_tracking flag)** | Split into finance and delivery subagents (M1) | M1 Q31 · M4 Q11 ✅ · M6 Q19 ✅ |
| ❌ | track_shipment throws a Python exception; the agent can only say something went wrong | agent has no next step | **Structured error: category, recoverable or not, suggestion (check the ID, search by order number)** | Retry with backoff inside the tool (M1) | M1 Q49 |
| ❌ | Every MCP tool error comes back as isError + Operation failed; the agent retries, escalates or asks the user at random | same message for every error | **Return structured error metadata at the source: errorCategory, isRetryable, a description** | New analyze_error tool called after each failure (M8); few-shot to read error patterns | M1 Q40 ✅ · M8 Q16 |
| ❌ | MCP: (1) missing required param, (2) API returns 404, (3) API returns 503 | which error type for each | **(1) JSON-RPC protocol error; (2) and (3) tool result with isError** | All three as isError (M1) | M1 Q51 · M4 Q28 ✅ |
| ❌ | lookup_order returns 40+ fields and fills context; 2 more orders to check | verbose tool output | **Keep only the relevant fields (items, purchase date, return deadline, status)** | Model writes a prose summary (M1) | M1 Q18 · M4 Q49 ✅ · M8 Q29, Q54 ✅ |
| ❌ | 3 issues in one session, near the context limit; at turn 48 the customer asks: what happened with my refund? | needs exact facts later (#A123, $89.99, approved) = a table, not a story | **Extract structured issue data (order IDs, amounts, statuses) into a separate context layer (guide 5.1 word for word)** | Prose / narrative summary of older turns (M1; also the M9 site key, wrong by guide) | M1 Q56 · M4 Q4 ✅ · M9 Q17 ⚠️ you were right |
| ❌ | Customer returns after 4 hours; old session has lookup_order PENDING; agent keeps citing it | even after fresh tool calls | **New session + structured summary of the old one + fresh tool calls before replying** | Resume and strip the old tool_results (M1) | M1 Q37 · M4 Q33 ✅ · M6 Q2 ✅ |
| ❌ | Confirm? dialog: 98% click within 2 seconds and still post to the wrong account / time / content | 2 seconds | **Show the full details (content, account, time, platform) in the confirmation** | Make the user type a confirmation phrase (M4) | M4 Q52 |
| ❌ | search_catalog fails 12%: 8% are timeouts that succeed on an immediate retry, 4% are syntax errors from bad user filters that never succeed | transient vs never-retryable | **Retry timeouts with backoff inside the tool; return syntax errors right away with parameter validation details** | Return every error with a retryable flag and let the agent spend turns retrying (M9) | M9 Q10 |
| ⚠️ | send_notification times out; unknown if it was sent; retries cause duplicates | status unknown | **By logic: report status unknown, may already be sent, do NOT retry** | Site key: retry_safe true (wrong by logic, see ⚠️ table) | M1 Q46 = M4 Q40 |
| 📗 | Incoming requests fall into clear categories (billing, technical, account), each handled differently | distinct categories | **Routing: classify the input, then send it to the specialized handler** | Prompt chaining (a fixed sequence) / orchestrator-workers (for unpredictable subtasks) | Site principle D1-4 |
| 📗 | Customer asks to match a competitor's price; the policy does not cover it | policy gap / exception | **Escalate. Triggers: the customer asks for a human, a policy exception or gap, or no progress** | Retry-count threshold / sentiment score / rigid rules engine / agent decides alone | Site principle D2-6 · guide 5.2 |
| 📗 | Different MCP tools return dates and status codes in different formats; the agent misreads them | normalize tool output | **PostToolUse hook that normalizes the results before the model sees them** | Prompt telling the model to convert formats / PreToolUse (runs before the call) | Guide 1.5 |
| 🟡 | 90-minute billing session; the summary turned a $184.60 credit (Mar 3, promised by May 10) into vague text | amounts, dates, promises lost | **Case facts block (amounts, dates, IDs) sent with every prompt, never summarized** | Better summarizer / bigger window / summarize later | M6 Q40 |
| 🟡 | The refund call times out midway while the customer waits | customer is waiting | **Explain, confirm eligibility, say it is a system error, offer escalation or retry later** | Keep retrying with backoff while the customer waits | M1 Q5 |
| 🟡 | Agent invents an order_id; the question asks for the root cause | root cause | **Fix the description: order_id must come from lookup_order (if it asked to guarantee: a gate)** | Gate / validation when the question asks for the root cause | M1 Q23 |
| 🟡 | remove_team_member(dry_run) preview is skipped in 15% of calls | ensure every, user explicitly confirms | **Two tools: preview_remove_member returns a single-use token; execute_remove_member requires it** | Prompt to always dry_run first / default dry_run=true | M6 Q28 |
| 🟡 | Asking 3 clarifying questions makes 40% of users give up | too many questions | **Make a reasonable assumption, state it, invite correction** | One question per turn / classifier / silent lookup table | M4 Q31 |
| 🟡 | Escalate a $847 refund (over the $500 limit); the human agent cannot see the transcript | human has no transcript | **Structured summary: customer ID, root cause, refund amount, recommended action** | Raw tool outputs / the whole transcript / a summary without IDs or a next step | M8 Q10 |
| 🟡 | 40-minute dinner-party chat at 78K tokens: shellfish allergy, 8 servings, room-temperature butter means 68°F, plus general chat | critical facts mixed with small talk | **Extract critical facts into a compact reference section + summarize the general chat + keep recent turns verbatim** | Summarize everything / sliding window / bigger window | M8 Q32 |
| 🟡 | A webhook says the package shipped while the user is mid-chat; the next reply should mention it naturally | the API is stateless | **Add the current shipping status to the system prompt before the next API call** | Anything that expects the model to know it without it being in the request | M9 Q47 |
| 🟡 | Refill agent: controlled substances need pharmacist approval; the prompt states it, yet 0.5% still go through | cannot be left to model discretion | **A hook that blocks submit_refill for controlled substances and routes them to a pharmacist** | Stronger prompt + examples / audit after submission / prompt-level self-check | M9 Q52 |
| 📘 | Agent skips get_customer in 12% of cases and refunds without a verified customer | 12%, skips a required step | **Gate in code: block process_refund until a verified customer ID exists** | Stronger system prompt / few-shot / routing classifier | Guide Q1 |
| 📘 | Agent mixes up two tools whose descriptions are one line each | first step, minimal descriptions | **Expand the tool descriptions (what it does, when to use it, inputs, examples)** | Few-shot examples / routing layer / merge the tools | Guide Q2 |
| 📘 | FCR 55%: agent escalates easy cases and handles hard ones alone | escalation is miscalibrated | **Explicit escalation criteria + few-shot examples in the system prompt** | Self-reported confidence score / separate classifier / sentiment analysis | Guide Q3 |

**2. Code Generation with Claude Code** (23 câu)

| | Story | Clue | ✅ Chọn | ❌ Bẫy (mock bạn đã chọn) | Câu |
|---|---|---|---|---|---|
| 🔴 | Intermittent 500 errors, 200+ files, the developer does not know which components are involved | does not know WHERE: each file you read tells you which file to read next | **Dynamic decomposition: decide each next step from what you just found (routes/orders.js -> OrderService -> PaymentClient: found in 3 files)** | Full plan of every code path before reading code (M2, M5); left blank (M9) | M2 Q12 · M5 Q6 · M9 Q15 |
| 🔁 | IaC repo with /terraform and /kubernetes: load only the rules for the file type being edited | a path pattern exists | **.claude/rules/ + paths: ["terraform/**/*"]** | Subfolder CLAUDE.md (M1); @import in the root CLAUDE.md (M4) | M1 Q25 · M4 Q21 |
| 🔁 | Monorepo with 15 packages and 3 standards; no naming pattern; maintainers know what each package needs | no pattern, maintainers decide | **@import the right standard in each package's CLAUDE.md** | .claude/rules/ with paths: listing each folder (M1); left blank (M4) | M1 Q20 · M4 Q29 |
| 🔁 | 8-item review checklist; the team also uses Claude for many other tasks | only needed when reviewing | **/review slash command (.claude/commands/review.md)** | Put it in CLAUDE.md (M2); dedicated review subagent (M5) | M2 Q44 · M5 Q34 |
| 🔁 | Add a Redis cache with 5-minute TTL; you are new to production caching | unfamiliar domain | **Have Claude interview you first (invalidation, consistency, failure modes)** | Plan mode reading the /products code (M2, M5) | M2 Q48 · M5 Q1 |
| 🔁 | Migration script mishandles records that contain null | one edge case | **Give a test case: input with null + expected output** | Describe the bug in words and rewrite the whole script (M2, M5) | M2 Q37 · M5 Q4 |
| ❌ | CLAUDE.md conventions are followed only sometimes; first diagnostic step? | first step, inconsistent | **/memory to see which memory files are loaded** | Search ~/.claude for conflicting rules (M1) | M1 Q50 · M4 Q15 ✅ |
| ❌ | 3 rules in CLAUDE.md, but Claude still edits db/migrations | never / prefer / after every edit | **permissions.deny for migrations + logging rule stays in CLAUDE.md + PostToolUse hook for Prettier** | Move everything to .claude/rules/ (M2) | M2 Q41 · M5 Q55 ✅ |
| ❌ | Production bug with a clear stack trace to one function, in a module you do not know | clear stack trace | **Direct execution: read the trace and the code, fix it** | Plan mode to list possible root causes (M5) | M2 Q10 ✅ · M5 Q12 · M6 Q26 ✅ · M8 Q13 ✅ |
| ❌ | Add one date check inside one function in one file | one file, small | **Direct execution** | Plan mode to analyze impact on the booking flow (M4) | M4 Q46 |
| ❌ | Auth library v2 to v3: callback to Promise, User type changed, 3 methods removed, imported in 45 files | breaking changes, several modules | **Plan mode: explore usage, map code paths, make a migration strategy, then implement** | Bump the version, run the tests, fix each failure (M6) | M6 Q22 |
| ❌ | Every PR gets the same 3 steps: style, security, docs | fixed, known steps | **Prompt chaining** | Orchestrator-workers (M2) | M2 Q5 · M5 Q5 ✅ |
| ⚠️ | PDF report: narrow columns, date format, page breaks; the three issues affect each other | issues interact | **All three in one detailed message (guide 3.5) - your pick, correct** | Site key: fix one at a time and test each (wrong by guide, see ⚠️ table) | M2 Q42 · M5 Q23 · M6 Q20 |
| 📗 | Request A: improve error handling across the service (open-ended, needs judgment). Request B: rename one function everywhere (mechanical) | open-ended + judgment-heavy | **Multi-phase workflow (analyze, propose, implement, review) for A; just do B directly** | Running the full multi-phase process for a simple rename | Site principle D1-3 |
| 📗 | A team MCP server must be shared through the repo without committing the API key | team-wide + secret | **.mcp.json in the repo, with ${ENV_VAR} for the secret** | ~/.claude.json (personal only) / hard-code the key | Guide 2.4 |
| 📗 | A teammate does not get a coding rule that works fine on your machine | only on my machine | **The rule sits in ~/.claude/CLAUDE.md (user level); move it into the repo CLAUDE.md** | Re-run /init / restart Claude Code | Guide 3.1 |
| 📗 | A skill produces long exploratory output that clutters the main conversation; it should also use only a few tools | skill frontmatter | **In the SKILL.md frontmatter: context: fork (own context) + allowed-tools (limits tools)** | Put these in settings.json / CLAUDE.md | Guide 3.2 |
| 🟡 | Code format is right only some of the time | every time | **PostToolUse hook, matcher Edit\|Write, runs Prettier** | Stop hook + prompt asking the model to check | M1 Q22 · M4 Q9 ✅ |
| 🟡 | Add tests to a 200-file legacy codebase; no priorities given | open-ended | **Glob/Grep to map the structure, prioritize key modules, adapt the plan** | Read all 200 files first / fixed schedule | M2 Q53 ✅ · M5 Q42 blank |
| 🟡 | Migrate every service off a deprecated HTTP client: 1,400 files, 30 directories, nobody knows who still uses it | unknown usage, open-ended | **Map usage with Grep and Glob, prioritize the most coupled modules, revise the plan as dependencies appear** | Read every file / split evenly by directory / start anywhere without a plan | M9 Q26 |
| 📘 | Create a /review command that the whole team gets | team-wide | **.claude/commands/ in the repo** | ~/.claude/commands/ (personal) / CLAUDE.md / .claude/config.json (does not exist) | Guide Q4 |
| 📘 | Split a monolith into microservices | large, architectural | **Plan mode** | Direct execution, fix as you go | Guide Q5 |
| 📘 | Conventions depend on file type; test files are scattered across folders | scattered files of the same type | **.claude/rules/ with glob paths:** | Root CLAUDE.md / skills / per-folder CLAUDE.md | Guide Q6 |

**3. Multi-Agent Research System** (26 câu)

| | Story | Clue | ✅ Chọn | ❌ Bẫy (mock bạn đã chọn) | Câu |
|---|---|---|---|---|---|
| 🔴 | Web data says 35% (2024), an internal report says 18% (2022); synthesis flags a contradiction | different years | **Subagents include publication / collection dates in their structured output** | Treat the most recent data as authoritative, older data to an appendix (M2, M5, M6) | M2 Q22 · M5 Q51 · M6 Q17 · M9 Q42 ✅ |
| 🔴 | Financial JSON, news prose and patent lists all get rendered as bullet points | tabular clarity, narrative flow, hard to scan | **Synthesis renders each type: financial = tables, news = prose, technical = structured lists** | Standardize all to prose (M6 twice); conversion layer to one common format (M5) | M2 Q27 ✅ · M5 Q53 · M6 Q27, Q30 · M9 Q48 ✅ |
| 🔁 | 12 precedents analyzed one by one (3 minutes); make it faster, but the coordinator must still track and debug | coordinator visibility | **Coordinator spawns several subagents in parallel and merges the results** | The analysis subagent spawns its own child subagents (M2, M5) | M2 Q4 · M5 Q24 |
| 🔁 | One analyze_document tool with a free-text instruction; 35% of results need re-requests | one tool, many jobs | **Split into extract_data_points, summarize_content, verify_claim_against_source, each with a contract** | Better description + examples (M1, M4) | M1 Q44 · M4 Q32 · M6 Q44 ✅ |
| ❌ | Coordinator calls web search, waits, then calls document analysis; the two are independent | independent but sequential | **Coordinator emits 2 Task calls in one response** | Async orchestration layer outside the agent (M5) | M2 Q35 ✅ · M5 Q29 |
| ❌ | Coordinator gives step-by-step orders; subagents fail on new topics | over-specified | **Give goals + quality criteria; the subagent chooses how to search** | Classifier for well-defined vs exploratory tasks (M1) | M1 Q7 · M4 Q13 ✅ · M9 Q9 ✅ |
| ❌ | The final report loses which source each fact came from; synthesis drops the citations when combining | source metadata lost | **Subagents return a structured claim-source mapping (claim, URL/doc, quote, date); synthesis must preserve and merge it** | Coordinator injects source-ID prefixes into the text and parses them later (M9); inline citations in prose | M1 Q55 · M4 Q45 · M9 Q22 · M9 Q28 ✅ |
| ❌ | Curation agent makes 18+ sequential calls; it must see all candidates to choose | see everything to choose | **Combined discover_and_analyze returns all candidates + scores; add_to_collection stays separate** | Preview + approve by a fixed rule (M1) | M1 Q3 · M4 Q37 ✅ |
| ❌ | Analysis agent notices gaps (no token refresh details / no appeal deadlines) but search has already finished | gap insight is not actionable | **Analysis reports each gap to the coordinator; the coordinator runs targeted searches AND re-runs analysis until coverage is sufficient** | Coordinator scans the output and re-runs search only (M8 Q52); confidence label / upfront planner / wider retrieval | M1 Q16 ⚠️ · M8 Q52 · M8 Q55 ✅ · M9 Q7 ✅ |
| 📗 | Coordinator has AgentDefinitions and talks about delegating, but no subagent ever runs; no errors are logged | talks about delegating, nothing happens | **Add "Task" to the coordinator's allowedTools** | Rewrite the prompt / change the model / add retries | Site principle D1-7 · guide 1.3 |
| 📗 | Subagent B needs a large output that subagent A produced | large content between subagents | **Pass reference identifiers to a shared store; the coordinator forwards what B needs** | Inline the full raw content into B's prompt / rely on callbacks or automatic context inheritance (they do not exist) | Site principle D1-11 |
| 📗 | The analysis subagent replies that it has no information about what the search subagent found | subagents do not share context | **The coordinator must explicitly put the search results into the analysis subagent's prompt** | Assume subagents see each other's output / one shared conversation | Site principle D1-16 · guide 1.3 |
| 📗 | The report generator writes claims without citations; it only receives the synthesis draft | the report stage lost the sources | **Pass the draft together with a structured source index (claim, URL, excerpt)** | Pass all raw content / source names only / match citations afterwards | Site principle D1-18 |
| 📗 | A design proposes that subagents call each other directly or share an event bus | who talks to whom | **Everything goes through the coordinator (hub); it forwards output into the next subagent's prompt** | Direct subagent-to-subagent calls / event bus / automatic sibling access | Site principle D1-19 · guide 1.2 |
| 📗 | Every subagent gets all 18+ tools; tool selection accuracy keeps dropping | too many irrelevant tools | **Give each subagent only its 4-5 role-relevant tools** | Better descriptions for all 18 / bigger model / one super-agent with everything | Site principle D2-4 · guide 2.3 |
| 📗 | Long input: the model handles the start and the end well but misses findings in the middle | position, not volume | **Put key findings at the top and organize with clear section headers** | Bigger model / bigger context window | Guide 5.1 |
| 📗 | A search returns zero results vs. the search service times out | empty result vs access failure | **Zero results = valid success; timeout = an error with context (what was tried, retryable or not)** | Treat both the same / report empty results as errors / return a timeout as an empty success | Guide 2.2, 5.3 |
| 🟡 | Summarizing a follow-up takes 40 seconds through a subagent | the coordinator already has the context | **The coordinator summarizes from its own context** | Prompt caching for the subagent | M1 Q6 |
| 🟡 | A multi-agent job crashes; resume without redoing the work | resume after a crash | **Each agent writes a manifest file; the coordinator reads it on resume** | Restart from scratch / rely on chat history | M1 Q45 |
| 🟡 | Query types are diverse and evolving | diverse and evolving | **The coordinator (LLM) decides how to route each query** | Fast-path rules / pattern routing / trained classifier | M2 Q16 |
| 🟡 | A contract amendment changes 30 days to 45 days | two values, both real | **Schema keeps multiple values + source + effective date** | Pick one value | M2 Q32 · M8 Q27 ✅ |
| 🟡 | Newsroom assistant with 4 subagents; which ones a query needs varies and shifts every news cycle | varies per query, only clear after reading it | **Orchestrator-workers: a coordinator LLM decides per query which and how many subagents to call** | Fixed pipeline / trained classifier / keyword routing | M9 Q24 |
| 🟡 | Two cost-effectiveness studies with different methods get averaged into one number in the report | different methods | **Keep each study's original method and wording; separate settled findings from contested ones** | Average them / silently drop uncertain data / require a two-source minimum | M9 Q42 ✅ · site principle D1-21 |
| 📘 | Report about creative industries is missing music, writing and film | each subagent did its own part well | **The coordinator decomposed the topic too narrowly** | Blame the search or synthesis subagents | Guide Q7 |
| 📘 | Web search subagent times out | what the coordinator should receive | **Structured error context: what was tried, partial results, alternatives** | Generic status / empty result as success / stop the whole workflow | Guide Q8 |
| 📘 | Synthesis needs to verify facts; 85% are simple checks | 85% simple | **Give synthesis one narrow verify_fact tool; complex checks go via the coordinator** | Give synthesis all search tools / batch verify / pre-cache | Guide Q9 |

**4. Developer Productivity** (22 câu)

| | Story | Clue | ✅ Chọn | ❌ Bẫy (mock bạn đã chọn) | Câu |
|---|---|---|---|---|---|
| 🔴 | After reading 8 of 45 files, answers get worse and earlier patterns are forgotten | context degrading, same task | **Subagents for specific questions (find all test files); the main agent keeps the big picture** | Summary report + clear everything (M2, M8); Grep function names instead of reading (M5) | M2 Q26 · M5 Q50 · M8 Q15 |
| 🔁 | Insert a function in the middle of a file; Edit fails because no anchor text is unique | not unique | **Read the whole file, insert, Write it back** | Edit with replace_all (M2); Edit with a very long old_string of 30+ lines (M9) | M2 Q38 · M5 Q16 ✅ · M9 Q34 |
| 🔁 | Cache logic is spread over 15 files; understand it before adding a trigger | understand before changing | **Follow imports + class hierarchy, find the base class, Read it, trace each invalidation** | Glob + read the largest file (M2); Grep invalidate and read nearby lines (M5) | M2 Q6 · M5 Q21 · M9 Q43, Q55 ✅ |
| 🔁 | Agent uses Grep instead of analyze_dependencies (description: Analyzes dependency graph) | one job, vague description | **Expand the description: what it returns (direct imports, transitive deps, cycles)** | Split into 3 tools (M2); routing instructions in the system prompt (M5) | M2 Q7 · M5 Q26 · M9 Q16, Q60 ✅ |
| 🔁 | An MCP server exposes prompts (templates) besides tools | MCP prompts | **They show up as slash commands that users run** | Added to the tool registry for the model to call (M1, M4) | M1 Q21 · M4 Q42 |
| ❌ | Find every file that imports @company/auth | text inside the files | **Grep the import line (content search)** | find -type d -name *auth* (M2) | M2 Q17 · M5 Q31 ✅ |
| ❌ | A new dev must understand auth across 800+ files and many services | one flow across services | **Grep the auth entry point, Read it, follow imports and calls** | Parallel subagent per service (M3) | M3 Q11 · M8 Q21 ✅ |
| ❌ | 30+ minutes of exploration; answers are inconsistent; the dev has to repeat things | long session | **Scratchpad file with key findings, re-read when needed** | Summarize every file before exploring (M2) | M2 Q29 · M5 Q2 ✅ |
| ❌ | 25 minutes on rendering; answers now say typical rendering patterns; next question is how physics integrates with rendering | typical patterns, integrates with | **Summarize the rendering findings, spawn a physics subagent with that summary** | Independent physics subagent, merge yourself (M5); /clear | M2 Q8 ✅ · M5 Q22 · M9 Q11 ✅ |
| ❌ | 3 MCP servers (git, Jira, docs); one request needs all three | how the tools become available | **Every server's tools are discovered at connect and usable together** | Agent picks one server and loads only its tools (M5) | M2 Q14 ✅ · M5 Q9 |
| ❌ | 3 MCP servers (issues, wiki, DB); the agent makes 8-10 blind calls because it does not know what each has | blind exploratory calls | **Expose each server's catalog as MCP resources** | Orchestrator routes by keyword to one server (M3) | M3 Q2 · M9 Q14 ✅ |
| ❌ | User says delete old backups; agent calls delete_file although policy says archive | most directly improve tool selection | **Expand both descriptions (when to use each, not for backups)** | Server-side validation that blocks deletes (M4) | M1 Q59 ✅ · M4 Q56 |
| ❌ | get_neighborhood_info(address) always needs get_property_details first, only to get the address | a call made only to fetch one field | **get_neighborhood_info takes property_id and looks up the address itself** | Merge both into one tool (M4) | M1 Q60 ✅ · M4 Q57 |
| ❌ | One tool for refund / cancel / reship, each with different params; missing or extra params | different param sets | **Split into 3 tools, each with only its own params** | if-then-else schema / nested object / all optional + few-shot; left blank (M4) | M1 Q27 ✅ · M4 Q54 |
| ❌ | Document of 175-190K tokens, last third missed, 200K context, tool definitions take 2,500 tokens | add up the numbers | **Tool definitions + system prompt + document nearly fill the 200K** | Exceeds the effective attention span (M5) | M2 Q43 ✅ · M5 Q35 |
| ❌ | Find all callers before removing a function; wrapper modules re-export it under new names (calculateTax becomes computeOrderTax) | renamed / re-exported | **Read the library + wrappers to list every exposed name, then Grep each name across the codebase** | Grep files that import the modules, then read each one (M8); Grep only the original name | M5 Q56 ✅ · M8 Q38 |
| 📗 | You worked on other things since; now you want back the session named payment-audit | one specific earlier session | **claude --resume payment-audit (loads that exact named session)** | --continue (only resumes the most recent conversation) | Site principle D3-3 · guide 1.7 |
| 🟡 | Find every eval( call, or the SYNC_CONFLICT error string across 12 services | text inside files | **Grep** | Glob *eval* / ls -R (file names only) | M3 Q5 · M2 Q45 · M9 Q30 ✅ |
| 🟡 | Subagent read 47 files, the connection dropped, a teammate renamed 2 functions | most context still valid | **Resume the subagent + tell it about the renamed functions** | New session / paste the whole transcript / ignore the rename | M5 Q58 · M6 Q46 |
| 🟡 | Yesterday's session is still useful; 3 of the 12 analyzed files were modified | small, known change | **Resume + tell it which 3 files changed so it re-reads them** | New session / re-read all 12 / say nothing | M2 Q49 ✅ · M5 Q11 blank |
| 🟡 | Try 2 refactor approaches from the same analysis | two branches from one point | **fork_session** | Redo the analysis twice | M2 Q40, Q54 |
| 🟡 | Need standard access to Jira data | standard integration | **Use an existing community MCP server for Jira** | Write a custom server / curl / export to markdown | M3 Q4 |

**5. Claude Code for CI/CD** (18 câu)

| | Story | Clue | ✅ Chọn | ❌ Bẫy (mock bạn đã chọn) | Câu |
|---|---|---|---|---|---|
| 🔁 | Review misses callers in unchanged files that use the old argument order; reviews run async | unchanged files not included | **Turn-limited agentic review: the model reads files and searches via tools** | Chain-of-thought (M2); parallel per-file passes + dependents + summary call (M6) | M2 Q33 · M5 Q19 ✅ · M6 Q8 |
| ❌ | CI test generation: trivial asserts, hand-built records instead of fixture factories | in the first place | **CLAUDE.md: test standards + good vs trivial examples + list of fixture factories** | Second Claude pass that scores and deletes weak tests (M6) | M3 Q9 ✅ · M6 Q15 · M9 Q50 ✅ |
| ❌ | One prompt reviews security + API + logic; few-shot raises logic 34% to 41% but API drops 82% to 68% | one area up, another down | **Separate prompts per area, each with its own examples, then merge findings** | Replace the few-shot with a checklist in the same prompt (M3) | M3 Q3 |
| ❌ | 30+ file PR; report_findings JSON is cut off at max_tokens | truncated output | **Split into several calls by file group, merge the findings arrays** | Return a markdown list instead (M3) | M3 Q6 |
| 📗 | CI needs Claude Code output that a script can parse reliably | machine-readable | **claude -p with --output-format json (+ --json-schema)** | Parse the free-text answer with regex | Guide 3.6 |
| 📗 | The same session that wrote the code reviews it and misses its own bugs | self-review | **Review with a second, independent Claude instance that does not have the generator's reasoning** | Ask the same session to review harder / add extended thinking | Guide 4.6 |
| 📗 | You want to learn which code patterns cause false-positive review findings | analyze false positives | **Add a detected_pattern field to each finding and analyze it** | Ask developers to report false positives in chat / raise the threshold | Guide 4.4 |
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

**6. Structured Data Extraction** (23 câu)

| | Story | Clue | ✅ Chọn | ❌ Bẫy (mock bạn đã chọn) | Câu |
|---|---|---|---|---|---|
| 🔴 | lookup_citations runs before the DOI exists; extract_metadata must run first | two options start the same, read the end | **Forced tool_choice {"type":"tool","name":"extract_metadata"}, enrichment in subsequent turns** | The same forced choice for every API call (M2, M5, M6) | M2 Q51 · M5 Q46 · M6 Q11 |
| 🔴 | 12% semantic errors pass the schema (30 minutes put in an ingredient quantity field); reviewers can check 20% | semantic errors | **Field-level confidence + calibrate thresholds on a labeled set** | Documents with formatting anomalies / unusual layouts (M5, M6, M8, never flagged) | M2 Q57 ✅ · M5 Q47 · M6 Q50 · M8 Q50 |
| 🔁 | Batch of 10,000 documents; 300 fail with context_length_exceeded | input too long | **Chunk and resubmit only the 300 failed documents** | Raise max_tokens (M2, M5) | M2 Q19 · M5 Q41 · M8 Q8 ✅ |
| 🔁 | 12% fail Pydantic (expected float, got 2 to 3); a plain retry fails the same way | unchanged retry fails | **Resubmit with the specific validation error** | Preprocess the source documents (M2, M5) | M2 Q46 · M5 Q45 |
| 🔁 | Main benefit of JSON fields over free text for downstream agents | the word deterministic is a trap | **The agent reads exact values without parsing text** | The model processes JSON deterministically (M1, M4) | M1 Q33 · M4 Q26 |
| 🔁 | Reviewers can check only 5% of extractions; which ones should they get? | limited capacity | **Low-confidence extractions + ambiguous or contradictory documents** | A random 5% sample (M2, M5) | M2 Q18 · M5 Q32 · M8 Q9, Q37 ✅ |
| ❌ | materials field: cotton blend vs Cotton/Polyester mix vs empty | inconsistent format | **Few-shot with 2-3 input/output pairs** | Bigger model (M2) | M2 Q13 · M5 Q49 ✅ |
| ❌ | 23% of corrections are measures like a handful or a splash: invented numbers or blanks | a repeated pattern | **Few-shot showing how to keep the original measure text** | Fine-tune on the 847 corrections (M2) | M2 Q50 · M5 Q43 ✅ |
| ❌ | property_type enum fails 8%: studio, loft, duplex... and new types keep appearing | long-term, new types | **Enum + other + a property_type_detail field** | Free string + normalize later (M2) | M2 Q55 · M5 Q14 ✅ |
| ❌ | Review schema: Great product! gets invented pros/cons; sarcastic reviews get an arbitrary sentiment | fix exactly the two problems | **Allow empty arrays for pros/cons + add unclear to the sentiment enum** | Optional fields + add neutral and unclear (M8): sarcasm is not neutral | M8 Q56 |
| ⚠️ | Batch API (50% off, up to 24h); SLA 30 hours with 99.9% reliability | 99.9%, worst case | **Submit every 4 hours (4 + 24 = 28h) - your pick, correct** | Site key: every 6 hours (exactly 30h, no margin, see ⚠️ table) | M6 Q32 · M9 Q56 |
| 📗 | Invoice extraction: the stated total sometimes does not match the sum of the line items | the numbers do not add up | **Extract calculated_total next to stated_total and flag mismatches (conflict_detected) for human review** | Let the model or a second pass silently fix the numbers | Site principle D4-9 · guide 4.4 |
| 📗 | Documents of unknown type and several extraction tools (invoice, receipt, contract); output must always be structured | must call a tool, unknown which | **tool_choice "any": the model must call a tool and picks which one** | auto (may answer in text) / forcing one specific tool | Guide 4.3 |
| 🟡 | Retry-with-error fixes most failures in 2-3 tries; when is it LEAST effective? | the info is not in the input | **Co-authors shown as et al. when the full list exists only in another document** | Format errors (retries fix those) | M6 Q37 |
| 🟡 | Calendar JSON is often invalid and downstream rejects it | syntax errors | **Tool use with an input schema** | Prompt + parse the text | M2 Q3, Q59 |
| 🟡 | skills string[]: Python and SQL sometimes joined, unstated skills added, length 5-10 vs 40+ | all three are inconsistency | **Few-shot showing how to split, what counts as stated, level of detail** | Limit to 10-20 skills | M2 Q20 ✅ · M5 Q15 blank · M8 Q30 ✅ |
| 🟡 | The field is nullable but the model still invents 500 | the schema is already nullable | **Instruct it to return null when the info is absent** | Make the field required | M2 Q36 |
| 🟡 | 5% of fields are empty although the document has the info (inline citations vs bibliography) | different document structures | **Few-shot with varied document structures** | Retry unchanged / make the fields optional | M2 Q58 |
| 🟡 | 12% errors hide in high-confidence results; you need ongoing measurement | measure | **Stratified random sampling every week** | Re-extract / lower the threshold / heuristics | M2 Q15 · M5 Q13 |
| 🟡 | 97% overall accuracy; is it ready to automate? | an aggregate can hide a weak type | **Measure per document type and per field first** | Trust the overall number / pilot and wait for errors | M2 Q52 |
| 🟡 | ML extraction confidence: 23% of wrong ones still pass, 31% of right ones still go to review | routing by confidence | **Return field + confidence + request_review set by a tested threshold in code + reason** | Raw score + few-shot so the model reads it | M1 Q13 · M4 Q55 |
| 🟡 | Prices come as $12 vs 12.00, icons vs text | normalization | **Strict schema + normalization rules in the prompt** | Post-processing script / second call | M2 Q28 · M5 Q8 |
| 🟡 | 50,000 contracts, 2-week deadline, 82% pass the schema on the first try | cost-efficient + deadline | **Batch all, then resubmit only the failures in new batches, refining the prompt between them** | Real-time API for everything / resubmit everything | M6 Q25 |

### ⚠️ Đáp án mock đã kiểm tra là SAI

| Nguồn + câu | Mock ghi | Đúng theo guide |
|---|---|---|
| M1 Q46 = M4 Q40 (send_notification timeout, không biết đã gửi chưa => bị gửi trùng) | A: `retry_safe: true` cho timeout (M4: bạn chọn A, được chấm đúng) | ⚠️ **Sai logic**: báo "retry an toàn" => gửi trùng **thêm**. Nên là B: báo rõ "status unknown, có thể đã gửi, **đừng retry**" (instructive error) |
| M1 Q32 = M4 Q58 (update_user_profile thiếu `user_id`) | A: strict JSON schema (M4: bạn chọn A) | ⚠️ **Tranh cãi**: docs Anthropic nói description chi tiết là yếu tố **quan trọng nhất** (D). Mẹo: "bảo đảm / loại bỏ lỗi cấu trúc" => schema; "giúp model **hiểu** nên điền gì" => description |
| M1 Q16 (gap phát hiện sau analysis) | C: coordinator tự dò gap rồi search lại | ⚠️ **Sát nút**: B (analysis báo gap cho coordinator, search + analysis lại tới khi đủ) cũng khớp `[G 1.2]`. Điểm chung cần nhớ: vòng lặp đi **qua coordinator**. **M8 Q52** (site khác) chấm đúng kiểu B: analysis **báo gap** + search **và analysis lại tới khi đủ** (khớp vòng lặp guide 1.2). Thi: chọn đáp án có **vòng lặp đầy đủ** |
| M1 Q8 (khách "want someone who can actually help") | B: đề nghị làm ngay **hoặc** escalate | ⚠️ **Xám** với `[G 5.2]` "đòi người rõ ràng => escalate ngay". Phân biệt: Q8 = bực + việc làm được; Q29 = "real person NOW" => escalate ngay |
| M2 Q42 = M5 Q23 = M6 Q20 (PDF report: cột hẹp, ngày sai format, ngắt trang sai, 3 lỗi **ảnh hưởng nhau**) | B: sửa **lần lượt** (cột => ngày => ngắt trang), test sau mỗi bước (M5: bạn lại chọn C, bị chấm sai. M6: site **khác** cũng ghi vậy, bạn chọn "1 message", bị chấm sai) | ⚠️ **Sai theo guide 3.5**: lỗi **ảnh hưởng nhau** => gửi **cả 3 trong 1 message** (C, bạn chọn). Sửa lần lượt = cho lỗi **độc lập** (mục 4.5) |
| M6 Q32 (batch rẻ 50%, tới 24h; SLA 30h, độ tin cậy 99.9%; gửi batch mỗi mấy giờ) | B: mỗi **6h** (bạn chọn A: 4h, bị chấm sai) | ⚠️ **Sai theo guide 4.5** nguyên văn: "**4-hour windows** to guarantee 30-hour SLA with 24-hour batch processing". 6h + 24h = **đúng 30h**, không còn dư cho retry, mà đề đòi 99.9%. 4h + 24h = 28h, dư 2h. **M9 Q56** lại chấm 6h, trong khi **bài học D5-2 của chính site** ghi "4 giờ + 24 giờ = 28 giờ, dư 2 giờ" => key tự mâu thuẫn |
| M9 Q17 (3 vấn đề trong 1 session: refund / subscription / payment; lượt 48 khách hỏi lại refund, gần hết context) | C: tóm tắt lượt cũ thành **văn xuôi**, giữ nguyên lịch sử chỉ cho vấn đề đang làm (bạn chọn A, bị chấm sai) | ⚠️ **Sai theo guide 5.1** nguyên văn: "Extracting and persisting **structured issue data (order IDs, amounts, statuses) into a separate context layer** for multi-issue sessions" = A, bạn chọn. Văn xuôi làm mất số (🔁 dòng 2). Bài học D2-14 của site dạy ngược guide => **thi theo guide** |
| Cheatsheet site M6 (luật 21) | "retry không sửa được thông tin thiếu => chỉ few-shot hoặc dữ liệu nguồn tốt hơn" | Guide 4.4: thông tin **không có** trong nguồn => retry vô ích; few-shot **cũng không** tạo ra thông tin thiếu => để null / đánh dấu thiếu / đưa người xem. Few-shot chỉ giúp khi thông tin **có** nhưng ở **dạng lạ** (inline citation vs bibliography, M2 Q58). *(Luật 17 "tách coverage / threshold stage" trước đây ghi ⚠️ **nhầm**: nó **khớp** guide 4.6 "self-reports confidence alongside each finding" + M3 Q7. Xem cặp precision / recall ở 5.1)* |
| M2 (giải thích) | Q47 nói `--allowedTools` "không tồn tại"; Q49 gộp 2 đáp án thành 1 dòng | flag `--allowedTools` **có thật** (đáp án Q47 vẫn đúng). Q49 lỗi hiển thị của site, đáp án vẫn chấm được |
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
| Q54 | chat support 35 lượt (~50K token) => trả lời chậm + kém. Đề cho số: 94% câu hỏi chỉ cần 3-5 lượt gần nhất, 6% còn lại khách dễ nói lại | **prompt caching** + vẫn gửi hết lịch sử | **sliding window**: mỗi request chỉ gửi 8-10 lượt mới nhất; cần chi tiết cũ thì nhờ khách nói lại | caching chỉ làm **rẻ + nhanh** hơn, model **vẫn đọc đủ 50K token** => vẫn kém. Số liệu đề = bỏ lượt cũ an toàn. Xem **Giải thích kỹ** bên dưới | 6.1 |
| Q56 | 3 vấn đề trong 1 session, gần hết context, hỏi lại vấn đề đầu | **tóm tắt văn xuôi** lượt cũ | **trích issue data có cấu trúc** (ID, số tiền, status) vào lớp context riêng | = guide nguyên văn; văn xuôi mất số | 6.1 |

**Câu đúng nhưng bạn còn phân vân**

| Câu | Bạn nghi | Vì sao đáp án đúng thắng |
|---|---|---|
| Q5 (refund timeout giữa chừng) | C: retry backoff, giữ hội thoại tới khi xong | khách chờ vô hạn. ✅ A: giải thích + xác nhận đủ điều kiện + báo lỗi hệ thống + đề nghị escalate / thử lại sau |
| Q6 (tóm tắt follow-up mất 40s) | A: prompt caching cho subagent | vẫn spawn + đẩy 80K token mỗi lần. ✅ B: coordinator tự tóm tắt bằng context đang có `[G 1.2]` |
| Q13 (confidence của ML extraction) | A: điểm thô + few-shot dạy model đọc | vẫn để model đoán = đang hỏng. ✅ B: `request_review` boolean tính bằng **ngưỡng đã test** trong code + lý do (calibrate, 6.5) |
| Q22 (format code lúc đúng lúc sai) | D: Stop hook + prompt nhờ model kiểm tra format | D vẫn để **model chấm** = xác suất => vẫn lúc đúng lúc sai. ✅ A: **PostToolUse** hook, matcher `Edit\|Write`, chạy **Prettier** (chương trình, lần nào cũng ra giống nhau) ngay sau mỗi lần sửa file. Xem **Giải thích kỹ** |
| Q40 (mọi lỗi đều "Operation failed") | B: few-shot dạy đọc pattern lỗi | mọi lỗi **cùng 1 chữ** => không có pattern để học. ✅ C: thêm `errorCategory`, `isRetryable`, mô tả ở nguồn |
| Q24 (thiết kế lỗi của tool) | (phân vân) | mỗi **loại lỗi** trả lỗi **riêng** (timeout, không tìm thấy, không có quyền...) + **gợi ý bước tiếp** => agent biết nên thử lại, hỏi khách hay escalate. ❌ 1 câu lỗi chung cho mọi trường hợp (3.2) |
| Q45 (multi-agent dừng giữa chừng, cần chạy tiếp) | (phân vân) | mỗi agent ghi **trạng thái** (xong gì, tìm được gì, còn gì) ra file ở **chỗ cố định** = **manifest**. Resume => coordinator **đọc manifest**, đưa vào prompt => chạy tiếp, không làm lại từ đầu (6.4) |
| Q55 (report cuối mất nguồn) | (phân vân) | subagent trả **từng claim kèm nguồn** (URL / tên tài liệu, trích đoạn, ngày) = **claim-source mapping**; synthesis agent **giữ** liên kết đó khi gộp. Subagent trả văn xuôi => nguồn mất **trước** khi tới synthesis (6.6) |

**Giải thích kỹ: Q54, Q22, Q24, Q45, Q55** *(Claude)*

Q24, Q45, Q55: đề gốc không lưu lại, chỉ còn đáp án => phần dưới giải thích ý chính, không phải đề nguyên văn.

**Q54: chat dài thì chậm + kém => sliding window, không phải prompt caching**
- Tình huống: chat support 35 lượt (~50K token), trả lời chậm, chất lượng giảm. Đề cho 2 con số: **94%** câu hỏi chỉ cần **3-5 lượt gần nhất**; **6%** còn lại khách **dễ nói lại** thông tin cũ.
- Bạn chọn: prompt caching + vẫn gửi hết lịch sử. ✅ Đúng: **sliding window**: mỗi request chỉ gửi **8-10 lượt mới nhất**, cần chi tiết cũ thì nhờ khách nói lại.
- Vì sao:
  - Prompt caching = phần đầu prompt **giống hệt** lần trước thì xử lý **rẻ + nhanh** hơn. Nhưng model **vẫn đọc đủ 50K token**. Cái làm kém là **quá nhiều chữ cũ không liên quan** (lost in the middle, nhiễu). Caching không bỏ được token nào.
  - 2 con số là gợi ý: lượt cũ gần như không cần, khi cần thì cách lấy lại rất rẻ (khách nói lại). Giữ 8-10 lượt trong khi chỉ cần 3-5 => có dư an toàn.
  - **Sliding window** (cửa sổ trượt) = chỉ giữ N lượt mới nhất. Có lượt mới => bỏ lượt cũ nhất, như cái cửa sổ trượt dọc theo cuộc chat. Do **code app** làm, không phải setting: xem **Sliding window: cách hoạt động** ở 6.1.
- Ví dụ: lượt 2 "Đơn của tôi đâu?" ... lượt 34 "Đổi mật khẩu thế nào?". Trả lời lượt 34 không cần lượt 2.
- ⚠️ Đừng dùng bừa: Q56 nhìn giống nhưng đáp án khác. Lượt cũ có **số quan trọng** (mã đơn, $89.99, status refund) => **không** bỏ, trích vào **case facts block** (6.1). Q54 đúng là sliding window chỉ vì đề nói rõ chi tiết cũ hiếm khi cần + lấy lại dễ.
- 🧭 Luật: vấn đề là "**context quá dài**" => làm context **nhỏ lại**. Caching = sửa **chi phí / tốc độ**, không sửa **độ dài context** (🔁 dòng 7).

**Q22: format lúc đúng lúc sai => PostToolUse hook chạy Prettier**
- Tình huống: Claude Code sửa file, lúc theo format của team, lúc không. Muốn đúng **mọi lần**.
- Bạn phân vân: D: Stop hook + prompt nhờ model kiểm tra format. ✅ Đúng: A: **PostToolUse** hook, matcher `Edit|Write`, chạy **Prettier**.
- Vì sao:
  - D vẫn để **model chấm** => xác suất => có lúc sót. Đúng y vấn đề ban đầu.
  - Prettier là chương trình bình thường: cùng input => cùng output, **lần nào cũng vậy** (deterministic, xem 📖).
  - PostToolUse chạy **ngay sau mỗi tool call**. Matcher `Edit|Write` = chỉ chạy sau khi file bị sửa / ghi => file nào đổi cũng được format ngay, model không cần nhớ gì.
  - Stop hook chỉ chạy **1 lần** khi Claude trả lời xong cả lượt => muộn, và phần prompt vẫn là model đoán.
- Ví dụ `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write" }
        ]
      }
    ]
  }
}
```

- 🧭 Luật: "phải xảy ra **mọi lần**" + có **công cụ** làm được => hook chạy công cụ đó (code). ❌ nhờ model kiểm tra.
- ⚠️ So với 🔁 dòng 6 (Q2, Q52): hook **thắng** prompt / model chấm. Nhưng hook **thua** một thiết kế code **đầy đủ hơn** (tool tự enforce, kiểm tra sau khi loop dừng).

**Q24: lỗi của tool => lỗi riêng cho từng loại + bước tiếp theo**
- Cùng bài học với Q14, Q40, Q49 (🔁 dòng 3).
- ❌ Mọi lỗi đều trả `"Operation failed"` => agent không phân biệt được timeout với sai mã => chỉ nói được "có trục trặc".
- ✅ Mỗi loại lỗi 1 kiểu riêng, kèm gợi ý làm gì tiếp:

```json
{ "isError": true, "errorCategory": "not_found", "isRetryable": false,
  "message": "No shipment for tracking ID TR-99. Ask the customer to check the ID, or search by order number." }
```

```json
{ "isError": true, "errorCategory": "timeout", "isRetryable": true,
  "message": "Carrier API timed out. Safe to retry in a few seconds." }
```

- Agent đọc là biết: timeout => thử lại. Không tìm thấy => hỏi khách. Không có quyền => escalate.

**Q45: multi-agent dừng giữa chừng => manifest**
- Tình huống: nhiều agent cùng làm 1 việc dài, hệ thống crash / bị dừng. Khi resume, không muốn làm lại từ đầu.
- ✅ Mỗi agent ghi **trạng thái** ra file ở **chỗ cố định** (= **manifest**): xong gì, tìm được gì, còn gì. Khi resume, coordinator **đọc các manifest** và đưa vào prompt => mỗi agent chạy tiếp từ chỗ đã dừng.
- Ví dụ manifest của 1 agent:

```json
{
  "agent": "find-test-files",
  "status": "partial",
  "done": ["src/payments", "src/orders"],
  "todo": ["src/users"],
  "findings": ["RefundService has no tests"]
}
```

- 🎮 Giống **file save** trong game: thua thì load save, không chơi lại từ màn 1. Memory files + MEMORY.md của Claude Code cũng làm vậy (6.4).
- ❌ Ý sai hay gặp: làm lại từ đầu (phí hết việc đã làm); trông vào lịch sử chat cũ (có thể mất sau crash, lại dài + rối).

**Q55: report cuối mất nguồn => claim-source mapping**
- Tình huống: subagent đi tìm nguồn (web, tài liệu), synthesis agent gộp thành 1 report. Đọc report cuối không biết fact nào lấy từ nguồn nào.
- ✅ (1) Subagent trả **từng claim kèm nguồn** (URL / tên tài liệu, trích đoạn ngắn, ngày) = **claim-source mapping**. (2) Synthesis agent **giữ** liên kết đó khi gộp, không viết lại thành văn xuôi mất nguồn.
- Vì sao: subagent chỉ trả tóm tắt văn xuôi => nguồn mất **trước** khi tới synthesis, sau đó không ai lấy lại được => sửa ở **output của subagent**, rồi giữ nguyên khi gộp.
- Ví dụ output của subagent:

```json
[
  { "claim": "Market grew 12% in 2025",
    "source": "Industry report 2026, p.4",
    "quote": "...revenue rose 12% year over year...",
    "date": "2026-03" }
]
```

- Thêm (6.6): 2 nguồn uy tín **mâu thuẫn** => giữ **cả 2** kèm nguồn, ❌ tự chọn 1.

🧭 **Điểm chung**: Q24, Q45, Q55 (và Q56) cùng 1 luật: **truyền dữ liệu có cấu trúc, không truyền văn xuôi** (🔁 dòng 2).

**Bài học thêm từ câu đúng**
- Q1 vs Q52: tool trả lỗi "please escalate" (Q1-A) vẫn để model tự escalate => ❌. Tool **tự tạo yêu cầu duyệt** (Q52-A) => ✅. Gate trong tool chỉ thắng khi nó làm **trọn** hành động an toàn.
- Q23: đề hỏi "**root cause**" agent bịa `order_id` => sửa **description** (order_id phải lấy từ `lookup_order`). Nếu đề hỏi "**guarantee**" => gate.
- Q27 vs Q31: tool chung có **bộ tham số khác nhau** => **tách**. 2 tool **cùng một việc** => **gộp**.
- Q59: 2 tool description 1 dòng (archive vs delete) => **mở rộng description** (giống câu mẫu Q2).
- Q60: tool B cần dữ liệu mà tool A trả => cho tool B **nhận ID và tự tra** bên trong, bỏ chuỗi phụ thuộc.

**Nhận xét chung**: sai nhiều nhất ở **D1 agent / multi-agent**, **D2 thiết kế tool + error**, **D3 cấu hình Claude Code**, **D5 context**. Kiểu sai lặp lại: chọn đáp án "**hỏi thêm / điều tra trước**", "**tóm tắt văn xuôi**", "**hook**" khi có thiết kế đầy đủ hơn, "**prompt caching**". Xem bảng 🔁.

#### [M2] Mock 2 - 60 câu (2026-11-21): **37/60 = 61.7%**

Bộ thứ 2 của cùng site với M1. Câu sai: 4, 5, 6, 7, 12, 13, 17, 18, 19, 22, 26, 29, 33, 37, 38, 41, 42, 44, 46, 48, 50, 51, 55. Q42 đáp án site **sai theo guide** (bạn chọn đúng guide) => tính theo guide là **38/60 = 63%**. Claude đã xem **cả 60 câu** (đáp án + lựa chọn của bạn qua màu trên trang kết quả) và đối chiếu guide. Tóm tắt bằng lời của Claude, không chép nguyên đề.

**Câu sai (23)**

| Câu | Tình huống (rút gọn) | Bạn chọn | ✅ Đúng | Vì sao | Guide |
|---|---|---|---|---|---|
| Q4 | phân tích 12 tiền lệ tuần tự mất 3 phút; muốn nhanh hơn mà coordinator **vẫn theo dõi + debug được** | subagent phân tích **tự spawn** subagent con | **coordinator spawn nhiều subagent song song**, mỗi cái 1 phần tiền lệ, gộp kết quả trước synthesis | hub-and-spoke: mọi giao tiếp đi **qua coordinator** => coordinator thấy hết. Subagent tự spawn con => coordinator mất dấu. Queue / đệ quy = phức tạp, khó debug | 1.2 |
| Q5 | review mọi PR theo **đúng 3 bước cố định** (style, security, docs) | orchestrator-workers | **prompt chaining** | bước **biết trước, giống nhau mọi lần** => chaining. Orchestrator-workers = khi **chưa biết** cần làm gì, LLM tự quyết => thừa ở đây | 1.6 |
| Q6 | logic cache rải 15 file (~8.000 dòng), cần hiểu trước khi thêm trigger, giữ context gọn | Glob tên file cache, đọc file **to nhất** trước | **xem import + class hierarchy => tìm base class, Read nó, rồi trace từng chỗ invalidation** | hiểu code **từ từ theo luồng** (interface trước, chi tiết sau). File to nhất ≠ file quan trọng nhất | 2.5 |
| Q7 | agent cứ dùng Grep thay vì `analyze_dependencies`, description chỉ có "Analyzes dependency graph" | **tách** thành 3 tool nhỏ | **viết description chi tiết** (làm gì, trả gì: direct imports, transitive deps, cycles) | gốc lỗi = description sơ sài (giống Q1, bạn làm đúng). Tách tool chỉ khi 1 tool làm **nhiều việc** 🔁 | 2.1, 2.4 |
| Q12 | lỗi 500 lúc có lúc không, 200+ file, **chưa biết** component nào liên quan | lập **kế hoạch đầy đủ** mọi code path trước khi đọc code | **tạo subtask động** theo cái vừa tìm ra, đổi kế hoạch khi có thông tin mới | việc **mở** => dynamic decomposition. Không thể lập kế hoạch đầy đủ khi chưa biết lỗi nằm đâu 🔁 | 1.6 |
| Q13 | field "materials" lúc "cotton blend", lúc "Cotton/Polyester mix", lúc bỏ trống | đổi **model to hơn** | **few-shot 2-3 cặp input / output** với format chuẩn | output không nhất quán => few-shot dạy format. Model to = làm quá tay, không dạy được format 🔁 | 4.2 |
| Q17 | tìm mọi file `import @company/auth` | Bash `find -type d -name "*auth*"` | **Grep** câu import trong **nội dung** file | câu import nằm **bên trong** file => Grep. `find` / Glob chỉ xem **tên** file, thư mục 🔁 | 2.5 |
| Q18 | reviewer chỉ xem được 5%, chọn cái nào đưa người xem | random 5% | **model báo confidence thấp, hoặc tài liệu mơ hồ / mâu thuẫn** | sức người có hạn => dồn vào chỗ **dễ sai nhất**. Random sampling = để **đo** error rate (Q15), không phải để chọn | 5.5 |
| Q19 | batch 10.000 tài liệu, 300 cái lỗi `context_length_exceeded` | tăng `max_tokens` cho 300 cái | **chỉ gửi lại 300 cái, chia nhỏ (chunk)** rồi gộp kết quả | lỗi do **input** quá dài. `max_tokens` = giới hạn **output**, không liên quan. Gửi lại cả batch = phí | 4.5 |
| Q22 | 2024: 35% vs 2021: 18%, synthesis coi là **mâu thuẫn** thay vì tăng trưởng | luôn tin số **mới nhất**, số cũ để phụ lục | **subagent ghi ngày xuất bản / thu thập** trong structured output | không có ngày => synthesis không biết đây là **xu hướng theo thời gian**. Tin số mới nhất = vứt dữ liệu xu hướng | 5.6 |
| Q26 | đọc 8/45 file thì trả lời kém dần, quên pattern đã bàn | viết summary report, **clear hết** context, chỉ dùng report | **subagent cho câu hỏi cụ thể** ("tìm mọi test file", "trace refund flow"), main agent giữ bức tranh lớn | = ví dụ **nguyên văn** guide (mục 6.4 có sẵn). Clear hết + 1 report = mất chi tiết 🔁 | 5.4 |
| Q29 | phiên khám phá 30+ phút, trả lời không nhất quán, dev phải nhắc lại | **tóm tắt mọi file** trước khi khám phá | **scratchpad file** ghi key findings, đọc lại khi cần | scratchpad = trí nhớ ngoài, ghi **cái đã tìm ra**. Tóm tắt trước = đoán cái gì quan trọng khi chưa biết gì 🔁 | 5.4 |
| Q33 | review 1 lần chỉ có diff + file đã đổi, sót bug ở **file không đổi** (caller dùng tham số cũ) | thêm **chain-of-thought** liệt kê reference | **agentic có giới hạn lượt**: model tự Read / Grep codebase, đi theo reference để kiểm | model **không thấy** file không có trong prompt => suy luận kỹ mấy cũng không thấy caller. Phải cho tool đi tìm. Nhồi file 2 hop = quá nhiều | 3.6, 4.6 |
| Q37 | migration script xử lý sai record có `null` | mô tả lỗi bằng lời + **viết lại cả script** | **đưa test case** (input có null + output mong muốn) rồi nhờ sửa | test case = rõ nhất, không hiểu nhầm. Viết lại cả script = dễ phá phần đang đúng 🔁 | 3.5 |
| Q38 | chèn hàm vào giữa file, Edit lỗi vì không có text unique | Edit `replace_all` | **Read cả file, chèn, Write lại** | `replace_all` chèn vào **mọi** chỗ khớp => sai. Guide: Edit không tìm được text unique => Read + Write 🔁 | 2.5 |
| Q41 | 3 yêu cầu ghi trong CLAUDE.md, Claude vẫn sửa file migration | chuyển hết vào `.claude/rules/` | **`permissions.deny` cho `Edit(./db/migrations/**)`** + logging giữ ở CLAUDE.md + **PostToolUse hook** chạy Prettier | rules vẫn chỉ là **lời dặn** (xác suất). "Never" => chặn cứng. "Prefer" => CLAUDE.md. "Sau mọi lần edit" => hook (= M1 Q22) 🔁 | 3.1, 3.3 |
| Q42 ⚠️ | PDF report có 3 lỗi format **ảnh hưởng nhau** (cột, ngày, ngắt trang) | gửi **cả 3 trong 1 message** | site: sửa **lần lượt**, test sau mỗi bước | ⚠️ **Site sai theo guide**: lỗi **ảnh hưởng nhau** => 1 message; lỗi **độc lập** => lần lượt. Bạn chọn đúng guide | 3.5 |
| Q44 | checklist review 8 mục; team còn dùng Claude cho nhiều việc khác | thêm vào **CLAUDE.md** | **slash command `/review`** gọi khi review | CLAUDE.md **luôn load** => checklist chiếm context cả khi viết feature. Command / skill = chỉ load **khi cần** 🔁 | 3.2 |
| Q46 | 12% fail Pydantic ("expected float, got '2 to 3'"), retry y nguyên => y lỗi | **tiền xử lý** tài liệu nguồn | **gửi lại kèm lỗi validation** để model tự sửa | retry **kèm lỗi cụ thể** sửa được lỗi **format**. Retry không đổi gì = vô ích (đề nói rõ). Tiền xử lý = phải đoán trước mọi dạng lạ | 4.4 |
| Q48 | làm cache Redis TTL 5 phút, nhưng **mới** với cache production | plan mode đọc code `/products` trước | **để Claude phỏng vấn bạn** (invalidation, consistency, failure mode) trước khi làm | domain **lạ** => interview pattern (mục 4.5). Đọc code không cho bạn biết **mình còn thiếu yêu cầu gì** 🔁 | 3.5 |
| Q50 | 23% bản sửa là do "a handful", "a splash" (bịa số hoặc bỏ trống) | **fine-tune** trên 847 bản sửa | **few-shot** chỉ cách giữ **nguyên văn** cách đo không chuẩn | fine-tune **không thi** + quá tay. Pattern lặp lại => đưa vào few-shot 🔁 | 4.2 |
| Q51 | "extract metadata và cho biết bao nhiêu citation" => gọi `lookup_citations` trước, thiếu DOI | forced `extract_metadata` cho **mọi** request | forced `extract_metadata` **ở request đầu**, enrichment ở **lượt sau** | forced mọi request => **không bao giờ** gọi được tool enrichment. `tool_choice` đặt **từng request** (mục 3.3 có nguyên văn) | 2.3, 4.3 |
| Q55 | enum 4 loại nhà, gặp "studio", "loft"... và loại mới xuất hiện liên tục | đổi sang **string tự do** + chuẩn hóa sau | enum thêm **"other" + field `property_type_detail`** | giữ enum cho loại phổ biến + có chỗ ghi loại lạ. String tự do = mất cấu trúc. Mở rộng enum mãi = không theo kịp | 4.3 |

**Câu đúng nhưng bạn còn phân vân** (bạn đánh dấu 29 câu)

| Câu | Bạn nghi | Vì sao đáp án đúng thắng |
|---|---|---|
| Q3 (JSON lịch, downstream từ chối JSON hỏng) | A (prompt + schema, parse text) vs B | ✅ B: **tool + input schema** => hết lỗi cú pháp `[G 4.3]`. A = lời dặn => xác suất. Q59 cùng ý |
| Q8 (25 phút khám phá rendering, trả lời "typical patterns") | | ✅ B: tóm tắt findings rendering, spawn subagent physics **kèm summary đó**. "typical patterns" = dấu hiệu context xuống cấp. C: subagent không có context rendering. D `/clear` = mất hết |
| Q10 (bug production, stack trace rõ) | | ✅ D direct execution: bug **rõ, 1 chỗ** `[G 3.4]`. Plan mode = thừa |
| Q14 (3 MCP server) | | ✅ A: tool của **mọi** server được discover lúc connect, dùng **cùng lúc** (mục 3.4) |
| Q15 (12% lỗi ở confidence cao, cần đo lâu dài) | | ✅ C stratified random sampling hằng tuần => **đo** error rate + bắt lỗi kiểu mới. A re-extract = model lặp cùng lỗi. B hạ ngưỡng = tăng việc, không đo. D heuristic = chỉ bắt lỗi **đã biết** |
| Q16 (thấy cả 4 đúng) | | ✅ D coordinator tự quyết. Chữ khóa "**diverse and evolving**" => luật cố định (A fast-path, B pattern routing) sẽ lỗi thời; C classifier cần data có nhãn + train lại (luật vàng 2). Coordinator là LLM, tự hiểu được loại query mới |
| Q20 (skills `string[]` có 3 vấn đề) | | ✅ A few-shot: cả 3 vấn đề đều là "**làm không nhất quán**" => ví dụ dạy được cả 3. D giới hạn 10-20 = số tùy ý, cắt mất skill thật. B, C không sửa cách trích |
| Q27 (tài chính / tin tức / patent bị ép thành bullet) | | ✅ A: mỗi loại 1 format (tài chính = bảng, tin = văn xuôi), mục 6.6 nguyên văn |
| Q28 (giá "$12" vs "12.00", icon vs text) | | ✅ A: schema strict + quy tắc chuẩn hóa ngay trong prompt. 1 lần gọi là xong |
| Q32 (hợp đồng có amendment 30 => 45 ngày) | | ✅ C: schema giữ **nhiều giá trị** + nguồn + ngày hiệu lực. Giống Q22: giữ hết + ngày, ❌ tự chọn 1 |
| Q35 (2 subagent độc lập chạy tuần tự) | | ✅ D: coordinator gọi **2 Task trong 1 response** |
| Q36 (field nullable mà vẫn bịa "500") | | ✅ A: dặn trả `null` khi không có. Schema **đã** nullable, chỉ thiếu lời dặn. B required = càng bịa |
| Q40, Q54 (thử 2 hướng từ cùng 1 phân tích) | | ✅ `fork_session`: 2 nhánh từ cùng 1 điểm, không phân tích lại |
| Q43 (tài liệu 175-190K token, sót 1/3 cuối, context 200K) | | ✅ D: tool definition (2.500 token) + system prompt + tài liệu => gần 200K. Số liệu trong đề chỉ thẳng D. *(Claude)* API thật: vượt context thì **báo lỗi**, không tự cắt; đề muốn bạn **cộng số** |
| Q45 (lỗi "SYNC_CONFLICT", 12 service) | | ✅ C: Grep chuỗi lỗi đặc trưng (Grep = nội dung) |
| Q47 (không hiểu đáp án) | | ✅ A `--append-system-prompt`. `--system-prompt` **thay toàn bộ** system prompt mặc định của Claude Code (gồm phần hướng dẫn dùng tool đọc file, đi theo code) => Claude chỉ xử lý diff. `--append-system-prompt` = **thêm** vào cuối, giữ phần mặc định. D sai: `-p` **không tắt** Read / Glob / Grep (lại còn có `--dangerously-skip-permissions`) |
| Q52 (thấy cả 4 đúng) | | ✅ B: đo **theo loại tài liệu + field**, vì 97% tổng có thể che 1 loại kém (mục 6.5 nguyên văn). A, C vẫn nhìn **con số tổng**. D pilot = "chạy thử rồi chờ lỗi" (đáp án nhiễu ở mục 6.5) |
| Q53 (thêm test cho 200 file, không nói ưu tiên gì) | | ✅ B: Glob / Grep vẽ cấu trúc, ưu tiên module quan trọng, sửa kế hoạch khi gặp phụ thuộc (= dynamic decomposition) |
| Q57 (12% lỗi semantic, reviewer xem được 20%) | | ✅ B: confidence **từng field** + calibrate bằng labeled set. D random = để đo, không để chọn (giống Q18) |
| Q58 (5% field rỗng dù tài liệu có thông tin) | | ✅ C: few-shot với tài liệu **cấu trúc khác nhau** (citation inline vs bibliography). B retry không đổi gì = vô ích. D optional = giấu lỗi |

**Bài học thêm từ M2**
- Q5 vs Q12 vs Q53: các bước **cố định** => prompt chaining. Việc **mở** (điều tra lỗi, thêm test cho code cũ) => dynamic, vừa làm vừa sửa kế hoạch.
- Q15 vs Q18 vs Q57: random / stratified sampling = để **đo** error rate. Chọn cái đưa người xem khi sức người có hạn = **confidence thấp (đã calibrate) / tài liệu mơ hồ**.
- Q1 (đúng) vs Q7 (sai): cùng 1 bài (MCP tool description sơ sài). Đáp án "tách tool" nghe hợp lý nhưng chỉ đúng khi tool làm **nhiều việc**.
- Q41: map **từng yêu cầu** vào **đúng cơ chế**: "never" => `permissions.deny`, "prefer" => CLAUDE.md, "sau mỗi lần edit" => PostToolUse hook.
- Q46 vs Q58 vs Q36: retry **kèm lỗi cụ thể** sửa được lỗi format. Retry **không đổi gì** = vô ích. Tài liệu **không có** thông tin => trả `null`, không retry.
- Nhiều câu sai có đáp án **nguyên văn trong notes** (Q17, Q22, Q26, Q29, Q37, Q38, Q48, Q51) => đọc lại mục 3.3, 3.5, 4.5, 6.4, 6.6 trước mock 3.

**Nhận xét chung**: 37/60 (M1: 39/60). Sai nhiều nhất ở **D4 structured output** (Q13, Q19, Q46, Q50, Q51, Q55), **D2 built-in tool + MCP** (Q6, Q7, Q17, Q38), **D3 Claude Code** (Q37, Q41, Q44, Q48), **D5 context** (Q18, Q22, Q26, Q29), **D1 chia task** (Q4, Q5, Q12). Kiểu sai lặp lại: chọn cách "**làm to hơn**" (model to hơn, fine-tune, orchestrator-workers, kế hoạch đầy đủ trước) và "**tóm tắt / clear context**" thay vì scratchpad / subagent. Xem bảng 🔁 dòng 8-12.

#### [M3] Mock 3 - 14 câu (2026-11-21): **10/14 = 71%**

Bộ thứ 3 cùng site, chỉ **14 câu** (gần hết là scenario CI/CD + developer productivity). Câu sai: 2, 3, 6, 11. Bạn nói không chắc **câu nào** => Claude giải thích **cả 14**. 3 chi tiết sản phẩm (REVIEW.md, `--bare`, `--max-budget-usd`) đã kiểm với docs Claude Code: **có thật**. Không có đáp án site nào sai.

**Câu sai (4)**

| Câu | Tình huống (rút gọn) | Bạn chọn | ✅ Đúng | Vì sao | Guide |
|---|---|---|---|---|---|
| Q2 | agent nối 3 MCP server (issue, wiki, DB); câu hỏi chéo hệ thống => 8-10 tool call tuần tự, gọi **dò dẫm** vì không biết server nào có gì, hết context | orchestrator **route theo keyword** tới 1 server | **expose catalog mỗi server thành MCP resources** (tóm tắt issue, cây tài liệu, DB schema) | agent **thấy trước** có gì => bớt call dò dẫm (mục 3.4 nguyên văn). Keyword routing = routing layer (luật vàng 2), lại còn câu hỏi **chéo 3 hệ thống** không route về 1 server được | 2.4 |
| Q3 | 1 prompt review cả security + API + business logic; thêm few-shot logic => logic 34% lên 41%, nhưng API 82% tụt 68% | thay few-shot bằng **checklist** edge case logic | **tách thành prompt riêng** (security + API / business logic), mỗi cái có ví dụ riêng, rồi gộp findings | gốc = 1 prompt ôm quá nhiều => thêm cho mảng này thì mảng kia tụt (chú ý bị chia). Checklist vẫn nhồi vào **cùng prompt** => vẫn đánh đổi, lại chỉ bắt case đã liệt kê 🔁 | 4.6 |
| Q6 | review PR 30+ file bằng tool `report_findings`, output chạm `max_tokens` => JSON bị cắt giữa chừng, parser lỗi | bỏ tool_use, trả **markdown list** | **chia thành nhiều call**, mỗi call 1 nhóm file, rồi gộp mảng findings | markdown vẫn bị cắt, lại mất cấu trúc. Tăng `max_tokens` + viết ngắn = PR to hơn lại hỏng. Chỉ báo critical = mất findings. Chia nhỏ = per-file pass (câu mẫu Q12) 🔁 | 4.6, 4.3 |
| Q11 | người mới cần hiểu kiến trúc auth trước khi sửa, 800+ file nhiều service | **subagent song song** cho từng service rồi tổng hợp | **Grep tìm entry point auth, Read, rồi đi theo import / function call** để vẽ luồng auth dần dần | cần hiểu **1 luồng** xuyên service => đi theo luồng. Chia theo **service** = mỗi subagent tả cả service, không bám câu hỏi auth. (Khác M2 Q26: subagent đúng khi context **đã** xuống cấp và mỗi subagent nhận **1 câu hỏi cụ thể**) 🔁 | 2.5 |

**Câu đúng** (bạn không chắc câu nào => giải thích hết)

| Câu | Vì sao đáp án đúng thắng |
|---|---|
| Q1 (Code Review managed qua GitHub App, 18 findings / PR, 3 loại nhiễu) | ✅ A **REVIEW.md** ở gốc repo: luật bỏ qua (lint đã có CI, `src/gen/`) + finding về rendering phải **chỉ ra dòng cụ thể** sai. Review chạy qua **GitHub App**, không qua workflow => B, D (sửa workflow file) không tác động. C CLAUDE.md = context chung cho mọi việc, không phải luật riêng của review (mục 4.6) |
| Q4 (truy cập dữ liệu Jira **chuẩn**) | ✅ A dùng **MCP server Jira có sẵn**. Mục 3.4: tích hợp chuẩn => community server; tự viết (C) chỉ cho workflow **riêng** của team. B curl = tự lo auth + parse. D export markdown = cũ ngay |
| Q5 (tìm mọi `eval(`) | ✅ D **Grep** = nội dung. A Glob `*eval*` = tìm **tên file** có chữ eval. B `ls -R` cũng chỉ liệt kê **tên** file |
| Q7 (prompt "chỉ báo lỗi chắc chắn, bỏ qua cái không chắc" => bug thật bị giấu) | ✅ D báo **tất cả** kèm confidence + severity, lọc ở bước sau. Bỏ đúng **câu gây giấu lỗi** mà vẫn giữ output có tag. A pass 2 cùng prompt = cùng bị giấu. B thinking: model **đã** điều tra rồi, vấn đề là lời dặn "đừng báo". C bỏ hết severity = mất tag |
| Q8 (giới hạn số lượt + số tiền, do **Claude Code tự** chặn) | ✅ B `--max-turns 10 --max-budget-usd 2.00`. D `timeout-minutes` = **runner** chặn, không giới hạn tiền. C model rẻ = không có giới hạn cứng. A `dontAsk` = chuyện **quyền**, không phải giới hạn |
| Q9 (55% test sinh ra vô giá trị, giảm **ngay từ đầu**) | ✅ A ghi chuẩn test + fixture + ví dụ test tốt / test vô nghĩa vào **CLAUDE.md** (mục 4.6). C, D = lọc **sau** khi đã sinh. B = né vấn đề |
| Q10 (35% false positive theo pattern; muốn model **tổng quát hóa** cho code chưa gặp) | ✅ C **few-shot** có chú thích: ví dụ dạy **cách phán đoán** => áp được cho pattern mới (mục 5.2). A spec dài = chỉ phủ case đã liệt kê. D "be conservative" = vô dụng (luật vàng 10). B keyword filter = dễ vỡ |
| Q12 (nửa số finding bị bỏ qua vì vụn vặt; "**before adding infrastructure**") | ✅ A **tiêu chí rõ**: báo gì (bug, security) / bỏ gì (style nhỏ, pattern local). B tự chấm 1-10 = không calibrate (luật vàng 6). C "highly confident" = mơ hồ. D classifier = **hạ tầng**, đề đã loại |
| Q13 (30% false positive do convention riêng; "**persistent context on every review**") | ✅ C ghi convention vào **CLAUDE.md**. "Ngăn ngay từ đầu" + "context mọi lần review" => CLAUDE.md. A, B = lọc sau. D bỏ context xung quanh = càng hiểu sai |
| Q14 (CI khởi động 18 giây vì auto-discovery; vẫn cần chuẩn trong root CLAUDE.md) | ✅ B `--bare` (bỏ auto-discovery) + `--append-system-prompt-file ./CLAUDE.md` (**thêm** chuẩn team). A `--system-prompt-file` = **thay** prompt mặc định (= bài M2 Q47). C chép tiêu chí vào `-p` = 2 nơi, dễ lệch nhau. D không giảm thời gian khởi động |

**Bài học thêm từ M3**
- Q1 vs Q13 vs Q9: rule **chỉ cho review** của Code Review managed => **REVIEW.md**. Convention / chuẩn test dùng cho **mọi** việc (cả `/code-review` local) => **CLAUDE.md**.
- Q3, Q6 (+ M2 Q33, câu mẫu Q12): 1 prompt / 1 call ôm quá nhiều => **chia nhỏ** rồi gộp. Không sửa bằng cách nhồi thêm vào cùng prompt hay đổi format.
- Q14 = M2 Q47: `--system-prompt*` **thay**, `--append-system-prompt*` **thêm**. Bạn làm đúng lần này.
- Q7 vs Q12 vs Q10: "chỉ báo cái chắc chắn" giấu bug (Q7) => báo hết + tag + lọc sau. Nhiều finding vụn (Q12) => tiêu chí rõ báo / bỏ. False positive cần **tổng quát hóa** (Q10) => few-shot.

**Nhận xét chung**: 10/14 = 71%, cao hơn M1 (65%) và M2 (62%), nhưng chỉ 14 câu nên **chưa đủ** để kết luận. Bạn làm tốt nhóm "viết prompt cho review" (tiêu chí, few-shot, CLAUDE.md, flag CLI). Sai do: route theo keyword (Q2), nhồi thêm vào 1 prompt (Q3), đổi format thay vì chia nhỏ (Q6), chia subagent theo service thay vì đi theo luồng (Q11). Xem bảng 🔁 dòng 11, 13.

#### [M4] Làm lại bộ 1 (cùng đề M1, thứ tự câu khác) - 60 câu (2026-11-22): **46/60 = 76.7%**

Sai 11: 18, 21, 22, 26, 32, 42, 46, 52, 56, 57, 60. **Bỏ trống** 3 (không quyết được): 29, 35, 54. Đánh dấu "không chắc" 24 câu: 13 đúng, 10 sai, 1 bỏ trống. Q40 bạn chọn đúng **key của site**, nhưng key đó **sai logic** (⚠️ M1 Q46) => tính theo guide là **45/60 = 75%**. Lần đầu (M1): 39/60. ⚠️ Làm lại cùng đề nên điểm có thể **cao hơn thực lực** (nhớ đáp án).

**So với lần 1 (M1)**
- ✅ Đã sửa được (M1 sai, giờ đúng): max_turns guarantee (Q6), `discover_and_analyze` (Q37), goals + quality criteria (Q13), khách bực nhưng làm được (Q19), "real person NOW" (Q20), 40+ field (Q49), decision tree (Q8), gộp tool trùng (Q11), lớp issue data riêng (Q4), session mới + summary (Q33), `/memory` (Q15), JSON-RPC (Q28), structured error (Q41), instructive error (Q12).
- 🔁 **Sai cả 2 lần** (cùng 1 câu): Q18 (= M1 Q52), Q21 (= M1 Q25), Q26 (= M1 Q33), Q32 (= M1 Q44), Q42 (= M1 Q21), Q60 (= M1 Q14). Bỏ trống 2 câu M1 cũng sai: Q29 (= M1 Q20), Q35 (= M1 Q54).
- ⬇️ **Lần 1 đúng, lần này sai / bỏ trống**: Q54 (= M1 Q27), Q56 (= M1 Q59), Q57 (= M1 Q60). Có thể do đổi ý khi phân vân => tin luật trong notes hơn là cảm giác.

**Câu sai (11)**

| Câu | Tình huống (rút gọn) | Bạn chọn | ✅ Đúng | Vì sao | Guide |
|---|---|---|---|---|---|
| Q18 🔁 | hoàn tiền > $500 phải quản lý duyệt, **không lách được** | PreToolUse hook gắn flag `requires_approval`, tool đọc flag | **tool tự enforce**: < $500 trả luôn, > $500 tạo yêu cầu duyệt + trả "pending" | luật nằm **ngay chỗ chi tiền**. Hook + flag = 2 mảnh phải khớp nhau (tool vẫn phải tự kiểm flag). Tool tự làm = 1 chỗ, không phụ thuộc gì (🔁 dòng 6) | 1.4, 2.3 |
| Q21 🔁 | IaC: `/terraform`, `/kubernetes`, `/pipelines`; chỉ load rule hợp **loại file** đang sửa | `@import` trong root CLAUDE.md | **`.claude/rules/` + `paths: ["terraform/**/*"]`** | có **pattern đường dẫn** => rules + `paths:`. `@import` vẫn load **luôn** (không tiết kiệm token). Ngược với Q29 (🔁 dòng 4) | 3.3 |
| Q22 | xác minh danh tính nhiều bước; tới câu thứ 3 agent hỏi lại tên như chưa từng nói | tool xác minh xóa state của agent | **không gửi lịch sử hội thoại** ở request sau | API **stateless**: mỗi request phải gửi **đủ lịch sử** (mục 6.1). Tool không xóa được "trí nhớ" của model; không có giới hạn "2 lượt" | 5.1 |
| Q26 🔁 | lợi ích chính của JSON có field so với text | "model xử lý JSON **deterministic**" | **agent lấy giá trị chắc chắn, không phải parse text** | model **không bao giờ** deterministic (🔁 dòng 15) | 5.3 |
| Q32 🔁 | 1 tool `analyze_document` + lệnh tự do => format lung tung, 35% phải hỏi lại | viết description + ví dụ | **tách 3 tool có contract** (extract / summarize / verify) | 1 tool làm **nhiều việc** => tách (ví dụ nguyên văn guide). Description hay đến mấy, 1 tool vẫn phải đoán output nào (🔁 dòng 5) | 2.1 |
| Q42 🔁 | MCP server có **MCP prompts** (template) ngoài tools | vào tool registry, model tự gọi | **slash command** user tự chạy | tool = model gọi, resource = dữ liệu đọc (`@`), **prompt = template user chạy** (🔁 dòng 14) | (MCP thật) |
| Q46 | thêm 1 điều kiện kiểm tra ngày vào **1 hàm, 1 file** | plan mode phân tích ảnh hưởng tới luồng đặt chỗ | **direct execution** | việc **nhỏ, rõ, 1 file** => direct (mục 4.4). Đề không nói gì về ảnh hưởng rộng => đừng tự thêm độ phức tạp | 3.4 |
| Q52 | xác nhận đăng bài "Confirm?": 98% bấm trong 2 giây, vẫn đăng sai tài khoản / giờ / nội dung | bắt user **gõ câu xác nhận** | **hiện đủ** nội dung bài, tài khoản, giờ đăng, nền tảng trong câu xác nhận | user sai vì **không thấy** mình đang xác nhận cái gì. Gõ chữ / chờ thêm = thêm phiền, vẫn không thấy thông tin. Tự duyệt = bỏ luôn bước kiểm | (thiết kế human-in-the-loop) |
| Q56 ⬇️ | user nói "xóa backup cũ" => agent gọi `delete_file`, policy bắt archive; description chỉ "Archives a file" / "Deletes a file" | validation phía server chặn delete backup | **mở rộng description** (khi nào dùng, "không dùng cho backup") | đề hỏi cách cải thiện **chọn tool** "most directly" => description (gốc lỗi). Validation = chặn sau khi đã chọn sai (lần 1 bạn làm đúng) | 2.1 |
| Q57 ⬇️ | `get_neighborhood_info(address)` luôn phải gọi `get_property_details` trước chỉ để lấy address | gộp thành 1 tool trả cả 2 | **cho `get_neighborhood_info` nhận `property_id`**, tự tra address bên trong | bỏ chuỗi phụ thuộc, mỗi tool vẫn 1 việc. Gộp = tool to, trả thừa dữ liệu khi chỉ cần 1 phần (lần 1 bạn làm đúng) | 2.1 |
| Q60 🔁 | `control_device` timeout, agent chỉ nói "device không phản hồi" | lỗi kỹ thuật: device ID, thời gian timeout, mã API (để debug) | **isError + nguyên nhân có thể + bước khắc phục** để agent nói với user | đề cần agent **giúp user bước tiếp** => thông tin cho user, không phải cho dev. (Lần 1 bạn chọn "Device offline + tool riêng", cũng sai) (🔁 dòng 3) | 2.2 |

**Câu bỏ trống (3)**

| Câu | Tình huống | ✅ Đúng | Vì sao |
|---|---|---|---|
| Q29 | monorepo 15 package, 3 chuẩn, **không** có pattern tên package, maintainer tự biết package mình cần gì | **`@import` trong CLAUDE.md từng package** đúng chuẩn liên quan | **không** có pattern để viết `paths:` + đề nói maintainer tự cấu hình => `@import`. A (rules + liệt kê từng thư mục) = phải sửa rule mỗi lần thêm package. Đây là **cặp đôi** với Q21 |
| Q35 | 35 lượt, 50K token; 94% câu hỏi chỉ cần 3-5 lượt gần, 6% còn lại khách dễ nói lại | **sliding window**: giữ system prompt + 8-10 lượt mới nhất, cần chi tiết cũ thì nhờ khách nói lại | số liệu đề chỉ thẳng đáp án (mục 6.1 "Sliding window"). Caching không làm context nhỏ đi. Retrieval / progressive summary = phức tạp hơn mức cần khi 94% chỉ cần vài lượt gần |
| Q54 | refund (amount + reason), cancel (reason), reship (address), chung `order_id`; 1 tool gộp => thiếu / thừa tham số | **tách 3 tool**, mỗi tool chỉ có tham số của nó | **bộ tham số khác nhau** => tách (lần 1 bạn làm đúng). if-then-else schema / object lồng = vẫn bắt model đoán. Few-shot + mọi field optional = không ép được |

**Câu đúng nhưng bạn đánh dấu không chắc (13)**

| Câu | Vì sao đáp án đúng thắng |
|---|---|
| Q4 (3 vấn đề trong 1 session, hỏi lại refund) | ✅ trích **dữ liệu từng issue có cấu trúc** (ID, số tiền, status) vào lớp context riêng. Văn xuôi mất số; sliding window 30 lượt làm mất issue đầu (khác Q35: ở đây dữ liệu cũ **cần giữ**) |
| Q6 (hết max_turns giữa chừng, phải **bảo đảm** kết thúc = xong hoặc chuyển người) | ✅ **code kiểm tra sau khi loop dừng**, chưa xong thì code gọi `escalate_to_human`. Prompt = xác suất; 80% max_turns = ngưỡng tùy ý; chia 2 agent = vẫn có thể hết lượt |
| Q8 (sau `lookup_order` 45 ngày, chọn refund hay escalate thế nào) | ✅ kết quả tool vào hội thoại, **model tự suy luận**. Không có decision tree hay kế hoạch cố định trong agentic loop |
| Q9 (30% file sai format dù CLAUDE.md đã dặn) | ✅ **PostToolUse hook** `Edit\|Write` chạy Prettier = chắc chắn. Stop hook + prompt = model chấm (xác suất); rules / skill = vẫn là lời dặn |
| Q11 (4 => 10 tool, sai vì tool **trùng nghĩa**) | ✅ **gộp** tool trùng (`resolve_compensation`, `include_tracking`). Tách subagent vẫn để 2 tool trùng chung 1 agent; few-shot không bỏ được chỗ trùng |
| Q19 (khách bực "muốn người giúp được", việc **làm được ngay**) | ✅ ghi nhận bực + nói làm được ngay + **đề nghị làm hoặc escalate**. Khác Q20: chưa **đòi người rõ ràng** |
| Q28 (MCP: thiếu param / 404 / 503) | ✅ (1) thiếu param = **JSON-RPC protocol error** (request hỏng, chưa tới tool); (2) + (3) = tool result `isError` (tool chạy mà lỗi) |
| Q31 (hỏi 3 câu làm rõ => 40% bỏ cuộc) | ✅ **tự giả định hợp lý, nói rõ giả định, mời sửa**. Hỏi 1 câu / lượt vẫn chậm; classifier = hạ tầng thừa; lookup table không nói giả định = dễ sai mà user không biết |
| Q33 (khách quay lại sau 4h, tool result "PENDING" cũ) | ✅ **session mới + structured summary + gọi tool mới trước**. Resume thì câu trả lời cũ của assistant vẫn nhắc dữ liệu cũ |
| Q37 (curation 18+ call, cần **thấy hết** ứng viên để chọn) | ✅ tool gộp `discover_and_analyze` trả hết ứng viên + điểm, `add_to_collection` để riêng. Rule cố định / curate tự động = lấy mất quyền chọn của model |
| Q40 ⚠️ (timeout, không biết đã gửi chưa => gửi trùng) | Site chấm A (`retry_safe: true`) là đúng, bạn chọn A. Nhưng theo logic: báo "retry an toàn" => gửi trùng **thêm**. Nên là **B**: "status unknown, có thể đã gửi, **đừng retry**". Thi thật gặp câu kiểu này => chọn B |
| Q45 (metadata nguồn mất khi tóm tắt) | ✅ mỗi agent trả **structured data**: nội dung tách riêng khỏi metadata nguồn (URL, tên tài liệu, số trang) = claim-source mapping. Cite inline trong văn xuôi vẫn dễ mất khi tóm tắt tiếp |
| Q55 (confidence ML: 23% sai vẫn đi tiếp, 31% đúng vẫn đưa người xem) | ✅ trả field + confidence + **`request_review` tính bằng ngưỡng đã test** trong code + lý do. Để model tự đọc điểm thô = đang hỏng; điểm tổng = che field kém |

**Bài học thêm từ M4**
- **Cặp Q21 / Q29** (sai + bỏ trống): cùng 1 câu hỏi "load đúng chuẩn cho đúng chỗ", khác ở **có pattern đường dẫn hay không**. Có => rules + `paths:`. Không, người phụ trách tự biết => `@import` từng package.
- **Tool design** (Q32, Q54, Q56, Q57, Q11): 1 tool nhiều việc / nhiều bộ tham số => **tách**. 2 tool trùng nghĩa => **gộp**. Description sơ sài => **viết lại**. Tool B phụ thuộc tool A chỉ để lấy 1 field => **B nhận ID tự tra**.
- **Q52 (mới)**: xác nhận mà ai cũng bấm trong 2 giây => vấn đề là **thiếu thông tin** trong câu xác nhận, không phải thiếu "rào cản".
- **Câu làm lại vẫn sai**: 6/11 câu sai là câu **đã sai ở M1** và đã có trong notes / 🔁. Ôn bảng 🔁 trước khi thi là việc **lợi nhất** lúc này.

**Nhận xét chung**: 46/60 (theo guide 45/60), tăng từ 39/60 nhưng là đề **làm lại**. Mạnh lên rõ ở D1 agent loop / escalation (Q6, Q8, Q19, Q20) và D5 context. Còn yếu: **D3 cấu hình Claude Code** (Q21, Q29, Q42, Q46), **D2 tool design** (Q32, Q54, Q56, Q57), **D2 error cho user** (Q60). Xem bảng 🔁 dòng 3, 4, 5, 6, 14, 15.

#### [M5] Làm lại bộ 2 (cùng đề M2, thứ tự câu khác) - 60 câu (2026-11-24): **36/60 = 60%**

Sai 21: 1, 4, 6, 9, 12, 21, 22, 23, 24, 26, 29, 32, 34, 35, 41, 45, 46, 47, 50, 51, 53. **Bỏ trống** 3: 11, 15, 42. Đánh dấu 28. Q23 bạn chọn đúng **theo guide** (site sai, ⚠️) => tính theo guide **37/60 = 62%**. Lần đầu (M2): 37/60 (38 theo guide) => làm lại **không tăng**.

**So với lần 1 (M2)**
- ✅ Đã sửa được 9: scratchpad (Q2), prompt chaining (Q5), enum + "other" (Q14), Read + Write (Q16), review agentic (Q19), Grep import (Q31), few-shot đo lường (Q43), few-shot materials (Q49), `permissions.deny` (Q55).
- 🔁 **Cùng đáp án sai y như lần 1** (9 câu): Q1, Q4, Q6, Q24, Q32, Q41, Q45, Q46, Q51. Sai lần 2 nhưng chọn đáp án sai khác: Q21, Q26, Q34, Q50.
- ⬇️ **Lần 1 đúng, lần này sai / bỏ trống** (10 câu): Q9, Q12, Q22, Q29, Q35, Q47, Q53 sai; Q11, Q15, Q42 bỏ trống.
- 6 câu **không đánh dấu mà vẫn sai** (tưởng chắc): Q1, Q12, Q26, Q45, Q46, Q51 => nguy hiểm nhất, vì lúc thi bạn sẽ không xem lại.

**Câu sai (21)**

| Câu | Tình huống (rút gọn) | Bạn chọn | ✅ Đúng | Vì sao | Guide |
|---|---|---|---|---|---|
| Q1 🔁 | làm cache Redis, **mới** với cache production | plan mode đọc code `/products` (y như M2) | **để Claude phỏng vấn bạn** trước | thiếu **yêu cầu**, không thiếu hiểu code. Plan mode đọc code, không hỏi được "invalidation thế nào?" (🔁 dòng 12, 16) | 3.5 |
| Q4 🔁 | migration script sai với `null` | mô tả lỗi + viết lại cả script (y như M2) | **test case** input có null + output mong muốn | test case rõ nhất, không phá phần đang đúng (🔁 dòng 12) | 3.5 |
| Q6 🔁 | lỗi 500 lúc có lúc không, 200+ file, chưa biết ở đâu | lập kế hoạch đầy đủ trước (y như M2) | **dynamic**: vừa tìm vừa đổi kế hoạch | việc **mở** => không lập kế hoạch đầy đủ được (🔁 dòng 8) | 1.6 |
| Q9 ⬇️ | 3 MCP server (git, Jira, docs), 1 yêu cầu dùng cả 3 | agent tự chọn 1 server hợp nhất, chỉ load tool server đó | **tool của mọi server discover lúc connect, dùng cùng lúc** | mục 3.4 nguyên văn. Lần 1 bạn làm đúng | 2.4 |
| Q12 ⬇️ | bug production, **stack trace rõ** chỉ tới 1 hàm, module lạ | plan mode phân tích + liệt kê nguyên nhân | **direct execution**: đọc stack trace, đọc code, sửa | bug rõ, 1 chỗ => direct. "Module lạ" không làm việc thành to (🔁 dòng 16) | 3.4 |
| Q21 🔁 | logic cache 15 file, cần hiểu trước khi thêm trigger | Grep "invalidate" / "expire", đọc vài dòng quanh đó | **import + class hierarchy => base class => trace từng chỗ invalidation** | đọc vài dòng lẻ = không hiểu **interface** chung. Phải đi từ class gốc (🔁 dòng 11) | 2.5 |
| Q22 ⬇️ | khám phá rendering 25 phút, bắt đầu trả lời "typical patterns", giờ hỏi physics | spawn subagent physics **độc lập**, rồi tự gộp | **tóm tắt findings rendering, spawn subagent physics kèm summary đó** | câu hỏi là physics **gắn với** rendering => subagent cần biết rendering. Subagent độc lập không có context đó (🔁 dòng 10) | 5.4 |
| Q23 ⚠️ | 3 lỗi format PDF **ảnh hưởng nhau** | gửi cả 3 trong 1 message | site: sửa lần lượt | **bạn đúng theo guide** (lỗi ảnh hưởng nhau => 1 message). Xem ⚠️ | 3.5 |
| Q24 🔁 | 12 tiền lệ phân tích tuần tự, muốn nhanh mà coordinator vẫn theo dõi được | subagent phân tích tự spawn con (y như M2) | **coordinator spawn nhiều subagent song song** | mọi thứ đi **qua coordinator** => mới theo dõi / debug được (🔁 dòng 19) | 1.2 |
| Q26 🔁 | agent dùng Grep thay vì `analyze_dependencies` ("Analyzes dependency graph") | thêm lời dặn route vào system prompt | **viết description MCP tool chi tiết** | gốc = description sơ sài. Lời dặn route = vá ngoài, không sửa gốc (lần 1 bạn chọn tách tool) (🔁 dòng 5) | 2.1 |
| Q29 ⬇️ | coordinator gọi web search rồi chờ, rồi mới gọi document analysis, 2 việc độc lập | lớp async **bên ngoài** agent, chạy nhiều cặp coordinator-subagent | coordinator gọi **2 Task trong 1 response** | song song có sẵn trong agent loop, không cần hạ tầng ngoài. Lần 1 bạn làm đúng (🔁 dòng 19) | 1.2, 1.3 |
| Q32 🔁 | reviewer xem được 5%, chọn cái nào | random 5% (y như M2) | **confidence thấp / tài liệu mơ hồ, mâu thuẫn** | random = để **đo**, không để **chọn** (🔁 dòng 17) | 5.5 |
| Q34 🔁 | checklist review 8 mục, team dùng Claude cho nhiều việc khác | **subagent review riêng** (lần 1 chọn CLAUDE.md) | **slash command `/review`** | chỉ cần **nạp checklist khi review**. Subagent = nặng hơn mức cần; CLAUDE.md = luôn load (🔁 dòng 4) | 3.2 |
| Q35 ⬇️ | tài liệu 175-190K token, tool definition 2.500 token, context 200K, sót 1/3 cuối | "vượt effective attention span dù chưa tới giới hạn" | **tool definition chiếm context, tổng gần 200K** | đề cho số để bạn **cộng**: 190K + 2,5K + system prompt ≈ 200K. "Attention span" = chữ mơ hồ, không có số nào ủng hộ. Lần 1 bạn làm đúng | 5.1 |
| Q41 🔁 | batch 10.000, 300 cái lỗi `context_length_exceeded` | tăng `max_tokens` (y như M2) | **chunk 300 cái lỗi, gửi lại chỉ chúng** | lỗi do **input** dài; `max_tokens` = **output** (🔁 dòng 18) | 4.5 |
| Q45 🔁 | 12% fail Pydantic ("got '2 to 3'"), retry y nguyên ra y lỗi | tiền xử lý tài liệu (y như M2) | **gửi lại kèm lỗi validation** | retry **kèm lỗi cụ thể** sửa được lỗi format (🔁 dòng 18) | 4.4 |
| Q46 🔁 | gọi `lookup_citations` trước khi có DOI | forced `extract_metadata` **mọi** request (y như M2) | forced `extract_metadata` **request đầu**, enrichment lượt sau | forced mọi request => không bao giờ gọi được tool enrichment (🔁 dòng 18) | 2.3, 4.3 |
| Q47 ⬇️ | 12% lỗi semantic, reviewer xem 20% | xem hết tài liệu có **layout lạ** | **confidence từng field + calibrate bằng labeled set** | lỗi semantic không gắn với layout. Lần 1 bạn làm đúng (🔁 dòng 17) | 5.5 |
| Q50 🔁 | đọc 8/45 file thì quên dần pattern | đổi sang Grep tên hàm thay vì đọc cả file | **subagent cho câu hỏi cụ thể**, main agent giữ bức tranh lớn | ví dụ **nguyên văn** guide. Grep bớt token nhưng không sửa việc context **đã** xuống cấp (lần 1 bạn chọn clear + report) (🔁 dòng 10) | 5.4 |
| Q51 🔁 | 2024: 35% vs 2021: 18% bị coi là mâu thuẫn | tin số mới nhất (y như M2) | **subagent ghi ngày** trong structured output | không có ngày => không biết là xu hướng (🔁 dòng 19) | 5.6 |
| Q53 ⬇️ | tài chính / tin tức / patent bị ép hết thành bullet | thêm **lớp chuyển đổi** về 1 format chung | synthesis **render theo loại** (tài chính = bảng, tin = văn xuôi) | format chung = lại ép mọi thứ về 1 dạng, đúng cái đang hỏng. Lần 1 bạn làm đúng (🔁 dòng 19) | 5.6 |

**Câu bỏ trống (3)** (cả 3 lần đầu bạn đều làm **đúng**)

| Câu | Tình huống | ✅ Đúng | Vì sao |
|---|---|---|---|
| Q11 | session hôm qua còn dùng được, 3/12 file vừa bị sửa | **resume + báo agent đúng 3 file đã đổi** để đọc lại | giữ context 9 file còn đúng, chỉ cập nhật 3 file. Session mới = mất hết; đọc lại 12 = thừa; không báo = dùng thông tin cũ. (Site gộp 2 đáp án B, C thành 1 dòng) |
| Q15 | `skills: string[]`: "Python and SQL" lúc gộp lúc tách, thêm skill không nêu, độ dài 5-10 vs 40+ | **few-shot** chỉ cách tách, tiêu chí "nêu rõ", độ chi tiết | cả 3 vấn đề là "**làm không nhất quán**" => ví dụ dạy được cả 3. Giới hạn 10-20 = số tùy ý (🔁 dòng 9) |
| Q42 | thêm test cho code cũ 200 file, không nói ưu tiên | **Glob / Grep vẽ cấu trúc, ưu tiên module quan trọng, sửa kế hoạch khi gặp phụ thuộc** | việc mở => dynamic (🔁 dòng 8). Đọc hết 200 file trước / lịch cố định = sai cùng kiểu Q6 |

**Câu đúng bạn đánh dấu không chắc (10)**: Q2 scratchpad, Q8 schema + quy tắc chuẩn hóa, Q13 stratified sampling hằng tuần, Q16 Read + Write, Q19 review agentic, Q52 coordinator tự quyết, Q55 `permissions.deny` + CLAUDE.md + hook, Q56 tìm mọi tên export rồi Grep, Q58 resume + báo hàm bị đổi tên, Q59 tool + schema. Lý do từng câu: xem bảng "câu đúng" của M2 (cùng đề).

**Bài học thêm từ M5**
- **Đọc lại notes chưa đủ**: 9 câu chọn **y nguyên** đáp án sai lần trước dù notes đã ghi đáp án đúng. Cần **tự kiểm tra** (che đáp án, tự trả lời, rồi mới xem) thay vì đọc lướt.
- **Đổi ý làm mất điểm**: 10 câu lần 1 đúng, lần này sai / bỏ trống. Khi phân vân giữa 2 đáp án => dùng **luật trong 🔁**, đừng chọn đáp án "nghe đầy đủ hơn".
- **Plan mode / hạ tầng thêm** là bẫy hay mắc: Q1, Q12 (plan mode), Q29 (lớp async ngoài), Q53 (lớp chuyển đổi), Q34 (subagent riêng). Đề mà việc **nhỏ / đã có cơ chế sẵn** => chọn cách **đơn giản nhất** sửa đúng gốc (luật vàng 2).

**Nhận xét chung**: 36/60 (37 theo guide), **không tăng** so với lần 1 dù là đề làm lại => cách ôn hiện tại (đọc notes) chưa hiệu quả. Yếu nhất: **D5 context + human review** (Q22, Q32, Q47, Q50), **D4 xử lý lỗi extraction** (Q41, Q45, Q46), **D1 multi-agent** (Q6, Q24, Q29, Q51, Q53), **D3 plan mode / iterative** (Q1, Q4, Q12, Q34). Xem bảng 🔁 dòng 16-19 (mới) và 8, 10, 12.

#### [M6] Site luyện thi khác (nguồn #8 mục 9, nhiều câu trùng bộ 1, 2) (2026-11-24): **48/60 = 80%** (theo guide 50/60 = 83%)

60 câu, làm trong 33:37 (giới hạn 120 phút). Điểm, đáp án bạn chọn, câu đánh dấu: đọc lại từ **lưu trữ trình duyệt** của site (không có tài khoản). Theo domain (cách site chia domain, có thể khác guide): D1 12/16, D2 9/11, D3 9/12, D4 10/12, D5 8/9. Sai 12 (site): Q4 (playlist), Q8, Q11, Q15, Q17, Q20, Q22, Q27, Q30, Q32, Q50, Q53. Q20, Q32 bạn chọn **đúng theo guide** (site sai, ⚠️) => **sai 10 theo guide**. Đánh dấu: 9 câu đúng + 8 câu sai (Q8, Q15, Q20, Q22, Q27, Q30, Q32, Q53).

**Điểm chính**
- 🔴 **Sai lần 3, cùng 1 kiểu đáp án**: Q11 (forced **mọi** call, = M2 Q51, M5 Q46), Q17 (tin số mới nhất, = M2 Q22, M5 Q51). Render theo loại: M5 Q53 + M6 Q27, Q30 (câu này xuất hiện 2 lần trong đề, sai cả 2).
- 4 câu **không đánh dấu mà vẫn sai** (tưởng chắc): Q4 (playlist), Q11, Q17, Q50 => nguy hiểm nhất.
- Đề **trùng nhiều câu** với bộ 2 => sai lại = chưa nhớ **luật**, không phải gặp câu lạ.

**Câu sai (12)**

| Câu | Tình huống (rút gọn) | Bạn chọn | ✅ Đúng | Vì sao | Guide |
|---|---|---|---|---|---|
| Q4 🔁 | app chọn nhạc nhiều lượt; user nói thích jazz, 2 lượt sau Claude hỏi lại thích thể loại gì | vượt context window | **app không gửi tin cũ trong `messages`** | 2 lượt không thể đầy context. API **stateless** (= M4 Q22) (🔁 dòng 20) | 5.1 |
| Q8 🔁 | review PR 1 call, chỉ diff + file đổi; sót caller ở file **không đổi** (đổi thứ tự tham số); lỗi xuyên file = 35% incident; review chạy async | pass song song từng file + dependents trực tiếp, rồi 1 call tóm tắt gộp | **review agentic giới hạn lượt**: model tự Read / search codebase, đi theo reference | thiếu **context**, không phải thiếu suy luận. Danh sách dependents tĩnh sót reference nhiều tầng / động. Async => chịu được chậm; giới hạn lượt => chặn chi phí (= M2 Q33) (🔁 dòng 21) | 3.6, 4.6 |
| Q11 🔴 | `lookup_citations` chạy trước khi có DOI | `tool_choice` forced `extract_metadata` **mọi** call | forced `extract_metadata` **lượt đầu**, enrichment ở lượt sau | forced mọi call => `lookup_citations`, `verify_doi` **không bao giờ** chạy được. **Sai lần 3** (🔁 dòng 18) | 2.3, 4.3 |
| Q15 | (chọn 2) CI sinh unit test kém: chỉ assert "không throw", tự tạo patient record thay vì dùng fixture factory; muốn **bớt sinh** test kém | A (CLAUDE.md chuẩn test + ví dụ) ✅ + C (Claude pass 2 chấm điểm, xóa 1/3 kém nhất) | A + **D: liệt kê fixture factory + khi nào dùng, trong CLAUDE.md** | "**in the first place**" = sửa ở **nguồn**. Pass lọc sau = vẫn sinh test kém, tốn thêm call. Guide 3.6 nguyên văn: CLAUDE.md ghi testing standards + fixtures | 3.6 |
| Q17 🔴 | web search: 2024 35%, tài liệu nội bộ: 2022 18% => synthesis báo mâu thuẫn | tin số mới nhất, số cũ để phụ lục | **subagent ghi ngày** (xuất bản / thu thập) trong structured output | là **tăng trưởng**, không phải mâu thuẫn. Không có ngày thì synthesis không biết. **Sai lần 3** (🔁 dòng 19) | 5.6 |
| Q20 ⚠️ | PDF 3 lỗi ảnh hưởng nhau (cột, ngày, ngắt trang) | gửi cả 3 trong 1 message | site: sửa lần lượt, test mỗi bước | **bạn đúng theo guide 3.5** (= M2 Q42, M5 Q23). Xem ⚠️ | 3.5 |
| Q22 | auth library v2 => v3: `authenticate()` callback => Promise, đổi type `User`, bỏ 3 method; import ở 45 file nhiều module | bump version, chạy test, sửa từng lỗi | **plan mode**: khám phá chỗ dùng, vẽ code path, lập chiến lược rồi mới sửa | việc **to, nhiều module, breaking change** => plan mode. Bạn sửa quá tay sau 🔁 16 (chiều ngược: Q26 stack trace => direct, bạn làm đúng) | 3.4 |
| Q27 🔁 | tài chính JSON / tin tức văn xuôi / patent list bị ép hết thành bullet | chuẩn hóa mọi output thành văn xuôi | synthesis **render theo loại** (bảng / văn xuôi / list) | văn xuôi cho tất cả = **lại 1 format chung**, đúng cái đang hỏng (🔁 dòng 19) | 5.6 |
| Q30 🔁 | y hệt Q27 (câu lặp trong cùng đề) | văn xuôi + inline citation | render theo loại | như Q27 | 5.6 |
| Q32 ⚠️ | batch rẻ 50%, tới 24h; SLA 30h, 99.9% | gửi batch mỗi **4h** | site: mỗi 6h | **bạn đúng theo guide 4.5** (ví dụ nguyên văn "4-hour windows"). Xem ⚠️ | 4.5 |
| Q50 🔁 | 12% lỗi semantic qua được schema, người xem được 20% | xem tài liệu **layout lạ** (y như M5 Q47) | **confidence từng field + calibrate bằng labeled set** | layout không báo trước field nào sai; confidence thấp mới báo (🔁 dòng 17) | 5.5 |
| Q53 🔁 | sliding window 25 cặp, user bị quên chủ đề / sở thích cũ | tăng lên 50 cặp | **hybrid**: tóm tắt tin cũ + giữ tin mới nguyên văn | window to hơn = vẫn mất, chỉ mất **muộn hơn** ("làm to hơn", 🔁 dòng 9, 20) | 5.1 |

**Câu đúng bạn đánh dấu không chắc (9)**

| Câu | Tình huống | ✅ Đúng | Nhớ |
|---|---|---|---|
| Q2 | khách quay lại sau 4h, session 32 lượt có `lookup_order` "PENDING" cũ; resume thì agent cứ nhắc dữ liệu cũ dù đã gọi tool mới | **session mới + structured summary + gọi tool mới trước** | tool result cũ **sai** và model cứ nhắc => bỏ session cũ (= M4 Q33) |
| Q19 | 7 tool, accuracy 86% => 71%, nhầm `issue_credit` / `process_refund`, `check_delivery_status` / `lookup_order` | **gộp** tool trùng nghĩa (tham số `action`, cờ `include_tracking`) | trùng nghĩa => gộp (🔁 dòng 5) |
| Q25 | 50.000 hợp đồng, 2 tuần, 82% pass lần đầu | batch tất cả, rồi batch lại **chỉ cái fail**, sửa prompt giữa các lượt | gửi lại chỉ cái lỗi (🔁 dòng 18) |
| Q26 | bug production, stack trace rõ, module lạ | **direct execution** | cặp với Q22 (🔁 dòng 16) |
| Q28 | `remove_team_member(dry_run)`, 15% gọi thẳng `dry_run=false` | 2 tool: `preview_remove_member` trả **token dùng 1 lần**, `execute_remove_member` bắt buộc token đó | ép bằng **cấu trúc**, không bằng prompt (luật vàng 1) |
| Q37 | retry kèm lỗi, lúc nào **ít** hiệu quả nhất | "et al." khi danh sách tác giả đầy đủ nằm ở tài liệu **khác**, không có trong input | retry không tạo ra thông tin không có |
| Q40 | 90 phút, summary biến "$184.60, roaming 3/3, hứa trước 10/5" thành "khách khiếu nại roaming" | **case facts block** (số tiền, ngày, ID) gửi kèm mọi prompt | số liệu không đem đi tóm tắt (cặp với Q53) |
| Q44 | 1 tool `analyze_document` + instruction tự do, 35% phải hỏi lại | **tách** thành `extract_data_points`, `summarize_content`, `verify_claim_against_source`, input / output rõ | 1 tool nhiều việc => tách (cặp với Q19) |
| Q46 | subagent đọc 47 file, mất kết nối, teammate đổi tên 2 hàm | **resume** subagent + báo 2 hàm đổi tên | context cũ **phần lớn còn đúng** => resume + báo phần đổi (cặp với "khách quay lại") |

**Cặp trong cùng đề (nhớ theo cặp)**

| Tình huống A | Tình huống B | Luật |
|---|---|---|
| Q26 stack trace rõ => **direct** ✅ | Q22 library breaking change, 45 file => **plan mode** ❌ | plan mode chỉ khi việc to / nhiều module |
| Q46 2 hàm đổi tên => **resume + báo** ✅ | khách quay lại, `lookup_order` cũ => **session mới + summary + gọi tool mới** ✅ | phần lớn context còn đúng => resume. Tool result cũ sai và model cứ nhắc => session mới |
| Q19 tool trùng nghĩa => **gộp** ✅ | Q44 1 tool làm nhiều việc => **tách** ✅ | trùng => gộp; ôm nhiều việc => tách |
| Q53 quên chủ đề cũ => **hybrid summary** ❌ | Q40 summary mất $184.60 => **case facts block** ✅ | summary cho chủ đề / sở thích; case facts cho số tiền, ngày, ID |

**Bài học thêm từ M6**
- **3 bẫy lặp mãi**: forced `tool_choice` **mọi** call, "số **mới nhất** là đúng", "**1 format chung** cho mọi loại nội dung". Trước giờ thi đọc lại 🔁 dòng 18, 19.
- **Sửa quá tay** sau khi học 1 luật: học "plan mode khi không cần" xong thì Q22 (cần plan mode) lại chọn sửa dần. Luật nào cũng có **2 chiều** => hỏi "việc **to / nhiều module / breaking change**?" trước khi chọn.
- "**Thêm 1 bước / 1 call nữa** để lọc / gộp" (Q15 C, Q8 C) = bẫy "làm thêm". Đề nói "**in the first place**" / gốc lỗi là **thiếu context** => sửa ở nguồn (CLAUDE.md, cho tool đi tìm).

**Nhận xét chung**: 48/60 = 80% (50/60 = 83% theo guide), **lần đầu chạm mục tiêu 80%**. Nhưng đề trùng nhiều câu cũ => điểm có thể cao hơn thực lực. Câu sai giờ dồn vào 🔁 dòng 16-21 => ôn đúng mấy dòng này, tự che đáp án rồi trả lời.

#### [M7] Site nguồn #8, full mock (2026-11-24): **49/60 = 81.7%**

Chỉ còn điểm theo domain (D1 13/16, D2 10/11, D3 10/12, **D4 8/12**, D5 8/9), 31 câu đánh dấu, 46 phút. **Câu hỏi + đáp án mất**: tab kết quả đã đóng, site chỉ lưu điểm + lựa chọn trong trình duyệt, ngân hàng câu hỏi trên trang bị xóa nội dung. => Từ M8: làm mock **trong tab group của Claude**, xong thì để nguyên trang kết quả.

#### [M8] Site nguồn #8, full mock (2026-11-25): **53/60 = 88%**

40:23. D1 15/16, D2 9/11, D3 10/12, D4 10/12, **D5 9/9**. Multiple response 3/3. Sai 7: Q14, Q15, Q16, Q38, Q50, Q52, Q56. Đánh dấu 19 (13 đúng, 6 sai). Không đánh dấu mà vẫn sai: **Q50**. Đáp án site lần này **khớp guide** hết (không có ⚠️). Xu hướng: M6 80% => M7 82% => **M8 88%**.

**Câu sai (7)**

| Câu | Tình huống (rút gọn) | Bạn chọn | ✅ Đúng | Vì sao | Guide |
|---|---|---|---|---|---|
| Q14 🔁 | sliding window 25 cặp, quên chủ đề / sở thích cũ | tăng lên 50 cặp (y như M6 Q53) | **hybrid**: tóm tắt tin cũ + giữ tin mới nguyên văn | window to hơn = vẫn mất, chỉ mất muộn hơn (🔁 dòng 9, 20) | 5.1 |
| Q15 🔴 | đọc 8/45 file thì kém dần, chưa tìm hết test file / luồng thanh toán | summary report + **clear** context (y như M2 Q26) | **subagents cho câu hỏi cụ thể** ("find all test files", "trace refund flow"), main agent giữ tổng quan | clear = mất hiểu biết từ 8 file; 1 report thành nguồn duy nhất, nén mất chi tiết. **Sai lần 3** (🔁 dòng 10) | 5.4 |
| Q16 | MCP tool trả lỗi giống nhau (`isError` + "Operation failed"), agent retry / escalate / hỏi user lung tung | tạo tool **`analyze_error`** gọi sau mỗi lỗi | **structured error metadata** trong response: `errorCategory`, `isRetryable`, mô tả | guide 2.2 nguyên văn. Sửa **ở nguồn**; tool phân tích lỗi cũng chỉ thấy "Operation failed". Cùng bẫy "tool riêng" như M1 Q14 (🔁 dòng 3) | 2.2 |
| Q38 | tìm mọi chỗ gọi hàm trước khi xóa; wrapper đổi tên (`calculateTax` => `computeOrderTax`) | Grep file import library / wrapper rồi đọc từng file | **đọc library + wrapper lấy mọi tên được export, rồi Grep từng tên** | guide 2.5 nguyên văn. Cách của bạn chạy được nhưng vòng vèo, phải đọc tay mọi file import. M5 Q56 bạn làm đúng (🔁 dòng 11) | 2.5 |
| Q50 🔴 | 12% lỗi semantic ("30 minutes" vào field số lượng), người xem 20% | xem tài liệu **formatting anomalies** (y như M5, M6) | **confidence từng field + calibrate bằng labeled set** | **Sai lần 3, cả 3 lần không đánh dấu**. Cùng luật bạn làm **đúng** ở Q9, Q37 cùng đề => chỉ câu chuyện này lừa được bạn (🔁 dòng 17) | 5.5 |
| Q52 | analysis agent thấy **gap** (thiếu token refresh) nhưng search đã xong | **coordinator** tự dò output tìm dấu hiệu gap rồi **search lại** | **analysis báo gap** cho coordinator => search có mục tiêu **và chạy lại analysis tới khi đủ** | đọc **đuôi**: đáp án đúng có **vòng lặp đủ** (search + analysis lại + "until sufficient"), của bạn dừng ở search. Cùng ý Q55 bạn làm **đúng** (🔁 dòng 19, ⚠️ M1 Q16) | 1.2 |
| Q56 | review sản phẩm: "Great product!" bị bịa pros / cons; câu mỉa mai thì sentiment chọn bừa | pros / cons **optional** + thêm **"neutral"** và "unclear" | **cho phép mảng rỗng** + thêm **"unclear"** | sát nút. Bẫy = thêm **"neutral"** (mỉa mai không phải trung lập => thêm 1 ngăn sai). Mảng rỗng = nói rõ "không có". Chọn đáp án sửa **đúng 2 vấn đề**, không thêm gì | 4.3 |

**Câu đúng bạn đánh dấu không chắc (13)**

| Câu | Tình huống | ✅ Đúng |
|---|---|---|
| Q3 | bị trừ tiền 2 lần, "có cần gặp người thật không?", refund 1 call là xong | ghi nhận bực + **đề nghị refund ngay, để khách chọn** (khách nhắc lại đòi người => escalate) |
| Q8 | 150 / 20.000 lỗi `context_length_exceeded` | **chunk chỉ 150 cái**, gửi lại, gộp kết quả |
| Q9 | form thuế, người xem 8%, chữ viết tay sửa mâu thuẫn số in | field **confidence thấp (đã calibrate)** + nguồn **mâu thuẫn** => người xem |
| Q10 | escalate refund $847 (> $500), người nhận không đọc được transcript | **structured summary**: customer ID, nguyên nhân, số tiền, đề xuất |
| Q13 | stack trace rõ, module lạ | **direct execution** |
| Q21 | người mới, auth 800+ file | **Grep entry point**, đọc, đi theo import / function call |
| Q27 | amendment 30 => 45 ngày | schema giữ **nhiều giá trị + vị trí nguồn + ngày hiệu lực** |
| Q29, Q54 | `lookup_order` 40-48 field, agent lẫn hạn trả giữa các đơn | **cắt còn field cần cho việc trả hàng** trước khi vào context |
| Q30 | `skills: string[]` 3 kiểu không nhất quán | **few-shot** (cách tách cụm, tiêu chí "nêu rõ", độ chi tiết) |
| Q32 | chat tiệc tối 78K token: dị ứng tôm cua, 8 phần ăn, "bơ nhiệt độ phòng" = 68°F | **trích dữ kiện quan trọng** ra phần riêng (case facts) + tóm tắt chuyện chung + giữ lượt mới nguyên văn |
| Q37 | (chọn 2) chứng chỉ chất lượng, người xem 10% đang bốc ngẫu nhiên | **confidence từng field** + **calibrate ngưỡng bằng labeled set** |
| Q55 | analysis ghi "thiếu hạn kháng cáo" nhưng coordinator chuyển thẳng cho synthesis | **analysis báo gap** => search có mục tiêu => chạy lại analysis |

**Cặp trong cùng đề**
- Q52 ❌ vs Q55 ✅: cùng luật vòng lặp gap. Chọn đáp án có **vòng lặp đầy đủ qua coordinator**.
- Q50 ❌ vs Q9, Q37 ✅: cùng luật chọn cái đưa người xem. Chỉ câu chuyện "30 minutes" lừa được bạn => nhớ **câu chuyện**, không chỉ nhớ luật.
- Q32 ✅ vs Q14 ❌: hội thoại dài có **dữ kiện quan trọng** => trích ra + tóm tắt phần còn lại; mất sở thích cũ => hybrid summary. Không bao giờ chọn **window to hơn**.

**Bài học thêm từ M8**
- 2 câu sai **lần 3 với đúng đáp án sai cũ** (Q15, Q50): bạn **nhận ra câu** nhưng tay vẫn chọn đáp án quen. Lúc thi gặp câu chuyện quen => dừng 3 giây, nhớ lại flashcard 🔴, rồi mới chọn.
- "Tạo **tool mới** để xử lý vấn đề" (Q16 `analyze_error`) = bẫy "làm thêm". Sửa ở **chỗ sinh ra vấn đề** (response của chính tool).
- Đáp án có **thêm 1 thứ không được hỏi** (Q56 "neutral") => thường sai.

**Nhận xét chung**: 53/60 = 88%, cao nhất từ trước tới giờ, D5 tuyệt đối. Còn lại đều là câu **đã gặp** trong 🔁 / 🎯 / flashcard (trừ Q38, Q56) => ôn flashcard "Missed 2+ times" là đủ trúng.

#### [M9] Site nguồn #8, full mock (2026-11-25): **54/60 = 90%** (theo guide **56/60 = 93%**)

52:17. D1 15/16, D2 9/11, D3 10/12, **D4 12/12**, D5 8/9. Sai 5 + bỏ trống 1: Q10, Q15 (trống), Q17 ⚠️, Q22, Q34, Q56 ⚠️. Đánh dấu 22. Q17 + Q56 bạn chọn **đúng theo guide** (key site sai) => 56/60. Xu hướng: M6 80% => M7 82% => M8 88% => **M9 90%**. ⚠️ Ngân hàng chỉ 287 câu => **trùng nhiều**, điểm cao hơn thực lực.

**Câu sai (6)**

| Câu | Tình huống (rút gọn) | Bạn chọn | ✅ Đúng | Vì sao | Guide |
|---|---|---|---|---|---|
| Q10 | `search_catalog` lỗi 12%: 8% timeout retry ngay là được, 4% lỗi cú pháp filter không bao giờ được | trả mọi lỗi kèm cờ `retryable` + loại lỗi | **tool tự retry (backoff) cho timeout**; lỗi cú pháp **trả ngay** kèm chi tiết validation | guide 2.2: "local error recovery for transient failures". Agent không phải thấy timeout. **Khác M1 Q49**: lỗi "không tìm thấy" không tạm => ❌ retry trong tool (🔁 dòng 3) | 2.2 |
| Q15 🔴 | lỗi 500 lúc có lúc không, 200+ file, dev **không biết** component nào | **bỏ trống** | **dynamic**: tạo subtask theo cái vừa tìm ra, đổi kế hoạch | lần 3 (M2, M5, M9). Chữ khóa "**doesn't know which components**" (🔁 dòng 8) | 1.6 |
| Q17 ⚠️ | 3 vấn đề 1 session, lượt 48 hỏi lại refund, gần hết context | **structured issue data trong lớp context riêng** | site: tóm tắt văn xuôi, giữ nguyên vấn đề đang làm | **bạn đúng theo guide 5.1 nguyên văn**. Xem ⚠️ | 5.1 |
| Q22 | synthesis làm mất nguồn khi gộp | coordinator chèn **prefix mã nguồn** vào text rồi parse lại | subagent trả **claim-source mapping có cấu trúc**, synthesis phải giữ + gộp | prefix trong text = dễ vỡ. Cùng đề Q28 bạn làm **đúng** (🔁 dòng 2) | 5.6 |
| Q34 | chèn hàm giữa file 150 dòng, `Edit` không có text unique | `Edit` với `old_string` **dài 30+ dòng** | **Read + Write** | lần 2 (M2 chọn `replace_all`). Chuỗi dài vẫn dễ lệch (🔁 dòng 11) | 2.5 |
| Q56 ⚠️ | batch, SLA 30h, 99.9% | **4h** | site: 6h | **bạn đúng** (guide 4.5 + bài học D5-2 của chính site). Xem ⚠️ | 4.5 |

**Câu đúng bạn đánh dấu không chắc (18)**: Q7 vòng lặp gap (hôm qua sai, nay đúng), Q9 mục tiêu + tiêu chí chất lượng, Q11 tóm tắt + subagent (CandidateRanker), Q14 MCP resources, Q16 + Q60 viết lại description, Q24 orchestrator-workers (newsroom), Q26 bỏ HTTP client cũ ở 1.400 file: Grep / Glob vẽ chỗ dùng, ưu tiên module dính nhiều, sửa kế hoạch dần, Q28 tách nội dung khỏi metadata nguồn, Q30 Grep SYNC_CONFLICT, Q36 tool tự chặn $500, Q42 (chọn 2) ghi ngày + giữ phương pháp từng nghiên cứu, Q43 = Q55 base class, **Q47** webhook báo đã giao hàng => **thêm trạng thái mới vào system prompt trước lần gọi API sau** (API stateless), Q48 render theo loại, Q50 CLAUDE.md chuẩn test, Q52 thuốc kiểm soát => **hook chặn** `submit_refill`.

**Mẹo nhớ 2 câu khó nhớ**
- **Q15**: "**Mỗi file đọc xong chỉ ra file đọc tiếp**" => **dynamic**. Ví dụ từng file (`routes/orders.js` => `OrderService` => `PaymentClient`, 3 file là ra) ở **mục 2.6**. Ngược lại M6 Q22 (migration): **biết** chỗ (migration guide + Grep 45 file) => plan mode.
- **Q17**: "**Sau này cần số chính xác => lưu bảng, không lưu câu chuyện**". Ví dụ đơn #A123, $89.99, approved 20/11 ở **mục 6.1** (giống bệnh án: bác sĩ đọc chỉ số, không đọc chuyện kể).

**Chủ đề CHƯA GẶP trong mock** (đối chiếu 67 nguyên tắc của site + guide, đã thêm flashcard 📗)
- Site: multi-phase workflow (analyze => propose => implement => review) cho việc mở, cần phán đoán · **routing** khi input chia rõ loại · `"Task"` thiếu trong `allowedTools` · truyền **reference ID** tới shared store thay vì nhồi nội dung · subagent **không tự thấy** output của nhau, coordinator phải chép vào prompt · **structured source index** cho report generator · không có gọi trực tiếp subagent-subagent / event bus · mỗi subagent chỉ **4-5 tool** của vai trò · tiêu chí escalate (đòi người, **policy gap**, không tiến triển) · `--resume <name>` vs `--continue` · `calculated_total` vs `stated_total`.
- Guide (chưa mock nào hỏi): `.mcp.json` + `${ENV_VAR}` · rule ở `~/.claude/CLAUDE.md` teammate không nhận · `context: fork` + `allowed-tools` trong SKILL.md · PostToolUse **chuẩn hóa** output tool · `--output-format json` (+ `--json-schema`) · review bằng **instance độc lập** · lost in the middle => key findings lên đầu · **rỗng** (thành công) vs **timeout** (lỗi) · `tool_choice: "any"` · field `detected_pattern`.

**Nhận xét chung**: 56/60 theo guide, cao nhất. 2 câu "sai" là key site sai, bạn **tin guide đúng**. Câu sai thật đều là chủ đề đã có trong 🔁 / 🎯. Vì đề trùng nhiều, đừng làm thêm mock bộ này: ôn flashcard **"Missed 2+ times"** + **"New topics"**.
