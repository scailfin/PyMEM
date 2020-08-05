#!/usr/bin/env bash

# echo $PWD
pip install numpy
if [[ ! -d ttbar_output ]]; then
  if [[ -f ttbar.mg5 ]]; then
    mg5_aMC ttbar.mg5
  fi
fi
cd ttbar_output/SubProcesses
make allmatrix2py.so
# cd ../../
# ls -lhtra
cp ../../test.py .
# export PYTHONPATH=${PYTHONPATH}:${PWD}/ttbar_output/SubProcesses
python test.py
