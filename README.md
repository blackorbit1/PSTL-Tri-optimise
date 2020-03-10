# PSTL-Tri-optimise

Test et implémentation de plusieurs algorithmes de tri en vue de trouver un
successeur au TimSort


## Variables de fonctions pour array_generator_config.json

- t = taille de la liste précédente (taille début pour la première)
- tf = taille_fin
- td = taille_départ
- nb = nombre total de listes
- n = numéro de liste


## Requirements

- CMake version >= 3.15
- Librairie de micro-benchmarking de Google :
  https://github.com/google/benchmark


## Build

Lancer `make`, les exécutables générés se trouvent dans le dossier `build`
