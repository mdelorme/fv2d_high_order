#! /bin/bash

rm -rf hse
mkdir hse

echo "Generating models"
python3 generate_hse.py $1 isentropic
python3 generate_hse.py $1 isothermal

echo "Running models"
./fv2d profile_isothermal_$1.ini > log_isothermal_$1 && mkdir hse/isothermal_$1 && mv run.* hse/isothermal_$1/ && mv profile_isothermal_$1* hse/isothermal_$1/
./fv2d profile_isentropic_$1.ini > log_isentropic_$1 && mkdir hse/isentropic_$1 && mv run.* hse/isentropic_$1/ && mv profile_isentropic_$1* hse/isentropic_$1/


