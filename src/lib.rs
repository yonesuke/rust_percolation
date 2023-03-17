use pyo3::prelude::*;

use rand::Rng;

mod unionfind;
pub use unionfind::UnionFind;

#[pyclass]
pub struct Percolation {
    l: usize,
    n: usize,
    p: f64,
    uf: UnionFind,
}

#[pymethods]
impl Percolation {
    #[new]
    pub fn new(l: usize, p: f64) -> PyResult<Self> {
        let n = l * l;
        Ok(Self {
            l: l,
            n: n,
            p: p,
            uf: UnionFind::new(n),
        })
    }

    fn pos2idx(&self, mut ix: usize, mut iy: usize) -> usize {
        ix = (ix + self.l) % self.l;
        iy = (iy + self.l) % self.l;
        return ix + iy * self.l;
    }

    pub fn connect(&mut self, i: usize, j: usize) -> () {
        let mut rng = rand::thread_rng();
        let r: f64 = rng.gen();
        if r < self.p {
            self.uf.union(i, j);
        }
    }

    pub fn one_step(&mut self) -> () {
        for i in 0..(self.l - 1) {
            for j in 0..(self.l - 1) {
                let idx = self.pos2idx(i, j);
                self.connect(idx, self.pos2idx(i + 1, j));
                self.connect(idx, self.pos2idx(i, j + 1));
            }
        }
        for k in 0..(self.l - 1) {
            self.connect(self.pos2idx(self.l - 1, k), self.pos2idx(self.l - 1, k + 1));
            self.connect(self.pos2idx(k, self.l - 1), self.pos2idx(k + 1, self.l - 1));
        }
    }

    pub fn percolation_probability(&mut self, reset: bool) -> f64 {
        if reset {
            self.uf = UnionFind::new(self.n);
            self.one_step();
        }
        let max_cluster_size = self.uf.max_size();
        return max_cluster_size as f64 / self.n as f64;
    }

    pub fn monte_carlo(&mut self, n_step: usize) -> Vec<f64> {
        let mut vals: Vec<f64> = Vec::new();
        for _ in 0..n_step {
            vals.push(self.percolation_probability(true));
        }
        return vals;
    }
}

#[pymodule]
fn rust_percolation(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_class::<Percolation>()?;
    Ok(())
}
