import matplotlib.pyplot as plt

def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as file:
            lignes = file.readlines()
        return [int(ligne.strip()) for ligne in lignes]
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
        return []

def generer_graphique(nom_fichier):
    # Lire les valeurs depuis le fichier
    valeurs = lire_fichier(nom_fichier)

    if not valeurs:
        return

    # Créer le graphique
    plt.scatter(range(1, valeurs[0]), valeurs[1:], marker='o')
    plt.xlabel('Générations')
    plt.ylabel('Valeurs')
    plt.title('Meilleur score par génération')
    plt.show()

# Appeler la fonction pour générer le graphique
nom_fichier = "valeurs_graphes.txt"
generer_graphique(nom_fichier)
