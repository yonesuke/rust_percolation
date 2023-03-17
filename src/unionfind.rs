use std::mem::swap;

pub struct UnionFind {
    // n: number of elements
    // parents: parent of each element
    n: usize,
    parents: Vec<i64>,
}

impl UnionFind{
    pub fn new(n: usize) -> UnionFind {
        // initialize UnionFind
        UnionFind {
            n: n,
            parents: vec![-1; n],
        }
    }

    pub fn find(&mut self, i: usize) -> usize {
        // find root of i
        if self.parents[i] < 0 {
            return i;
        } else {
            let parent_i = self.parents[i] as usize;
            self.parents[i] = self.find(parent_i) as i64;
            return self.parents[i] as usize;
        }
    }

    pub fn union(&mut self, i: usize, j: usize) -> () {
        // unite i and j
        let mut root_i = self.find(i);
        let mut root_j = self.find(j);
        if root_i == root_j {
            return;
        }
        if root_i > root_j {
            swap(&mut root_i, &mut root_j);
        }
        self.parents[root_i] += self.parents[root_j];
        self.parents[root_j] = root_i as i64;
    }

    pub fn same(&mut self, i: usize, j: usize) -> bool {
        // check if i and j are in the same group
        return self.find(i) == self.find(j);
    }

    pub fn size(&mut self, i: usize) -> i64 {
        // return size of group of i
        let root_i = self.find(i);
        return -self.parents[root_i];
    }

    pub fn max_size(&mut self) -> i64 {
        // return max size of groups
        let mut max_val: i64 = 0;
        for i in 0..self.n {
            if max_val < -self.parents[i] {
                max_val = -self.parents[i];
            }
        }
        return max_val;
    }

}