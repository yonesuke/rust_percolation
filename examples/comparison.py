from percolation import Percolation as PyPercolation
from rust_percolation import Percolation as RustPercolation
import numpy as np
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.5f} seconds")
        return result
    return wrapper

@timeit
def run_py(l, p, n_step):
    py = PyPercolation(l, p)
    vals = np.array(py.monte_carlo(n_step))
    return f"> percolation prob.: mean: {vals.mean():.5f}, std: {vals.std():.5f}"

@timeit
def run_rust(l, p, n_step):
    rust = RustPercolation(l, p)
    vals = np.array(rust.monte_carlo(n_step))
    return f"> percolation prob.: mean: {vals.mean():.5f}, std: {vals.std():.5f}"

if __name__ == "__main__":
    l = 100
    p = 0.7
    n_step = 1000
    print(run_py(l, p, n_step))
    print(run_rust(l, p, n_step))