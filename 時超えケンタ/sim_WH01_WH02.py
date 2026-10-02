#!/usr/bin/env python3
"""
【WH-01 / WH-02】第4話: 3D カシミール負エネルギーワームホール & 3D 幾何重力崩壊
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

def run_simulation(out_dir="./sim_assets_3d"):
    os.makedirs(out_dir, exist_ok=True)
    
    # 1. 安定: 3D ワームホールハイパーボロイド
    fig = plt.figure(figsize=(6, 4), dpi=80)
    fig.patch.set_facecolor('#0f172a')
    ax = fig.add_subplot(111, projection='3d')
    
    u = np.linspace(0, 2*np.pi, 25)
    v = np.linspace(-1.5, 1.5, 25)
    U, V = np.meshgrid(u, v)

    def update_3d_wh(frame):
        ax.clear()
        ax.set_facecolor('#1e293b')
        ax.set_title("Task WH-01: 3D Casimir Wormhole Throat (0.5nm)", color='#f8fafc', fontsize=10)
        
        r0 = 0.5 + 0.03 * np.sin(frame * 0.3)
        R = np.sqrt(r0**2 + V**2)
        X = R * np.cos(U)
        Y = R * np.sin(U)
        Z = V
        
        ax.plot_surface(X, Y, Z, cmap='cool', alpha=0.85)
        ax.set_zlim(-2, 2)
        ax.view_init(elev=20, azim=frame*4)

    ani1 = animation.FuncAnimation(fig, update_3d_wh, frames=22, interval=80)
    ani1.save(os.path.join(out_dir, "sim_ep4_casimir_wormhole_stable_3d.gif"), writer='pillow')
    plt.close()

    # 2. 失敗: 3D 重力崩壊
    fig = plt.figure(figsize=(6, 4), dpi=80)
    fig.patch.set_facecolor('#0f172a')
    ax = fig.add_subplot(111, projection='3d')

    def update_3d_collapse(frame):
        ax.clear()
        ax.set_facecolor('#1e293b')
        ax.set_title("Task WH-02: 3D Gravitational Collapse", color='#f8fafc', fontsize=10)
        
        r0 = max(0.02, 1.2 - frame * 0.06)
        R = np.sqrt(r0**2 + V**2)
        X = R * np.cos(U)
        Y = R * np.sin(U)
        Z = V
        
        ax.plot_surface(X, Y, Z, cmap='magma', alpha=0.9)
        ax.set_zlim(-2, 2)
        ax.view_init(elev=30, azim=frame*5)

    ani2 = animation.FuncAnimation(fig, update_3d_collapse, frames=20, interval=80)
    ani2.save(os.path.join(out_dir, "sim_ep4_gravitational_collapse_3d.gif"), writer='pillow')
    plt.close()

if __name__ == "__main__":
    run_simulation()
