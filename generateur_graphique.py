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
        pyplot.savefig('temps_taille.png')


    if graphique == "temps/entropie":
        pyplot.figure(graphique)
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
        pyplot.savefig('temps_entropie.png')


    if graphique == "new_temps/entropie":
        pyplot.figure(graphique)
        #print(liste_benchs)
        liste_benchs_entropie = []



        entro = 0
        next_entro = 1
        iteration = 1
        len_iteration = 0
        boites = dict()
        #while entro != next_entro:
        for key in liste_benchs:
            liste_benchs_entropie = sorted(liste_benchs[key], key=lambda k: float(k['entropie']))
            i = 0
            for bench in liste_benchs_entropie:
                entro = float(bench["entropie"])
                """
                if float(bench["entropie"]) > entro:
                    next_entro = float(bench["entropie"])
                    len_iteration = i-1
                    break
                """

                if not key in boites :
                    boites[key] = dict()
                if not entro in boites[key]:
                    boites[key][entro] = dict()
                boites[key][entro][i] = float(bench["time"])/1000000



                i += 1

            #print(i)

        #print(boites)

        #data_01 = [1,2,3,4,5,6,7,8,9]
        #data_02 = [15,16,17,18,19,20,21,22,23,24,25]
        #data_03 = [5,6,7,8,9,10,11,12,13]

        #boxName = ['data 01','data 02','data 03']
        #data = [data_01,data_02,data_03]

        boxName = list()
        data = list()
        for key in boites["AdaptativeShiverSort"].keys():
            boxName.append(key)
            data.append(list(boites["AdaptativeShiverSort"][key].values()))

        import seaborn as sns
        import pandas as pd
        import numpy as np



        temps = list()
        nb_entro = 0
        nb_val = 0
        for key in boites.keys():
            nb_entro = 0
            for key, val in boites[key].items():
                nb_entro += 1
                #print(val)
                nb_val = val.values()
                print(">> ", key, " >>>> : ", nb_val)
                temps += list(val.values())

            #values = values + [val for val in boites[key].values()]

        print(next(iter(boites)))

        print("nb algos : ", len(boites.keys()))
        print("nb entropies : ", nb_entro)
        print("nb vals : ", nb_val)

        algos = list()

        """
        for key in boites.keys():
            algos = algos + [key for i in range(len(boites[key].values()))] * len(list(list(boites.values())[0].values())[0])
        #algos = algos*int(len(values)/len(algos))
        """


        for key1 in boites.keys():
            for key2, val in boites[key1].items():
                algos += [key1] * len(val.values())


        entropy = list()

        """
        for i in range(len(boites.keys())):
            for key in list(boites.values())[i].keys():
                entropy = entropy + [key] * len(list(list(boites.values())[0].values())[0])
            #entropy = entropy + [key for key in list(boites.values())[0].keys()] * len(list(list(boites.values())[0].values())[0])
        #temps = temps*int(len(values)/len(temps))
        """



        for key1 in boites.keys():
            for key2, val in boites[key1].items():
                entropy += [key2] * len(val.values())




        print("nb val par entro : ", len(list(list(boites.values())[0].values())[0]))

        #print(int(len(values)/len(algos)))
        #print(len(list(list(boites.values())[0].values())[0]))
        #exit()


        print(len([key for key in list(boites.values())[0].keys()]))
        print(len([key for key in boites.keys()]))

        print(len(algos))
        print(len(entropy))
        print(len(temps))

        #print((algos))
        #print((temps))
        #print((values))

        df = pd.DataFrame({'Algorithme': algos,
                           'Entropie': entropy,
                           'Temps': temps })

        ax = sns.boxplot(x='Entropie', hue='Algorithme', y='Temps', data=df, showcaps = False, whis = "range", linewidth=0.5)
        #ax = sns.boxplot(x='Entropie', hue='Algorithme', y='Temps', data=df, showcaps = False, whis = "range", palette = ["red", "yellow", "green", "orange"], linewidth=0.5, color="white")




        #X = np.repeat(np.atleast_2d(np.arange(len([key for key in list(boites.values())[0].keys()]))),len([key for key in boites.keys()]), axis=0)+ np.array([[-.2],[.2]])

        pyplot.show()

        exit()

        #print(boxName)
        #print(data)

        pyplot.boxplot(data)

        pyplot.ylim(0,0.6)

        pyplot.xticks([1,2,3], boxName)
        pyplot.xticks([i for i in range(len(boxName))], boxName)

        #pyplot.savefig('MultipleBoxPlot02.png')
        pyplot.show()



        """

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
        """

### --- --- --- Affichage de tous les graphiques --- --- --- ###


pyplot.show()
