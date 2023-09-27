

#import :
import time
import random
import sys
from pystyle import Colors

#titre :
print(Colors.white + "\n\n\n*Le nombre mystère*\nPar les studios de Lord of game")


#Le menu :
while True:
    choise_starting = input("\n\nQue voulez-vous faire ?\n1 : Jouer\n2 : Règles\n3 : Crédits\n4 : Quitter le jeu\n")
    if choise_starting == "1":
        break
    elif choise_starting == "2":
        print("\nLe but du jeu est de deviner le nombre mystère situé entre deux nombres plus ou moins éloigné en\nfonction de la difficulté, pour cela vous avez 5 tentatives et je vous dirais à chaque fois si il est\nplus grand ou plus petit.")
    elif choise_starting == "3":
        print("\n\n\n------------*Le nombre mystère*------------")
        time.sleep(1)
        print("--------Par les Studios de Lord of game--------")
        time.sleep(1)
        print("\n\n--------Direction des Studios de Lord of game--------")
        time.sleep(1)
        print("- président directeur général    :   Claudel Antoine")
        time.sleep(1)
        print("- directeur développement        :   Claudel Antoine")
        time.sleep(1)
        print("\n--------Direction du Projet--------")
        time.sleep(1)
        print("- directeur général              :   Claudel Antoine")
        time.sleep(1)
        print("- directeur dévéloppement        :   Claudel Antoine")
        time.sleep(1)
        print("\n----équipe de dévéloppement du projet----")
        time.sleep(1)
        print("développeurs :                   - Claudel Antoine")
        time.sleep(1)
        print("\n----aide extérieur aux studios de Lord of Game----")
        time.sleep(1)
        print("développeurs :                   - Garand Isaac")
        time.sleep(1)
    elif choise_starting == "4":
        sys.exit()
    else:
        print("Ceci n'est pas une réponse valide !")

#Le jeu :
while True:
    while True:
        level = input("\nen quel niveau de difficulté voulez-vous jouer ?\n1 : facile ( de 1 à 50 )\n2 : moyen ( de 1 à 100 )\n3 : difficile ( de 1 à 200 )\n")
        if level == "1":
            number_max = 50
            break
        elif level == "2":
            number_max = 100
            break
        elif level == "3":
            number_max = 200
            break
        else:
            print("\nCeci n'est pas une réponse valide !")
    number_min = 1
    number = random.randint (number_min, number_max)
    tries = 5
    print("\nOk alors commençons !")
    while True:
        if tries == 0:
            print (f"\nVous n'avez plus de tentatives...\nDommage vous ferez mieux la prochaine fois.\nLe nombre mystère était {number}.")
            break
        choise_number = input("\nProposez un nombre.\n")
        if not choise_number.isdigit():
            print("Veuillez entrer un nombre valides !")
            continue
        if int(choise_number) > number_max:
            print("Ce nombre est supérieur à la limite maximale !")
            continue
        if int(choise_number) < number_min:
            print("Ce nombre est inférieur à la limite minimale !")
            continue
        if int(choise_number) < number:
            print ("Le nombre mystère est plus grand que votre nombre.")
            tries = tries - 1
        elif int(choise_number) > number:
            print ("Le nombre mystère est plus petit que votre nombre.")
            tries = tries - 1
        elif int(choise_number) == number:
            print ("\nBravo vous avez gagné !!")
            print (f"vous avez utilisé {6 - tries} tentatives.")
            break
    #retour au menu :
    while True:
        Choise_restarting = input("\n\nQue voulez-vous faire ?\n1 : Rejouer\n2 : Revoir les règles\n3 : Crédit\n4 : Quiter le jeu\n")
        if Choise_restarting == "1":
            break
        elif Choise_restarting == "2":
            print("\nLe but du jeu est de deviner le nombre mysthère situé entre deux nombres plus ou moins éloigné en\nfonction de la difficulté, pour cela vous avez 5 tetatives et je vous dirais à chaque fois si il est\nplus grand ou plus petit.")
        elif Choise_restarting == "3":
            print("\n\n\n------------*Le nombre mystère*------------")
            time.sleep(1)
            print("--------Par les Studios de Lord of game--------")
            time.sleep(1)
            print("\n\n--------Direction des Studios de Lord of game--------")
            time.sleep(1)
            print("- président directeur général    :   Claudel Antoine")
            time.sleep(1)
            print("- directeur développement        :   Claudel Antoine")
            time.sleep(1)
            print("\n--------Direction du Projet--------")
            time.sleep(1)
            print("- directeur général              :   Claudel Antoine")
            time.sleep(1)
            print("- directeur dévéloppement        :   Claudel Antoine")
            time.sleep(1)
            print("\n----équipe de dévéloppement du projet----")
            time.sleep(1)
            print("développeurs :                   - Claudel Antoine")
            time.sleep(1)
            print("\n----aide extérieur aux studios de Lord of Game----")
            time.sleep(1)
            print("développeurs :                   - Garant Isaac")
            time.sleep(1)
        elif Choise_restarting == "4":
            sys.exit()
        else:
            print("Ceci n'est pas une réponse valide !")
    continue