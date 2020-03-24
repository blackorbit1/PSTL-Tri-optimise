from matplotlib import pyplot
from math import log
import math
import random, json, os, time

def get_entropy(run_size, list_size):
    # Calcul de l'entropie
    entropie_reel = 0
    for i in range(int(list_size/run_size) - 1):
        xi = run_size / list_size
        if xi :
            entropie_reel -= xi * math.log2(xi)
    return entropie_reel

def get_entropy_from_runs_separation(liste_separation_runs, list_size):
    # Calcul de l'entropie
    entropie_reel = 0

    for i in range(len(liste_separation_runs) - 1):
        run_size = liste_separation_runs[i+1] - liste_separation_runs[i]
        xi = run_size / list_size
        if xi :
            entropie_reel -= xi * math.log2(xi)

    return entropie_reel


ENTROPY = 0.95
TAILLE_LISTE = 100000000


def get_nb_runs_from_entropy(entropy, list_size):
    max_entropy = get_entropy(1, list_size)
    #print("max_entropy : ", max_entropy)
    wanted_entropy = entropy * max_entropy
    #print("wanted : ", wanted_entropy)

    for run_size in range(1, list_size, 1):
        current_entropy = get_entropy(run_size, list_size)
        #print("current : ", current_entropy)
        if (current_entropy <= wanted_entropy) or ((current_entropy - get_entropy((run_size + 1), list_size))/2 > (current_entropy - wanted_entropy)) :
            return int(list_size / run_size)

    return 1

def get_runs_size_from_entropy(entropy, list_size):
    max_entropy = get_entropy(1, list_size)
    #print("max_entropy : ", max_entropy)
    wanted_entropy = entropy * max_entropy
    #print("wanted : ", wanted_entropy)

    for run_size in range(1, list_size, 1):
        current_entropy = get_entropy(run_size, list_size)
        #print("current : ", current_entropy)
        if (current_entropy <= wanted_entropy) or ((current_entropy - get_entropy((run_size + 1), list_size))/2 > (current_entropy - wanted_entropy)) :
            return run_size

    return list_size

"""
print("wanted    : ", ENTROPY)
nb_runs = get_nb_runs_from_entropy(ENTROPY, TAILLE_LISTE)
print("need runs : ", nb_runs)
print("got       : ", get_entropy(TAILLE_LISTE / nb_runs, TAILLE_LISTE) / get_entropy(1, TAILLE_LISTE))

"""