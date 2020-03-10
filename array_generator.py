import random, json, os

configuration = json.load(open('array_generator_config.json'))

methode = configuration["methode_tri"]
nb_listes = configuration["nb_listes"]
taille_formule = configuration["taille"]
taille_depart = configuration["taille_depart"]
taille_fin = configuration["taille_fin"]
taille_liste = taille_depart

nb_runs_depart = configuration["nb_runs_depart"]
nb_runs_fin = configuration["nb_runs_fin"]
nb_runs = nb_runs_depart

anthropie = configuration["anthropie"]

borne_sup = configuration["borne_sup"]
borne_inf = configuration["borne_inf"]

decroissant = bool(configuration["contiens_runs_decroissants"])

# creation d'un fichier qui contient le path de tous les fichiers de listes
fichier_path = open("paths","w+")

for num_liste in range(nb_listes):
    #taille_liste = int(taille_liste + (taille_fin - taille_depart)/nb_listes)
    
    t = taille_liste
    tf = taille_fin
    td = taille_depart
    nb = nb_listes
    n = num_liste # variable utilisé dans le fichier json de configuration
    taille_liste = int(eval(taille_formule))
    
    nb_runs = int(nb_runs + (nb_runs_fin - nb_runs_depart)/nb_listes)

    liste = [None]*taille_liste

    if methode == "alea" :
        for i in range(len(liste)):
            liste[i] = random.randint(borne_inf, borne_sup)


    elif methode == "parti_tri_run_constant_croiss_lineaires":

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


    elif methode == "parti_tri_run_non_constant":

        liste_separation_runs = [0, taille_liste]
        for _ in range(nb_runs - 1 if nb_runs > 0 else 0):
            liste_separation_runs.append(random.randint(0, taille_liste))
        liste_separation_runs.sort()
        for i in range(len(liste_separation_runs) - 1):
            for j in range(liste_separation_runs[i], liste_separation_runs[i+1]):
                liste[j] = random.randint(borne_inf, borne_sup)
            sub_list = sorted(liste[liste_separation_runs[i]:liste_separation_runs[i+1]])
            if(decroissant and random.randint(0, 1)):
                liste[liste_separation_runs[i]:liste_separation_runs[i+1]] = reversed(sub_list)
            else:
                liste[liste_separation_runs[i]:liste_separation_runs[i+1]] = sub_list


    elif methode == "parti_tri_entropie":
        # "séparation" = bornes des runs

        # On crée une liste de séparation parfaite qui nous servira de référence pour choisir l'anthropie
        liste_separation_runs_parfaite = [i for i in range(0, (taille_liste), int(taille_liste/nb_runs))]
        liste_separation_runs_parfaite[-1] = taille_liste

        # On met les deux extremums de la liste des séparations
        liste_separation_runs = [0, taille_liste]
        for i in range(1, nb_runs - 0 if nb_runs > 0 else 0):
            separation_min = liste_separation_runs_parfaite[i] - (liste_separation_runs_parfaite[i] * anthropie / 100) #0 if (i - 1) < 0 else liste_separation_runs_parfaite[i-1]
            separation_max = liste_separation_runs_parfaite[i] + ((liste_separation_runs_parfaite[-1] - liste_separation_runs_parfaite[i]) * anthropie / 100)
            liste_separation_runs.append(random.randint(int(separation_min), int(separation_max)))
        
        # On tri les séparations dans le cas où l'anthropie ait permis des cheuvauchements de bornes
        liste_separation_runs.sort()

        # On crée la liste finale en remplissant les runs
        for i in range(len(liste_separation_runs) - 1):
            for j in range(liste_separation_runs[i], liste_separation_runs[i+1]):
                liste[j] = random.randint(borne_inf, borne_sup)
            liste[liste_separation_runs[i]:liste_separation_runs[i+1]] = sorted(liste[liste_separation_runs[i]:liste_separation_runs[i+1]])
    else:
        print("Aucune méthode valide n'a été précisé")
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


