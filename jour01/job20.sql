-- Active: 1706522473235@@127.0.0.1@3306@laplateforme
USE laplateforme;

SELECT COUNT(*) AS nombre_etudiants_mineurs
FROM etudiant
WHERE age < 18;
