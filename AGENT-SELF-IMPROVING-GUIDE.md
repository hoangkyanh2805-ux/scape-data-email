Self-Improving AI Agent — Guide (from @precisox video)
Nguồn: Video 1 giờ của ex-Google engineer, post trên X bởi @precisox
Status:
x.com

Timestamp gốc (từ video):

Thời gian
Nội dung
00:00	Cómo nace un agente que se construye a sí mismo
03:01	soul.md: el archivo que lo controla todo
30:16	RAG inteligente: solo traes 20 mensajes relevantes, no los 2.000
31:48	El loop que sabe cuándo parar solo
35:14	Detectar el error y arreglar el prompt en el momento
50:22	Cómo Claude comprime y optimiza tu memoria automáticamente
Video không có public transcript. Hướng dẫn này dựa trên timestamps + mô tả từ video.

1. Cấu trúc repo hướng dẫn
Dùng cấu trúc này cho bất kỳ dự án agent nào:

agent-project/ ├── README.md # Hướng dẫn tổng ├── soul.md # Identity + hard rules + accountability loop (slot #1 trong system prompt) ├── rag/ │ ├── embed.py # Semantic embedding function │ ├── retrieve.py # Cosine similarity + top-k retrieval │ └── config.yaml # Embedding model, retrieval params ├── loop/ │ ├── terminate.py # Quality gate: dừng khi không improve │ └── config.yaml # max_iterations, no_improvement threshold ├── error_fix/ │ ├── detect.py # Error detection (validation, exception, feedback) │ ├── fix_prompt.py # Root cause → propose fix → commit versioned │ └── prompt_history/ # Prompt version files (timestamped JSON) └── memory/ ├── compress.py # Periodic compress → summary └── snapshots/ # Compressed summaries + pointer files


---

## 2. soul.md — Slot #1 trong system prompt

### Từ video

- Model đọc soul.md đầu tiên, trước mọi instruction khác
- Soul.md cậy → agent cậy; soul.md sâu → agent sâu
- Accountability loop là secret: agent tự kiểm tra trước delivery

### Template soul.md (dùng cho dự án khác)

