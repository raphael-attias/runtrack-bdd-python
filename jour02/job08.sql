/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
DROP TABLE IF EXISTS animal;
CREATE TABLE `animal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `race` varchar(255) NOT NULL,
  `id_cage` int DEFAULT NULL,
  `date_naissance` date NOT NULL,
  `pays_origine` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_cage` (`id_cage`),
  CONSTRAINT `animal_ibfk_1` FOREIGN KEY (`id_cage`) REFERENCES `cage` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS cage;
CREATE TABLE `cage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `superficie` float NOT NULL,
  `capacite_max` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO animal(id,nom,race,id_cage,date_naissance,pays_origine) VALUES('2','\'chat\'','\'Félin\'','1','\'2020-01-15\'','\'Afrique\''),('3','\'Girafe\'','\'Mammifère\'','2','\'2019-05-20\'','\'Afrique\''),('4','\'Panda\'','\'Ours\'','2','\'2021-03-10\'','\'Chine\'');
INSERT INTO cage(id,superficie,capacite_max) VALUES('1','10.5','5'),('2','15','8');