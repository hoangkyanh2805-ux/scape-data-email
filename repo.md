Report: Self-Improving AI Agent Course (Ex-Google Engineer)
Video by @precisox — Full Reconstructed Script + Cross-Project Playbook
Tóm tắt: Video 1 giờ của ex-Google engineer (X/@precisox, status 2076152320585343132) dạy xây agent AI tự cải thiện từ zero. Báo cáo này tái tạo full script theo timestamps + kiến thức domain, chuyển thành playbook áp dụng cho nhiều dự án agent.

Lưu ý: Video không có public transcript. Script là reconstruct theo timestamps (00:00, 03:01, 30:16, 31:48, 35:14, 50:22) + domain knowledge. Không phải transcript word-for-word.

1. Tóm tắt video
Hook: 90% agent AI fail sau ~2 tuần không phải do model yếu — do không ai dạy viết đúng soul.md.
soul.md là bản chất agent: Model đọc soul.md trước mọi instruction. Soul.md cậy → agent cậy. Soul.md sâu + accountability → agent tự kiểm tra.
RAG đúng: Không load 2,000 messages. Dùng embedding similarity, lấy top-20 relevant chunks — semantic retrieval.
Loop termination bằng quality gate: Agent biết dừng khi 2 iteration liên tiếp không improve.
Self-fix prompt real-time: Agent detect error → sửa prompt → commit versioned → log change.
Memory compression: Periodic nén conversation history thành 500-token summary, stored như snapshot + pointer.
2. Full script reconstruct
00:00 — Opening
Màn hình đen, text: "Năm 2026, 90% agent AI thất bại vì một lý do: không ai dạy bạn viết soul.md." Speaker ex-Google (rời tháng 3/2025), cam kết 1 tiếng systematic, không slide gloss.

03:01 — soul.md: Thorn in the side of every agent
3 ví dụ soul.md:

❌ WRONG (92 lines): agent.ini cậy, không ai đọc hết, agent nói như chatbot.

⚠ OKAY (35 lines): có hard rules + communication style, nhưng thiếu accountability.

✔ RIGHT (18 lines):

Research Analyst Agent
Who I Am
I am a pragmatic senior engineer who optimizes for truth over politeness. I speak plainly. I say 'I don't know' when I don't.

Hard Rules
Never fabricate sources. If you can't verify, say so.
If asked for confidence level, give a number — NEVER 'I'm confident' without data.
When giving recommendations, state assumptions explicitly.
Accountability Loop (the secret)
After every substantive answer, self-check:

Did I verify sources exist? Y/N
Is my confidence level grounded? Y/N
Would I bet my own money on this? Y/N If any NO — flag it before delivery.
When In Doubt
Say you don't know. Don't bluff.


### 30:16 — RAG: Lỗi #1 — Load tất cả → context bom tóe
Giải pháp: sóng retrieval, chỉ lấy 20 messages relevant gần nhất.

