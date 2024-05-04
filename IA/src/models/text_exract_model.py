import spacy

#Charger le model de la lague francaise

nlp = spacy.load("fr_core_news_sm")

#Description de l'offre d'emploi

description_offre = """
    Nous recherchons un developpeur web experimenté pour rejoindre notre equipe dynamique.
    Le candidat idéal devriait avoir une solide experience dans le developpement front-end et back-end,
    ainsi qu'une connaissance approfondie des languages de programmation tels que HTML,CSS,Javascript, PHP et MySQL.
    Une experince préalable avec les framworks javascript comme Angular ou React serait un plus.
    Le candidat retenu travaillera en etroite collaboration avec notre equipe de conception pour developper des interfaces 
    utilisateur attrayantes et des fonctionnalités robustes pour nos application web.
    """
# Traitement du texte avec spaCy

doc = nlp(description_offre)

#Extraction des entities nommées
entites_nomees = [(ent.etxt, ent.label_) for ent in doc.ents]

#Extration des phrases clées
phrases_cles = [chunk.text for chunk in doc.noun_chunks]

#Afficher les resultats
print("Entitiés nomées: {} \n".format(entites_nomees))
print("Phrases clés : {} \n".format(phrases_cles))