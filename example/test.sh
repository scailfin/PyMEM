#!/usr/bin/env bash

# Generate feynman diagrams from physics processes
if [[ ! -d ttbar_output ]]; then
  if [[ -f ttbar.mg5 ]]; then
    mg5_aMC ttbar.mg5
    # Clean unnecessary auxilary output files
    rm nsqso_born.inc
    rm py.py
  fi
fi
# compile FORTRAN and wrap it in Python
cd ttbar_output/SubProcesses
if [[ ! -f allmatrix2py.cpython-38-x86_64-linux-gnu.so ]]; then
  make allmatrix2py.so
fi
# Navigate to top level of process directory structure (same level as Cards/)
cd ..
python ../test.py "Cards"
