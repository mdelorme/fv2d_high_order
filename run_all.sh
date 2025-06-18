#! /bin/bash

rm -rf hse
mkdir hse

echo "==== Generating profiles and initial conditions ===="
./generate_all.sh

echo "\n\n==== Running FV2D ===="
for N in 32 64 128 256 512 1024 2048;
do
  echo "Running isothermal profile for N=$N"
  ./fv2d profile_isothermal_$N.ini > log_isothermal_$N.out && mkdir hse/isothermal_$N && mv run.* hse/isothermal_$N/ && mv profile_isothermal_$N* hse/isothermal_$N/
  echo "Running isentropic profile for N=$N"
  ./fv2d profile_isentropic_$N.ini > log_isentropic_$N.out && mkdir hse/isentropic_$N && mv run.* hse/isentropic_$N/ && mv profile_isentropic_$N* hse/isentropic_$N/
done

echo "\n\n==== Running post processing ===="
python3 extract_comparison.py
