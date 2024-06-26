import spacy
import re

nlp = spacy.load("fr_core_news_sm")
def recupere_prix(texte):
    pattern = r'\b(\d{1,3}(?:\s?\d{3})*(?:[\.,]\d{1,2})?)\s*(?:MGA|ariary|MGA|Ar)\b'
    matches = re.findall(pattern, texte)
    if matches:
        prix = matches[0]
        return prix
    else:
        prix = 0
        return prix

#Fonction qui utilise le NLP pour reconnaitre les societe present dans des references clients
def recupere_societe(text):
    doc = nlp(text)

    societe_identifie = [ent.text for ent in doc.ents if ent.label_ == "ORG"]

    #Afficher le resultats
    if societe_identifie:
        return societe_identifie
    else:
        societe_identifie = "";
        return societe_identifie

def recupere_duree(texte):
    pattern = r'\b(\d+\s*(?:ans?|mois|jours?|heures?|semaines?))\b'
    matches = re.findall(pattern, texte)
    if matches:
        duree = ', '.join(matches)
        return duree
    else:
        duree = 0
        return duree

