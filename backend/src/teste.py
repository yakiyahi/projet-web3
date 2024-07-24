import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import string

# Télécharger les ressources nécessaires
nltk.download('punkt')
nltk.download('stopwords')

# Offre contenant le titre, la description, la date de publication et la date de fin
offre = {
    "titre": "Développement d'une application web",
    "description": "Nous cherchons une solution innovante pour développer une application web qui optimise les processus de gestion.",
    "date_publication": "2023-01-01",
    "date_fin": "2023-01-15",
    "prix": 4800,
    "duree": 8,
    "references": 3
}

# Exemple de données des candidats
candidats = [
    {"nom": "Candidat A", "prix": 5000, "duree": 12, "solution": "Solution innovante et efficace.", "references": 2},
    {"nom": "Candidat B", "prix": 5100, "duree": 3, "solution": "Optimisation des processus et réduction des coûts.", "references": 1},
    {"nom": "Candidat C", "prix": 5000, "duree": 18, "solution": "Solution innovante et efficace pour optimiser les processus.", "references": 3}
]

# Critères et poids
poids = {
    "prix": 0.25,
    "duree": 0.25,
    "solution": 0.25,
    "references": 0.25
}

# Préparer les données
prix_offre = offre["prix"]
duree_offre = offre["duree"]
solution_offre = offre["description"]
references_offre = offre["references"]

# Normaliser les prix et les durées (inverser pour donner priorité aux valeurs plus basses)
data = np.array([[c["prix"], c["duree"], c["references"]] for c in candidats] + [[prix_offre, duree_offre, references_offre]])
data[:, 0] = -data[:, 0]
data[:, 1] = -data[:, 1]

scaler = MinMaxScaler()
data_normalized = scaler.fit_transform(data)

# Séparer les données normalisées des candidats et de l'offre
data_normalized_candidats = data_normalized[:-1]
data_normalized_offre = data_normalized[-1]

# Calculer la similarité textuelle entre la solution de l'offre et celles des candidats
vectorizer = TfidfVectorizer(stop_words=stopwords.words('french'))
solutions = [c["solution"] for c in candidats] + [solution_offre]
tfidf_matrix = vectorizer.fit_transform(solutions)
cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]

# Calculer les scores pour chaque candidat
scores = []
for i, candidat in enumerate(candidats):
    score_prix = data_normalized_candidats[i][0] * poids["prix"]
    score_duree = data_normalized_candidats[i][1] * poids["duree"]
    score_references = data_normalized_candidats[i][2] * poids["references"]
    score_solution = cosine_similarities[i] * poids["solution"]
    score_total = score_prix + score_duree + score_references + score_solution
    scores.append(score_total)
    candidat["score"] = score_total

# Trouver le meilleur candidat
meilleur_candidat = max(candidats, key=lambda x: x["score"])

# Afficher le meilleur candidat
print("Le meilleur candidat est :", meilleur_candidat["nom"])
print("Détails :", meilleur_candidat)