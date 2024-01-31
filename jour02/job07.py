import mysql.connector

def connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="R@ph@e?13*?",
        database="LaPlateforme"
    )

def create_database():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS LaPlateforme")
    conn.close()

def create_employe_table():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employe (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(255),
            prenom VARCHAR(255),
            salaire DECIMAL(10, 2),
            id_service INT
        )
    """)
    conn.close()

def create_service_table():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS service (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(255)
        )
    """)
    conn.close()

def insert_employes():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employe (nom, prenom, salaire, id_service)
        VALUES
        ('Doe', 'John', 3500.50, 1),
        ('Smith', 'Alice', 2800.75, 2),
        ('Johnson', 'Bob', 4200.00, 1)
    """)
    conn.commit()
    conn.close()

def insert_services():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO service (nom)
        VALUES
        ('Finance'),
        ('IT')
    """)
    conn.commit()
    conn.close()

def employeriche(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employe WHERE salaire > 3000")
    for employe in cursor.fetchall():
        print(employe)

def employeservice(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.nom, e.prenom, s.nom AS service_name
        FROM employe e
        INNER JOIN service s ON e.id_service = s.id
    """)
    for employe in cursor.fetchall():
        print(employe)

create_database()
create_employe_table()
create_service_table()

insert_employes()
insert_services()

conn = connection()

print("Employé avec un salaire plus de 3000:")
employeriche(conn)

print("\nEmployés et leur service:")
employeservice(conn)

conn.close()
