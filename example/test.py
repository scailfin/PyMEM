#!/usr/bin/env python3
import allmatrix2py


def main():
    allmatrix2py.initialise("../Cards/param_card.dat")
    # allmatrix2py.initialise("ttbar_output/Cards/param_card.dat")

    def invert_momenta(p):
        """ fortran/C-python do not order table in the same order"""
        new_p = []
        for i in range(len(p[0])):
            new_p.append([0] * len(p))
        for i, onep in enumerate(p):
            for j, x in enumerate(onep):
                new_p[j][i] = x
        return new_p

    p = [
        [0.5000000e03, 0.0000000e00, 0.0000000e00, 0.5000000e03],
        [0.5000000e03, 0.0000000e00, 0.0000000e00, -0.5000000e03],
        [0.5000000e03, 0.1040730e03, 0.4173556e03, -0.1872274e03],
        [0.5000000e03, -0.1040730e03, -0.4173556e03, 0.1872274e03],
    ]

    p = invert_momenta(p)
    nhel = -1  # means sum over all helicity
    pdgs = [21, 21, 6, -6]  # which pdg is requested
    scale2 = 0.0  # only used for loop matrix element. should be set to 0 for tree-level
    alphas = 0.13

    ans = allmatrix2py.smatrixhel(pdgs, p, alphas, scale2, nhel)
    print(f"matrix element is: {ans}")


if __name__ == "__main__":
    main()
