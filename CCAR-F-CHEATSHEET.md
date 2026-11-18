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
| 3 | Error cho model (Q14, Q49, Q51) | Có **loại + retry được không + bước tiếp**. Request hỏng => JSON-RPC protocol error. Tool chạy mà lỗi => `isError` |
| 4 | Cấu hình Claude Code (Q20, Q25, Q50) | Có **pattern tên file** => rules + `paths:`. Không pattern, maintainer tự biết => **@import**. Lúc theo lúc không => **/memory** trước |
| 5 | Gộp / tách tool (Q3, Q31, Q44) | 1 tool **nhiều việc** => tách. 2 tool **trùng nghĩa** => gộp. Model cần **thấy hết** để chọn => tool trả dữ liệu, hành động để riêng |
| 6 | Hook khi có cách đầy đủ hơn (Q2, Q52) | Nhiều đáp án là code => chọn cái **phủ mọi trường hợp** (kiểm tra sau khi loop dừng; tool tự tạo yêu cầu duyệt) |
| 7 | Prompt caching (Q6, Q54) | Caching chỉ là **chi phí / tốc độ**, không sửa gốc. Chi tiết ngoài phạm vi thi => thường là **bẫy** |

---

## 3. ⚠️ Đáp án mock đã kiểm tra là SAI (đừng học theo)

| Câu | Mock ghi | Đúng theo guide |
|---|---|---|
| M1 Q46 (timeout, không biết đã gửi chưa) | `retry_safe: true` | báo "**status unknown, đừng retry**" (retry => gửi trùng) |
| M1 Q32 (thiếu `user_id`) | strict schema | ⚠️ tranh cãi: "bảo đảm cấu trúc" => schema; "giúp **hiểu**" => description |
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

**Claude Code (D3)**

| Cặp | Phân biệt |
|---|---|
| `~/.claude/CLAUDE.md` vs `CLAUDE.md` repo | `~/.claude/` = **chỉ máy mình**, teammate không nhận. Trong repo = **cả team** nhận qua git (4.1) |
| `.claude/rules/` + `paths:` vs **CLAUDE.md thư mục** | file cùng loại nằm **rải rác** nhiều thư mục => rules + glob. CLAUDE.md thư mục chỉ áp cho **1 thư mục** (4.3) |
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
| CI | `-p` (không treo chờ input) + `--output-format json` + `--json-schema` (output máy đọc được) (4.6) |
| Tự review vs **phiên độc lập** | phiên vừa viết code tự review = **kém** (còn nhớ lý luận cũ, ít nghi ngờ). Phiên **mới** review = **tốt hơn** (4.6, 5.6) |

**Prompt + output (D4)**

| Cặp | Phân biệt |
|---|---|
| Lỗi **syntax** vs **semantic** | syntax = JSON **hỏng cú pháp** (thiếu ngoặc) => **tool_use + schema** là hết. Semantic = JSON đúng cú pháp nhưng **nội dung sai** (cộng các dòng không ra tổng, giá trị nằm nhầm field) => schema không bắt được => code kiểm tra + **retry kèm lỗi** (5.3) |
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
| Context xuống cấp (trả lời chung chung "typical patterns") | ghi findings ra **scratchpad file** (file nháp), giao câu hỏi cụ thể cho subagent, `/compact` (6.4) |
| Crash recovery | mỗi agent ghi trạng thái ra file cố định (**manifest**), coordinator đọc file đó khi chạy lại (6.4) |
| 97% tổng thể, đã tự động hóa được chưa? | con số tổng có thể che 1 loại tài liệu kém => đo **riêng từng loại tài liệu + từng field**, lấy mẫu kiểm tra **chia theo nhóm** (stratified sampling) (6.5) |
| Confidence | confidence **từng field**, calibrate với **dữ liệu có đáp án đúng** => chọn cái đưa người xem. ❌ agent tự chấm 1-10 thô để escalate (Q3). ❌ chỉnh ngưỡng theo điểm tổng (6.5) |
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
