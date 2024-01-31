import mysql.connector

def initialiser_base_de_donnees():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R@ph@e?13*?",
        database="zoo"
    )
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS animal (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(255) NOT NULL,
            race VARCHAR(255) NOT NULL,
            id_cage INT,
            date_naissance DATE NOT NULL,
            pays_origine VARCHAR(255) NOT NULL,
            FOREIGN KEY (id_cage) REFERENCES cage(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cage (
            id INT AUTO_INCREMENT PRIMARY KEY,
            superficie FLOAT NOT NULL,
            capacite_max INT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    
def ajouter_cage(superficie, capacite_max):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R@ph@e?13*?",
        database="zoo"
    )
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO cage (superficie, capacite_max)
        VALUES (%s, %s)
    ''', (superficie, capacite_max))

    conn.commit()
    conn.close()
    
def ajouter_animal(nom, race, id_cage, date_naissance, pays_origine):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R@ph@e?13*?",
        database="zoo"
    )
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine)
        VALUES (%s, %s, %s, %s, %s)
    ''', (nom, race, id_cage, date_naissance, pays_origine))

    conn.commit()
    conn.close()

def afficher_animaux():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R@ph@e?13*?",
        database="zoo"
    )
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM animal
    ''')
    animaux = cursor.fetchall()

    for animal in animaux:
        print(animal)

    conn.close()


def afficher_animaux_par_cage():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R@ph@e?13*?",
        database="zoo"
    )
    cursor = conn.cursor()

    cursor.execute('''
        SELECT c.id, c.superficie, c.capacite_max, a.*
        FROM cage c
        LEFT JOIN animal a ON c.id = a.id_cage
    ''')
    animaux_par_cage = cursor.fetchall()

    for animal_cage in animaux_par_cage:
        print(animal_cage)

    conn.close()


def calculer_superficie_totale():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R@ph@e?13*?",
        database="zoo"
    )
    cursor = conn.cursor()

    cursor.execute('''
        SELECT SUM(superficie) FROM cage
    ''')
    superficie_totale = cursor.fetchone()[0]

    print("Superficie totale des cages :", superficie_totale)

    conn.close()

initialiser_base_de_donnees()

ajouter_cage(10.5, 5)
ajouter_cage(15.0, 8)

ajouter_animal("chat", "Félin", 1, "2020-01-15", "Afrique")
ajouter_animal("Girafe", "Mammifère", 2, "2019-05-20", "Afrique")
ajouter_animal("Panda", "Ours", 2, "2021-03-10", "Chine")

afficher_animaux()
afficher_animaux_par_cage()
calculer_superficie_totale()
