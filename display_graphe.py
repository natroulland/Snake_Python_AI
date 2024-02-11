import matplotlib.pyplot as plt
import numpy as np

axes = plt.gca()

def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as file:
            lignes = file.readlines()
        return [float(ligne.strip()) for ligne in lignes]
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
        return []

def generer_graphique():
    valeurs_sigmoid = lire_fichier("graphs/valeurs_graphes_sigmoid.txt")
    valeurs_tanh = lire_fichier("graphs/valeurs_graphes_tanh.txt")
    valeurs_relu = lire_fichier("valeurs_graphes.txt")

    if not valeurs_sigmoid or not valeurs_tanh or not valeurs_relu:
        return

    # plt.scatter(range(1, int(valeurs_sigmoid[0])+1), valeurs_sigmoid[1:], marker='o', color='red', label = "Fonction sigmoid")
    plt.scatter(range(1, int(valeurs_relu[0])+1), valeurs_relu[1:], marker='o', color='blue', label = "Fonction relu")
    # plt.scatter(range(1, int(valeurs_tanh[0])+1), valeurs_tanh[1:], marker='o', color='green', label = "Fonction tanh")
    plt.xlabel('Générations')
    plt.ylabel('Scores')
    axes.set_yticks(ticks=[0, 1, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11])
    plt.title('Moyenne des scores par génération')
    plt.legend()
    plt.show()

generer_graphique()
