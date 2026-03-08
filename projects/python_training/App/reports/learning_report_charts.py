←
←
"""
Generate a chart-based learning report (PDF) for the first versions of Task1–Task4.

Dependencies:
    pip install matplotlib

Run:
    cd /Users/longe/Desktop/demo/App
    python3 learning_report_charts.py

Output:
    learning_report_task1_4.pdf  (saved in the same directory)
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np


def get_score_data():
    """Return score data for this mini assessment."""
    sections = [
        "Theory MCQ",
        "Task1 /test",
        "Task2 /translation",
        "Task3 /time",
        "Task4 /echo",
        "Debug /api/bad",
    ]
    scores = np.array([10, 7, 9, 7, 3, 6], dtype=float)
    full = 10.0
    return sections, scores, full


def page_summary(ax, sections, scores, full_mark):
    """Page 1: Overall summary."""
    ax.set_axis_off()

    avg = scores.mean()
    total_ratio = avg / full_mark
    overall = int(round(total_ratio * 100))

    text_lines = [
        "Flask Practice Assessment Report (Task1–Task4, First Versions Only)",
        "",
        f"Overall score (approx.): {overall} / 100",
        "",
        f"Average score per section: {avg:.2f} / {full_mark}",
        "",
        "Strengths:",
        "- Solid understanding of HTTP / Flask / CORS / JSON concepts.",
        "- Can translate task requirements into endpoint design and response structures.",
        "",
        "Areas for improvement:",
        "- Python / Flask syntax details (methods argument, function call parentheses, None checks).",
        "- Systematic handling of invalid JSON, missing fields, and other edge cases.",
    ]

    ax.text(
        0.02,
        0.95,
        "\n".join(text_lines),
        fontsize=10,
        va="top",
        ha="left",
        wrap=True,
    )


def page_bar_scores(ax, sections, scores, full_mark):
    """Page 2: Bar chart of scores by task."""
    x = np.arange(len(sections))
    width = 0.6

    ax.bar(x, scores, width=width, color="#4C72B0", label="Score")
    ax.axhline(full_mark, linestyle="--", color="gray", linewidth=1, label="Full mark")

    ax.set_xticks(x)
    ax.set_xticklabels(sections, rotation=30, ha="right", fontsize=8)
    ax.set_ylim(0, full_mark + 1)
    ax.set_ylabel("Score (out of 10)")
    ax.set_title("Scores by section")
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.legend(loc="lower right", fontsize=8)

    for xi, s in zip(x, scores):
        ax.text(xi, s + 0.1, f"{s:.0f}", ha="center", va="bottom", fontsize=8)


def page_radar(ax, sections, scores, full_mark):
    """Page 3: Radar chart showing strengths and weaknesses."""
    # Choose 5 representative dimensions (merging related ones)
    labels = ["Theory", "Simple endpoint", "Error handling", "Time endpoint", "Echo/robustness"]

    # Map original scores into 5 dimensions (rough visualization)
    theory = scores[0]
    simple_endpoint = scores[1]
    error_handling = scores[2]  # translation 400 case
    time_endpoint = scores[3]
    echo_robust = (scores[4] + scores[5]) / 2.0  # echo + debug task

    data = np.array(
        [theory, simple_endpoint, error_handling, time_endpoint, echo_robust],
        dtype=float,
    )

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    data = np.concatenate((data, [data[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    ax.plot(angles, data, "o-", linewidth=2, color="#55A868", label="Current level")
    ax.fill(angles, data, alpha=0.25, color="#55A868")

    ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels, fontsize=9)
    ax.set_ylim(0, full_mark)
    ax.set_title("Skill radar overview")
    ax.grid(True, linestyle="--", alpha=0.4)


def page_detail_text(ax):
    """Page 4: Detailed comments per section."""
    ax.set_axis_off()
    lines = [
        "Detailed comments (first versions only):",
        "",
        "1. Theory MCQ (10/10)",
        "   - Correct understanding of HTTP methods, status codes, CORS, request.get_json(), etc.",
        "   - Shows that conceptual foundation is strong enough to support practical work.",
        "",
        "2. Task1 `/test` (7/10)",
        "   - Response fields are well-designed and reflect the request method and endpoint health.",
        "   - Key issue: route definition uses multiple lists for the methods argument, causing a SyntaxError.",
        "",
        "3. Task2 `/api/translation` (9/10)",
        "   - Cleanly separates success, missing prompt, and unexpected error with 200/400/500.",
        "   - Further improvement: handle data is None (invalid JSON) explicitly with a 400 response.",
        "",
        "4. Task3 `/api/time` (7/10)",
        "   - Path, method, and response structure are correct; issue is in the datetime.now() call.",
        "   - This 'missing parentheses' bug is very common early on; reading traceback carefully helps.",
        "",
        "5. Task4 `/api/echo` (3/10)",
        "   - Shows awareness of distinguishing valid/invalid JSON, but syntax and logic diverge from the spec.",
        "   - Key improvements: check data is None, echo back client JSON instead of hardcoding, and use 400.",
        "",
        "6. Debug task `/api/bad` (6/10)",
        "   - Correctly identifies that name may be missing and uses data.get('name', '') as a fix.",
        "   - Next step: also consider data being None and unify defensive patterns around request.get_json().",
    ]
    ax.text(
        0.02,
        0.98,
        "\n".join(lines),
        fontsize=9,
        va="top",
        ha="left",
        wrap=True,
    )


def build_pdf(output_path: Path):
    sections, scores, full_mark = get_score_data()

    with PdfPages(output_path) as pdf:
        # Page 1: Summary text
        fig, ax = plt.subplots(figsize=(8.27, 11.69))  # A4 portrait
        page_summary(ax, sections, scores, full_mark)
        pdf.savefig(fig, bbox_inches="tight")
        plt.close(fig)

        # Page 2: Bar chart
        fig, ax = plt.subplots(figsize=(8.27, 5))
        page_bar_scores(ax, sections, scores, full_mark)
        pdf.savefig(fig, bbox_inches="tight")
        plt.close(fig)

        # Page 3: Radar chart
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111, polar=True)
        page_radar(ax, sections, scores, full_mark)
        pdf.savefig(fig, bbox_inches="tight")
        plt.close(fig)

        # Page 4: Detail text
        fig, ax = plt.subplots(figsize=(8.27, 11.69))
        page_detail_text(ax)
        pdf.savefig(fig, bbox_inches="tight")
        plt.close(fig)


def main():
    out = Path(__file__).with_name("learning_report_task1_4.pdf")
    build_pdf(out)
    print(f"Generated PDF report: {out}")


if __name__ == "__main__":
    main()


