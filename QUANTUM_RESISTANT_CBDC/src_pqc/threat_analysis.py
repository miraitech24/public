#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 12:39:59 2025

@author: iwamura
"""

# P08_QUANTUM_RESISTANT_CBDC/src_pqc/threat_analysis.py

from sympy import symbols, log, exp, O, sqrt
import pandas as pd
import json

# 記号の定義
L = symbols('L') # 鍵長 (bits)
N_mod = symbols('N') # RSAモジュラス
H_bits = symbols('H_bits') # ハッシュ出力長 (bits)

print("\n--- 1. 量子脅威解析: 計算複雑性の比較 ---")

# 1. Shorのアルゴリズム (素因数分解、RSA/ECCの解読)
# 鍵長 L に対する計算時間 (時間複雑性)

# 古典的な最良アルゴリズム (一般数体ふるい法, GNFS)
# O(exp((L**(1/3)) * (log(L)**(2/3))))
Complexity_Classical_RSA = exp(O((L**(1/3)) * (log(L)**(2/3))))
print(f"1.1 古典RSA解読 (GNFS): {Complexity_Classical_RSA}")

# 量子Shorのアルゴリズム
# 時間複雑性は多項式時間 (Polynomial Time) に激減する。
Complexity_Shor = O(L**3)
print(f"1.2 量子RSA解読 (Shor): {Complexity_Shor} <-- 古典暗号の壊滅的脅威")

# 2. Groverのアルゴリズム (総当たり検索、ハッシュ衝突)
# N個の候補に対する検索時間

# 古典的な総当たり検索
Complexity_Classical_Search = O(2**H_bits)
print(f"\n2.1 古典検索 (ハッシュ): {Complexity_Classical_Search}")

# 量子Groverのアルゴリズム
# 時間複雑性は、平方根に短縮される (二次的な高速化)。
Complexity_Grover = O(sqrt(2**H_bits))
print(f"2.2 量子検索 (Grover): {Complexity_Grover} <-- 対称鍵/ハッシュの鍵長を2倍にする必要がある")

# 3. 量子耐性暗号 (格子暗号) の困難性
# 格子暗号の困難性 (SVP/CVP) は、ShorやGroverの影響を受けない。
# 現状、最良の量子アルゴリズムでも指数時間である。
C_dim = symbols('C_dim') # 格子の次元
Complexity_PQC = exp(O(C_dim)) 
print(f"\n3. 量子耐性暗号 (格子/PQC): {Complexity_PQC}")
print("   => 量子時代でも指数時間 (Exponential Time) の困難性を維持する。")

def create_complexity_table(L_val=2048, H_val=256):
    """
    主要な暗号アルゴリズムの実効セキュリティレベルを比較し、データフレームとして返す。
    """
    # 実際は数値計算が必要だが、ここでは論理的な比較表を作成
    data = {
        '暗号技術': ['RSA (2048)', 'AES (256)', 'PQC (Lattice)'],
        '古典的計算量': [f"O(exp(L^{1/3}))", "O(2^256)", "O(exp(C_dim))"],
        '量子的計算量': [f"O(L^3)", "O(2^{256/2})", "O(exp(C_dim))"],
        '実効セキュリティ': ['ほぼゼロ', '128 bits', '256 bits (目標)'],
        '脅威': ['Shor (壊滅的)', 'Grover (二次的)', 'なし']
    }
    df = pd.DataFrame(data)
    return df

def save_threat_data(df, filename='../data/shor_complexity.csv'):
    """
    解析結果をCSVファイルに保存する。
    """
    # ディレクトリが存在しない場合は作成
    dirname = os.path.dirname(filename)
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname)
        
    df.to_csv(filename, index=False)
    print(f"\n=> 脅威解析結果を '{filename}' に保存しました。")

if __name__ == '__main__':
    import os
    
    # 計算複雑性の比較表を生成
    complexity_df = create_complexity_table()
    
    print("\n--- 4. 実効セキュリティレベル比較表 ---")
    print(complexity_df.to_markdown(index=False)) # 見やすいMarkdown形式で出力 
    
    # 結論
    print("\n[結論]: リーマン予想が裏付ける古典的なRSAの困難性は、量子Shorアルゴリズムの前では多項式時間に崩壊する。")
    print("CBDCのセキュリティ維持には、格子暗号のような量子時代でも指数時間(Exponential Time)の困難性を保つPQCへの移行が不可欠である。")
    
    # データ保存
    save_threat_data(complexity_df)