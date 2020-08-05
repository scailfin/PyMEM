#!/usr/bin/env python3
# Generated output directory (ttbar_output) has __init__.py so can import
import ttbar_output.SubProcesses.allmatrix2py as allmatrix2py
import numpy as np
import sys


# https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/FAQ-General-4
def main():
    cmdline_args = sys.argv[1:]
    cards_directory_path = cmdline_args[0]
    # Seems to require that in same directory or below Cards/
    allmatrix2py.initialise(cards_directory_path + "/param_card.dat")

    momenta = [
        [0.5000000e03, 0.0000000e00, 0.0000000e00, 0.5000000e03],
        [0.5000000e03, 0.0000000e00, 0.0000000e00, -0.5000000e03],
        [0.5000000e03, 0.1040730e03, 0.4173556e03, -0.1872274e03],
        [0.5000000e03, -0.1040730e03, -0.4173556e03, 0.1872274e03],
    ]
    # fortran/C-python do not order table in the same order
    transposed_momenta = np.array(momenta).T.tolist()

    n_helicity = -1  # means sum over all helicity
    pdg_ids = [21, 21, 6, -6]  # which pdg ids are requested
    scale2 = 0.0  # only used for loop matrix element. should be set to 0 for tree-level
    alphas = 0.13

    result = allmatrix2py.smatrixhel(
        pdg_ids, transposed_momenta, alphas, scale2, n_helicity
    )
    print(f"matrix element is: {result}")


if __name__ == "__main__":
    main()