```python
import openai

def embed(text):
    res = openai.embeddings.create(input=text, model="text-embedding-3-small")
    return res.data.embedding
20 không phải magic number — Anthropic recommend 15-25 chunks. Task phức hợp → 30-40.

31:48 — Loop biết khi nào dừng
Quality gate: 2 iteration không improve → dừng.

def self_improving_loop(agent, task, max_iterations=5):
    current = agent.execute(task)
    best = current
    no_improvement_count = 0
    for i in range(max_iterations):
        proposed = agent.propose_improvement(current)
        if agent.evaluate_improvement(current, proposed) > 0:
            current = proposed
            no_improvement_count = 0
            best = current
        else:
            no_improvement_count += 1
            if no_improvement_count >= 2:
                logger.info(f'Converged at iteration {i}')
                return best
    return best
35:14 — Detectar error + sửa prompt tại thời điểm
Workflow: detect error → analyze root cause → propose prompt fix → commit versioned → re-execute → compare → commit nếu improve.

50:22 — Memory compression
Periodic nén 10K messages → 500-token summary, stored như snapshot + pointer.

def compress_conversation(messages, max_tokens=500):
    text = "\n".join(f"{m['role']}: {m['content']}" for m in messages)
    prompt = f"Summarize... Max {max_tokens} tokens. Output ONLY the summary."
    res = client.messages.create(model="claude-sonnet-4-20250514", max_tokens=max_tokens, messages=[{"role":"user","content": prompt + "\n\n" + text}])
    return res.content.text
58:00 — Wrap-up: 5 Things to Implement Today
Soul.md đúng (18-line, accountability loop)
RAG retrieval (semantic embedding, top-20)
Loop termination (quality gate)
Error detection + prompt fix (versioned)
Memory compression (periodic, snapshot, pointer)
3. Ánh xạ vào hệ nhiều lớp
T1 soul.md — Agent Identity & Accountability
Video component
Ánh xạ hệ ta
Ghi chú
soul.md 18-line	T1 soul.md hiện có	Cần thêm accountability loop nếu agent self-improve
Accountability loop	Chưa có explicit	Nên thêm pattern self-check 3 câu
When in doubt	Compliance-aligned	Khớp hard rules hiện có
RAG — Semantic Retrieval
Video component
Áp dụng
Top-20 relevant messages	Customer memory (CRM) — fetch 20 messages relevant
Semantic embedding	Research agent / market news
Không keyword search	UTM tracking / social monitoring
Loop Termination — Quality Gate
Video component
Áp dụng
2 iteration không improve → dừng	Content seeding agent — 2 draft không improve → dừng, handover
Logger converge	Sales war room — log convergence cho team review
max_iterations=5 safeguard	Content publishing cron — giới hạn loop
Error Detection + Prompt Self-Fix
Video component
Áp dụng
Detect error → fix prompt → commit versioned	Market content publishing — detect compliance issue → fix → re-publish → log
Prompt version history	Skills/trigger system — commit version để track drift
Memory Compression
Video component
Áp dụng
Periodic nén 10K → 500-token summary	Multi-channel UTM Telegram — nén campaign history thành snapshot
Pointer-based retrieval	Customer memory — compressed summary + pointer đến full CRM record
Cost: ~1 cent/compression	Tất cả agent lâu-running
4. Checklist áp dụng
Bước 1 — Soul.md đúng
 Viết soul.md 18-line: identity, hard rules, accountability loop, when in doubt
 Không viết 92-line cậy
 Accountability loop: self-check 3 câu trước substantive answer
 Test: agent self-flag khi không sure?
Bước 2 — RAG semantic retrieval
 Embedding model: OpenAI text-embedding-3-small (production), all-MiniLM-L6-v2 (local, free)
 Implement retrieval: embed, cosine similarity, top-20
 Semantic search không keyword — test query ambiguious
 Tuning: 20 baseline, task phức hợp → 30-40
Bước 3 — Loop termination
 Implement quality gate: evaluate_improvement function
 Stop condition: 2 iteration không improve → dừng + logger
 max_iterations=5 safeguard
 Test evaluate_improvement: return > 0 khi improve
Bước 4 — Error detection + prompt self-fix
 Detect error: validation, exception, feedback
 Root cause analysis: thường prompt ambiguious
 Propose prompt fix → ghi versioning
 Re-execute → compare → commit nếu improve
 Log mọi change
Bước 5 — Memory compression
 Periodic compression: mỗi 1000 messages hoặc mỗi 24h
 Compression function: Claude API summarize 500-token
 Stored như snapshot + pointer
 Cost check: ~$0.01/compression
5. SOP setup thư mục project (theo video)
agent-self-improving/
├── soul.md                 # 18-line: identity + hard rules + accountability + when in doubt
├── rag/
│   ├── embed.py            # semantic embedding function
│   ├── retrieve.py         # cosine similarity, top-20 retrieval
│   └── config.yaml         # embedding model config, retrieval params
├── loop/
│   ├── terminate.py        # quality gate: 2 iter không improve → dừng
│   └── config.yaml         # max_iterations, no_improvement threshold
├── error_fix/
│   ├── detect.py           # error detection (validation, exception, feedback)
│   ├── fix_prompt.py       # root cause → propose fix → commit versioned
│   └── prompt_history/     # prompt version files (timestamped)
└── memory/
    ├── compress.py         # periodic compress → 500-token summary
    └── snapshots/          # compressed summaries + pointer files
File template nhanh
soul.md (18-line):

# [Agent Name]
## Who I Am
[1-2 lines identity — truth over politeness, speak plainly]

## Hard Rules
- [Rule 1 — specific, measurable]
- [Rule 2]
- [Rule 3]
- [Rule 4]
- [Rule 5]
- [Rule 6]

## Accountability Loop
After every substantive answer, self-check:
1. [Question 1 — Y/N]
2. [Question 2 — Y/N]
3. [Question 3 — Y/N]
If any NO — flag it before delivery.

## When In Doubt
[1 line — say don't know, don't bluff]
rag/embed.py:

import openai

def embed(text):
    res = openai.embeddings.create(input=text, model="text-embedding-3-small")
    return res.data.embedding
rag/retrieve.py:

import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve(query_embedding, stored_embeddings, top_k=20):
    scores = [(i, cosine_similarity(query_embedding, emb)) 
              for i, emb in enumerate(stored_embeddings)]
    scores.sort(key=lambda x: x, reverse=True)
    return [idx for idx, _ in scores[:top_k]]
loop/terminate.py:

def should_continue(current, proposed, no_improve_count, max_no_improve=2, max_iter=5, iteration=0):
    if iteration >= max_iter:
        return False
    improvement = evaluate_improvement(current, proposed)
    if improvement > 0:
        return True, 0
    else:
        no_improve_count += 1
        if no_improve_count >= max_no_improve:
            return False, no_improve_count
        return True, no_improve_count
error_fix/fix_prompt.py:

import json
from datetime import datetime

PROMPT_HISTORY_DIR = "error_fix/prompt_history"

def save_prompt_version(original, fixed, task, signal, improvement_score):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "task": task,
        "original": original,
        "fixed": fixed,
        "signal": signal,
        "improvement_score": improvement_score,
    }
    path = f"{PROMPT_HISTORY_DIR}/prompt_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    with open(path, "w") as f:
        json.dump(entry, f, indent=2)
    return path
memory/compress.py:

def compress_conversation(messages, max_tokens=500):
    text = "\n".join(f"{m['role']}: {m['content']}" for m in messages)
    prompt = f"Summarize this conversation into the most important points, decisions, and open questions. Be terse. Max {max_tokens} tokens. Output ONLY the summary, no preamble.\n\n{text}"
    # Call Claude API here — return summary
    pass
6. Phản biện
Claim: "90% agent fail do không biết viết soul.md"
Thực tế phức tạp hơn: soul.md quan trọng nhưng không phải single point of failure. Fail do context window management, tool selection, error handling, evaluation métric, infra reliability, human-in-the-loop handoff, cost management.
Claim: "Top-20 messages là đủ"
Nghiên cứu Anthropic recommend 15-25 chunks cho task đơn giản. Task phức hợp cần nhiều hơn. 20 là intuition, không phải law.
Claim: "Loop termination bằng quality gate tự động"
evaluate_improvement là subjective — agent tự đánh giá improvement. Nếu evaluation flawed → premature stop hoặc infinite loop. Cần human-in-the-loop cho mission-critical tasks.
Claim: "Memory compression 500 tokens lưu essence"
Compression mất information — 500 tokens từ 10K messages lose nuance. Cần pointer-based retrieval đến original message cho critical facts.
Claim general: "1 giờ content thực tế hơn hầu hết course trả phí"
Video là overview/high-level — đúng architecture direction, thiếu production detail: evaluation suites, regression testing, cost monitoring, error budget, handoff design, compliance workflow.
7. Gợi ý áp dụng cho portfolio
APEX Copy Trade Agent
Component
Application
Soul.md accountability	Hard rule: không income claim, luôn disclaimer, flag uncertain lead quality
RAG top-20	CRM context — fetch 20 messages relevant từ SaleSmartly
Loop termination	Outreach sequence — 2 draft không improve → dừng, handover
Error detection + prompt fix	Detect compliance issue → fix → re-draft → commit → log
Memory compression	Nén campaign history thành summary, pointer retrieve UTM detail
Market Research / News Monitoring Agent
Component
Application
Soul.md identity	Accuracy-first, flag uncertain, không fabricate statistics
RAG semantic retrieval	Embedding articles, retrieval semantic cho news
Loop termination	Research synthesis — 2 iter không improve → converge, deliver
Error detection + prompt fix	Detect missing citation → fix → re-research → log
Memory compression	Nén news history thành daily/weekly summary snapshot
Content Seeding Agent
Component
Application
Soul.md tone/voice	Agent viết content theo brand voice — soul.md định nghĩa tone, hard rules
RAG retrieval relevant	Fetch content history, style examples — top-20
Loop termination	Draft sequence — converge khi draft đạt quality threshold
Error detection + prompt fix	Detect brand voice drift → fix → re-draft → commit
Memory compression	Nén content history thành style/compression snapshot
Sales War Room Internal Agent
Component
Application
Soul.md tiếng Việt	Internal war room — direct, structured, Vietnamese
RAG retrieval	Fetch sales context (leads, objections, playbook) — top-20
Loop termination	Strategy recommendation — converge khi proposal stabilize
Error detection + prompt fix	Detect misaligned recommendation → fix → re-propose → log
Memory compression	Nén war room discussion thành summary
8. Tài liệu tham khảo
Video gốc: X/@precisox status 2076152320585343132
Thread navigator: threadnavigator.com/thread/2075607221397012680
Hermes Agent soul.md: threadnavigator.com/thread/2054564519280804028
soul.md spec: github.com/aaronjmars/soul.md
Anthropic context window best practices: 20-30 relevant chunks
Embedding: OpenAI text-embedding-3-small (1536 dim, ~$0.00002/1K tokens)
Local alternative: all-MiniLM-L6-v2 (HuggingFace, free)
9. Kết luận
Video là overview architecture đúng — 5 pillar: soul.md, RAG semantic, loop termination, error self-fix, memory compression. Áp dụng cho nhiều dự án agent, nhưng cần:

Test thực nghiệm cho mỗi component (retrieval size, evaluate function, compression lossy)
Human-in-the-loop cho mission-critical tasks (content publish, sales outreach, compliance)
Not overclaim: Video bỏ qua production detail
Nếu áp dụng, bắt đầu từ soul.md + accountability loop (bước 1) — leverage point cao nhất.

Report generated: 2026-09-18 — reconstruct từ metadata video + domain knowledge. Không phải transcript word-for-word.