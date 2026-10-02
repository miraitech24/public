# 『時超えケンタ (CHRONO KENTA)』 Ver 3.0 (jv3) 運用・開発ガイド

ハードSF数値解析アドベンチャー『時超えケンタ』の JupyterLab / GitHub 統合環境（Ver 3.0）の利用および自作シナリオ開発ガイドです。

---

## 🚀 1. ゲームの起動方法 (JupyterLab)

JupyterLabのセルで以下を実行するだけでゲームが起動します：

```python
%run kenta_game_jv3.py
```

* 画面上の「シナリオ選択」ドロップダウンから **`kenta_scenario_master.json`（正史マスター）** や **`adhoc.json`（カスタム連結シナリオ）** を切り替えてプレイできます。

---

## 🛠️ 2. 自作シナリオ (Ad-hoc) の構築方法

`episodes/` フォルダ内に配置したエピソードJSON群を1つのシナリオデータ (`adhoc.json`) に統合します：

```bash
python build_adhoc_scenario.py
```

---

## 📂 3. ユーザー自作アセット（画像・GIF・コード）の配置とJSON書き方

自作シナリオで画像やアニメ、計算コードを追加・指定する場合は、以下のフォルダにファイルを置き、JSONでファイル名を指定してください。

### ① ファイルの配置先フォルダ

* 🖼️ **漫画コマ画像 (PNG/JPG)** ➔ **`./kenta_manga/`** (またはルートディレクトリ)
* 🎬 **結果アニメーション (GIF)** ➔ **`./sim_assets/`** (またはルートディレクトリ)
* 💻 **数値解析計算コード (.py / .mac)** ➔ **`./sim_code/`** (またはルートディレクトリ)

### ② シナリオJSON内の指定キー（各項目は任意指定・自由記述OK）

エピソードJSONのシーンや選択肢において、指定したい項目のみを自由に記述できます：

```json
{
  "scene_id": "my_scene_01",
  "speaker": "AIケンタ",
  "text": "自作の3D軌道計算を実行します。",
  "image_file": "my_manga_01.png",            // 漫画コマ画像名
  "calc_code": "my_sim_01.py",                // 計算コード名 (未指定時は "???.mac" が補完)
  "options": [
    {
      "label": "【計算実行】3Dワームホール解析（※自作GIFアニメあり）",
      "result_animation": "my_3d_anim.gif",    // 選択結果のGIFアニメ名
      "result_text": "【物理的帰結】3D空間上で時空歪みの収束を確認！"
    }
  ]
}
```

* **補足**: `image_file` や `result_animation` を指定しない場合でも、エンジン側が未指定枠を自動表示するためエラーにならず動作します。
