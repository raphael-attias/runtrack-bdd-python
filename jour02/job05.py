import mysql.connector

def calcul_superficie():
        connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="R@ph@e?13*?",
            database="LaPlateforme"
        )     
        curseur = connexion.cursor()  
        curseur.execute("SELECT SUM(superficie) FROM etage")
        resultat = curseur.fetchone()
        superficie_totale = resultat[0]  
        print(f"La superficie de La Plateforme est de {superficie_totale} m**2")

calcul_superficie()