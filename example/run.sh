#!/usr/bin/env bash

docker run --rm \
  -v "${PWD}":"${PWD}" \
  -w "${PWD}" \
  scailfin/madgraph5-amc-nlo:mg5_amc2.8.1 \
  "bash test.sh"
