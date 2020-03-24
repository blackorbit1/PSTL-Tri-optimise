from matplotlib import pyplot
from math import log
import random, json, os



liste_benchs = dict()

for path in open('paths'):
    res_path = str(path).replace("/tab/", "/res/").split("\n")[0]
    configuration = json.load(open(res_path))

    for resultat_test in configuration["content"]:
        methode_liste, taille_liste, entropie = str(resultat_test["meta"]).split(" / ")
        algo = resultat_test["algo"]
        if algo not in liste_benchs : liste_benchs[algo] = []
        liste_benchs[algo].append({
            "methode_liste" : methode_liste.split(".")[0].replace("_", " "),
            "taille_liste" : taille_liste,
            "time" : resultat_test["time"],
            "entropie" : entropie
        })
"""
fig, host = pyplot.subplots()
par1 = host.twinx()
par2 = host.twinx()
"""

for key in liste_benchs:
    pyplot.plot([i["taille_liste"] for i in liste_benchs[key]], [(int(i["time"])/1000000) for i in liste_benchs[key]], marker='o', linestyle="-", label=key)
    pyplot.ylabel("temps (sec)")
    pyplot.xlabel("nb elements")

# Plot y2 vs x in red on the right vertical axis.
pyplot.twinx()
pyplot.ylabel("entropie", color="r")
pyplot.tick_params(axis="y", labelcolor="r")
#print([i["entropie"] for i in liste_benchs[key]])
pyplot.plot([i["taille_liste"] for i in liste_benchs[key]], [i["entropie"] for i in liste_benchs[key]], "r-", marker='o', linestyle=":")
#pyplot.plot(x, y2, "r-", linewidth=2)



pyplot.legend(loc="upper right")
pyplot.savefig('result.png')
pyplot.show()