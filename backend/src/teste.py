import spacy
from transformers import pipeline

# Charger le modèle spaCy pour le français
nlp_spacy = spacy.load("fr_core_news_md")

# Charger un pipeline de reconnaissance d'entités nommées (NER) avec un modèle pré-entraîné
ner_pipeline = pipeline("ner", model="Jean-Baptiste/camembert-ner", tokenizer="Jean-Baptiste/camembert-ner")

def extraire_informations(description):
    doc = nlp_spacy(description)
    ner_results = ner_pipeline(description)

    solution = ""
    cout = ""
    duree = ""
    references = []

    for ent in ner_results:
        entity_text = ent['word']
        entity_label = ent['entity']

        if "SOLUTION" in entity_label:
            solution += " " + entity_text
        elif "COUT" in entity_label:
            cout += " " + entity_text
        elif "DUREE" in entity_label:
            duree += " " + entity_text
        elif "REFERENCE" in entity_label:
            references.append(entity_text)

    return {
        "solution_proposee": solution.strip(),
        "cout_de_realisation": cout.strip(),
        "duree_de_realisation": duree.strip(),
        "references_clients": references
    }

# Exemple de descriptions de soumissions
soumission_1 = """
Nous proposons une solution de construction clé en main pour le nouveau bâtiment administratif. Notre approche comprend la conception architecturale personnalisée, l'utilisation de matériaux de haute qualité et la mise en œuvre de technologies innovantes pour assurer l'efficacité énergétique et le confort des occupants.
Notre offre compétitive s'élève à 2,5 millions d'euros, comprenant tous les frais de conception, de construction, de main-d'œuvre et de matériaux.
Le projet sera complété en 18 mois.
Nous avons réalisé avec succès des projets similaires pour des clients prestigieux tels que l'entreprise ABC Corp et la municipalité de Villeville.
"""

soumission_2 = """
Nous proposons une approche de construction innovante en utilisant des techniques modulaires préfabriquées. Notre solution offre une construction rapide, flexible et durable, avec la possibilité d'adaptation future aux besoins changeants de l'entreprise. Nous mettons l'accent sur la durabilité environnementale et la réduction des coûts à long terme.
Notre offre compétitive s'élève à 2,2 millions d'euros.
Le projet sera achevé en 15 mois.
Notre entreprise a réalisé avec succès des projets similaires pour des clients renommés tels que l'entreprise XYZ Group et le gouvernement local de la région.
"""

# Extraire les informations des soumissions
informations_soumission_1 = extraire_informations(soumission_1)
informations_soumission_2 = extraire_informations(soumission_2)

print("Informations Soumission 1:")
print(informations_soumission_1)
print("\nInformations Soumission 2:")
print(informations_soumission_2)
