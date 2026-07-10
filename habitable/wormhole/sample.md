---
marp: true
theme: default
class: lead
paginate: true               # ページ番号（スライド番号）を表示
backgroundColor: "#ffffff"   # 画像が読み込めなかったときの背景色
color: "#000000"             # 文字色を黒に設定
style: |
  /* ──────────────────────────────────────
     カスタム CSS
     ────────────────────────────────────── */

  /* ① 背景画像を全スライドに適用 */
  section {
    background-image: url('https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
  }

  /* ② 文字色を黒に統一（見出し・本文） */
  h1, h2, h3, h4, h5, h6,
  p, li, blockquote, code {
    color: #000000 !important;
  }

  /* ③ ページ番号の文字色も黒に */
  .marp-pagination {
    color: #000000 !important;
  }

  /* ④ 必要なら文字の可読性を上げるための影を付ける */
  .lead, .lead * {
    text-shadow: 0 0 3px rgba(255,255,255,0.8);
  }
---

# タイトルスライド

## プレゼンテーションの概要

- 背景は気の利いた画像
- 文字は黒で見やすく

---

# セクション 1

- ポイント A
- ポイント B
- ポイント C

---

# セクション 2

> 「引用文」や強調したいテキストは黒のまま

---

# まとめ

- 背景画像は全スライドで共通
- 文字は黒で統一
- ページ番号も黒で表示

---

# Q&A

ご質問はスライド右下の QR コードからどうぞ。
