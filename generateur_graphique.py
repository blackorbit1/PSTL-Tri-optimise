from matplotlib import pyplot
import json, sys
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

for path in open('paths'):
    try:
        res_path = str(path).replace("/tab/", "/res/").split("\n")[0]
        configuration = json.load(open(res_path))

        for resultat_test in configuration["content"]:
            methode_liste, taille_liste, entropie = str(resultat_test["meta"]).split(" / ")
            if resultat_test["algo"] != "MergeSort": # <<<<< A SUPP
                algo = resultat_test["algo"]
                if algo not in liste_benchs: liste_benchs[algo] = []
                liste_benchs[algo].append({
                    "methode_liste": methode_liste.split(".")[0].replace("_", " "),
                    "taille_liste": taille_liste,
                    "time": resultat_test["time"],
                    "entropie": entropie
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

for graphique, n in zip(sys.argv[1:], range(1, len(sys.argv))):

    if graphique == "temps/taille":
        pyplot.figure(graphique)
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
        pyplot.savefig('result.png')

    if graphique == "temps/entropie":
        pyplot.figure(graphique)
        #print(liste_benchs)
        liste_benchs_entropie = []

        """

        entro = 0
        next_entro = 0
        iteration = 1
        len_iteration = 0
        boites = dict()
        while entro != next_entro:
            for key in liste_benchs:
                liste_benchs_entropie = sorted(liste_benchs[key], key=lambda k: float(k['entropie']))
                i = 0
                for bench in liste_benchs_entropie:
                    if bench["entropie"] > entro:
                        next_entro = bench["entropie"]
                        len_iteration = i-1
                        break
                    boites[key][entro][i] = bench["time"]

                    i += 1



        entro = 0
        next_entro = 0
        iteration = 0
        boites = dict()
        while entro != next_entro:
            for key in liste_benchs:
                liste_benchs_entropie = sorted(liste_benchs[key], key=lambda k: float(k['entropie']))
                i = 0
                for bench in liste_benchs_entropie:
                    if bench["entropie"] > entro:
                        next_entro = bench["entropie"]
                        len_iteration = i-1
                        break
                    boites[key][entro][i] = bench["time"]

                    i += 1
                    
        """



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
        pyplot.savefig('result.png')

### --- --- --- Affichage de tous les graphiques --- --- --- ###


pyplot.show()
