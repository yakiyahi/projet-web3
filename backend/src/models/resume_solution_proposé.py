from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import spacy


def summarize_text(text, sentence_count=3):
    # Charger le modèle de langue français
    nlp = spacy.load("fr_core_news_sm")

    # Prétraiter le texte avec spaCy
    doc = nlp(text)

    # Convertir le texte en phrases
    sentences = [sent.string.strip() for sent in doc.sents]

    # Utiliser sumy pour générer le résumé
    parser = PlaintextParser.from_string(text, Tokenizer("french"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)

    # Convertir le résumé en texte
    summarized_text = " ".join([str(sentence) for sentence in summary])
    return summarized_text


# Exemple de texte en français
texte = """
La solution proposée implique plusieurs étapes pour traiter efficacement le problème. Tout d'abord, nous réaliserons une analyse approfondie du système actuel afin d'identifier les problèmes clés et leurs causes profondes. Cette analyse comprendra la collecte de données de diverses sources et la consultation des parties prenantes pour obtenir une compréhension globale des enjeux.

Ensuite, nous concevrons un plan détaillé qui énonce les actions spécifiques nécessaires pour traiter chaque problème. Ce plan inclura des échéances, les ressources requises et les responsabilités des différents membres de l'équipe. Nous établirons également des métriques pour mesurer le succès de la solution et garantir qu'elle est mise en œuvre efficacement.

Une fois le plan en place, nous commencerons la phase de mise en œuvre. Cette phase comprendra les modifications nécessaires au système, la formation du personnel sur les nouvelles procédures et la surveillance continue des progrès pour s'assurer que les changements produisent l'effet souhaité.

Enfin, nous réaliserons un examen de suivi pour évaluer l'impact global de la solution et apporter les ajustements nécessaires. Cet examen impliquera la collecte de retours des parties prenantes, l'analyse des données de performance et les modifications finales pour garantir que la solution est durable à long terme.
"""

# Générer et afficher le résumé
resume = summarize_text(texte, sentence_count=3)
print("Résumé de la solution proposée :")
print(resume)
