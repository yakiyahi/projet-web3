import spacy
import re

# Charger le modèle de langue français de spaCy
nlp = spacy.load("fr_core_news_md")


# Fonction pour extraire les informations
def extraire_informations(description):
    doc = nlp(description)

    # Expressions régulières pour extraire les informations
    solution_pattern = re.compile(r"solution proposée.*?(?=coût|durée|références|$)", re.IGNORECASE | re.DOTALL)
    cout_pattern = re.compile(r"coût.*?(?=solution|durée|références|$)", re.IGNORECASE | re.DOTALL)
    duree_pattern = re.compile(r"durée.*?(?=solution|coût|références|$)", re.IGNORECASE | re.DOTALL)

    # Extraire les informations
    solution = solution_pattern.search(description)
    cout = cout_pattern.search(description)
    duree = duree_pattern.search(description)

    # Nettoyer les résultats
    solution = solution.group(0).strip() if solution else "Non spécifié"
    cout = cout.group(0).strip() if cout else "Non spécifié"
    duree = duree.group(0).strip() if duree else "Non spécifié"

    return {
        "solution_proposee": solution,
        "cout_de_realisation": cout,
        "duree_de_realisation": duree
    }


# Exemple de descriptions de soumissions
soumission_1 = """
Conernant la Solution proposée, Nous proposons une solution de construction clé en main pour le nouveau bâtiment administratif. Notre approche comprend la conception architecturale personnalisée, l'utilisation de matériaux de haute qualité et la mise en œuvre de technologies innovantes pour assurer l'efficacité énergétique et le confort des occupants.
Coût de réalisation : Notre offre compétitive s'élève à 2,5 millions d'euros, comprenant tous les frais de conception, de construction, de main-d'œuvre et de matériaux.
Durée de réalisation : Le projet sera complété en 18 mois.
Références clients : Nous avons réalisé avec succès des projets similaires pour des clients prestigieux tels que l'entreprise ABC Corp et la municipalité de Villeville.
"""

soumission_2 = """
Solution proposée : Nous proposons une approche de construction innovante en utilisant des techniques modulaires préfabriquées. Notre solution offre une construction rapide, flexible et durable, avec la possibilité d'adaptation future aux besoins changeants de l'entreprise. Nous mettons l'accent sur la durabilité environnementale et la réduction des coûts à long terme.
Coût de réalisation : Notre offre compétitive s'élève à 2,2 millions d'euros.
Durée de réalisation : Le projet sera achevé en 15 mois.
Références clients : Notre entreprise a réalisé avec succès des projets similaires pour des clients renommés tels que l'entreprise XYZ Group et le gouvernement local de la région.
"""

soumission_3 = """
 Nous proposons une approche de construction innovante en utilisant des techniques modulaires préfabriquées. Notre solution offre une construction rapide, flexible et durable, avec la possibilité d'adaptation future aux besoins changeants de l'entreprise. Nous mettons l'accent sur la durabilité environnementale et la réduction des coûts à long terme.
 Notre offre compétitive s'élève à 2,2 millions d'euros.
 Le projet sera achevé en 15 mois.
 Notre entreprise a réalisé avec succès des projets similaires pour des clients renommés tels que l'entreprise XYZ Group et le gouvernement local de la région.
"""
# Extraire les informations des soumissions
informations_soumission_1 = extraire_informations(soumission_1)
informations_soumission_2 = extraire_informations(soumission_2)
informations_soumission_3 = extraire_informations(soumission_3)

print("Informations Soumission 1:")
print(informations_soumission_1)
print("\n Informations Soumission 2:")
print(informations_soumission_2)

print("\n Informations Soumission 3:")
print(informations_soumission_3)

