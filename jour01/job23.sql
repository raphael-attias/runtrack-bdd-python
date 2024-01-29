-- Active: 1706522473235@@127.0.0.1@3306@laplateforme
USE laplateforme;

SELECT *
FROM etudiant
WHERE age = (SELECT MAX(age) FROM etudiant);
