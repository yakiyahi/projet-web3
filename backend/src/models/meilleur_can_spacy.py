import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import spacy

# Charger le modèle de langue français
nlp = spacy.load("fr_core_news_sm")

# Exemple de données
candidats = [
    {"nom": "Candidat A", "coût": 45000, "références": 5, "durée": 10, "solution": "La solution proposée est innovante et efficace."},
    {"nom": "Candidat B", "coût": 45000, "références": 7, "durée": 10, "solution": "Notre solution optimise les processus et réduit les coûts."},
    {"nom": "Candidat C", "coût": 45000, "références": 9, "durée": 11, "solution": "Une solution complète et intégrée pour une meilleure performance."},
]

# Critères et poids
poids = {
    "coût": 0.2,
    "références": 0.4,
    "durée": 0.2,
    "solution": 0.2
}

# Préparer les données pour la normalisation
data = np.array([[c["coût"], c["références"], c["durée"]] for c in candidats])

# Inverser les valeurs pour le coût et la durée pour que les plus petites valeurs soient meilleures
data[:, 0] = -data[:, 0]
data[:, 2] = -data[:, 2]

# Normaliser les données entre 0 et 1
scaler = MinMaxScaler()
data_normalized = scaler.fit_transform(data)

# Extraire les solutions proposées
solutions = [c["solution"] for c in candidats]

# Vectoriser les solutions avec TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(solutions)

# Réduire la dimensionnalité avec SVD (LSA)
svd = TruncatedSVD(n_components=1)
lsa_matrix = svd.fit_transform(tfidf_matrix)

# Normaliser les scores des solutions
lsa_normalized = MinMaxScaler().fit_transform(lsa_matrix)

# Combiner les données normalisées et les scores des solutions
combined_data = np.hstack((data_normalized, lsa_normalized))

# Calculer les scores pondérés
weights = np.array([poids["coût"], poids["références"], poids["durée"], poids["solution"]])
scores = np.dot(combined_data, weights)

# Ajouter les scores aux candidats
for i, candidat in enumerate(candidats):
    candidat["score"] = scores[i]

# Trouver le meilleur candidat
meilleur_candidat = max(candidats, key=lambda x: x["score"])

# Afficher le meilleur candidat
print("Le meilleur candidat est :", meilleur_candidat["nom"])
print("Détails :", meilleur_candidat)
