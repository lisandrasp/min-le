#!/usr/bin/env sage -python

'''Testing decorate interface for parallel computation.
eigenvalues() output is 'NO DATA'.'''

from sage.all import *

n = 4
parameters = f"{n} -c {n}:{n}"
graphs = list(graphs.nauty_geng(parameters))

def matrices(graphs):
    return [graph.kirchhoff_matrix() for graph in graphs]

@parallel(ncpus=7)
def char_values(matrices):
    return [matrix.eigenvalues() for matrix in matrices]

matrices_list = matrices(graphs)
spectra = char_values(matrices_list)

for spectrum in spectra:
    print(spectrum)
