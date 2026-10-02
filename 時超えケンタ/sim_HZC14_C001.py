#!/usr/bin/env python3
"""
【HZC-14 / C001】第3話: 3D 12m岩盤モンテカルロ遮蔽 & 3D M型フレアEMP
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
    
    # 1. 安定: 3Dモンテカルロ岩盤粒子衰退
    fig = plt.figure(figsize=(6, 4), dpi=80)
    fig.patch.set_facecolor('#0f172a')
    ax = fig.add_subplot(111, projection='3d')
    
    def update_3d_mc(frame):
        ax.clear()
        ax.set_facecolor('#1e293b')
        ax.set_title("Task HZC-14: 3D Monte Carlo Cave Shielding (12m)", color='#f8fafc', fontsize=10)
        
        n_p = 80
        x = np.random.exponential(scale=3.0, size=n_p)
        y = np.random.uniform(-5, 5, size=n_p)
        z = np.random.uniform(-5, 5, size=n_p)
        
        yb, zb = np.mgrid[-5:5:8j, -5:5:8j]
        xb = 12 * np.ones_like(yb)
        ax.plot_surface(xb, yb, zb, color='#78716c', alpha=0.3)
        
        ax.scatter(x[x < 12], y[x < 12], z[x < 12], c='#38bdf8', s=12, alpha=0.7)
        ax.set_xlim(0, 15)
        ax.set_ylim(-5, 5)
        ax.set_zlim(-5, 5)
        ax.view_init(elev=20, azim=frame*4)

    ani1 = animation.FuncAnimation(fig, update_3d_mc, frames=22, interval=80)
    ani1.save(os.path.join(out_dir, "sim_ep3_cave_radiation_shielding_3d.gif"), writer='pillow')
    plt.close()

    # 2. 失敗: 3D EMP波動
    fig = plt.figure(figsize=(6, 4), dpi=80)
    fig.patch.set_facecolor('#0f172a')
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-3, 3, 20)
    y = np.linspace(-3, 3, 20)
    X, Y = np.meshgrid(x, y)

    def update_3d_emp(frame):
        ax.clear()
        ax.set_facecolor('#1e293b')
        ax.set_title("Task C001: 3D M-Flare EMP Wavefront Damage", color='#f8fafc', fontsize=10)
        
        R = np.sqrt(X**2 + Y**2) + 0.1
        Z = np.sin(3 * R - frame * 0.4) * np.exp(frame * 0.05)
        ax.plot_surface(X, Y, Z, cmap='plasma')
        ax.set_zlim(-3, 3)
        ax.view_init(elev=30, azim=frame*5)

    ani2 = animation.FuncAnimation(fig, update_3d_emp, frames=20, interval=80)
    ani2.save(os.path.join(out_dir, "sim_ep3_solar_flare_emp_burn_3d.gif"), writer='pillow')
    plt.close()

if __name__ == "__main__":
    run_simulation()
