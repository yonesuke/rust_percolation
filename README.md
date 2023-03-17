# Percolation

Rust binding of python implementation of percolation

# Setting
First, clone this repository.

```bash
git clone git@github.com:yonesuke/rust_percolation.git
```

Then, install this repo as follows.

```bash
python -m pip install -e rust_percolation/
```

Now you can load this library in python.
```python
import rust_percolation
```

If you unfortunately decide to uninstall this library, you can do it as follows.

```bash
python -m pip uninstall rust_percolation
```

# Usage
Calculate the percolation probability of a lattice with size 10 and probability 0.3.
```python
from rust_percolation import Percolation
l, p = 10, 0.3
model = Percolation(l, p)
model.one_step()
model.percolation_probability(reset=False) # 0.09
```

Monte Carlo simulation of percolation probability.
```python
from rust_percolation import Percolation
l, p = 10, 0.3
model = Percolation(l, p)
model.monte_carlo(1000) # [0.11, 0.28, ..., 0.15]
```

# Comparison with python implementation
The following is the comparison of the percolation probability of a lattice with size 100 and probability 0.7 between python and rust implementation.
Total Monte Carlo simulation is 1000 times.

```bash
python examples/comparison.py
```

| Implementation | Mean | Std | Time |
|:---:|:---:|:---:|:---:|
| Python | 0.98628 | 0.00176 | 15.81442 seconds |
| Rust | 0.98636 | 0.00169 | 0.38791 seconds |
