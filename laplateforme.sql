-- Active: 1706522473235@@127.0.0.1@3306@laplateforme
/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
DROP TABLE IF EXISTS etudiant;
CREATE TABLE `etudiant` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(25) NOT NULL,
  `age` int NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO etudiant(id,nom,prenom,age,email) VALUES('1','\'Spaghetti\'','\'Betty\'','23','\'betty.Spaghetti@laplateforme.io\''),('2','\'Steak\'','\'Chuck\'','45','\'chuck.steak@laplateforme.io\''),('3','\'Doe\'','\'John\'','18','\'john.doe@laplateforme.io\''),('4','\'Barnes\'','\'Binkie\'','16','\'binkie.barnes@laplateforme.io\''),('5','\'Dupuis\'','\'Gertrude\'','20','\'gertrude.dupuis@laplateforme.io\'');
USE laplateforme;

SELECT * FROM etudiant
WHERE age < 18;
