#!/usr/bin/env python3
"""
【C110 / MER-16】第1話: 3D非定常熱伝導方程式 & 3D CFL拡散限界爆発
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
    
    # 1. 安定: 3D陰解法熱放熱
    fig = plt.figure(figsize=(6, 4), dpi=80)
    fig.patch.set_facecolor('#0f172a')
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.linspace(-2, 2, 20)
    y = np.linspace(-2, 2, 20)
    X, Y = np.meshgrid(x, y)

    def update_3d_heat(frame):
        ax.clear()
        ax.set_facecolor('#1e293b')
        ax.set_title("Task C110: 3D Heat Diffusion (Crank-Nicolson)", color='#f8fafc', fontsize=10)
        Z = np.exp(-(X**2 + Y**2)) * np.exp(-0.1 * frame)
        ax.plot_surface(X, Y, Z, cmap='coolwarm', vmin=0, vmax=1)
        ax.set_zlim(0, 1.2)
        ax.view_init(elev=30, azim=frame*4)

    ani1 = animation.FuncAnimation(fig, update_3d_heat, frames=20, interval=80)
    ani1.save(os.path.join(out_dir, "sim_ep1_heat_conduction_stable_3d.gif"), writer='pillow')
    plt.close()

    # 2. 失敗: 3D CFL爆発
    fig = plt.figure(figsize=(6, 4), dpi=80)
    fig.patch.set_facecolor('#0f172a')
    ax = fig.add_subplot(111, projection='3d')

    def update_3d_cfl(frame):
        ax.clear()
        ax.set_facecolor('#1e293b')
        ax.set_title("Task MER-16: 3D Explicit Euler CFL Explosive Divergence", color='#f8fafc', fontsize=10)
        noise = ((-1.3) ** frame) * 0.05 * np.sin(5*X) * np.cos(5*Y)
        Z = np.exp(-(X**2 + Y**2)) + noise
        ax.plot_surface(X, Y, Z, cmap='inferno')
        ax.set_zlim(-3, 3)
        ax.view_init(elev=30, azim=frame*5)

    ani2 = animation.FuncAnimation(fig, update_3d_cfl, frames=18, interval=90)
    ani2.save(os.path.join(out_dir, "sim_ep1_cfl_thermal_explosion_3d.gif"), writer='pillow')
    plt.close()

if __name__ == "__main__":
    run_simulation()
