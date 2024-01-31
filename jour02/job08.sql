-- Active: 17065225689@@127.0.0.1@3306@zoo
CREATE DATABASE IF NOT EXISTS zoo;
USE zoo;

CREATE TABLE animal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    race VARCHAR(255),
    id_cage INT,
    date_naissance DATE,
    pays_origine VARCHAR(255)
);

CREATE TABLE cage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    superficie FLOAT, -- Modification ici
    capacite_max INT
);