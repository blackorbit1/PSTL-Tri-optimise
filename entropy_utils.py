from matplotlib import pyplot
from math import log
import math
import random, json, os, time

"""
def get_entropy(run_size, list_size):
    # Calcul de l'entropie
    entropie_reel = 0
    for i in range(int(list_size/run_size) - 1):
        xi = run_size / list_size
        if xi :
            entropie_reel -= xi * math.log2(xi)
    return entropie_reel
"""

def get_entropy_from_nb_runs(nb_run):
    return math.log2(nb_run)


def get_entropy_from_runs_separation(liste_separation_runs, list_size):
    # Calcul de l'entropie
    entropie_reel = 0

    for i in range(len(liste_separation_runs) - 1):
        run_size = liste_separation_runs[i+1] - liste_separation_runs[i]
        xi = run_size / list_size
        if xi :
            entropie_reel -= xi * math.log2(xi)

    return entropie_reel

def get_entropy(liste):
    liste_separation_runs = [0]
    last_element = liste[0]
    for element, i in zip(liste[1:], range(1, len(liste))):
        if last_element > element:
            liste_separation_runs.append(i)
    if len(liste) - 1 not in liste_separation_runs : liste_separation_runs.append(len(liste) - 1)
    return get_entropy_from_runs_separation(liste_separation_runs, len(liste))


"""
def get_nb_runs_from_entropy(entropy, list_size):
    max_entropy = get_entropy_from_nb_runs(1, list_size)
    #print("max_entropy : ", max_entropy)
    wanted_entropy = entropy * max_entropy
    #print("wanted : ", wanted_entropy)

    for run_size in range(1, list_size, 1):
        current_entropy = get_entropy_from_nb_runs(run_size, list_size)
        #print("current : ", current_entropy)
        if (current_entropy <= wanted_entropy) or ((current_entropy - get_entropy_from_nb_runs((run_size + 1), list_size))/2 > (current_entropy - wanted_entropy)) :
            return int(list_size / run_size)

    return 1

def get_runs_size_from_entropy(entropy, list_size):
    max_entropy = get_entropy_from_nb_runs(1, list_size)
    #print("max_entropy : ", max_entropy)
    wanted_entropy = entropy * max_entropy
    #print("wanted : ", wanted_entropy)

    for run_size in range(1, list_size, 1):
        current_entropy = get_entropy_from_nb_runs(run_size, list_size)
        #print("current : ", current_entropy)
        if (current_entropy <= wanted_entropy) or ((current_entropy - get_entropy_from_nb_runs((run_size + 1), list_size))/2 > (current_entropy - wanted_entropy)) :
            return run_size

    return list_size
"""

def get_nb_runs_from_entropy(entropy, list_size):
    max_entropy = get_entropy_from_nb_runs(list_size)
    wanted_entropy = entropy * max_entropy

    for nb_runs in range(1, list_size, 1):
        current_entropy = get_entropy_from_nb_runs(nb_runs)
        if (current_entropy >= wanted_entropy) or ((current_entropy - get_entropy_from_nb_runs((nb_runs + 1)))/2 < (current_entropy - wanted_entropy)) :
            return int(nb_runs)

    return 1

def get_runs_size_from_entropy(entropy, list_size):
    max_entropy = get_entropy_from_nb_runs(list_size)
    wanted_entropy = entropy * max_entropy

    for nb_runs in range(1, list_size, 1):
        current_entropy = get_entropy_from_nb_runs(nb_runs)
        if (current_entropy >= wanted_entropy) or ((current_entropy - get_entropy_from_nb_runs((nb_runs + 1)))/2 < (current_entropy - wanted_entropy)) :
            return int(list_size / nb_runs)

    return list_size

