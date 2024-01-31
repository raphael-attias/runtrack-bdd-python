import mysql.connector

def recuperer_salles():
    try:        
        connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="R@ph@e?13*?",
            database="LaPlateforme"
        ) 
        curseur = connexion.cursor()
        curseur.execute("SELECT nom, capacite FROM salle")
        salles = curseur.fetchall()   
        print(salles)

    except mysql.connector.Error as e:
        print(f"Une erreur est survenue: {e}")
        
recuperer_salles()