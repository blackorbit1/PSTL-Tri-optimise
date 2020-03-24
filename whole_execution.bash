#!/bin/bash

python3 array_generator.py
./bench.bash paths
python3 generateur_graphique.py