-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: anna
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `announcements`
--

DROP TABLE IF EXISTS `announcements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `announcements` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `body` text NOT NULL,
  `picture` varchar(500) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `displayed` tinyint(1) DEFAULT '0',
  `link` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `channel` (`link`),
  CONSTRAINT `announcements_ibfk_1` FOREIGN KEY (`link`) REFERENCES `channels` (`link`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `announcements`
--

LOCK TABLES `announcements` WRITE;
/*!40000 ALTER TABLE `announcements` DISABLE KEYS */;
INSERT INTO `announcements` VALUES (35,'Weekly Meetup Reminder','Don\'t forget our community meetup this Friday at 6 PM in the main hall!','https://picsum.photos/seed/1/600/400','https://example.com/meetup','2025-04-01 12:00:00',0,'anna-general'),(36,'New Feature: Finance Dashboard','We\'ve launched a redesigned dashboard with live market charts and alerts.','https://picsum.photos/seed/2/600/400','https://finance.example.com/dashboard','2025-04-02 13:15:00',0,'anna-finance'),(37,'Live Sports Event Tonight','Tune in at 8 PM for the live coverage of the Tigers vs. Hawks game.','https://picsum.photos/seed/3/600/400','https://sports.example.com/live/tigers-hawks','2025-04-03 22:00:00',0,'anna-sports'),(38,'General Maintenance Notice','Server maintenance scheduled April 6th from 1–3 AM UTC. Expect brief downtime.','https://picsum.photos/seed/4/600/400','https://example.com/maintenance','2025-04-04 11:30:00',0,'anna-general'),(39,'Quarterly Earnings Released','Q1 earnings beat expectations with a 12% increase in revenue year‑over‑year.','https://picsum.photos/seed/5/600/400','https://finance.example.com/q1-earnings','2025-04-05 20:45:00',0,'anna-finance'),(40,'Local Team Wins Championship','Congratulations to the Spartans on winning the 2025 city league championship!','https://picsum.photos/seed/6/600/400','https://sports.example.com/championship','2025-04-07 00:00:00',0,'anna-sports'),(41,'Community Guidelines Update','We\'ve updated our community guidelines to improve clarity on posting etiquette.','https://picsum.photos/seed/7/600/400','https://example.com/guidelines','2025-04-07 18:20:00',0,'anna-general'),(42,'Market Analysis: Crypto Trends','Our analysts predict Bitcoin may test $70k by summer—read the full report.','https://picsum.photos/seed/8/600/400','https://finance.example.com/crypto-trends','2025-04-08 15:10:00',0,'anna-finance'),(43,'Upcoming Marathon Registration','Registration for the annual city marathon opens next Monday—secure your spot!','https://picsum.photos/seed/9/600/400','https://sports.example.com/marathon','2025-04-09 10:50:00',0,'anna-sports'),(44,'Holiday Schedule','Reminder: Office closed on April 15th and 16th for the spring holiday.','https://picsum.photos/seed/10/600/400','https://example.com/holiday-schedule','2025-04-10 16:00:00',0,'anna-general'),(47,'New crypto announced','Tremendo','https://variety.com/wp-content/uploads/2021/12/Bitcoin-Cryptocurrency-Placeholder.jpg?w=1000&h=563&crop=1','','2025-04-22 23:57:54',0,'anna-general'),(48,'Prueb','asd','','','2025-04-23 00:16:35',0,'anna-finance'),(49,'test for the prints','testi213','','','2025-04-23 00:49:10',0,'anna-general'),(50,'another simple test','testing\r\n','','','2025-04-23 00:51:40',0,'anna-general'),(51,'Testing Iteration through channels','Lorem','https://pbs.twimg.com/media/Gpjwl7fWMAA8ONR?format=jpg&name=medium','https://www.ilovepdf.com/','2025-04-28 15:26:18',0,'anna-general');
/*!40000 ALTER TABLE `announcements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `channels`
--

DROP TABLE IF EXISTS `channels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `channels` (
  `id` int NOT NULL AUTO_INCREMENT,
  `channel_name` varchar(255) NOT NULL,
  `owner` int NOT NULL,
  `link` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `link_unique` (`link`) USING BTREE,
  KEY `owner` (`owner`),
  CONSTRAINT `channels_ibfk_1` FOREIGN KEY (`owner`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channels`
