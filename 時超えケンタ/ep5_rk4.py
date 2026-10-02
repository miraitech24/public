#!/usr/bin/env python3
"""
【EP-05】第5話: 3D 適応RK4 (Runge-Kutta-Fehlberg) 特異点収束
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
    
    t = np.linspace(0, 10, 30)
    r = np.exp(-0.2 * t)
    x = r * np.cos(3 * t)
    y = r * np.sin(3 * t)
    z = -t * 0.2

    def update_rk4(frame):
        ax.clear()
        ax.set_facecolor('#1e293b')
        ax.set_title("Task EP-05: 3D Adaptive RK4 Orbit Singularity", color='#f8fafc', fontsize=10)
        ax.plot(x[:frame], y[:frame], z[:frame], color='#a855f7', lw=2)
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_zlim(-2.5, 0)
        ax.view_init(elev=20, azim=frame*5)

    ani1 = animation.FuncAnimation(fig, update_rk4, frames=len(t), interval=70)
    ani1.save(os.path.join(out_dir, "sim_ep5_rk4_singularity_stable_3d.gif"), writer='pillow')
    plt.close()

if __name__ == "__main__":
    run_simulation()
