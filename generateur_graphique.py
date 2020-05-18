from matplotlib import pyplot
import json, sys
import seaborn as sns
import pandas as pd
import math
import numpy as np
from operator import itemgetter

if len(sys.argv) < 2:
    print("--------------------------------------------------------")
    print("   Usage: $ " + sys.argv[0] + " param_1 [param_n]")
    print(" ")
    print("   * param_1: name of a graphic you want")
    print("   * ...")
    print("   * param_n: name of a graphic you want")
    print("--------------------------------------------------------")
    exit(0)

### --- --- --- Parsing des résultats --- --- --- ###

liste_benchs = dict()
algos_a_retirer = ["MergeSort"]
nb_algos = 0

for path in open('paths'):
    try:
        res_path = str(path).replace("/tab/", "/res/").split("\n")[0]
        configuration = json.load(open(res_path))

        nb_algos = len(configuration["content"]) - len(algos_a_retirer)

        #print("nb algos : ", nb_algos)

        for resultat_test in configuration["content"]:
            methode_liste, taille_liste, entropie = str(resultat_test["meta"]).split(" / ")
            if not resultat_test["algo"] in algos_a_retirer: # <<<<< A SUPP
                algo = resultat_test["algo"]
                if algo not in liste_benchs: liste_benchs[algo] = []
                liste_benchs[algo].append({
                    "methode_liste": methode_liste.split(".")[0].replace("_", " "),
                    "taille_liste": taille_liste,
                    "time": resultat_test["time"],
                    "entropie": round(float(entropie), 3)
                })
    except Exception:
        pass
"""
fig, host = pyplot.subplots()
par1 = host.twinx()
par2 = host.twinx()
"""


"""
from matplotlib.pyplot import *
import numpy


def moy_e(M,T):
    return 1.0/(numpy.exp(1.0/T)-1)-M/(numpy.exp(M/T)-1)

def var_e(M,T):
    return numpy.exp(1.0/T)/(numpy.exp(1.0/T)-1)**2-M**2*numpy.exp(-M/T)/(1-numpy.exp(-M/T))**2

def ecart_e(M,T):
    return numpy.sqrt(var_e(M,T))

def Cv(M,T):
    return var_e(M,T)/T**2
"""


### --- --- --- Creations des graphiques demandés --- --- --- ###

