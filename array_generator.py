import random, json, os

configuration = json.load(open('array_generator_config.json'))

methode = configuration["methode_tri"]
nb_listes = configuration["nb_listes"]
taille_depart = configuration["taille_depart"]
taille_fin = configuration["taille_fin"]
taille_liste = taille_depart

nb_runs_depart = configuration["nb_runs_depart"]
nb_runs_fin = configuration["nb_runs_fin"]
nb_runs = nb_runs_depart

borne_sup = configuration["borne_sup"]
borne_inf = configuration["borne_inf"]

decroissant = bool(configuration["contiens_runs_decroissants"])

# creation d'un fichier qui contient le path de tous les fichiers de listes
fichier_path = open("paths","w+")

for num_liste in range(nb_listes):
    taille_liste = int(taille_liste + (taille_fin - taille_depart)/nb_listes)
    nb_runs = int(nb_runs + (nb_runs_fin - taille_depart)/nb_listes)

    liste = [None]*taille_liste

    if methode == "alea" :
        for i in range(len(liste)):
            liste[i] = random.randint(borne_inf, borne_sup)
    elif methode == "parti_tri_run_constant":
        taille_runs = taille_liste / nb_runs
        increment = 0
        run_decroissant = False
        for _ in range(nb_runs):
            nb_marches = int(increment + taille_runs) - int(increment)
            distance_var = (borne_sup - borne_inf)//nb_marches
            min_acc = borne_inf
            max_acc = borne_inf + distance_var
            if(decroissant and random.randint(0, 1)): run_decroissant = True
            for i in range(int(increment), min(int(increment + taille_runs), len(liste))):
                if run_decroissant:
                    liste[i] = borne_sup - random.randint(min_acc, max_acc)
                else:
                    liste[i] = random.randint(min_acc, max_acc)
                min_acc = min_acc + distance_var
                max_acc = max_acc + distance_var
            increment = increment + taille_runs
            run_decroissant = False
    else:
        print("Aucune méthode n'a été précisé")
        exit()

    # écriture de la liste dans un fichier
    fichier_liste = open("liste" + str(num_liste),"w+")
    fichier_liste_nom = os.path.abspath(fichier_liste.name)
    for element in liste:
        fichier_liste.write(str(element) + " ")
    fichier_liste.close()

    # ajout du fichier créé dans le fichier paths
    fichier_path.write(fichier_liste_nom + "\n")

# On n'oublie pas de bien refermer le fichier path
fichier_path.close()


