-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: localhost    Database: paperless
-- ------------------------------------------------------
-- Server version	8.0.22-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `joballotment`
--

DROP TABLE IF EXISTS `joballotment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `joballotment` (
  `job_id` int NOT NULL AUTO_INCREMENT,
  `alloted_by` int NOT NULL,
  `alloted_to` int NOT NULL,
  `allotment_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `submission_date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `title` varchar(150) NOT NULL,
  `task` varchar(255) DEFAULT NULL,
  `submission` varchar(255) DEFAULT NULL,
  `review` varchar(250) DEFAULT NULL,
  `reply` varchar(150) DEFAULT NULL,
  `approved_status` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`job_id`),
  KEY `alloted_by` (`alloted_by`),
  KEY `alloted_to` (`alloted_to`),
  CONSTRAINT `joballotment_ibfk_1` FOREIGN KEY (`alloted_by`) REFERENCES `users` (`uid`),
  CONSTRAINT `joballotment_ibfk_2` FOREIGN KEY (`alloted_to`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `joballotment`
--

LOCK TABLES `joballotment` WRITE;
/*!40000 ALTER TABLE `joballotment` DISABLE KEYS */;
INSERT INTO `joballotment` VALUES (1,2,1,'0000-00-00 00:00:00','2020-11-29 23:36:01','first task','static/joballotment/1606719810.079951-tcsWeek7.pdf','static/submission/1606720765.885802-Week -7 Problem Solving.pdf','my review','my reply',1),(2,4,3,'2020-11-29 23:06:14','2020-11-30 00:04:44','first task','static/joballotment/1606719974.772083-tcsWeek7.pdf',NULL,NULL,NULL,0),(3,2,1,'2020-11-29 23:07:01','2020-12-01 16:59:14','first task','static/joballotment/1606720021.547538-tcsWeek7.pdf',NULL,NULL,NULL,0);
/*!40000 ALTER TABLE `joballotment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manual`
--

DROP TABLE IF EXISTS `manual`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manual` (
  `man_id` int NOT NULL AUTO_INCREMENT,
  `uploaded_by` int NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `title` varchar(150) NOT NULL,
  `document` varchar(255) DEFAULT NULL,
  `department` varchar(150) NOT NULL,
  PRIMARY KEY (`man_id`),
  KEY `uploaded_by` (`uploaded_by`),
  CONSTRAINT `manual_ibfk_1` FOREIGN KEY (`uploaded_by`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manual`
--

LOCK TABLES `manual` WRITE;
/*!40000 ALTER TABLE `manual` DISABLE KEYS */;
INSERT INTO `manual` VALUES (1,2,'2020-11-29 19:59:57','testdoc','Week -7 Problem Solving.pdf','A'),(2,2,'2020-11-29 20:19:14','testdoc','static/manual/1606709954.243724-Week -7 Problem Solving.pdf','A');
/*!40000 ALTER TABLE `manual` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `uname` varchar(150) NOT NULL,
  `role` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `department` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `uc` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'anurag','employee','1234','A','test@test.com','2020-11-29 17:07:47'),(2,'heena','employer','1234','A','heena@gmail.com','2020-11-29 19:44:24'),(3,'jaya','employee','1234','B','jaya@gmail.com','2020-11-29 23:57:30'),(4,'tanvi','employer','1234','B','tanvi@gmail.com','2020-11-29 23:58:38');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-30 11:27:04
