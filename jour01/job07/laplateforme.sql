/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
DROP TABLE IF EXISTS etage;
CREATE TABLE `etage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `numero` int DEFAULT NULL,
  `superficie` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS etudiant;
CREATE TABLE `etudiant` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(25) NOT NULL,
  `age` int NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS salle;
CREATE TABLE `salle` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `id_etage` int DEFAULT NULL,
  `capacite` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_etage` (`id_etage`),
  CONSTRAINT `salle_ibfk_1` FOREIGN KEY (`id_etage`) REFERENCES `etage` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


INSERT INTO etudiant(id,nom,prenom,age,email) VALUES('1','\'Spaghetti\'','\'Betty\'','20','\'betty.Spaghetti@laplateforme.io\''),('2','\'Steak\'','\'Chuck\'','45','\'chuck.steak@laplateforme.io\''),('4','\'Barnes\'','\'Binkie\'','16','\'binkie.barnes@laplateforme.io\''),('5','\'Dupuis\'','\'Gertrude\'','20','\'gertrude.dupuis@laplateforme.io\'');