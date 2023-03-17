class UnionFind:
    """Union-Find data structure.
    """

    def __init__(self, n: int) -> None:
        """Initialize the Union-Find data structure.
        
        Args:
            n (int): Number of elements.
            
        Returns:
            None
            
        Errors:
            ValueError: If n is less than 1.
        """
        assert n > 0, "n must be positive"
        self.n = n
        self.parents = [-1] * n

    def find(self, i: int) -> int:
        """Find the root of an element.
        
        Args:
            i (int): Element.
            
        Returns:
            int: Root of i.
        """
        if self.parents[i] < 0:
            return i
        else:
            self.parents[i] = self.find(self.parents[i])
            return self.parents[i]

    def union(self, i: int, j: int) -> None:
        """Union two elements.
        
        Args:
            i (int): First element.
            j (int): Second element.
            
        Returns:
            None
        """
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return
        if root_i > root_j:
            root_i, root_j = root_j, root_i
        self.parents[root_i] += self.parents[root_j]
        self.parents[root_j] = root_i

    def same(self, i: int, j: int) -> bool:
        """Check if two elements are in the same set.
        
        Args:
            i (int): First element.
            j (int): Second element.
            
        Returns:
            bool: True if i and j are in the same set.
        """
        return self.find(i) == self.find(j)
    
    def size(self, i: int) -> int:
        """Return the size of the set containing i.
        
        Args:
            i (int): Element.
            
        Returns:
            int: Size of the set containing i.
        """
        return -self.parents[self.find(i)]
    
    def max_size(self) -> int:
        """Return the size of the largest set.
        
        Returns:
            int: Size of the largest set.
        """
        return -min(self.parents)
    
    def __repr__(self) -> str:
        """Return a string representation of the Union-Find data structure.
        
        Returns:
            str: String representation of the Union-Find data structure.
        """
        return f"UnionFind(n = {self.n})"