# Percolation

Rust binding of python implementation of percolation

# Setting
First, import this repository as a library.

```bash
git clone git@github.com:yonesuke/rust_percolation.git
```

Then, you can use this library as follows.

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