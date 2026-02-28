import numpy as np
import matplotlib.pyplot as plt

def plot_2d_no_solution(path):
    # Parallel lines: y = -x + 2 and y = -x + 3
    x = np.linspace(-1, 4, 200)
    y1 = -x + 2
    y2 = -x + 3

    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.set_title("2D : Tidak ada solusi (2 garis sejajar)")

    ax.plot(x, y1, linewidth=2, label=r"$\ell$1 : x + y = 2")
    ax.plot(x, y2, linewidth=2, label=r"$\ell$2 : x + y = 3")

    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 4)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="upper right")
    ax.grid(True, linewidth=0.5, alpha=0.4)

    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)

def plot_2d_unique_solution(path):
    # Intersecting lines: x+y=2 and x-y=0 (y=x). Intersection (1,1)
    x = np.linspace(-1, 4, 200)
    y1 = -x + 2
    y2 = x

    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.set_title("2D : Tepat 1 solusi (2 garis berpotongan)")

    ax.plot(x, y1, linewidth=2, label=r"$\ell$1 : x + y = 2")
    ax.plot(x, y2, linewidth=2, label=r"$\ell$2 : x - y = 0")

    ax.scatter([1], [1], s=60)
    ax.text(1, 1, "  (1,1)")

    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 4)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="upper left")
    ax.grid(True, linewidth=0.5, alpha=0.4)

    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)

def plot_2d_infinite_solutions(path):
    # Coincident lines: x+y=2 and 2x+2y=4
    x = np.linspace(-1, 4, 200)
    y = -x + 2

    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.set_title("2D : Solusi tidak hingga (2 garis berimpit)")

    ax.plot(x, y, linewidth=3, label=r"$\ell$1 : x + y = 2")
    ax.plot(x, y, linewidth=1.5, linestyle="--", label=r"$\ell$2 : 2x + 2y = 4")

    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 4)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="upper right")
    ax.grid(True, linewidth=0.5, alpha=0.4)

    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)

if __name__ == "__main__":
    plot_2d_no_solution("spl_2d_no_solution.png")
    plot_2d_unique_solution("spl_2d_unique_solution.png")
    plot_2d_infinite_solutions("spl_2d_infinite_solutions.png")
    print("Selesai : 3 gambar 2D tersimpan di folder yang sama dengan program ini.")