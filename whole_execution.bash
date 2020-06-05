#!/bin/bash

python3 array_generator.py
./bench.bash
python3 generateur_graphique.py new_temps/entropie_courbes --size 200000 600000 800000 1000000
python3 generateur_graphique.py temps/taille_box -i 0 20
python3 generateur_graphique.py temps/taille_box -i 20 40
python3 generateur_graphique.py temps/taille_box -i 40 65
python3 generateur_graphique.py temps/taille_box -i 65 100
python3 generateur_graphique.py heatmap