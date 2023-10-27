import histoire2foot

# Ici vos fonctions dédiées aux interactions
def verifier_equipe_liste(liste, equipe):
    val = False
    for match in liste:
        if match[1] == equipe or match[2] == equipe:
            val = True
    return val

def verifier_equipe_match(equipe, match):
    val = False
    if match[1] == equipe or match[2] == equipe:
        val = True
    return val


# ici votre programme principal
def programme_principal():
    val = None
    nom = input("Quel fichiers voulez vous ouvrir ? \n -1 le fichier 1? \n -2 le fichier 2 ? \n -3 le fichier 3 ? \n ")
    if int(nom) ==1:
        liste_ac=histoire2foot.charger_matchs("histoire1.csv")
        new = input("voulez vous ouvrir un autre match? \n -1 le match 2 \n -2 le match 3 \n -3 les 3 \n -4 Non \n  ")
        if int(new)==1:
            liste=histoire2foot.charger_matchs("histoire2.csv")
            liste_ac=histoire2foot.fusionner_matchs(liste_ac, liste)
        elif int(new)==2:
            liste=histoire2foot.charger_matchs("histoire3.csv")
            liste_ac=histoire2foot.fusionner_matchs(liste_ac, liste)
        elif int(new)==3:
            liste=histoire2foot.charger_matchs("histoire2.csv")
            liste_ac=histoire2foot.fusionner_matchs(liste, liste_ac)
            liste=histoire2foot.charger_matchs("histoire3.csv")
            liste_ac=histoire2foot.fusionner_matchs(liste_ac, liste)
        elif int(new)==4:
            pass
    elif int(nom) == 2 : 
        liste_ac=histoire2foot.charger_matchs("histoire2.csv")
        new = input("voulez vous ouvrir un autre match? \n -1 le match 1 \n -2 le match 3 \n -3 les 3 \n -4 Non \n  ")
        if int(new)==1:
            liste=histoire2foot.charger_matchs("histoire1.csv")
            liste_ac=histoire2foot.fusionner_matchs(liste_ac, liste)
        elif int(new)==2:
            liste=histoire2foot.charger_matchs("histoire3.csv")
            liste_ac=histoire2foot.fusionner_matchs(liste_ac, liste)
        elif int(new)==3:
            liste=histoire2foot.charger_matchs("histoire1.csv")
            liste_ac=histoire2foot.fusionner_matchs(liste, liste_ac)
            liste=histoire2foot.charger_matchs("histoire3.csv")
            liste_ac=histoire2foot.fusionner_matchs(liste_ac, liste)
        elif int(new)==4:
            pass
    elif int(nom) == 3 : 
        liste_ac = histoire2foot.charger_matchs("histoire3.csv")
        new = input("voulez vous ouvrir un autre match? \n -1 le match 1 \n -2 le match 2 \n -3 les 3  \n -4 Non \n ")
        if int(new)==1:
            liste=histoire2foot.charger_matchs("histoire1.csv")
            liste_ac=histoire2foot.fusionner_matchs(liste_ac, liste)
        elif int(new)==2:
            liste=histoire2foot.charger_matchs("histoire2.csv")
            liste_ac=histoire2foot.fusionner_matchs(liste_ac, liste)
        elif int(new)==3:
            liste=histoire2foot.charger_matchs("histoire1.csv")
            liste_ac=histoire2foot.fusionner_matchs(liste, liste_ac)
            liste=histoire2foot.charger_matchs("histoire2.csv")
            liste_ac=histoire2foot.fusionner_matchs(liste_ac, liste)
        elif int(new)==4:
            pass
    else:
        return "Désolé, cette action n'est pas possible. Veuillez réessayer"
    info = input("Que cherchez vous? \n -1 Infos d'une équipe: \n -2 Infos d'une liste \n")
    if info == '1':
        equipe = input("De quelle équipe voulez-vous des informations?")
        if verifier_equipe_liste(liste_ac, equipe) == False:
            return "Cette équipe n'existe pas ou ne se trouve pas dans le fichier"
        valeur = input("Quel type d'informations? \n -1 Ratio Victoire/Nul/Défaite \n -2 Date de prmière victoire \n -3 Plus longue Win Streak \n -4 Plus de victoire ou de défaite \n")
        if valeur == '1':
            val = histoire2foot.resultats_equipe(liste_ac, equipe)
            print("L'équipe a gagné",val[0],"fois, fait nul",val[1],"fois et a perdu",val[2],"fois")
        elif valeur == '2':
            val = histoire2foot.premiere_victoire(liste_ac, equipe)
            if val == None:
                print("L'équipe n'a pas encore gagné de match :(")
            else:
                print("La prmière victoire de cette équipe fut le",val)
        elif valeur == '3':
            val = histoire2foot.nb_matchs_sans_defaites(liste_ac, equipe)
            print("La plus grande Win streak de cette équipe est de",val,"victoires!")
        elif valeur == '4':
            val = histoire2foot.plus_de_victoires_que_defaites(liste_ac, equipe)
            if val == True:
                print("L'équipe a réalisé plus de victoires que de défaites")
            else:
                print("L'équipe a réalisé moins de victoires que de défaites ou autant de victoires que de défaites")
    if info == '2':
        cherche = input("Que cherchez vous? \n -1 Le gagnant d'un certain match \n -2 Si un certain match à été gagné à domicile \n -3 Le nombre de buts marqué dans un certain match \n -4 Tout les matchs d'une certaine ville \n -5 La moyenne des buts d'une compétition \n -6 Les plus grands écarts de buts \n -7 Les équipes de la liste \n -8 Les matchs avec le plus de buts \n -9 Les équipes avec le moins de défaites \n")
        if cherche == '1' or cherche == 2 or cherche == 3:
            date = input("Veuillez inserer une date:")
            equipe = input("Veuillez donner le nom d'une des équipes participantes")
            if cherche == '1':
                for match in liste_ac:
                    if match[0] == date and verifier_equipe_match(equipe, match) == True:
                        val = histoire2foot.equipe_gagnante(match)
                        if val == None:
                            print("Il y a eu un match nul")
                        else:
                            print(val,"a gagné ce match")
            elif cherche == '2':
                for match in liste_ac:
                    if match[0] == date and verifier_equipe_match(equipe, match) == True:
                        val = histoire2foot.victoire_a_domicile(match)
                        if val == True:
                            print("Il y a eu victoire à domicile")
                        else:
                            print("Il n'y a pas eu victoire à domicile")
            elif cherche == '3':
                for match in liste_ac:
                    if match[0] == date and verifier_equipe_match(equipe, match) == True:
                        val = histoire2foot.nb_buts_marques(match)
                        print(val,"buts ont été marqués")
        elif cherche == '4':
            ville = input("Veuillez donner le nom d'une ville")
            liste_ville = histoire2foot.match_ville(liste_ac, ville)
            print(liste_ville,"sont la liste des matchs qui se sont déroulés dans",ville)
        elif cherche == '5':
            compet = input("Veuillez donner le nom d'une compétition")
            moy = histoire2foot.nombre_moyen_buts(liste_ac, compet)
            print("Le nombre moyen de but par match sur cette compétition est de",moy)
        elif cherche == '6':
            liste_ecart = histoire2foot.plus_gros_scores(liste_ac)
            print(liste_ecart,"sont les matchs avec les plus grand écart de buts mis")
        elif cherche == '7':
            liste_equipe = histoire2foot.liste_des_equipes(liste_ac)
            print(liste_equipe,"sont toutes les équipes ayant participées aux matchs de la liste")
        elif cherche == '8':
            liste_spectaculaires = histoire2foot.matchs_spectaculaires(liste_ac)
            print(liste_spectaculaires,"sont les match où le nombre de but est le plus important")
        elif cherche == '9':
            liste_best = histoire2foot.meilleures_equipes(liste_ac)
            print(liste_best,"sont les équipes qui ont le moins de défaite")

print(programme_principal())