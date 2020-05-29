from matplotlib import pyplot
import json, sys, os
import seaborn as sns
import pandas as pd
import math
import numpy as np
import entropy_utils as e
from statistics import mean

from operator import itemgetter

if len(sys.argv) < 2:
    print("--------------------------------------------------------")
    print("   Usage: $ " + sys.argv[0] + " param_1 [param_n] [-s --size]")
    print(" ")
    print("   * param_1: name of a graphic you want")
    print("   * ...")
    print("   * param_n: name of a graphic you want")
    print(" ")
    print("   * -s / --size integer_1 ... integer_n : all list size you want to display")
    print("                                           otherwise, every size will be mixed")
    print("                                           (only for temps/entropie graph)")
    print("--------------------------------------------------------")
    exit(0)

### --- --- --- Parsing des résultats --- --- --- ###

liste_benchs = dict()
algos_a_retirer = ["MergeSort"]
#algos_a_retirer = ["AdaptativeShiverSort", "stdSort", "TimSort"]
nb_algos = 0
DOSSIER_RES = "res_lip6/"

for res_path in [os.getcwd() + "/" + DOSSIER_RES + x for x in os.listdir(DOSSIER_RES)]:
    if "liste" in res_path:
        #print(open(res_path))
        try:
            #res_path = str(path).replace("/tab/", "/res/").split("\n")[0]

            configuration = json.load(open(res_path))

            nb_algos = len(configuration["content"]) - len(algos_a_retirer)


            #print("nb algos : ", nb_algos)
            #print(configuration)
            #print(configuration["content"])

            for resultat_test in configuration["content"]:
                #print(str(resultat_test["meta"]))
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


    if param == "new_temps/taille":
        pyplot.figure(param)
        liste_benchs_entropie = []



        taille = 0
        boites = dict()
        for key in liste_benchs:
            liste_benchs_taille = sorted(liste_benchs[key], key=lambda k: float(k['taille_liste']))
            i = 0
            for bench in liste_benchs_taille:
                taille = float(bench["taille_liste"])

                if not key in boites :
                    boites[key] = dict()
                if not taille in boites[key]:
                    boites[key][taille] = dict()
                boites[key][taille][i] = float(bench["time"])/1000000

                i += 1

        temps = list()
        for key in boites.keys():
            for key, val in boites[key].items():
                temps += list(val.values())

        algos = list()
        for key1 in boites.keys():
            for key2, val in boites[key1].items():
                algos += [key1] * len(val.values())

        taille = list()
        for key1 in boites.keys():
            for key2, val in boites[key1].items():
                taille += [key2] * len(val.values())


        df = pd.DataFrame({'Algorithme': algos,
                           'Taille': taille,
                           'Temps': temps })

        ax = sns.boxplot(x='Taille', hue='Algorithme', y='Temps', data=df, showcaps = False, whis = [0, 100], linewidth=0.5)

        pyplot.savefig('new_temps_taille.png')

    if param == "heatmap":
        pyplot.figure(param)
        liste_benchs_entropie = []



        taille = 0
        boites = dict()
        for key in liste_benchs:
            liste_benchs_entropie = sorted(liste_benchs[key], key=lambda k: float(k['entropie']), reverse=False)

            i = 0
            for bench in liste_benchs_entropie:
                taille = float(bench["taille_liste"])
                entro = float(bench["entropie"])

                max_entropy = e.get_entropy_from_nb_runs(taille)
                taux_entropie = int(round(entro / max_entropy, 1) * 10)

                print("taux_entropie : ", taux_entropie)

                if not key in boites :
                    boites[key] = dict()
                if not taux_entropie in boites[key]:
                    boites[key][taux_entropie] = dict()
                if not taille in boites[key][taux_entropie]:
                    boites[key][taux_entropie][taille] = dict()

                boites[key][taux_entropie][taille][i] = float(bench["time"])/1000000

                i += 1
        taille_listes = len(list(list(list(boites.values())[0].values())[0].values())[0])
        tableau = list()#[[0]*20]*20
        for j in range(4):
            tableau.append(list())
            for i in range(10):
                temps_tab = list()
                for y in range(20):
                    temps_tab.append(0)
                tableau[j].append(temps_tab)
        x = 0
        y = 0
        i = 0
        for key1 in boites.keys():
            for key2, val in boites["AdaptativeShiverSort"].items():
                print(key2)

                for key3, val2 in boites[key1][key2].items():
                    #print(x, y)
                    #print(int(key3/5000)-1, key2, mean(list(val2.values())))
                    tableau[i][key2][int(key3/5000)-1] = mean(list(val2.values()))
                    y += 1
                x += 1
                y = 0
            i += 1

        print(tableau)


        for i in range(len(tableau)):
            pyplot.figure(param)
            ax = sns.heatmap(tableau[i], linewidth=0, cmap="inferno")
            ax.invert_yaxis()
            pyplot.savefig('heatmap' + str(i) + '.png')

        exit()

        pyplot.show()

    if param == "new_heatmap":

        algos_to_display = list()
        for algo in liste_benchs:
            algos_to_display.append(algo)



        pyplot.figure(param)
        liste_benchs_entropie = []



        columns = max(1, math.ceil(math.sqrt(len(algos_to_display))))
        rows = max(1, (columns - 1) if (columns - 1)*columns >= len(algos_to_display) else columns)
        print(columns, rows)
        fig, axes = pyplot.subplots(rows,columns,figsize=[10,10],frameon = False)

        if not type(axes) == np.ndarray :
            if type(axes) == tuple:
                axes = [list(axes)]
            else :
                axes = [[axes]]

        pyplot.tight_layout()
        pyplot.subplots_adjust(left=None, bottom=None, right=None, top= 0.9, wspace=0.25 , hspace=0.2)

        liste_sous_graphes = list()
        d = {}
        i = 0

        for r in range(rows):
            for c in range(columns):
                d[i] = axes[r][c]
                i += 1

        nb_sous_graphes = max(len(algos_to_display), 1)
        data = [dict() for _ in range(nb_sous_graphes)]

        time_min = 0
        time_max = 0

        for n, algo in zip(range(nb_sous_graphes), algos_to_display):

            entro = 0
            iteration = 1
            data[n]["boites"] = dict()
            for key in liste_benchs:
                liste_benchs_entropie = sorted(liste_benchs[key], key=lambda k: float(k['entropie']))
                i = 0
                for bench in liste_benchs_entropie:
                    taille = float(bench["taille_liste"])
                    entro = float(bench["entropie"])

                    max_entropy = e.get_entropy_from_nb_runs(taille)
                    taux_entropie = int(round(entro / max_entropy, 1) * 10)

                    if not key in data[n]["boites"] :
                        data[n]["boites"][key] = dict()
                    if not taux_entropie in data[n]["boites"][key]:
                        data[n]["boites"][key][taux_entropie] = dict()
                    if not taille in data[n]["boites"][key][taux_entropie]:
                        data[n]["boites"][key][taux_entropie][taille] = dict()

                    time = float(bench["time"])/1000000
                    if time > time_max : time_max = time
                    data[n]["boites"][key][taux_entropie][taille][i] = time

                    i += 1

            taille_listes = len(list(list(list(data[n]["boites"].values())[0].values())[0].values())[0])
            data[n]["tableau"] = list()#[[0]*20]*20
            for i in range(10):
                temps_tab = list()
                for y in range(20):
                    temps_tab.append(0)
                data[n]["tableau"].append(temps_tab)
            x = 0
            y = 0
            i = 0

            for key, val in data[n]["boites"][algo].items():
                for key3, val2 in data[n]["boites"][algo][key].items():
                    data[n]["tableau"][key][int(key3/5000)-1] = mean(list(val2.values()))



            data[n]["ax"] = sns.heatmap(data[n]["tableau"], linewidth=0, cmap="inferno", ax = d[n], vmin=time_min, vmax=time_max)
            data[n]["ax"].invert_yaxis()
            d[n].set_title("Performances de l'algorithme " + str(algos_to_display[n]))

        pyplot.savefig('new_heatmap.png')

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
        for arg, i in zip(sys.argv, [x for x in range(len(sys.argv))]):
            if (n+1) < len(sys.argv) and (arg == "--size" or arg == "-s") and (i+1) < len(sys.argv) and sys.argv[i+1].isnumeric():
                size_index = 0
                while (n + size_index + 2) < len(sys.argv) and sys.argv[n + size_index + 2].isnumeric():
                    size_to_display.append(int(sys.argv[n + size_index + 2]))
                    size_index += 1


        print(size_to_display)
        pyplot.figure(param)
        liste_benchs_entropie = []



        columns = max(1, math.ceil(math.sqrt(len(size_to_display))))
        rows = max(1, (columns - 1) if (columns - 1)*columns >= len(size_to_display) else columns)
        print(columns, rows)
        fig, axes = pyplot.subplots(rows,columns,figsize=[10,10],frameon = False)
        if not type(axes) == np.ndarray :
            if type(axes) == tuple:
                axes = [list(axes)]
            else :
                axes = [[axes]]

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

                    #print(key, entro, float(bench["time"])/1000000)

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

            #print("boites : ", data[n]["boites"])
            print("entropy : ", len(data[n]["entropy"]))
            print("algos : ", len(data[n]["algos"]))
            print("temps : ", len(data[n]["temps"]))
            print("size : ", size_to_display[n])
            #print("liste_benchs : ", liste_benchs)



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
