#!/usr/bin/env bash

docker run --rm \
  -v "${PWD}":"${PWD}" \
  -w "${PWD}" \
  matthewfeickert/madgraph5-amc-nlo:mg5_amc2.7.0-python3 \
  "bash test.sh"
