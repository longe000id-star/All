←
←
import streamlit as st
from groq import Groq
import json
import datetime
import random
import time
import os

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Personal Language Learning Assistant",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --bg: #0b0e17;
    --surface: #141824;
    --surface2: #1c2236;
    --accent: #4f8cff;
    --accent2: #a78bfa;
    --gold: #f5c542;
    --green: #34d399;
    --red: #f87171;
    --text: #e2e8f0;
    --muted: #64748b;
    --border: #1e2a42;
}

html, body, [class*="css"] {
    font-family: 'Sora', sans-serif;
    background-color: var(--bg);
    color: var(--text);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f1320 0%, #141824 100%);
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stRadio label {
    color: var(--muted) !important;
    font-size: 0.75rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

/* Headers */
h1, h2, h3 { font-family: 'Sora', sans-serif; font-weight: 700; }

/* Cards */
.card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
}
.card-accent {
    border-left: 3px solid var(--accent);
}
.card-gold {
    border-left: 3px solid var(--gold);
}
.card-green {
    border-left: 3px solid var(--green);
}
.card-purple {
    border-left: 3px solid var(--accent2);
}

/* Stat boxes */
.stat-row { display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
.stat-box {
    flex: 1; min-width: 110px;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1rem;
    text-align: center;
}
.stat-val { font-size: 1.9rem; font-weight: 700; color: var(--accent); }
.stat-lbl { font-size: 0.7rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.06em; margin-top: 2px; }

/* Badges */
.badge {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    margin-right: 4px;
}
.badge-blue  { background: rgba(79,140,255,0.15); color: var(--accent); border: 1px solid rgba(79,140,255,0.3); }
.badge-green { background: rgba(52,211,153,0.15); color: var(--green);  border: 1px solid rgba(52,211,153,0.3); }
.badge-gold  { background: rgba(245,197,66,0.15);  color: var(--gold);   border: 1px solid rgba(245,197,66,0.3); }
.badge-purple{ background: rgba(167,139,250,0.15); color: var(--accent2);border: 1px solid rgba(167,139,250,0.3);}

/* Code / mono */
.mono { font-family: 'JetBrains Mono', monospace; }

/* Score bar */
.score-bar-bg { background: var(--border); border-radius: 6px; height: 8px; margin: 6px 0 2px; }
.score-bar-fill { height: 8px; border-radius: 6px; background: linear-gradient(90deg, var(--accent), var(--accent2)); }

/* Streamlit overrides */
.stButton > button {
    background: linear-gradient(135deg, var(--accent), #3b6fd4);
    color: white;
    border: none;
    border-radius: 8px;
    font-family: 'Sora', sans-serif;
    font-weight: 600;
    padding: 0.5rem 1.5rem;
    transition: opacity 0.2s;
}
.stButton > button:hover { opacity: 0.85; }
.stTextArea textarea, .stTextInput input {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    border-radius: 8px !important;
    font-family: 'Sora', sans-serif !important;
}
.stSelectbox > div > div {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
}

/* Section titles */
.section-title {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
}

/* AI response box */
.ai-response {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent2);
    border-radius: 10px;
    padding: 1.25rem 1.5rem;
    line-height: 1.75;
    font-size: 0.95rem;
    white-space: pre-wrap;
}

/* Progress ring placeholder */
.ring-label {
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--green);
    text-align: center;
}
.ring-sub {
    font-size: 0.7rem;
    color: var(--muted);
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
</style>
""", unsafe_allow_html=True)


# ── Session state init ────────────────────────────────────────────────────────
def _init():
    defaults = {
        "history": [],          # [{role, content, ts, skill, lang}]
        "scores": [],           # [{date, skill, score, lang}]
        "streak": 0,
        "total_sessions": 0,
        "vocab_words": [],      # [{word, lang, added}]
        "active_lang": "日本語 (Japanese)",
        "active_skill": "Vocabulary",
        "study_plan": [],
        "last_active": None,
        "api_key": "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

_init()

# ── Helpers ───────────────────────────────────────────────────────────────────
LANGUAGES = [
    "日本語 (Japanese)", "中文 (Chinese)", "한국어 (Korean)",
    "Español (Spanish)", "Français (French)", "Deutsch (German)",
    "Italiano (Italian)", "Português (Portuguese)", "العربية (Arabic)",
    "Русский (Russian)",
]

SKILLS = ["Vocabulary", "Grammar", "Listening Comprehension",
          "Reading", "Writing", "Speaking Practice", "Translation", "Culture & Context"]

SKILL_ICONS = {
    "Vocabulary": "📚", "Grammar": "🔧", "Listening Comprehension": "👂",
    "Reading": "📖", "Writing": "✍️", "Speaking Practice": "🎤",
    "Translation": "🔄", "Culture & Context": "🌸",
}

LEVELS = ["Beginner (A1-A2)", "Elementary (A2-B1)", "Intermediate (B1-B2)",
          "Upper-Intermediate (B2-C1)", "Advanced (C1-C2)"]

def get_client():
    key = st.session_state.get("api_key") or os.environ.get("GROQ_API_KEY", "")
    if not key:
        return None
    return Groq(api_key=key)

def call_claude(system_prompt: str, user_msg: str, max_tokens=1200) -> str:
    client = get_client()
    if not client:
        return "⚠️ API key not set. Please add your Groq API key in the sidebar Settings."
    try:
        resp = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=max_tokens,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_msg},
            ],
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"⚠️ API error: {e}"

def record_score(skill: str, lang: str, score: int):
    st.session_state.scores.append({
        "date": datetime.date.today().isoformat(),
        "skill": skill,
        "lang": lang,
        "score": score,
    })

def avg_score(skill=None):
    s = st.session_state.scores
    if skill:
        s = [x for x in s if x["skill"] == skill]
    return round(sum(x["score"] for x in s) / len(s), 1) if s else 0

def update_streak():
    today = datetime.date.today().isoformat()
    if st.session_state.last_active != today:
        st.session_state.streak += 1
        st.session_state.total_sessions += 1
        st.session_state.last_active = today


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🌐 LinguaCore")
    st.markdown("<span class='badge badge-purple'>Personal · Private</span>", unsafe_allow_html=True)
    st.divider()

    st.markdown("<div class='section-title'>Language</div>", unsafe_allow_html=True)
    st.session_state.active_lang = st.selectbox(
        "Target language", LANGUAGES,
        index=LANGUAGES.index(st.session_state.active_lang), label_visibility="collapsed"
    )

    st.markdown("<div class='section-title'>Skill Focus</div>", unsafe_allow_html=True)
    st.session_state.active_skill = st.selectbox(
        "Skill", SKILLS,
        index=SKILLS.index(st.session_state.active_skill), label_visibility="collapsed"
    )

    level = st.selectbox("Level", LEVELS, index=2)

    st.divider()
    st.markdown("<div class='section-title'>⚙️ Settings</div>", unsafe_allow_html=True)
    api_input = st.text_input("Anthropic API Key", type="password",
                              value=st.session_state.api_key,
                              placeholder="sk-ant-…")
    if api_input:
        st.session_state.api_key = api_input

    st.divider()
    # Quick stats
    st.markdown("<div class='section-title'>Stats</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c1.metric("🔥 Streak", f"{st.session_state.streak}d")
    c2.metric("📊 Sessions", st.session_state.total_sessions)
    if st.session_state.scores:
        st.metric("⭐ Avg Score", f"{avg_score()}%")


# ── Main layout ───────────────────────────────────────────────────────────────
lang  = st.session_state.active_lang
skill = st.session_state.active_skill
icon  = SKILL_ICONS.get(skill, "🎯")

st.markdown(f"# {icon} {skill}")
st.markdown(
    f"<span class='badge badge-blue'>{lang}</span>"
    f"<span class='badge badge-gold'>{level}</span>"
    f"<span class='badge badge-green'>Active Session</span>",
    unsafe_allow_html=True
)
st.write("")

tab_practice, tab_test, tab_vocab, tab_plan, tab_history, tab_dashboard = st.tabs(
    ["✨ Practice", "📝 Test", "📚 Vocab Bank", "📅 Study Plan", "💬 History", "📊 Dashboard"]
)


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 1 — PRACTICE
# ═══════════════════════════════════════════════════════════════════════════════
with tab_practice:
    st.markdown("<div class='section-title'>Session Setup</div>", unsafe_allow_html=True)

    col_left, col_right = st.columns([2, 1])
    with col_left:
        focus = st.text_area(
            "What would you like to practice? (optional context / material)",
            placeholder="E.g. JLPT N3 grammar patterns, business email vocabulary, daily conversation…",
            height=90,
        )
        mode = st.radio(
            "Practice mode",
            ["Generate exercises", "Free conversation", "Explain a concept", "Drill & repeat"],
            horizontal=True,
        )
    with col_right:
        num_ex = st.slider("Number of items", 3, 10, 5)
        native_lang = st.selectbox("Explanations in", ["English", "中文", "日本語", "한국어", "Español"])

    if st.button("🚀 Start Practice", use_container_width=False):
        update_streak()
        system = f"""You are an expert {lang} language tutor specializing in {skill}.
The student's level is {level}.
Provide clear, structured, engaging content.
When generating exercises, number them and include answers/explanations at the end.
Use {native_lang} for meta-instructions and explanations.
Keep responses focused, practical, and encouraging."""

        if mode == "Generate exercises":
            prompt = f"Generate {num_ex} {skill} exercises for a {level} student of {lang}. Topic/context: {focus or 'general'}"
        elif mode == "Free conversation":
            prompt = f"Start a natural conversation practice session in {lang} for a {level} student. Topic: {focus or 'everyday life'}"
        elif mode == "Explain a concept":
            prompt = f"Explain this {lang} concept clearly with examples at {level}: {focus or 'a key grammar point for this level'}"
        else:
            prompt = f"Create a drill-and-repeat exercise set ({num_ex} items) for {lang} {skill}. Focus: {focus or 'common patterns'}"

        with st.spinner("Generating practice content…"):
            result = call_claude(system, prompt, max_tokens=1500)

        st.markdown("<div class='section-title'>Practice Content</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='ai-response'>{result}</div>", unsafe_allow_html=True)

        # Save to history
        st.session_state.history.append({
            "role": "Practice", "content": result,
            "ts": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "skill": skill, "lang": lang,
        })

    st.divider()
    st.markdown("<div class='section-title'>Ask Anything</div>", unsafe_allow_html=True)
    user_q = st.text_input("Quick question", placeholder="Why does this sentence use は instead of が?")
    if st.button("Ask") and user_q:
        sys2 = f"You are a patient, expert {lang} tutor. Level: {level}. Answer concisely and accurately."
        with st.spinner("Thinking…"):
            ans = call_claude(sys2, user_q, max_tokens=800)
        st.markdown(f"<div class='ai-response'>{ans}</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 2 — TEST
# ═══════════════════════════════════════════════════════════════════════════════
with tab_test:
    st.markdown("<div class='section-title'>Auto-Generated Test</div>", unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        test_type = st.selectbox("Test type", [
            "Multiple choice (4 options)",
            "Fill-in-the-blank",
            "Translation (target → native)",
            "Translation (native → target)",
            "Error correction",
            "Short answer"
        ])
        test_topic = st.text_input("Topic / material scope (optional)",
                                   placeholder="Chapter 5 vocabulary, past tense verbs…")
    with col_b:
        q_count = st.slider("Questions", 5, 20, 10)
        timed = st.checkbox("Timed mode (display timer)", value=False)

    if st.button("📝 Generate Test", use_container_width=False):
        sys_test = f"""You are an automated test generator for {lang} learners.
Level: {level}. Skill: {skill}.
Generate a well-structured {test_type} test with exactly {q_count} questions.
Format: number each question clearly. After all questions, provide an ANSWER KEY section.
Make questions progressively slightly harder. Topic scope: {test_topic or 'general ' + skill}."""

        prompt_test = f"Generate the test now."
        with st.spinner("Generating test…"):
            test_content = call_claude(sys_test, prompt_test, max_tokens=2000)

        if timed:
            st.info(f"⏱️ Suggested time: {q_count * 90} seconds")

        st.markdown("<div class='section-title'>Your Test</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='ai-response'>{test_content}</div>", unsafe_allow_html=True)

        st.session_state.history.append({
            "role": "Test", "content": test_content,
            "ts": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "skill": skill, "lang": lang,
        })

    st.divider()
    st.markdown("<div class='section-title'>Submit & Score Your Answers</div>", unsafe_allow_html=True)
    with st.expander("Paste your answers for AI grading"):
        test_ref   = st.text_area("Original test questions (paste here)", height=120)
        user_ans   = st.text_area("Your answers (paste here)", height=120)
        if st.button("🎯 Grade My Answers") and user_ans and test_ref:
            sys_grade = f"""You are a strict but fair {lang} language examiner.
Grade the student's answers. Provide: overall score (0-100), per-question feedback,
common error patterns, and 2-3 targeted improvement suggestions. Level: {level}."""
            prompt_grade = f"TEST:\n{test_ref}\n\nSTUDENT ANSWERS:\n{user_ans}"
            with st.spinner("Grading…"):
                grade_result = call_claude(sys_grade, prompt_grade, max_tokens=1500)
            st.markdown(f"<div class='ai-response'>{grade_result}</div>", unsafe_allow_html=True)

            # Try to extract numeric score
            import re
            nums = re.findall(r'\b([0-9]{1,3})\s*(?:/\s*100|%|out of 100)', grade_result)
            if nums:
                record_score(skill, lang, int(nums[0]))
                st.success(f"✅ Score recorded: {nums[0]}%")


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 3 — VOCAB BANK
# ═══════════════════════════════════════════════════════════════════════════════
with tab_vocab:
    st.markdown("<div class='section-title'>Vocabulary Bank</div>", unsafe_allow_html=True)

    col_v1, col_v2 = st.columns([2, 1])
    with col_v1:
        new_words = st.text_area(
            "Add words / phrases (one per line)",
            placeholder="食べる\n勉強する\n難しい",
            height=100,
        )
        if st.button("➕ Add to Bank") and new_words:
            for w in new_words.strip().splitlines():
                w = w.strip()
                if w:
                    st.session_state.vocab_words.append({
                        "word": w, "lang": lang,
                        "added": datetime.date.today().isoformat()
                    })
            st.success(f"Added {len(new_words.strip().splitlines())} words!")
    with col_v2:
        st.markdown(f"""
        <div class='card card-gold'>
          <div class='stat-val'>{len(st.session_state.vocab_words)}</div>
          <div class='stat-lbl'>Words in bank</div>
        </div>""", unsafe_allow_html=True)

    if st.session_state.vocab_words:
        st.markdown("<div class='section-title'>AI Vocab Actions</div>", unsafe_allow_html=True)
        vcol1, vcol2, vcol3 = st.columns(3)
        bank_words_str = "\n".join(x["word"] for x in st.session_state.vocab_words[-30:])

        if vcol1.button("📖 Explain & Translate"):
            sys_v = f"You are a {lang} vocabulary coach. For each word, provide: reading/pronunciation, meaning, example sentence. Level: {level}."
            with st.spinner():
                vr = call_claude(sys_v, f"Words:\n{bank_words_str}")
            st.markdown(f"<div class='ai-response'>{vr}</div>", unsafe_allow_html=True)

        if vcol2.button("🃏 Flashcard Quiz"):
            sys_v = f"Create a 10-question flashcard quiz from these {lang} words. Format: Question | Expected answer. Shuffle word→meaning and meaning→word."
            with st.spinner():
                vr = call_claude(sys_v, f"Words:\n{bank_words_str}")
            st.markdown(f"<div class='ai-response'>{vr}</div>", unsafe_allow_html=True)

        if vcol3.button("✍️ Story Generator"):
            sys_v = f"Write a short, engaging story (8-10 sentences) in {lang} using as many of the vocabulary words as possible. Then provide a translation. Level: {level}."
            with st.spinner():
                vr = call_claude(sys_v, f"Vocabulary:\n{bank_words_str}")
            st.markdown(f"<div class='ai-response'>{vr}</div>", unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='section-title'>Word List</div>", unsafe_allow_html=True)
        for i, item in enumerate(reversed(st.session_state.vocab_words[-50:])):
            col_w, col_l, col_d = st.columns([3, 1, 1])
            col_w.write(item["word"])
            col_l.markdown(f"<span class='badge badge-blue'>{item['lang'][:2]}</span>", unsafe_allow_html=True)
            col_d.caption(item["added"])


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 4 — STUDY PLAN
# ═══════════════════════════════════════════════════════════════════════════════
with tab_plan:
    st.markdown("<div class='section-title'>Personalized Study Plan</div>", unsafe_allow_html=True)

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        goal = st.text_input("Learning goal",
            placeholder="Pass JLPT N3 in 6 months, hold a business conversation…")
        hours_week = st.slider("Hours available per week", 1, 20, 7)
    with col_p2:
        weak_areas = st.multiselect("Weak areas to focus on", SKILLS,
                                    default=["Vocabulary", "Grammar"])
        duration_weeks = st.slider("Plan duration (weeks)", 2, 52, 12)

    if st.button("🗓️ Generate Study Plan"):
        sys_plan = f"""You are a professional language learning curriculum designer.
Create a detailed {duration_weeks}-week study plan for {lang} at {level}.
Available study time: {hours_week} hours/week.
Weak areas: {', '.join(weak_areas) or 'general'}.
Goal: {goal or 'overall fluency improvement'}.

Structure the plan with:
- Weekly themes and goals
- Daily activity breakdown (listening, reading, writing, speaking)
- Specific resource types to use
- Milestone checkpoints every 2-4 weeks
- Recommended review intervals for vocabulary (spaced repetition)"""

        with st.spinner("Building your plan…"):
            plan = call_claude(sys_plan, "Generate the plan now.", max_tokens=2500)

        st.session_state.study_plan = plan
        st.markdown(f"<div class='ai-response'>{plan}</div>", unsafe_allow_html=True)

    elif st.session_state.study_plan:
        st.markdown("**Last generated plan:**")
        st.markdown(f"<div class='ai-response'>{st.session_state.study_plan}</div>", unsafe_allow_html=True)

    st.divider()
    st.markdown("<div class='section-title'>Today's Tasks</div>", unsafe_allow_html=True)
    today_tasks = [
        f"📖 Read 1 passage in {lang} (15 min)",
        f"📚 Review/add 10 vocabulary words",
        f"🔧 Complete 5 grammar exercises",
        f"🎤 Record yourself speaking for 2 minutes",
        f"✍️ Write 5 sentences using today's vocab",
    ]
    for task in today_tasks:
        done = st.checkbox(task, key=f"task_{task}")


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 5 — HISTORY
# ═══════════════════════════════════════════════════════════════════════════════
with tab_history:
    st.markdown("<div class='section-title'>Session History</div>", unsafe_allow_html=True)

    if not st.session_state.history:
        st.info("No history yet. Complete a practice or test session to see it here.")
    else:
        for item in reversed(st.session_state.history[-20:]):
            badge_cls = "badge-blue" if item["role"] == "Practice" else "badge-gold"
            with st.expander(
                f"{item['ts']} · {item['skill']} · {item['lang']}"
            ):
                st.markdown(
                    f"<span class='badge {badge_cls}'>{item['role']}</span>",
                    unsafe_allow_html=True
                )
                st.write(item["content"][:1200] + ("…" if len(item["content"]) > 1200 else ""))

    if st.session_state.history and st.button("🗑️ Clear history"):
        st.session_state.history = []
        st.rerun()


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 6 — DASHBOARD
# ═══════════════════════════════════════════════════════════════════════════════
with tab_dashboard:
    st.markdown("<div class='section-title'>Performance Overview</div>", unsafe_allow_html=True)

    # Summary stats
    total_tests    = len([x for x in st.session_state.history if x["role"] == "Test"])
    total_practice = len([x for x in st.session_state.history if x["role"] == "Practice"])
    avg_all        = avg_score()

    st.markdown(f"""
    <div class='stat-row'>
      <div class='stat-box'>
        <div class='stat-val'>{st.session_state.streak}</div>
        <div class='stat-lbl'>Day Streak</div>
      </div>
      <div class='stat-box'>
        <div class='stat-val'>{st.session_state.total_sessions}</div>
        <div class='stat-lbl'>Sessions</div>
      </div>
      <div class='stat-box'>
        <div class='stat-val'>{total_practice}</div>
        <div class='stat-lbl'>Practices</div>
      </div>
      <div class='stat-box'>
        <div class='stat-val'>{total_tests}</div>
        <div class='stat-lbl'>Tests</div>
      </div>
      <div class='stat-box'>
        <div class='stat-val'>{avg_all or "—"}{'%' if avg_all else ''}</div>
        <div class='stat-lbl'>Avg Score</div>
      </div>
      <div class='stat-box'>
        <div class='stat-val'>{len(st.session_state.vocab_words)}</div>
        <div class='stat-lbl'>Vocab Words</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Per-skill scores
    st.markdown("<div class='section-title'>Scores by Skill</div>", unsafe_allow_html=True)
    for s in SKILLS:
        a = avg_score(s)
        pct = int(a)
        st.markdown(f"""
        <div style='margin-bottom:0.6rem;'>
          <div style='display:flex;justify-content:space-between;font-size:0.82rem;'>
            <span>{SKILL_ICONS[s]} {s}</span>
            <span class='mono' style='color:var(--accent)'>{pct}%</span>
          </div>
          <div class='score-bar-bg'>
            <div class='score-bar-fill' style='width:{pct}%'></div>
          </div>
        </div>""", unsafe_allow_html=True)

    # Recent scores table
    if st.session_state.scores:
        st.markdown("<div class='section-title'>Recent Test Scores</div>", unsafe_allow_html=True)
        import pandas as pd
        df = pd.DataFrame(st.session_state.scores[-15:])
        st.dataframe(df, use_container_width=True, hide_index=True)

    # Adaptive suggestions
    st.markdown("<div class='section-title'>AI Feedback & Suggestions</div>", unsafe_allow_html=True)
    if st.button("🔍 Generate Adaptive Suggestions"):
        score_summary = json.dumps(st.session_state.scores[-20:]) if st.session_state.scores else "No scores yet"
        sys_fb = f"You are a data-driven language learning coach. Analyze the student's performance data and provide 3-5 specific, actionable improvement suggestions. Be direct and practical."
        prompt_fb = f"Language: {lang}, Level: {level}\nRecent scores: {score_summary}\nSessions completed: {st.session_state.total_sessions}"
        with st.spinner("Analyzing…"):
            fb = call_claude(sys_fb, prompt_fb, max_tokens=600)
        st.markdown(f"<div class='ai-response'>{fb}</div>", unsafe_allow_html=True)

    if not st.session_state.scores:
        st.info("Complete some tests to unlock adaptive suggestions and score charts.")
