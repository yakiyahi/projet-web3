import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Exemple de données
cands = [
    {"nom": "Candidat A", "cout": 1000, "references": 1, "duree": 1, "solution": 4, "qualite": 9,
     "delais": 8.0, "commun": 9.0, "satis": 7},
    {"nom": "Candidat B", "cout": 100, "references": 1, "duree": 2, "solution": 1,
     "qualite": 8, "delais": 6.0, "commun": 8.0, "satis": 7
     },
    {"nom": "Candidat C", "cout": 5000, "references": 2, "duree": 5, "solution": 4, "qualite": 7,
     "delais": 9.0, "commun": 6.0, "satis": 8}
]
def evaluer_candidats(candidats):
    # Critères et poids
    poids = {
        "prix": 0.3,
        "references": 0.4,
        "duree": 0.2,
        "passe": 0.5
    }

    # Préparer les données
    data = np.array([[c["prix"], c["references"], c["duree"], c["passe"]] for c in candidats])

    # Inverser les valeurs pour le coût et la durée pour que les plus petites valeurs soient meilleures
    data[:, 0] = -data[:, 0]  # Inverser les coûts
    data[:, 2] = -data[:, 2]  # Inverser les durées

    # Normaliser les données entre 0 et 1
    scaler = MinMaxScaler()
    data_normalized = scaler.fit_transform(data)

    # Calculer les scores pondérés
    scores = np.dot(data_normalized, np.array([poids['prix'], poids['references'], poids['duree'], poids['passe']]))
    soumis = []
    # Ajouter les scores aux candidats
    for i, candidat in enumerate(candidats):
        candidat["score"] = scores[i]
        #print('candidats: ', candidat)
        soumis.append(candidat)

    # Trouver le meilleur candidat
    meilleur_candidat = max(candidats, key=lambda x: x["score"])

    # Afficher le meilleur candidat
    #print("Le meilleur candidat est :", meilleur_candidat["nom"])
    #print("Détails :", meilleur_candidat)

    return soumis, meilleur_candidat