```markdown
# [TÊN AGENT]
## Who I Am
[1-2 sentences — identity, communication style, priority]

## Hard Rules
- [Rule cụ thể, measurable — không abstract]
- [Rule 2]
- [Rule 3]
- [Rule 4]
- [Rule 5]
- [Rule 6]

## Accountability Loop
After every substantive answer, self-check:
1. [Câu hỏi kiểm tra 1 — Y/N]
2. [Câu hỏi kiểm tra 2 — Y/N]
3. [Câu hỏi kiểm tra 3 — Y/N]
If any NO — flag it before delivery.

## When In Doubt
[1 câu — khi không sure, làm gì]
Điều không làm (từ video)
Không viết soul.md 90+ lines — agent không đọc hết
Không dùng "be helpful", "be friendly" làm personality — quá abstract
Không bỏ accountability loop
3. RAG — Semantic retrieval, không load tất cả
Từ video
Lỗi phổ biến nhất: load 2,000 messages vào context → model drowning
Giải pháp: sóng retrieval, chỉ lấy top-20 relevant gần nhất
Dùng embedding similarity, không keyword search
20 là intuition, không phải law — task phức hợp có thể cần 30-40
Template embed.py
import openai

def embed(text):
    """Semantic embedding cho 1 text."""
    res = openai.embeddings.create(input=text, model="text-embedding-3-small")
    return res.data.embedding
Template retrieve.py
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve(query_embedding, stored_embeddings, top_k=20):
    """Lấy top-k messages relevant nhất."""
    scores = [(i, cosine_similarity(query_embedding, emb)) 
              for i, emb in enumerate(stored_embeddings)]
    scores.sort(key=lambda x: x, reverse=True)
    return [idx for idx, _ in scores[:top_k]]
Config rag/config.yaml
embedding:
  model: "text-embedding-3-small"
  dimensions: 1536

retrieval:
  top_k: 20
  # Nếu task phức hợp, tăng top_k lên 30-40
Điều không làm
Không load toàn bộ conversation history (2,000 messages) vào context
Không dùng keyword search cho semantic task
Không cố định top_k=20 cho mọi task — tuning theo thực tế
4. Loop termination — Quality gate, không max_iterations cứng
Từ video
Infinite loop là đoạn most dangerous — agent tự cải thiện không biết dừng
Termination phải là quality gate: chỉ loop khi có measurable improvement
2 iteration liên tiếp không improve → dừng + log convergence
Template terminate.py
def should_continue(current, proposed, no_improve_count, 
                     max_no_improve=2, max_iter=5, iteration=0):
    """
    Quality gate cho self-improving loop.
    Return (continue_bool, updated_no_improve_count).
    """
    if iteration >= max_iter:
        return False, no_improve_count
    
    improvement = evaluate_improvement(current, proposed)
    if improvement > 0:
        return True, 0  # Reset counter khi có improve
    else:
        no_improve_count += 1
        if no_improve_count >= max_no_improve:
            return False, no_improve_count
        return True, no_improve_count

def evaluate_improvement(current, proposed):
    """
    So sánh current vs proposed.
    Return > 0 nếu proposed tốt hơn, ≤ 0 nếu không.
    Cài đặt cụ thể tùy task — ví dụ: self-evaluation, human review, test suite.
    """
    # TODO: cài đặt evaluation cụ thể cho project
    pass
Config loop/config.yaml
loop:
  max_iterations: 5          # Safeguard, không dùng làm primary stop
  max_no_improvement: 2      # Dừng khi 2 iter liên tiếp không improve
Điều không làm
Không dùng max_iterations=10 làm stop condition duy nhất
Không bỏ evaluation function — nếu evaluation flawed, agent converge sớm hoặc infinite loop
Không bỏ log convergence — user cần biết agent dừng ở iteration nào
5. Error detection + prompt self-fix
Từ video
Agent detect error → analyze root cause → propose prompt fix → commit versioned → re-execute → compare → commit nếu improve
Prompt versioning: ghi mỗi version vào file, timestamp, task, signal, improvement score
Template detect.py
def detect_error(last_result, context):
    """
    Detect error từ:
    - Validation check failed
    - Runtime exception
    - User feedback signal
    - Compliance issue (VD: income claim, guarantee, v.v.)
    Return error description hoặc None nếu không có error.
    """
    # TODO: cài đặt detection cụ thể cho project
    pass
Template fix_prompt.py
import json
from datetime import datetime
from pathlib import Path

PROMPT_HISTORY_DIR = Path("error_fix/prompt_history")
PROMPT_HISTORY_DIR.mkdir(parents=True, exist_ok=True)

def save_prompt_version(original, fixed, task, signal, improvement_score):
    """Commit prompt version vào history."""
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "task": task,
        "original": original,
        "fixed": fixed,
        "signal": signal,
        "improvement_score": improvement_score,
    }
    path = PROMPT_HISTORY_DIR / f"prompt_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    path.write_text(json.dumps(entry, indent=2), encoding="utf-8")
    return str(path)
Điều không làm
Không self-fix prompt mà không log change — agent trở thành black box
Không re-execute mà không compare result vs trước — không biết có improve không
Không commit prompt fix nếu không có improvement
6. Memory compression
Từ video
Context window dù 200K tokens là finite — agent quên sau vài ngày
Periodic nén conversation history thành summary 500-token information-dense
Stored như snapshot + pointer (message IDs) — không keep full context trong memory
Cost: ~1 cent/compression, chạy mỗi 1000 messages hoặc mỗi 24h
Template compress.py
def compress_conversation(messages, max_tokens=500):
    """
    Nén N messages thành summary information-dense.
    Dùng Claude API (hoặc model tương đương).
    """
    text = "\n".join(f"{m['role']}: {m['content']}" for m in messages)
    prompt = (
        f"Summarize this conversation into the most important points, "
        f"decisions, and open questions. Be terse. Max {max_tokens} tokens. "
        f"Output ONLY the summary, no preamble.\n\n{text}"
    )
    # Gọi Claude API ở đây
    # res = client.messages.create(
    #     model="claude-sonnet-4-20250514",
    #     max_tokens=max_tokens,
    #     messages=[{"role": "user", "content": prompt}]
    # )
    # return res.content.text
    pass  # Placeholder — cài đặt API call cụ thể cho project

def save_snapshot(summary, message_ids, path):
    """Lưu compressed snapshot + pointer đến original messages."""
    snapshot = {
        "summary": summary,
        "message_ids": message_ids,  # Pointer để retrieve đầy đủ nếu cần
        "compressed_at": datetime.utcnow().isoformat(),
    }
    Path(path).write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
Config memory
memory:
  compression:
    max_tokens: 500
    frequency: "every_1000_messages"  # Hoặc "every_24h"
  storage:
    snapshots_dir: "memory/snapshots"
Điều không làm
Không keep full conversation history trong memory — chỉ compressed summary + pointer
Không nén khi chưa cần — chỉ periodic (mỗi 1000 messages hoặc mỗi 24h)
Không compressed memory dùng cho critical facts cần exact wording — cần pointer retrieval đến original
7. Checklist áp dụng cho dự án mới
Trước khi bắt đầu
 Viết soul.md 18-line (identity + hard rules + accountability loop + when in doubt)
 Không viết soul.md 90+ lines
 Accountability loop có 3 câu self-check trước mọi substantive answer
RAG
 Chọn embedding model (OpenAI text-embedding-3-small cho production, all-MiniLM-L6-v2 cho local free)
 Implement semantic retrieval: embed → cosine similarity → top-20
 Test semantic search với query ambiguious
 Tuning top_k theo task thực tế (20 baseline, phức hợp → 30-40)
Loop
 Implement evaluate_improvement function (self-evaluation, human review, test suite)
 Stop condition: 2 iteration không improve → dừng + log convergence
 max_iterations=5 làm safeguard, không làm primary stop
 Test evaluate_improvement: return > 0 khi improve, ≤ 0 khi không
Error fix
 Implement error detection (validation, exception, feedback, compliance)
 Implement prompt fix flow: detect → analyze → propose → commit versioned → re-execute → compare → commit nếu improve
 Log mọi prompt change vào error_fix/prompt_history/
Memory
 Implement periodic compression: mỗi 1000 messages hoặc mỗi 24h
 Compression function: Claude API summarize 500-token
 Stored như snapshot + pointer (message IDs)
 Cost check: ~$0.01/compression acceptable cho project
8. Phản biện (từ video + domain knowledge)
Soul.md 18-line tuyên bố "90% agent fail do soul.md cậy"
Không phải single point of failure. Agent fail do: context window management, tool selection, error handling, evaluation métric, infra reliability, human-in-the-loop handoff, cost management.
Accountability loop cần evaluation quality. Nếu evaluation function kém, agent "self-improve" về phía sai sophistocated.
Top-20 messages
Nghiên cứu Anthropic recommend 15-25 chunks cho task đơn giản. Task phức hợp (multi-hop reasoning) cần nhiều hơn.
20 là intuition, không phải law. Mỗi project cần experiment retrieval size vs performance.
Loop termination tự động
evaluate_improvement là subjective — agent tự đánh giá improvement. Nếu evaluation flawed → premature stop hoặc infinite loop.
Cần human-in-the-loop cho mission-critical tasks (content publish, sales outreach, compliance-sensitive).
Memory compression 500 tokens
Compression mất information — 500 tokens từ 10K messages lose nuance.
Không đủ cho critical facts cần exact wording — cần pointer retrieval đến original message.
Compressed memory có thể hallucinate summary — agent đọc summary có thể nhầm. Cần verification step cho critical facts.
"1 giờ content thực tế hơn hầu hết course trả phí"
Video là overview/high-level — đúng architecture direction, thiếu production detail: evaluation suites, regression testing, cost monitoring, error budget, handoff design, compliance workflow.
9. Gợi ý mapping sang dự án cụ thể
Dự án có CRM / customer memory
Video component
Áp dụng
Soul.md accountability	Hard rule: không income claim, luôn disclaimer, flag uncertain
RAG top-20	CRM context — fetch 20 messages relevant gần nhất
Loop termination	Outreach sequence — 2 draft không improve → dừng, handover
Error fix	Detect compliance issue → fix → re-draft → commit → log
Memory compression	Nén campaign history thành summary, pointer retrieve detail
Dự án market research / news monitoring
Video component
Áp dụng
Soul.md identity	Accuracy-first, flag uncertain, không fabricate statistics
RAG semantic retrieval	Embedding articles, retrieval semantic cho news
Loop termination	Research synthesis — 2 iter không improve → converge, deliver
Error fix	Detect missing citation → fix → re-research → log
Memory compression	Nén news history thành daily/weekly summary snapshot
Dự án content seeding
Video component
Áp dụng
Soul.md tone/voice	Agent viết content theo brand voice — soul.md định nghĩa tone, hard rules
RAG retrieval relevant	Fetch content history, style examples — top-20
Loop termination	Draft sequence — converge khi draft đạt quality threshold
Error fix	Detect brand voice drift → fix → re-draft → commit
Memory compression	Nén content history thành style/compression snapshot
Dự án sales war room internal
Video component
Áp dụng
Soul.md tiếng Việt	Internal war room — direct, structured, Vietnamese
RAG retrieval	Fetch sales context (leads, objections, playbook) — top-20
Loop termination	Strategy recommendation — converge khi proposal stabilize
Error fix	Detect misaligned recommendation → fix → re-propose → log
Memory compression	Nén war room discussion thành summary
10. Tài liệu tham khảo
Video gốc:
x.com
Thread navigator archive: AI/ML thread by @0xCodila | Thread Navigator
Hermes Agent soul.md docs: Tech/Development thread by @akshay_pachaar | Thread Navigator
soul.md spec (aaronjmars): GitHub - aeonfun/soul.md: The best way to build a personality for your agent. Let Claude Code / OpenClaw ingest your data & build your AI soul. · GitHub
Anthropic context window best practices: ~20-30 relevant chunks
Embedding model: OpenAI text-embedding-3-small (1536 dim, ~$0.00002/1K tokens)
Local embedding alternative: all-MiniLM-L6-v2 (HuggingFace, free)
Số lần sửa đổi: 1 — 2026-09-18
Nguồn: timestamps video @precisox + kiến thức domain. Không phải transcript word-for-word.

Lưu ý kỹ thuật
File không thể ghi tự động từ Hermes vào G:\... vì:

Docker sandbox không see Windows drive letter G:\
Proxy chặn mọi terminal/write_file/execute_code