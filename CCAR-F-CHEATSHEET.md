# CCAR-F - Đọc nhanh trước giờ thi (10-15 phút)

> Bản rút gọn của `CCAR-F-NOTES.md`: chỉ giữ **luật, keyword, lỗi lặp lại**. Cần chi tiết => xem số mục trong ngoặc (vd "3.2").

---

## 1. Trước khi làm bài: 5 thói quen

1. **Đọc CUỐI câu trước**: "most effective **first step**", "most **maintainable**", "**guarantee**", "reduce overhead **while maintaining reliability**"
2. **Đọc số liệu**: "12% skip", "85% simple / 15% complex", "18 tools", "14 files" => số liệu chỉ thẳng vào đáp án
3. **Gạch 4 loại đáp án sai**: prompt khi cần **đảm bảo** · **hạ tầng mới** (classifier, routing layer, model to hơn) khi chưa thử cách đơn giản · **đẩy việc cho dev** · **flag / file không tồn tại**
4. **Multiple response**: đề ghi chọn mấy => chọn **đủ**
5. Đề có **2 yêu cầu** => đáp án phải thỏa **cả 2**

⚙️ **Luật thi**: 60 câu, 4/6 scenario, 120 phút (~2 phút / câu), đậu **>= 720/1000**. Trả lời **hết mọi câu**.

---

## 2. 🔁 Lỗi đã lặp lại (đọc kỹ nhất)

| # | Chủ đề | Quy tắc 1 dòng |
|---|---|---|
| | *(điền sau các mock)* | |

---

## 3. ⚠️ Đáp án mock đã kiểm tra là SAI (đừng học theo)

| Câu | Mock ghi | Đúng theo guide |
|---|---|---|
| | *(điền khi gặp)* | |

---

## 4. 10 luật vàng (mục 0)

1. Cần **100%** (tiền, danh tính, thứ tự bắt buộc) => **hook / gate trong code**, ❌ prompt
2. "**First step**" => sửa root cause **rẻ nhất** (vd viết lại **tool description**)
3. Root cause ở **đúng chỗ log chỉ ra** (vd coordinator chia task hẹp), đừng đổ cho agent downstream
4. Lỗi => **structured error** (type, đã thử gì, partial, hướng khác). ❌ generic · ❌ rỗng như thành công · ❌ dừng cả workflow
5. **Least privilege** tool. Case phổ biến => **1 tool hẹp** (`verify_fact`)
6. **Sentiment** + **self-reported confidence** = không đáng tin
7. Model to / context dài **không** sửa attention dilution => **chia pass**
8. `CLAUDE_HEADLESS`, `--batch`, `.claude/config.json` commands = **không tồn tại**
9. **Batch** chỉ cho việc **không chặn**
10. "be conservative" / "high-confidence only" **vô dụng** => **tiêu chí cụ thể** + ví dụ

---

## 5. Các cặp dễ nhầm

**Agent + tool (D1, D2)**

| Cặp | Phân biệt |
|---|---|
| `stop_reason` **tool_use** vs **end_turn** | tool_use => chạy tool, append `tool_result`, lặp. end_turn => **dừng**. ❌ dừng theo chữ "done" / iteration cap / có text (2.1) |
| **Hook** vs **prompt** | hook = **chắc chắn**. prompt = **xác suất** (2.4, 2.5) |
| **PostToolUse** vs chặn tool call | PostToolUse = **sửa kết quả** (chuẩn hóa ngày giờ). Chặn call = **chặn hành động** (refund > $500 => escalate) (2.5) |
| **Prompt chaining** vs **dynamic decomposition** | việc **đoán trước được** (review từng file + cross-file) / việc **mở** (thêm test cho legacy code) (2.6) |
| **Resume** vs **session mới + summary** | context còn đúng => `--resume <name>`. Tool result **stale** => session mới + summary (2.7) |
| **fork_session** | so sánh **2 hướng** từ 1 bản phân tích chung (2.7) |
| Subagent **context** | **không** kế thừa => đưa findings **thẳng vào prompt**. Coordinator cần `"Task"` trong `allowedTools` (2.3) |
| Song song | **nhiều Task call trong 1 response** (2.3) |
| `tool_choice` **auto / any / forced** | có thể trả text / **phải** gọi tool nào đó / **phải** gọi đúng tool X (3.3) |
| **transient / validation / business / permission** | chỉ **transient** đáng retry. Business => `retriable: false` + lời giải thích cho khách (3.2) |
| **Access failure** vs **empty result** | gọi **không được** (cần quyết định retry) / gọi được, **không có** dữ liệu (thành công) (3.2, 6.3) |
| MCP **resource** vs **tool** | resource = **catalog để xem** (issue list, DB schema) => bớt dò dẫm. tool = **hành động** (3.4) |
| **Grep** vs **Glob** | Grep = tìm **nội dung**. Glob = tìm **tên file** (`**/*.test.tsx`) (3.5) |
| **Edit** fail | text không unique => **Read + Write** (3.5) |

