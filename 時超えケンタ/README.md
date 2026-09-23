# 🌌 時超えケンタ / Project HZ Trek: PhysicalAI Simulator

> **ハードSF数値解析漫画「時超えケンタ」の世界観をベースにした、物理法則＋AI共創型インタラクティブ・シミュレーションゲーム**

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Jupyter Support](https://img.shields.io/badge/Jupyter-Supported-orange.svg)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📖 概要 (Overview)

西暦2075年。水星ダイソン環（1.64PW）の光圧加速を受け、光速の20%（0.2c）で4.2光年先のプロキシマ・ケンタウリ系へ出航した自律PhysicalAI **「時超えケンタ」**。

本プロジェクトは、原作漫画の「正史」ストーリーを追体験しながら、プレイヤーの自由な発想（フリープロンプト）によって新しい物理的IFルートを開拓・データベース化していくゲームエンジンです。

---

## ✨ 主な特長 (Key Features)

1. **「正史」一本道 ＆ AI分岐のハイブリッド構造**
   
   - **`game.next()`** を実行するだけで、正史ストーリーと漫画コマを2〜4ページごとの節目（ノード）でサクサク進められます。
   - 気になる場面で **`game.submit("自由な作戦...")`** を入力すると、AI（Gemini API等）が特殊相対論・熱力学に則ってリアルタイム判定し、新たな選択肢と分岐を展開します。

2. **軽量な GitHub 親和型データ設計**
   
   - リポジトリ内には重い大容量画像を無理に格納する必要はありません。
   - シナリオ・漫画描画プロンプト・物理設定はすべて標準の **`kenta_game_db.json`** に格納されています。

3. **オンデマンド画像描画 & ローカル自動キャッシュ**
   
   - ローカルに漫画画像（`manga/*.png`）が存在すれば **0秒即表示**。
   - 画像が無い場合でも、APIキーを設定しておけば**AI（Gemini API）がその場で漫画コマを描画してローカル保存**。APIキーが無い場合でも**ビジュアルノベル風のコマ枠表示**でスムーズにプレイ可能です。

4. **マルチ環境対応（Jupyter Notebook & Python CLI）**
   
   - Jupyter Notebook / Google Colab でのインタラクティブ表示はもちろん、標準の Python ターミナル（CLI）だけでも完全に動作します。
   - Maxima 数式処理環境が無くても、Python内蔵の物理モジュールが自動計算（フォールバック）します。

---

## 📂 フォルダ構成 (Repository Structure)

```text
.
├── kenta_game_sim.py     # ゲームエンジン本体 (Python 3)
├── kenta_game_db.json    # 全シナリオ・描画プロンプト・物理マスターDB
├── kenta_game_sim.md     # Jupyter Notebook コピペ用単体コード
├── README.md             # 本ドキュメント
└── manga/                # 漫画画像用サブフォルダ (任意・自動検索対象)
    ├── kenta_ep1_page1_manga.png
    ├── kenta_ep1_page2_manga.png
    └── ...
```

---

## 🚀 クイックスタート (Quick Start)

### 1. Jupyter Notebook / Google Colab で遊ぶ場合（推奨）

ノートブック（`.ipynb`）と同じフォルダに `kenta_game_sim.py` と `kenta_game_db.json` を配置します。

```python
# 【セル 1】エンジンの起動
%run kenta_game_sim.py

# 【セル 2】Enter感覚で正史を次の場面（2〜4ページ）へ進める
game.next()

# 【セル 3】正史の選択肢を選ぶ場合 (例: 1番を選択)
game.select(1)

# 【セル 4】アドリブで自由な作戦を試す場合
game.submit("0.1cに減速して摩擦熱を低減したい")
```

---

### 2. Python ターミナル（CLI）だけで遊ぶ場合

Jupyter や GUI 環境が無くても、ターミナルから直接起動してプレイ可能です。

```bash
python3 kenta_game_sim.py
```

---

## ⚙️ ユーザー設定 (`USER_CONFIG`)

`kenta_game_sim.py` の冒頭にある `USER_CONFIG` で、画像生成モードやAPIキーを自由に変更できます。

```python
USER_CONFIG = {
    # 画像生成モード: "AUTO" (自動判定), "OFF" (生成なし/テキスト枠), "GEMINI" (Geminiで生成)
    "IMAGE_GEN_MODE": "AUTO",

    # Gemini APIキー (空文字 "" の場合は内蔵ローカルシミュレータで動きます)
    "GEMINI_API_KEY": "",

    # 画像の保存先・検索先サブフォルダ名
    "IMAGE_SAVE_DIR": "manga"
}
```

---

## 🧠 物理エンジンと共創データベース (PhysicalAI & DB)

本ゲームで開拓された新しい分岐ルートは、すべて **`kenta_game_db.json`** に自動保存されます。

- **相対論的運動エネルギー**: $E_k = (\gamma - 1) m_p c^2$
- **磁気シールド熱収支**: $P_{\text{mag}} \propto B^2$, 排熱ラジエーター温度限界 $1200\,\text{K}$
- **通信遅延**: $d_{\text{delay}} = 2 \times \frac{r}{c}$ （光年距離に応じた往復年数）

あなたがフリープロンプトで発見した面白い作戦やIFルートが記録された `kenta_game_db.json` は、Pull Request を送ることで公式データベースへ統合・共有できます！

---

## 📜 ライセンス (License)

[MIT License](LICENSE)

---

**Project HZ Trek / 時超えケンタ Production Team** by みらいテック