for param, n in zip(sys.argv[1:], range(1, len(sys.argv))):

    if param == "temps/taille":
        pyplot.figure(param)
        for key in liste_benchs:
            pyplot.plot([i["taille_liste"] for i in liste_benchs[key]],
                        [(int(i["time"]) / 1000000) for i in liste_benchs[key]], marker='o', linestyle="-", label=key)
            pyplot.ylabel("temps (sec)")
            pyplot.xlabel("nb elements")

        """
        # Plot y2 vs x in red on the right vertical axis.
        pyplot.twinx()
        pyplot.ylabel("entropie", color="r")
        pyplot.tick_params(axis="y", labelcolor="r")
        # print([i["entropie"] for i in liste_benchs[key]])
        pyplot.plot([i["taille_liste"] for i in liste_benchs[key]], [i["entropie"] for i in liste_benchs[key]], "r-",
                    marker='o', linestyle=":")
        # pyplot.plot(x, y2, "r-", linewidth=2)
        """


        pyplot.legend(loc="upper left")
        pyplot.savefig('temps_taille.png')


    if param == "old_temps/entropie":
        pyplot.figure(param)
        #print(liste_benchs)
        liste_benchs_entropie = []

        for key in liste_benchs:


            #pyplot.boxplot([[1, 2, 3, 4, 5, 13], [6, 7, 8, 10, 10, 11, 12], [1, 2, 3]])



            #print("\n", key, "\n")
            liste_benchs_entropie = sorted(liste_benchs[key], key=lambda k: float(k['entropie']))
            #liste_benchs_entropie = sorted(liste_benchs[key], key=itemgetter('entropie'))
            #print(liste_benchs_entropie)
            #print("\n\n")
            pyplot.plot([i["entropie"] for i in liste_benchs_entropie],
                        [(int(i["time"]) / 1000000) for i in liste_benchs_entropie], marker='o', linestyle="-", label=key)
            pyplot.ylabel("temps (sec)")
            pyplot.xlabel("entropie")

        pyplot.xticks(rotation=90, ha='right')
        # pyplot.axis.Axis.set_major_formatter(ticker.FormatStrFormatter('%0.4f'))
        pyplot.legend(loc="upper left")
        pyplot.tight_layout()
        pyplot.savefig('old_temps_entropie.png')


    if param == "temps/entropie":
        size_to_display = list()
        if (n+1) < len(sys.argv) and (sys.argv[n+1] == "--size" or sys.argv[n+1] == "-s") :
            size_index = 0
            while (n + size_index + 2) < len(sys.argv) and sys.argv[n + size_index + 2].isnumeric():
                size_to_display.append(int(sys.argv[n + size_index + 2]))
                size_index += 1

        pyplot.figure(param)
        liste_benchs_entropie = []



        columns = math.ceil(math.sqrt(len(size_to_display)))
        rows = (columns - 1) if (columns - 1)*columns >= len(size_to_display) else columns
        fig, axes = pyplot.subplots(rows,columns,figsize=[10,10],frameon = False)
        if not type(axes) == np.ndarray:
            axes = [list(axes)]
        pyplot.tight_layout()
        pyplot.subplots_adjust(left=None, bottom=None, right=None, top= 0.9, wspace=0.25 , hspace=0.2)

        liste_sous_graphes = list()
        d = {}
        i = 0

        for r in range(rows):
            for c in range(columns):
                d[i] = axes[r][c]
                i += 1

        nb_sous_graphes = max(len(size_to_display), 1)
        data = [dict() for _ in range(nb_sous_graphes)]

        for n in range(nb_sous_graphes):

            entro = 0
            iteration = 1
            data[n]["boites"] = dict()
            for key in liste_benchs:
                liste_benchs_entropie = sorted(liste_benchs[key], key=lambda k: float(k['entropie']))
                i = 0
                for bench in liste_benchs_entropie:
                    entro = float(bench["entropie"])

                    if not key in data[n]["boites"] :
                        data[n]["boites"][key] = dict()
                    if not entro in data[n]["boites"][key]:
                        data[n]["boites"][key][entro] = dict()
                    if (len(size_to_display) > 0 and size_to_display[n] == int(bench["taille_liste"])) or len(size_to_display) == 0 :
                        data[n]["boites"][key][entro][i] = float(bench["time"])/1000000

                    i += 1



            data[n]["temps"] = list()
            for key in data[n]["boites"].keys():
                for key, val in data[n]["boites"][key].items():
                    data[n]["temps"] += list(val.values())

            data[n]["algos"] = list()
            for key1 in data[n]["boites"].keys():
                for key2, val in data[n]["boites"][key1].items():
                    data[n]["algos"] += [key1] * len(val.values())

            data[n]["entropy"] = list()
            for key1 in data[n]["boites"].keys():
                for key2, val in data[n]["boites"][key1].items():
                    data[n]["entropy"] += [key2] * len(val.values())





            data[n]["df"] = pd.DataFrame({'Algorithme': data[n]["algos"],
                               'Entropie': data[n]["entropy"],
                               'Temps': data[n]["temps"] })


            data[n]["ax"] = sns.boxplot(ax = d[n], x='Entropie', hue='Algorithme', y='Temps', data=data[n]["df"], showcaps = False, whis = [0, 100], linewidth=0.5)
            if nb_sous_graphes > 1 :
                d[n].set_title("listes de taille " + str(size_to_display[n]))
            else :
                d[n].set_title("Temps d'execution par rapport à l'entropie")
        pyplot.savefig('temps_entropie.png')


### --- --- --- Affichage de tous les graphiques --- --- --- ###


#pyplot.show()
