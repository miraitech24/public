#!/usr/bin/env python3
"""
【SP-02】番外編①: 3D 拡張カルマンフィルタ (EKF) & 3D PID 暴走過渡応答
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
    
    fig = plt.figure(figsize=(6, 4), dpi=80)
    fig.patch.set_facecolor('#0f172a')
    ax = fig.add_subplot(111, projection='3d')
    
    t = np.linspace(0, 10, 25)
    x = np.sin(t)
    y = np.cos(t)
    z = t * 0.1
    
    def update_ekf(frame):
        ax.clear()
        ax.set_facecolor('#1e293b')
        ax.set_title("Task SP-02: 3D Extended Kalman Filter (EKF)", color='#f8fafc', fontsize=10)
        ax.plot(x[:frame], y[:frame], z[:frame], color='#4ade80', lw=2)
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_zlim(0, 1.2)
        ax.view_init(elev=20, azim=frame*4)

    ani1 = animation.FuncAnimation(fig, update_ekf, frames=len(t), interval=70)
    ani1.save(os.path.join(out_dir, "sim_sp2_kalman_filter_stable_3d.gif"), writer='pillow')
    plt.close()

    fig = plt.figure(figsize=(6, 4), dpi=80)
    fig.patch.set_facecolor('#0f172a')
    ax = fig.add_subplot(111, projection='3d')

    def update_pid(frame):
        ax.clear()
        ax.set_facecolor('#1e293b')
        ax.set_title("Task SP-02: 3D High-Gain PID Transient Divergence", color='#f8fafc', fontsize=10)
        amp = (1.3 ** frame) * 0.05
        x_div = amp * np.sin(5*t[:frame])
        y_div = amp * np.cos(5*t[:frame])
        z_div = t[:frame] * 0.1
        ax.plot(x_div, y_div, z_div, color='#f87171', lw=1.8)
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        ax.set_zlim(0, 1.2)
        ax.view_init(elev=25, azim=frame*5)

    ani2 = animation.FuncAnimation(fig, update_pid, frames=18, interval=80)
    ani2.save(os.path.join(out_dir, "sim_sp2_transient_divergence_3d.gif"), writer='pillow')
    plt.close()

if __name__ == "__main__":
    run_simulation()
