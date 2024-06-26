import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Exemple de données
candidats = [
    {"nom": "Candidat A", "cout": 100, "references": 1, "duree": 1, "solution": 4},
    {"nom": "Candidat B", "cout": 5100, "references": 1, "duree": 3, "solution": 1},
    {"nom": "Candidat C", "cout": 5000, "references": 3, "duree": 5, "solution": 4}
]

# Critères et poids
poids = {
    "cout": 0.2,
    "references": 0.5,
    "duree": 0.3,
    "solution": 0.2
}

# Préparer les données
data = np.array([[c["cout"], c["references"], c["duree"], c["solution"]] for c in candidats])

# Inverser les valeurs pour le coût et la durée pour que les plus petites valeurs soient meilleures
data[:, 0] = -data[:, 0]  # Inverser les coûts
data[:, 2] = -data[:, 2]  # Inverser les durées

# Normaliser les données entre 0 et 1
scaler = MinMaxScaler()
data_normalized = scaler.fit_transform(data)

# Calculer les scores pondérés
scores = np.dot(data_normalized, np.array([poids['cout'], poids['references'], poids['duree'], poids['solution']]))

# Ajouter les scores aux candidats
for i, candidat in enumerate(candidats):
    candidat["score"] = scores[i]

# Trouver le meilleur candidat
meilleur_candidat = max(candidats, key=lambda x: x["score"])

# Afficher le meilleur candidat
print("Le meilleur candidat est :", meilleur_candidat["nom"])
print("Détails :", meilleur_candidat)
