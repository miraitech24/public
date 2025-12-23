#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 11:30:02 2025

@author: iwamura
"""

# P08_QUANTUM_RESISTANT_CBDC/src_pqc/lattice_crypto.py

import numpy as np
import json
import os # ファイルシステムの操作のために追加

def generate_lwe_parameters(n_dim=256, m_dim=512, q_mod=3329, sigma_noise=1.5):
    """
    LWE (Learning With Errors) 問題に基づいた格子暗号のパラメータを定義する。
    
    Args:
        n_dim (int): 格子の次元 (n)。
        m_dim (int): サンプル数 (m)。
        q_mod (int): モジュラス q (通常は小さな素数)。
        sigma_noise (float): ノイズ e の標準偏差。
        
    Returns:
        dict: LWE問題の定義に必要なパラメータ。
    """
    print("\n--- 1. LWE (Learning With Errors) パラメータ定義 ---")
    
    # 1. 格子次元とモジュラス
    print(f" 格子次元 (n, m): ({n_dim}, {m_dim})")
    print(f" モジュラス q: {q_mod}")
    print(f" ノイズ標準偏差 sigma: {sigma_noise}")
    
    # 2. 公開鍵行列 A の生成
    # Aは Z_q 上でランダムに選ばれる (n x m 行列)
    A = np.random.randint(0, q_mod, size=(n_dim, m_dim))
    
    # 3. 秘密鍵ベクトル s の生成 (短いベクトル)
    # sは短いランダムな整数ベクトル (m x 1)
    s = np.random.randint(-1, 2, size=(m_dim, 1)) # 例えば、要素が {-1, 0, 1} の短いベクトル
    
    # 4. ノイズベクトル e の生成
    # eはガウス分布に従う小さな整数ノイズ (n x 1)
    # PQCの安全性は、このノイズeの追加によって、LWE問題が困難になることに依存する。
    e = np.round(np.random.normal(0, sigma_noise, size=(n_dim, 1))).astype(int)
    
    # 5. 公開ベクトル b の計算: b = A * s + e (mod q)
    b = (A @ s + e) % q_mod
    
    # 6. 公開鍵と秘密鍵の定義
    # 公開鍵 PK = (A, b)
    # 秘密鍵 SK = s
    
    # 保存用のパラメータ辞書を構築
    return {
        'n': n_dim, 'm': m_dim, 'q': q_mod, 'sigma': sigma_noise,
        'A_shape': A.shape, 's_shape': s.shape, 'b_shape': b.shape,
        'A_sample': A[0, :5].tolist(),  # 行列Aの最初の数要素のサンプル
        's_sample': s[:5, 0].tolist(), # 秘密ベクトルsの最初の数要素のサンプル
        'b_sample': b[:5, 0].tolist(), # 公開ベクトルbの最初の数要素のサンプル
    }

def save_lattice_parameters(params, filename='../data/lattice_params.json'):
    """
    生成されたパラメータをJSONファイルに保存する。
    ファイルパスにディレクトリーが存在しない場合、自動的に作成する。
    """
    # ディレクトリーパスを取得し、存在しない場合は作成
    dirname = os.path.dirname(filename)
    if dirname and not os.path.exists(dirname):
        # 🚨 エラー対策: data ディレクトリを自動作成
        os.makedirs(dirname)
        print(f"(注意: ディレクトリ '{dirname}' を自動作成しました。)")
    
    with open(filename, 'w') as f:
        json.dump(params, f, indent=4)
    print(f"\n=> 格子パラメータ統計を '{filename}' に保存しました。")
    
def simulate_key_generation(n_dim=256, m_dim=512, q_mod=3329):
    """
    格子暗号の鍵生成をシミュレーションし、結果を表示する。
    """
    print("\n--- 2. CBDCのための格子暗号鍵生成シミュレーション ---")
    
    # パラメータの生成
    params = generate_lwe_parameters(n_dim, m_dim, q_mod)
    
    # 公開鍵の要素表示
    print(f"\n 公開鍵 PK = (A, b)")
    print(f"  行列 A の一部 (Z_{q_mod} 上): {params['A_sample']}...")
    print(f"  ベクトル b の一部 (A*s+e): {params['b_sample']}...")
    
    # 秘密鍵の要素表示
    print(f" 秘密鍵 SK = s")
    print(f"  ベクトル s の一部 (短いベクトル): {params['s_sample']}...")
    
    # 鍵の安全性（困難性）の言及
    print("\n[重要性]: PKからSK (s) を特定することは、量子コンピュータでも困難なSVP/CVP問題に帰着する。")
    print("この困難性が、CBDCトランザクションの機密性と完全性を量子時代に保証する。")
    

    # データ保存
    save_lattice_parameters(params)
    
if __name__ == '__main__':
    # DilithiumなどのPQC標準に近いパラメータ設定で実行
    simulate_key_generation(n_dim=256, m_dim=512, q_mod=3329)