import psycopg2

# Se connecter à la base de données
conn = psycopg2.connect(
    dbname="evaluation_projet",
    user="yaki",
    password="yakiyahi",
    host="localhost"
)
# Créer un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()
def get_enterprise_info(entreprise):

    # Exécuter une requête SQL pour récupérer les évaluations
    cursor.execute("SELECT qualite, delais, communication, satisfaction FROM evaluations WHERE entreprise = %s", (entreprise,))
    row = cursor.fetchall()
    #cursor.close()
    #conn.close()
    return row
# Fermer le curseur et la connexion


#print(get_enterprise_info('ABC Construction'))