import os
import shutil

def vider_dossier(chemin_dossier):
    if os.path.exists(chemin_dossier):
        fichiers = os.listdir(chemin_dossier)

        for fichier in fichiers:
            chemin_fichier = os.path.join(chemin_dossier, fichier)

            if os.path.isdir(chemin_fichier):
                shutil.rmtree(chemin_fichier)
            else:
                os.remove(chemin_fichier)
    else:
        print(f"Le dossier {chemin_dossier} n'existe pas.")

