#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 12:42:13 2025

@author: iwamura
"""

# P08_QUANTUM_RESISTANT_CBDC/src_pqc/hash_signature.py

import hashlib
import json
import os

# セキュリティパラメータの定義 (threat_analysis.py の結果に基づく)
# Groverの脅威に対処するため、ハッシュ長を倍増させる
HASH_ALGORITHM = 'sha3_512' # 量子耐性を考慮し、512ビットハッシュを選択

def generate_ots_keypair(hash_func):
    """
    ワンタイム署名 (OTS: One-Time Signature, Lamport scheme) の鍵ペアを生成する。
    ハッシュベース署名の最小単位。
    """
    # 署名ビット長 (512 bits)
    L = hash_func().digest_size * 8
    
    # 秘密鍵 (sk): L個のランダムなペア (2L個のランダム値)
    sk = [os.urandom(hash_func().digest_size) for _ in range(2)] * (L // 8) # 概念的な簡略化
    
    # 公開鍵 (pk): skの各要素をハッシュ化したもの
    pk = [(hash_func(sk[i]).digest(), hash_func(sk[i+1]).digest()) for i in range(0, len(sk), 2)]
    
    return sk, pk, L

def simulate_merkle_tree_construction(pk_list, hash_func):
    """
    OTS公開鍵を結合し、マークルツリーを構築する（概念的な署名鍵）。
    """
    if not pk_list:
        return None, 0

    # リーフノードはOTS公開鍵のハッシュ
    leaves = [hash_func(b"".join([h[0] + h[1] for h in key])).digest() for key in pk_list]
    
    # ツリー構築 (簡略化)
    tree_height = 0
    current_level = leaves
    
    while len(current_level) > 1:
        new_level = []
        for i in range(0, len(current_level), 2):
            combined = current_level[i] + current_level[i+1]
            new_level.append(hash_func(combined).digest())
        current_level = new_level
        tree_height += 1
        
    return current_level[0], tree_height # ルートハッシュと高さ

def simulate_cbdc_pqc_signature(num_keys=16):
    """
    CBDCトランザクションのためのハッシュベース署名鍵の生成をシミュレーションする。
    """
    print("\n--- 1. CBDC PQC署名モデル: ハッシュベース署名 (XMSS/SPHINCS+ 概念) ---")
    
    # 1. 基盤となるOTS鍵の生成 (例として num_keys 組)
    ots_keys = []
    L_bits = 0
    for i in range(num_keys):
        sk, pk, L_bits = generate_ots_keypair(lambda data=b'': hashlib.new(HASH_ALGORITHM, data))
        ots_keys.append(pk)
        
    print(f" ハッシュアルゴリズム: {HASH_ALGORITHM} ({L_bits} bits)")
    print(f" ベース鍵数 (OTS): {num_keys}")
    
    # 2. マークルツリーの構築
    root_hash, height = simulate_merkle_tree_construction(
        ots_keys, lambda data=b'': hashlib.new(HASH_ALGORITHM, data)
    )
    
    # 3. 署名鍵の定義
    # 公開鍵 PK_PQC = マークルツリーのルートハッシュ
    # 秘密鍵 SK_PQC = マークルツリーの秘密鍵とOTS秘密鍵群
    
    print(f"\n 署名公開鍵 PK_PQC (Root Hash):\n   {root_hash.hex()[:64]}...")
    print(f" ツリーの高さ: {height} (署名回数に影響)")
    
    # 4. 量子耐性の確認
    print("\n[量子耐性]:")
    print(f" - Groverの脅威に対し、{L_bits} bitsハッシュにより実効セキュリティは {L_bits/2} bitsを維持する。")
    print(" - 署名生成・検証はハッシュ関数のみに依存するため、Shorアルゴリズムの影響を受けない。")
    
    return {'root_hash': root_hash.hex(), 'height': height, 'hash_algo': HASH_ALGORITHM, 'bits': L_bits}

def save_signature_params(params, filename='../data/signature_params.json'):
    """
    生成された署名パラメータをJSONファイルに保存する。
    """
    dirname = os.path.dirname(filename)
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname)
        
    with open(filename, 'w') as f:
        json.dump(params, f, indent=4)
    print(f"\n=> 署名パラメータ統計を '{filename}' に保存しました。")
    
if __name__ == '__main__':
    # 署名モデルのシミュレーションとパラメータの保存
    params = simulate_cbdc_pqc_signature(num_keys=16)
    save_signature_params(params, filename='../data/signature_params.json')