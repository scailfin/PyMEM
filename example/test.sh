#!/usr/bin/env bash

# echo $PWD
if [[ ! -d ttbar_output ]]; then
  if [[ -f ttbar.mg5 ]]; then
    mg5_aMC ttbar.mg5
  fi
fi
cd ttbar_output/SubProcesses
if [[ ! -f allmatrix2py.cpython-38-x86_64-linux-gnu.so ]]; then
  make allmatrix2py.so
fi
# cd ../../
# ls -lhtra
cp ../../test.py .
# export PYTHONPATH=${PYTHONPATH}:${PWD}/ttbar_output/SubProcesses
python test.py
