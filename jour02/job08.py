import mysql.connector

class GestionnaireZoo:
    def __init__(self):
        self.connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoo"
        )
        self.curseur = self.connexion.cursor()

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        requete = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        valeurs = (nom, race, id_cage, date_naissance, pays_origine)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()
        print(f"Animal {nom} ajouté avec succès.")

    def supprimer_animal(self, id_animal):
        requete = "DELETE FROM animal WHERE id = %s"
        valeurs = (id_animal,)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()
        print(f"Animal avec l'ID {id_animal} supprimé avec succès.")

    def modifier_animal(self, id_animal, nom, race, id_cage, date_naissance, pays_origine):
        requete = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
        valeurs = (nom, race, id_cage, date_naissance, pays_origine, id_animal)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()
        print(f"Animal avec l'ID {id_animal} modifié avec succès.")

    def afficher_liste_animaux(self):
        requete = "SELECT * FROM animal"
        self.curseur.execute(requete)
        resultats = self.curseur.fetchall()
        print("\nListe des animaux présents dans le zoo :")
        for row in resultats:
            print(row)

    def afficher_animaux_cages(self):
        requete = "SELECT a.*, c.superficie, c.capacite_max FROM animal a JOIN cage c ON a.id_cage = c.id"
        self.curseur.execute(requete)
        resultats = self.curseur.fetchall()
        print("\nAnimaux dans les cages avec informations sur les cages :")
        for row in resultats:
            print(row)

    def calculer_superficie_totale(self):
        requete = "SELECT SUM(superficie) FROM cage"
        self.curseur.execute(requete)
        resultat = self.curseur.fetchone()
        superficie_totale = resultat[0] if resultat[0] is not None else 0
        print(f"\nLa superficie totale de toutes les cages est de {superficie_totale} m**2.")

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()

gestionnaire_zoo = GestionnaireZoo()
gestionnaire_zoo.ajouter_animal("chat", "Félin", 1, "2020-04-01", "Afrique")
gestionnaire_zoo.ajouter_animal("cheval", "Mammifère", 2, "2015-02-21", "Asie")
gestionnaire_zoo.afficher_liste_animaux()
gestionnaire_zoo.afficher_animaux_cages()
gestionnaire_zoo.calculer_superficie_totale()
gestionnaire_zoo.fermer_connexion()
