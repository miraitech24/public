#!/usr/bin/env python3
"""
【SP-03】番外編②: 3D オイラー・丸山法 ストカスティック微分方程式
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
    
    np.random.seed(101)
    n = 25
    dt = 0.1
    dx = np.random.normal(0, np.sqrt(dt), n)
    dy = np.random.normal(0, np.sqrt(dt), n)
    dz = np.random.normal(0, np.sqrt(dt), n)
    
    x = np.cumsum(dx)
    y = np.cumsum(dy)
    z = np.cumsum(dz)

    def update_sde(frame):
        ax.clear()
        ax.set_facecolor('#1e293b')
        ax.set_title("Task SP-03: 3D SDE Euler-Maruyama Method", color='#f8fafc', fontsize=10)
        ax.plot(x[:frame], y[:frame], z[:frame], color='#38bdf8', lw=1.8)
        ax.scatter([x[frame-1] if frame>0 else 0], [y[frame-1] if frame>0 else 0], [z[frame-1] if frame>0 else 0], color='#4ade80', s=30)
        ax.view_init(elev=20, azim=frame*4)

    ani1 = animation.FuncAnimation(fig, update_sde, frames=n, interval=70)
    ani1.save(os.path.join(out_dir, "sim_sp3_sde_stochastic_stable_3d.gif"), writer='pillow')
    plt.close()

if __name__ == "__main__":
    run_simulation()
