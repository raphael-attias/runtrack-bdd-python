import mysql.connector

# Remplacez ces informations par les détails de votre base de données
host = "localhost"
user = "root"
password = ""
database = "R@ph@e?13*"

# Connexion à la base de données
conn = mysql.connector.connect(host = host, user = user, password = password, database = database)
cursor = conn.cursor()

query = "SELECT * FROM etudiant"
cursor.execute(query)

students = cursor.fetchall()

for student in students:
    print(student)

cursor.close()
conn.close()