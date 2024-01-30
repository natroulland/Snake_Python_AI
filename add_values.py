def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as file:
            lignes = file.readlines()
        return lignes
    except FileNotFoundError:
        return []

def ecrire_fichier(nom_fichier, nouvelles_valeurs):
    with open(nom_fichier, 'w') as file:
        file.writelines(nouvelles_valeurs)

def inscrire_et_modifier(nom_fichier, nouvelles_valeurs):
    # Lire les valeurs existantes du fichier
    valeurs = lire_fichier(nom_fichier)

    # Modifier la première valeur
    if valeurs:
        premiere_valeur = valeurs[0].strip().split(',')
        premiere_valeur[0] = str(nouvelles_valeurs[0])
        valeurs[0] = ','.join(premiere_valeur) + '\n'
    else:
        # Si le fichier est vide ou n'existe pas, créer une nouvelle entrée
        valeurs = [str(nouvelles_valeurs[0]) + '\n']

    # Ajouter les nouvelles valeurs dans le fichier
    for nouvelle_valeur in nouvelles_valeurs[1:]:
        valeurs.append(str(nouvelle_valeur) + '\n')

    # Écrire les nouvelles valeurs dans le fichier
    ecrire_fichier(nom_fichier, valeurs)