--

LOCK TABLES `channels` WRITE;
/*!40000 ALTER TABLE `channels` DISABLE KEYS */;
INSERT INTO `channels` VALUES (1,'General Bot News',1,'anna-general'),(2,'Sports News',1,'anna-sports'),(3,'Finance News',1,'anna-finance');
/*!40000 ALTER TABLE `channels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscriptions`
--

DROP TABLE IF EXISTS `subscriptions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subscriptions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `channel_id` bigint NOT NULL,
  `link` varchar(100) DEFAULT NULL,
  `webhook_url` varchar(2048) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `channel_link` (`channel_id`,`link`) USING BTREE,
  KEY `link` (`link`),
  CONSTRAINT `subscriptions_ibfk_1` FOREIGN KEY (`link`) REFERENCES `channels` (`link`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscriptions`
--

LOCK TABLES `subscriptions` WRITE;
/*!40000 ALTER TABLE `subscriptions` DISABLE KEYS */;
INSERT INTO `subscriptions` VALUES (1,1355583571716472993,'anna-general','https://discord.com/api/webhooks/1358528304268709918/ZMWCZrQRB5J2PGAnP_zOINmZEacpuf9W6RXMFpZUpADfeLFdExVkgB_2QPi-WBHIwChu'),(2,1326960634423672923,'anna-sports',''),(3,1360633500398649475,'anna-general','https://discord.com/api/webhooks/1360752687490011158/wfvcD119a_dMLptVo-eZDfIdLo36oDWb62P6GfTL9o3K_HlzcofeUtOW2GmM3i2TR3OU'),(7,1326960634423672923,'anna-general','https://discord.com/api/webhooks/1360752838115852339/Xcq8zKXPMBjk9RrzBUUbZlYkQZYQzgNwI5lu2049Jn3VGLmqgTwhFXflpEXFFJnh6TUP'),(17,1360633500398649475,'anna-finance','https://discord.com/api/webhooks/1360752687490011158/wfvcD119a_dMLptVo-eZDfIdLo36oDWb62P6GfTL9o3K_HlzcofeUtOW2GmM3i2TR3OU'),(19,1360633519537127699,'anna-sports','https://discord.com/api/webhooks/1360749498195906706/A4AYatVGRQ4bk6daSxXNhtfMgzyZpD_t8XmsPExSZg-GJN0sqHGbzU_c6Uad3DbtO5Gk'),(20,1364388717908856964,'anna-general','https://discord.com/api/webhooks/1364388770589446156/BSKHH3xLzmklJkMz0j11xy3a4sK9hsWqNSq3nj9e5ieA31dEEdL4RqFu3JE1MaNyQkM6'),(21,1364388856190992414,'anna-finance','https://discord.com/api/webhooks/1364388888767889449/2z_uH2gedwuk1BLyuFk2GVvTXtI9QlaA6Ahx1FpPLmx2w3dyycTD-PhWVECU7w3fzLO1'),(22,1364388952794202122,'anna-general','https://discord.com/api/webhooks/1364388984482037850/XwjIwEO52zPH9yA-vBfVxGjF_QRKk0_yyzoSwmAOHBVhg3YFnk0Cp8jQmKWJurOPF6ug'),(23,1364388952794202122,'anna-sports','https://discord.com/api/webhooks/1364388984482037850/XwjIwEO52zPH9yA-vBfVxGjF_QRKk0_yyzoSwmAOHBVhg3YFnk0Cp8jQmKWJurOPF6ug'),(24,1364388952794202122,'anna-finance','https://discord.com/api/webhooks/1364388984482037850/XwjIwEO52zPH9yA-vBfVxGjF_QRKk0_yyzoSwmAOHBVhg3YFnk0Cp8jQmKWJurOPF6ug');
/*!40000 ALTER TABLE `subscriptions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_user` (`username`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'anna','$2b$12$GfTRuppIC6LTj7aq/QnjTedXg8iOGNqk7twwy7mEwuaw/JwCmnfLK'),(2,'fabio','$2b$12$A0O5UpN96sv.ZbbGPaSFbuE7dZi93KhCnFKEYV.Uj/02KtDHT039O');
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

-- Dump completed on 2025-04-28 12:03:34
