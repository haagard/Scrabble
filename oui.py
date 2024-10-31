import pygame
import random

Mots_facile = ["nuit", "jour", "haut", "petit", "lune"]
Mots_moyen = ["actif", "brume", "carte", "rhume"]
Mots_difficile = ["adjuger", "grizzly", "jacuzzi", "voliere"]

def choisir_mots(niveau):
    if niveau == "oui":
        return random.sample(Mots_facile, 3)
    elif niveau == "moyen":
        return random.sample(Mots_moyen, 3)
    elif niveau == "difficile":
        return random.sample(Mots_difficile, 3)

def melanger_mots(mots):
    lettres = []
    for mot in mots:
        lettres.extend(list(mot))
    random.shuffle(lettres)
    return "".join(lettres)

def devine():
    niveau = "oui"  
    victoire = 0
    print("Bienvenue dans le jeu de scrabble 4.1 !")

    while niveau is not None:  
        mots_choisis = choisir_mots(niveau)
        mots_melanges = melanger_mots(mots_choisis)
        print("Voici les lettres mélangées :")
        print(mots_melanges)
        mots_devinés = []

        while len(mots_devinés) < len(mots_choisis):
            choix = input("Devinez un mot parmi les mots affichés : ").strip().lower()
            if choix in mots_choisis and choix not in mots_devinés:
                mots_devinés.append(choix)
                print(f"Bien joué ! Vous avez trouvé : {choix}")
            else:
                print("Ce mot n'est pas dans la liste ou a déjà été deviné.")
            mots_affiches = [mot if mot in mots_devinés else "_" for mot in mots_choisis]
            print("État actuel des mots trouvés :", " ".join(mots_affiches))

        victoire += 1  
        print("Félicitations ! Vous avez deviné tous les mots :", ", ".join(mots_choisis))

    
        if niveau == "oui":
            niveau = "moyen"
        elif niveau == "moyen":
            niveau = "difficile"
        else:
            niveau = None
    print(" G G t'as tout finis")

    
niveau = input("Souhaitez-vous lancer une partie ? (oui/non) : ").strip().lower()
devine()
