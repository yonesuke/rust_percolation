from rust_percolation import Percolation
import matplotlib.pyplot as plt
import numpy as np
from tqdm.auto import tqdm

def calc_mean_std(l, ps, n_step):
    means, stds = [], []
    for p in tqdm(ps):
        model = Percolation(l, p)
        vals = np.array(model.monte_carlo(n_step))
        means.append(vals.mean())
        stds.append(vals.std())
    return means, stds

if __name__ == "__main__":
    ls = [10, 20, 50, 100]
    ps = np.arange(0.1, 0.9, 0.01)
    n_step = 1000

    plt.figure(figsize=(10, 6))
    plt.rcParams.update({"font.size": 16})
    plt.xlim(0.1, 0.9)
    plt.ylim(0, 1)
    for l in ls:
        means, stds = calc_mean_std(l, ps, n_step)
        plt.plot(ps, means, lw=2, label=f"l={l}")
        plt.fill_between(ps, np.array(means) - np.array(stds), np.array(means) + np.array(stds), alpha=0.2)
    plt.xlabel("p")
    plt.ylabel("percolation probability")
    plt.legend()
    plt.savefig("percolation.png")