default: run

run: ttbar.mg5 test.py
	# Use CURDIR in Make instead of PWD
	docker run --rm \
  -v "${CURDIR}":"${CURDIR}" \
  -w "${CURDIR}" \
  scailfin/madgraph5-amc-nlo:mg5_amc2.8.1 \
  "bash run.sh"

clean:
	docker run --rm \
  -v "${CURDIR}":"${CURDIR}" \
  -w "${CURDIR}" \
  scailfin/madgraph5-amc-nlo:mg5_amc2.8.1 \
  "rm -rf ttbar_output"

run-27: ttbar.mg5 test.py
	# Use CURDIR in Make instead of PWD
	docker run --rm \
  -v "${CURDIR}":"${CURDIR}" \
  -w "${CURDIR}" \
  scailfin/madgraph5-amc-nlo:mg5_amc2.7.0-python3 \
  "bash run.sh"
