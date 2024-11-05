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
    score = 0
    print("Bienvenue dans le jeu de scrabble 4.1 !")
    
    while niveau is not None:
        mots_choisis = choisir_mots(niveau)
        mots_melanges = melanger_mots(mots_choisis)
        print("Voici les lettres mélangées :")
        print(mots_melanges)
        mots_devinés = []
        
        # Points gagnés par bonne réponse en fonction du niveau
        if niveau == "oui":
            points_par_mot = 1
        elif niveau == "moyen":
            points_par_mot = 2
        else:
            points_par_mot = 3

        while len(mots_devinés) < len(mots_choisis):
            choix = input("Devinez un mot parmi les lettres affichées ou tapez 'next' pour passer au niveau suivant : ").strip().lower()
            
            if choix in mots_choisis and choix not in mots_devinés:
                mots_devinés.append(choix)
                score += points_par_mot
                print(f"Bien deviné ! Votre score est maintenant : {score}")
            elif choix == "next":
                print("Vous avez choisi de passer au niveau suivant sans terminer. Votre score sera divisé par 2.")
                score /= 2  # Pénalité pour passer le niveau
                break
            else:
                score -= 1
                print("Mot incorrect ou déjà deviné. Score actuel :", score)
            
            mots_affiches = [mot if mot in mots_devinés else "_" for mot in mots_choisis]
            print("État actuel des mots trouvés :", " ".join(mots_affiches))
        
        # Passer au niveau suivant après avoir deviné tous les mots
        if niveau == "oui":
            niveau = "moyen"
        elif niveau == "moyen":
            niveau = "difficile"
        else:
            niveau = None  # Terminer le jeu si tous les niveaux sont terminés

    print("Bravo ! Le jeu est terminé.")
    print("Score final :", int(score))

print("Bienvenue dans le jeu du scrabble :\n"
      "En mode facile, vous gagnerez 1 point par bonne réponse.\n"
      "En mode moyen, vous gagnerez 2 points par bonne réponse.\n"
      "En mode difficile, vous gagnerez 3 points par bonne réponse.\n"
      "Cependant, soyez attentif, chaque mauvaise réponse vous fera perdre 1 point. \n"
      "Vous avez la possibilité de passer un niveau en contrepartie, votre score sera divisé par deux.")
niveau = input("Souhaitez-vous lancer une partie ? (oui/non) : ").strip().lower()
if niveau == "oui":
    devine()
