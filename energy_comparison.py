#!/usr/bin/env sage -python

from sage.all import *
from functions import laplacian_energy

# Setting graph parameters
n, m = 10, 10
c = 4

tadpole = graphs.TadpoleGraph(c, n - c)
tadpole.plot().save("tadpole_" + str(n) + ".png")
print(f"Tadpole Laplacian energy: {round(laplacian_energy(tadpole.spectrum(laplacian=True), n, m), 5)}")

cycle = graphs.CycleGraph(n)
cycle.plot().save("cycle_" + str(n) + ".png")
print(f"Cycle Laplacian energy: {round(laplacian_energy(cycle.spectrum(laplacian=True), n, m), 5)}")
