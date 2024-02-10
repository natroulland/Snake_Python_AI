import matplotlib.pyplot as plt
import numpy as np

axes = plt.gca()

def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as file:
            lignes = file.readlines()
        return [ligne.strip() for ligne in lignes]
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
        return []

def generer_graphique(nom_fichier):
    # Lire les valeurs depuis le fichier
    valeurs = lire_fichier(nom_fichier)
    print(valeurs)

    if not valeurs:
        return

    # Créer le graphique
    plt.scatter(range(1, int(valeurs[0])+1), valeurs[1:], marker='o')
    plt.xlabel('Générations')
    plt.ylabel('Moyenne des scores')
    axes.yaxis.set_ticks([0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
    plt.title('Meilleur score par génération')
    plt.show()

# Appeler la fonction pour générer le graphique
nom_fichier = "valeurs_graphes.txt"
generer_graphique(nom_fichier)
