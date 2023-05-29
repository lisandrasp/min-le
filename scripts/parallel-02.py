#!/usr/bin/env sage -python

'''Testing decorate interface for parallel computation.
Decorator works with kirchhoff_matrix() but doesn't with eigenvalues().
eigenvalues() output is 'INVALID DATA Ran out of input'.'''

from sage.all import *

n = 5
parameters = f"{n} -c {n}:{n}"
graphs = list(graphs.nauty_geng(parameters))

@parallel(ncpus=7)
def laplacian_energy(graphs):
    matrices = graphs.kirchhoff_matrix()
    char_values = matrices.eigenvalues()
    return char_values

spectra = laplacian_energy(graphs)

for spectrum in spectra:
    print(spectrum)
