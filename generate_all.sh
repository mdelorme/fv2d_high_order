#!/bin/bash

rm -rf profile*
for N in 32 64 128 256 512 1024 2048; do
    echo "--- Generating for N=$N ---"
    python3 generate_hse.py $N isentropic
    python3 generate_hse.py $N isothermal
done
