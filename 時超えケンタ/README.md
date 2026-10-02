# 『時超えケンタ (CHRONO KENTA)』 Ver 3.0 (jv3) システム概要

ハードSF数値解析アドベンチャー『時超えケンタ』の JupyterLab 実行環境（Ver 3.0）の利用ガイドです。

---

## 🌌 概要・設計思想

本システムは、サグラダ・ファミリア型の「データ駆動アーキテクチャ」を採用しています。
ゲームエンジン本体（Python/GUI）と、シナリオデータ・物理パラメータ・画像アセットを完全に分離・独立させており、エンジンコードを変更することなく、シナリオの追加やアセットの更新が可能です。

---

## 📁 ディレクトリ構造 & 構成ファイル

```text
chrono-kenta/
├── README.md                     # 本ドキュメント
├── kenta_game_jv3.py            # ゲームUI・実行エンジン (JupyterLab対応)
├── kenta_scenario_master.json   # 正史マスターシナリオ
├── build_adhoc_scenario.py     # Ad-hocカスタムシナリオ自動連結ツール
├── sim_code/                    # 💻 タスクID別・数値解析計算コード群
│   ├── sim_3002_MER12.py        # プロローグ: 1.64PW光圧レーザー推進＆照射ブレ
│   ├── sim_C110_MER16.py        # 第1話: 陰解法熱伝導＆CFL爆発
│   ├── sim_HZC13_MER03.py       # 第2話: ローレンツ力散乱＆相対論的塵衝突
│   ├── sim_HZC14_C001.py        # 第3話: 12m岩盤遮蔽＆M型フレアEMP
│   └── sim_WH01_WH02.py         # 第4話: カシミール負エネルギー＆ワームホール重力崩壊
├── episodes/                    # カスタムエピソードJSON格納フォルダ
```

---

## 🚀 使い方 (JupyterLabでの実行)

JupyterLabのセルで以下を実行するだけで、画面上にゲーム画面が起動します。

```python
%run kenta_game_jv3.py
```

画面上のドロップダウンメニューより「正史マスター」または「adhoc.json」を切り替えてプレイ可能です。

---

## 🛠️ Ad-hoc (カスタムシナリオ) の構築方法

`episodes/` フォルダ内のエピソード群を1つのシナリオデータ (`adhoc.json`) に連結できます：

```bash
python build_adhoc_scenario.py
```

実行後、ゲーム画面上のドロップダウンで `adhoc.json` を選択するだけでプレイ可能です。
