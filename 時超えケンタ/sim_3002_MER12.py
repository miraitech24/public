#!/usr/bin/env python3
"""
【#3002 / MER-12】プロローグ: 1.64PW 3D光圧レーザー推進 & 3D照準軸ブレ偏心熱歪み
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
    
    # 1. 正解: 3Dレーザー集光推進軌道
    fig = plt.figure(figsize=(6, 4), dpi=80)
    fig.patch.set_facecolor('#0f172a')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#1e293b')
    ax.tick_params(colors='#94a3b8')
    ax.set_title("Task #3002: 3D Laser Acceleration (0.20c)", color='#f8fafc', fontsize=10)
    
    t = np.linspace(0, 10, 30)
    x = t * 0.2
    y = np.sin(t) * 0.1
    z = np.cos(t) * 0.1
    line, = ax.plot([], [], [], color='#38bdf8', lw=2.5, label='Trajectory')
    
    ax.set_xlim(0, 2)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)

    def update_3d_accel(frame):
        line.set_data(x[:frame], y[:frame])
        line.set_3d_properties(z[:frame])
        ax.view_init(elev=20, azim=frame*4)
        return line,

    ani1 = animation.FuncAnimation(fig, update_3d_accel, frames=len(t), interval=70)
    ani1.save(os.path.join(out_dir, "sim_prologue_laser_acceleration_3d.gif"), writer='pillow')
    plt.close()

    # 2. 失敗: 照準ブレ 3D熱歪み
    fig = plt.figure(figsize=(6, 4), dpi=80)
    fig.patch.set_facecolor('#0f172a')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#1e293b')
    ax.tick_params(colors='#94a3b8')

    u = np.linspace(0, 2 * np.pi, 25)
    v = np.linspace(0, np.pi, 25)
    U, V = np.meshgrid(u, v)

    def update_3d_err(frame):
        ax.clear()
        ax.set_facecolor('#1e293b')
        ax.set_title("Task MER-12: 3D Thermal Deformation", color='#f8fafc', fontsize=10)
        R = 1.0 + 0.2 * np.sin(4 * U + frame * 0.3)
        X = R * np.sin(V) * np.cos(U)
        Y = R * np.sin(V) * np.sin(U)
        Z = R * np.cos(V)
        ax.plot_surface(X, Y, Z, cmap='magma', alpha=0.8)
        ax.view_init(elev=25, azim=frame*5)

    ani2 = animation.FuncAnimation(fig, update_3d_err, frames=20, interval=80)
    ani2.save(os.path.join(out_dir, "sim_prologue_beam_instability_3d.gif"), writer='pillow')
    plt.close()

if __name__ == "__main__":
    run_simulation()
