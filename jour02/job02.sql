-- Active: 1706522473235@@127.0.0.1@3306@laplateforme
USE laplateforme;

CREATE TABLE etage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    numero INT,
    superficie INT
);

-- Création de la table "salle"
CREATE TABLE salle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    id_etage INT,
    capacite INT
);