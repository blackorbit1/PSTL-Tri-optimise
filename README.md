# PSTL-Tri-optimise

Test et implémentation de plusieurs algorithmes de tri en vue de trouver un
successeur au TimSort


Pour lancer toute la chaine de tests, executer `whole_execution.bash`


## Variables de fonctions pour array_generator_config.json

**taille liste :**
- t = taille de la liste précédente (taille début pour la première)
- tf = taille_fin
- td = taille_départ
- nb = nombre total de listes
- n = numéro de liste

**nombre de runs :**
- *toutes les variables de taille de liste*
- nbr = nombre de runs du precedent calcul (nb_runs_depart pour le premier)
- nbrf = nb_runs_fin
- nbrd = nb_runs_depart

## Utilisation de generateur_graphique.py

```
Usage: $ generateur_graphique.py param_1 [param_n]
 
   * param_1: name of a graphic you want
   * ...
   * param_n: name of a graphic you want
```

Voici les différents types de graphiques disponibles :
- **temps/taille**\
  x = taille\
  y = temps execution
- **temps/entropie**\
  x = valeur entropie\
  y = temps execution
 
Exemple : 
```BASH
$ python3 generateur_graphique.py temps/entropie temps/taille`
```

## Requirements

- CMake version >= 3.15
- Librairie de micro-benchmarking de Google :
  https://github.com/google/benchmark


## Build

Lancer `make`, les exécutables générés se trouvent dans le dossier `build`
