# PSTL-Tri-optimise

Test et implémentation de plusieurs algorithmes de tri en vue de trouver un
successeur au TimSort


Pour lancer toute la chaine de tests, executer `whole_execution.bash`


## Utilisation de array_generator_config.json

**Méthodes de génération de listes :**
- alea *(= entropie max)*
- entropie_alea
- run_constant_croiss_lineaires 
- run_alea *(doit quand meme donner un nombre de runs)*
- run_delta 
- run_delta_with_unsorted *(certains runs sont non triés)*
- nb_runs_given_by_entropy *(tous les runs ont la meme taille)*

**Variables de taille liste :**
- nbrep = nombre de répétition pour chaque configuration de liste
- t = taille de la liste précédente (taille début pour la première)
- tf = taille_fin
- td = taille_départ
- nb = nombre total de listes (hors répétitions)
- n = numéro de liste (hors répétitions)

**Variables de nombre de runs :**
- *toutes les variables de taille de liste*
- nbr = nombre de runs du precedent calcul (nb_runs_depart pour le premier)
- nbrf = nb_runs_fin
- nbrd = nb_runs_depart

**Variable entropie :**
- la = entropie de l'itération précédente (0 à la 1ère itération)
- rep = nième répétition (en partant de 0)


## Utilisation de generateur_graphique.py

```
   Usage: $ generateur_graphique.py param_1 [param_n] [-s --size]
 
   * param_1: name of a graphic you want
   * ...
   * param_n: name of a graphic you want
 
   * -s / --size integer_1 ... integer_n : all list size you want to display
```

Voici les différents types de graphiques disponibles :
- **temps/taille**\
  x = taille\
  y = temps execution
- **temps/entropie**\
  x = valeur entropie\
  y = temps execution
- **heatmap**\
  -> pout chaque algo :\
  x = taille liste\
  y = entropie (en % de 0 à 1 avec 1 l'entropie maximum parmis toutes les heatmaps)\
  z = temps d'execution

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