**Claude Code (D3)**

| Cặp | Phân biệt |
|---|---|
| `~/.claude/CLAUDE.md` vs `CLAUDE.md` repo | user = **chỉ mình**, teammate không nhận. Project = **cả team** (4.1) |
| `.claude/rules/` + `paths:` vs **CLAUDE.md thư mục** | file **rải rác** nhiều thư mục => rules + glob. CLAUDE.md gắn **1 thư mục** (4.3) |
| `.claude/commands/` vs `~/.claude/commands/` | team (git) / cá nhân (4.2) |
| `.mcp.json` vs `~/.claude.json` | MCP team + `${ENV}` cho secret / MCP cá nhân, thử nghiệm (3.4) |
| **Skill** vs **CLAUDE.md** | gọi **khi cần** / **luôn load** (4.2) |
| `context: fork` / `allowed-tools` / `argument-hint` | **tách context** / **giới hạn tool** / **gợi ý tham số** (4.2) |
| **Plan mode** vs **direct** | lớn, nhiều file, kiến trúc / nhỏ, rõ, 1 file. Kết hợp: plan rồi direct (4.4) |
| **Explore subagent** | tách phần khám phá dài, trả tóm tắt (4.4) |
| `/memory` vs `/compact` | xem **file memory nào đang load** / **nén context** khi đầy (4.1, 6.4) |
| Lỗi **liên quan** vs **độc lập** | gửi **1 message** tất cả / sửa **lần lượt** (4.5) |
| CI | `-p` (không treo) + `--output-format json` + `--json-schema` (4.6) |
| Self-review vs **instance độc lập** | instance độc lập **tốt hơn** (4.6, 5.6) |

**Prompt + output (D4)**

| Cặp | Phân biệt |
|---|---|
| Lỗi **syntax** vs **semantic** | syntax => **tool_use + schema** hết. Semantic (tổng không khớp, sai field) => **validation + retry** (5.3) |
| Retry **có ích** vs **vô ích** | lỗi format / cấu trúc / thông tin **không có** trong tài liệu (5.4) |
| Field **required** vs **nullable** | có thể thiếu => **nullable**, không thì model **bịa** (5.3) |
| enum mở rộng | `"other"` + `detail`, `"unclear"` (5.3) |
| **Few-shot** | 2-4 ví dụ, case **mơ hồ**, có **lý do**. Format nhất quán, giảm hallucination extraction (5.2) |
| **Batch** | 50% rẻ, tới 24h, **không SLA**, **không** multi-turn tool, `custom_id`, gửi lại **chỉ cái lỗi** (5.5) |
| 1 pass vs **multi-pass** | nhiều file => **per-file + integration** (5.6) |

**Context + reliability (D5)**

| Cặp | Phân biệt |
|---|---|
| Tóm tắt mất số liệu | **case facts block** riêng, ngoài summary (6.1) |
| **Lost in the middle** | key findings lên **đầu** + section header (6.1) |
| Tool output dài | **cắt** còn field cần **trước** khi vào context (6.1) |
| Context xuống cấp ("typical patterns") | **scratchpad file**, subagent, `/compact` (6.4) |
| Crash recovery | agent export **manifest**, coordinator load khi resume (6.4) |
| 97% tổng thể | đo **theo loại tài liệu + field**, **stratified sampling** (6.5) |
| Confidence | **field-level**, calibrate bằng **labeled validation set** (6.5) |
| Nguồn **mâu thuẫn** | giữ **cả 2** + nguồn + **ngày** (6.6) |

---

## 6. Escalate hay không? (6.2)

| Tình huống | => |
|---|---|
| Khách **đòi người** | **escalate NGAY**, không điều tra |
| Khách bực, việc làm được | đề nghị giải quyết. Nhắc lại đòi người => escalate |
| Policy **im lặng / mơ hồ** (price-match đối thủ) | **escalate** |
| Không tiến triển | escalate |
| **Nhiều khách** khớp | **hỏi thêm** identifier, không đoán |
| Escalate lệch (dễ thì đẩy, khó thì ôm) | **tiêu chí rõ + few-shot** trong system prompt |
| Handoff | summary: customer ID, root cause, số tiền, đề xuất (người nhận **không có** transcript) |

---

## 7. ❌ Không thi (thấy đáp án nói về mấy cái này thì cảnh giác)

Fine-tuning · RLHF / Constitutional AI · auth / billing / OAuth · host MCP server · embedding / vector DB · computer use · vision · **streaming** · rate limit / tính giá · tokenizer · **prompt caching chi tiết** · cấu hình AWS / GCP / Azure · benchmark model
