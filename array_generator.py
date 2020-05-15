# -*- coding: UTF-8 -*-
import math
import random, json, os
import entropy_utils

configuration = json.load(open('array_generator_config.json'))


destination_folder = configuration["destination_folder"]

methode = configuration["methode_tri"]
nb_listes = configuration["nb_listes"]
nb_repetitions = configuration["nb_repetitions"] if configuration["nb_repetitions"] > 0 else 1
taille_formule = configuration["taille"]
taille_depart = configuration["taille_depart"]
taille_fin = configuration["taille_fin"]
taille_liste = taille_depart

nb_runs_formule = configuration["nb_runs"]
nb_runs_depart = configuration["nb_runs_depart"]
nb_runs_fin = configuration["nb_runs_fin"]
nb_runs = nb_runs_depart

delta = configuration["delta_separation_runs"] * 100

entropie_demandee_formule = configuration["entropy"] if configuration["entropy"] != "" else "0"

borne_sup = configuration["borne_sup"]
borne_inf = configuration["borne_inf"]

decroissant = bool(configuration["contiens_runs_decroissants"])

# creation d'un fichier qui contient le path de tous les fichiers de listes
fichier_path = open("paths","w+")

num_liste = 0
entropie_demandee = 0

for n in range(nb_listes):
    #taille_liste = int(taille_liste + (taille_fin - taille_depart)/nb_listes)

    # --- --- --- Calcul de la taille de la liste --- --- --- #
    t = taille_liste
    tf = taille_fin
    td = taille_depart
    nb = nb_listes
    n = n # (nième configuration de liste) variable utilisé dans le fichier json de configuration

    taille_liste = int(eval(taille_formule))

    # --- --- --- Calcul du nombre de runs --- --- --- #
    nbr = nb_runs
    nbrf = nb_runs_fin
    nbrd = nb_runs_depart

    nb_runs = int(eval(nb_runs_formule))


    # --- --- --- Calcul de l'entropie demandée --- --- --- #
    la = entropie_demandee

    entropie_demandee = float(eval(entropie_demandee_formule))



    #nb_runs = int(nb_runs + (nb_runs_fin - nb_runs_depart)/nb_listes)

    for repetition in range(nb_repetitions):

        liste = [None]*taille_liste
        entropie = 0.0

        if methode == "alea":
            for i in range(len(liste)):
                liste[i] = random.randint(borne_inf, borne_sup)

            # calcul de l'entropie de la liste
            entropie = entropy_utils.get_entropy(liste)


        elif methode == "run_constant_croiss_lineaires":

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

            # calcul de l'entropie de la liste
            entropie = entropy_utils.get_entropy_from_nb_runs(taille_liste // taille_runs)


        elif methode == "run_alea": # l'entropie est à peu près toujours la même

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

            # calcul de l'entropie de la liste
            entropie = entropy_utils.get_entropy_from_runs_separation(liste_separation_runs, taille_liste)

        elif methode == "entropie_alea": # l'entropie est à peu près toujours la même
            for i in range(len(liste)):
                liste[i] = random.randint(borne_inf, borne_sup)

            taille_max_run = random.randint(0, taille_liste//2)
            nb_runs = random.randint(0, taille_liste//taille_max_run)

            for i in range(nb_runs):
                # configuration du run
                taille_run = random.randint(0, taille_max_run)
                debut_run = random.randint(0, taille_liste - taille_run)
                # ajout du run dans la liste
                sub_list = sorted(liste[debut_run:debut_run+taille_run])
                liste[debut_run:debut_run+taille_run] = sub_list

            # calcul de l'entropie de la liste
            entropie = entropy_utils.get_entropy(liste)


        elif methode == "run_delta":
            # "séparation" = bornes des runs

            # On crée une liste de séparation parfaite qui nous servira de référence pour choisir l'anthropie
            liste_separation_runs_parfaite = [i for i in range(0, (taille_liste), int(taille_liste/nb_runs))]
            liste_separation_runs_parfaite[-1] = taille_liste

            # On met les deux extremums de la liste des séparations
            liste_separation_runs = [0, taille_liste]
            for i in range(1, nb_runs - 0 if nb_runs > 0 else 0):
                separation_min = liste_separation_runs_parfaite[i] - (liste_separation_runs_parfaite[i] * delta / 100) #0 if (i - 1) < 0 else liste_separation_runs_parfaite[i-1]
                separation_max = liste_separation_runs_parfaite[i] + ((liste_separation_runs_parfaite[-1] - liste_separation_runs_parfaite[i]) * delta / 100)
                liste_separation_runs.append(random.randint(int(separation_min), int(separation_max)))

            # On tri les séparations dans le cas où l'anthropie ait permis des cheuvauchements de bornes
            liste_separation_runs.sort()

            # On crée la liste finale en remplissant les runs
            for i in range(len(liste_separation_runs) - 1):
                for j in range(liste_separation_runs[i], liste_separation_runs[i+1]):
                    liste[j] = random.randint(borne_inf, borne_sup)
                liste[liste_separation_runs[i]:liste_separation_runs[i+1]] = sorted(liste[liste_separation_runs[i]:liste_separation_runs[i+1]])

            """
            # Calcul de l'entropie
            entropie_reel = 0
            for i in range(len(liste_separation_runs) - 1):
                xi = (liste_separation_runs[i+1] - liste_separation_runs[i]) / taille_liste
                if xi :
                    entropie_reel -= xi * math.log2(xi)
    
            print("entropie de la liste n°" + str(num_liste) + " : " + str(entropie_reel) + "\n")
            """
            # calcul de l'entropie de la liste
            entropie = entropy_utils.get_entropy_from_runs_separation(liste_separation_runs, taille_liste)


        elif methode == "run_delta_with_unsorted":
            # "séparation" = bornes des runs

            # On crée une liste de séparation parfaite qui nous servira de référence pour choisir l'anthropie
            liste_separation_runs_parfaite = [i for i in range(0, (taille_liste), int(taille_liste/nb_runs))]
            liste_separation_runs_parfaite[-1] = taille_liste



            # On met les deux extremums de la liste des séparations
            liste_separation_runs = [0, taille_liste]
            for i in range(1, nb_runs - 0 if nb_runs > 0 else 0):
                separation_min = liste_separation_runs_parfaite[i] - (liste_separation_runs_parfaite[i] * delta / 100) #0 if (i - 1) < 0 else liste_separation_runs_parfaite[i-1]
                separation_max = liste_separation_runs_parfaite[i] + ((liste_separation_runs_parfaite[-1] - liste_separation_runs_parfaite[i]) * delta / 100)
                liste_separation_runs.append(random.randint(int(separation_min), int(separation_max)))


            # On tri les séparations dans le cas où le delta ait permis des cheuvauchements de bornes
            liste_separation_runs.sort()

            nb_runs_non_tries = 5 # a supp
            # On prend des runs au hasard pour les rendres non triés
            runs_a_ne_pas_trier = dict()
            while nb_runs_non_tries > 0:
                index = random.randint(0, len(liste_separation_runs) - 1)
                if index not in runs_a_ne_pas_trier:
                    runs_a_ne_pas_trier.append(index)
                    nb_runs_non_tries = nb_runs_non_tries - 1

            # On crée la liste finale en remplissant les runs
            for i in range(len(liste_separation_runs) - 1):
                for j in range(liste_separation_runs[i], liste_separation_runs[i+1]):
                    liste[j] = random.randint(borne_inf, borne_sup)
                if i not in runs_a_ne_pas_trier:
                    liste[liste_separation_runs[i]:liste_separation_runs[i+1]] = sorted(liste[liste_separation_runs[i]:liste_separation_runs[i+1]])

            # calcul de l'entropie de la liste
            entropie = entropy_utils.get_entropy_from_runs_separation(liste_separation_runs, taille_liste)

        elif methode == "nb_runs_given_by_entropy":
            run_size_needed = entropy_utils.get_runs_size_from_entropy(entropie_demandee, taille_liste)
            print("run_size_needed : ", run_size_needed)
            liste_separation_runs = [i for i in range(run_size_needed, (taille_liste), run_size_needed)]
            liste_separation_runs.append(0)
            liste_separation_runs.append(taille_liste)
            liste_separation_runs.sort()
            #print("liste_separation_runs : ", liste_separation_runs)


            # On crée la liste finale en remplissant les runs
            for i in range(len(liste_separation_runs) - 1):
                for j in range(liste_separation_runs[i], liste_separation_runs[i+1]):
                    liste[j] = random.randint(borne_inf, borne_sup)
                liste[liste_separation_runs[i]:liste_separation_runs[i+1]] = sorted(liste[liste_separation_runs[i]:liste_separation_runs[i+1]])

            # calcul de l'entropie de la liste
            entropie = entropy_utils.get_entropy_from_nb_runs(taille_liste // run_size_needed)



        else:
            print("Aucune méthode valide n'a été précisé")
            exit()

        # écriture de la liste dans un fichier
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        fichier_liste = open(destination_folder + "/liste" + str(num_liste),"w+")
        fichier_liste_nom = os.path.abspath(fichier_liste.name)
        for element in liste:
            fichier_liste.write(str(element) + " ")
        # On écrit le type de liste et le nombre d'elements qu'il y a dedans
        #fichier_liste.write("\n" + methode + str(num_liste) + " " + str(taille_liste))
        #fichier_liste.write("""
        #{
        #    "type_liste": "%s",
        #    "id_liste": %d,
        #    "taille_liste": %d,
        #    "entropie": %f
        #}
        #""" % (methode, num_liste, taille_liste, entropie))

        fichier_liste.write("\n" + methode + "." + str(num_liste) + " / " + str(taille_liste) + " / " + str(entropie))


        fichier_liste.close()

        # ajout du fichier créé dans le fichier paths
        fichier_path.write(fichier_liste_nom + "\n")




        num_liste += 1



# On n'oublie pas de bien refermer le fichier path
fichier_path.close()

