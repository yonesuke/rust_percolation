from typing import List
from random import random
from unionfind import UnionFind

class Percolation:
    """2-dimensional percolation on a square lattice with open boundary conditions.

    Attributes:
        l (int): Square lattice size (l x l).
        p (float): Probability of a site being open.

    Example:
        >>> model = Percolation(10, 0.3)
        >>> model.one_step()
        >>> model.percolation_probability()
        0.09
        >>> model.monte_carlo(10)
        [0.08, 0.09, 0.1, 0.08, 0.06, 0.07, 0.09, 0.15, 0.13, 0.11]
    """

    def __init__(self, l: int, p: float) -> None:
        """Initialize a new percolation object.
        
        Args:
            l (int): Square lattice size (l x l).
            p (float): Probability of a site being open.
            
        Returns:
            None

        Error:
            ValueError: If l is not positive.
            ValueError: If p is not in [0, 1].
        """
        assert l > 0, "l must be positive"
        assert 0 <= p <= 1, 'p must be in [0, 1]'
        self.l = l
        self.p = p
        self.uf = UnionFind(l * l)

    def _pos2idx(self, ix: int, iy: int) -> int:
        """Convert a position to an index.

        Args:
            ix (int): x coordinate.
            iy (int): y coordinate.

        Returns:
            int: Index.
        """
        ix = (ix + self.l) % self.l
        iy = (iy + self.l) % self.l
        return ix + iy * self.l
    
    def connect(self, i: int, j: int) -> None:
        """Connect two sites with probability p.

        Args:
            i (int): First site index.
            j (int): Second site index.

        Returns:
            None
        """
        if random() < self.p:
            self.uf.union(i, j)

    def one_step(self) -> None:
        """Perform one step of percolation.
        
        Returns:
            None
        """
        for i in range(self.l - 1):
            for j in range(self.l - 1):
                self.connect(self._pos2idx(i, j), self._pos2idx(i, j + 1))
                self.connect(self._pos2idx(i, j), self._pos2idx(i + 1, j))

        for k in range(self.l - 1):
            self.connect(self._pos2idx(self.l - 1, k), self._pos2idx(self.l - 1, k + 1))
            self.connect(self._pos2idx(k, self.l - 1), self._pos2idx(k + 1, self.l - 1))

    def percolation_probability(self, reset=False) -> float:
        """Calculate the percolation probability.

        Args:
            reset (bool, optional): Reset the percolation object. Defaults to False.

        Returns:
            float: Percolation probability.
        """
        if reset:
            self.uf = UnionFind(self.l * self.l)
            self.one_step()
        max_cluster_size = self.uf.max_size()
        return max_cluster_size / (self.l * self.l)

    def monte_carlo(self, n_step: int) -> List[float]:
        """Perform n steps of percolation and calculate the percolation probability.

        Args:
            n_step (int): Number of steps.

        Returns:
            float: Percolation probability.
        """
        vals = []
        for _ in range(n_step):
            vals.append(self.percolation_probability(reset=True))
        return vals
