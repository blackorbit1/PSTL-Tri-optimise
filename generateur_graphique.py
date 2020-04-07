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


        pyplot.legend(loc="upper right")
        pyplot.savefig('result.png')

    if graphique == "temps/entropie":
        pyplot.figure(graphique)
        #print(liste_benchs)
        liste_benchs_entropie = []

        for key in liste_benchs:
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
        pyplot.legend(loc="upper right")
        pyplot.tight_layout()
        pyplot.savefig('result.png')

### --- --- --- Affichage de tous les graphiques --- --- --- ###


pyplot.show()
