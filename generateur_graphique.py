from matplotlib import pyplot
from math import log
import random, json, os

configuration = json.load(open('data.json'))


liste_benchs = dict()

for benchmark in configuration["benchmarks"]:
    nom_benchmark = benchmark["name"].split("/")[0]
    if nom_benchmark not in liste_benchs : liste_benchs[nom_benchmark] = []
    liste_benchs[nom_benchmark].append(benchmark["iterations"])

for key in liste_benchs:
    pyplot.plot([i for i in range(len(liste_benchs[key]))], liste_benchs[key], marker='o', linestyle="-", label=key)
    pyplot.ylabel("iterations par secondes")
    pyplot.xlabel("n° liste")




pyplot.legend(loc="upper right")
pyplot.show()