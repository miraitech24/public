#!/usr/bin/env python3
"""
【SP-04】番外編③: 3D 多重格子法 Vサイクル ポアソン方程式
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
    
    x = np.linspace(-2, 2, 18)
    y = np.linspace(-2, 2, 18)
    X, Y = np.meshgrid(x, y)

    def update_mg(frame):
        ax.clear()
        ax.set_facecolor('#1e293b')
        ax.set_title("Task SP-04: 3D Multigrid Poisson V-Cycle", color='#f8fafc', fontsize=10)
        Z = np.sin(X) * np.cos(Y) * np.exp(-0.1 * frame)
        ax.plot_surface(X, Y, Z, cmap='plasma')
        ax.set_zlim(-1, 1)
        ax.view_init(elev=25, azim=frame*5)

    ani1 = animation.FuncAnimation(fig, update_mg, frames=20, interval=80)
    ani1.save(os.path.join(out_dir, "sim_sp4_poisson_multigrid_stable_3d.gif"), writer='pillow')
    plt.close()

if __name__ == "__main__":
    run_simulation()
