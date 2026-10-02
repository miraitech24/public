#!/usr/bin/env python3
"""
【HZC-13 / MER-03】第2話: 3D 3.2T超電導磁場ローレンツ力プラズマ偏向散乱
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
    
    # 1. 安定: 3Dローレンツ偏向
    fig = plt.figure(figsize=(6, 4), dpi=80)
    fig.patch.set_facecolor('#0f172a')
    ax = fig.add_subplot(111, projection='3d')
    
    np.random.seed(42)
    n_part = 30
    x0 = -3 * np.ones(n_part)
    y0 = np.random.uniform(-1.5, 1.5, n_part)
    z0 = np.random.uniform(-1.5, 1.5, n_part)

    def update_3d_lorentz(frame):
        ax.clear()
        ax.set_facecolor('#1e293b')
        ax.set_title("Task HZC-13: 3D 3.2T Lorentz Plasma Deflection", color='#f8fafc', fontsize=10)
        
        x = x0 + frame * 0.18
        r2 = x**2 + y0**2 + z0**2 + 0.1
        y = y0 + 0.8 * (1 / r2) * np.sign(y0)
        z = z0 + 0.8 * (1 / r2) * np.sign(z0)
        
        ax.scatter(x, y, z, c='#4ade80', s=15, alpha=0.8)
        u, v = np.mgrid[0:2*np.pi:12j, 0:np.pi:12j]
        xs = 0.4 * np.cos(u) * np.sin(v)
        ys = 0.4 * np.sin(u) * np.sin(v)
        zs = 0.4 * np.cos(v)
        ax.plot_wireframe(xs, ys, zs, color='#38bdf8', alpha=0.4)
        
        ax.set_xlim(-3, 3)
        ax.set_ylim(-2, 2)
        ax.set_zlim(-2, 2)
        ax.view_init(elev=20, azim=frame*4)

    ani1 = animation.FuncAnimation(fig, update_3d_lorentz, frames=25, interval=70)
    ani1.save(os.path.join(out_dir, "sim_ep2_lorentz_plasma_deflection_3d.gif"), writer='pillow')
    plt.close()

    # 2. 失敗: 3D塵アブレーション
    fig = plt.figure(figsize=(6, 4), dpi=80)
    fig.patch.set_facecolor('#0f172a')
    ax = fig.add_subplot(111, projection='3d')

    def update_3d_dust(frame):
        ax.clear()
        ax.set_facecolor('#1e293b')
        ax.set_title("Task MER-03: 3D Particle Ablation Impact", color='#f8fafc', fontsize=10)
        
        px = 2.5 - frame * 0.18
        py = 0
        pz = 0
        if px > 0:
            ax.scatter([px], [py], [pz], c='#f87171', s=50)
        else:
            sp_x = np.random.uniform(-0.5, 0.5, 20)
            sp_y = np.random.uniform(-0.5, 0.5, 20)
            sp_z = np.random.uniform(-0.5, 0.5, 20)
            ax.scatter(sp_x, sp_y, sp_z, c='#f59e0b', s=20)
            
        ax.set_xlim(-2, 3)
        ax.set_ylim(-2, 2)
        ax.set_zlim(-2, 2)
        ax.view_init(elev=25, azim=frame*5)

    ani2 = animation.FuncAnimation(fig, update_3d_dust, frames=22, interval=70)
    ani2.save(os.path.join(out_dir, "sim_ep2_particle_impact_ablation_3d.gif"), writer='pillow')
    plt.close()

if __name__ == "__main__":
    run_simulation()
