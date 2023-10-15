/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.22-MariaDB : Database - ev_station
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ev_station` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `ev_station`;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `center_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `end_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`center_id`,`user_id`,`date`,`time`,`status`,`amount`,`end_time`) values (2,2,2,'15/9/2023','1:06','pending','288.0','1:11'),(3,2,2,'15/9/2023','2:05','pending','288.0','2:0999999999999996'),(4,2,2,'15/9/2023','2:55','pending','288.0','2:6'),(5,2,2,'15/9/2023','2:45','pending','288.0','2:5'),(6,2,2,'15/9/2023','2:45','pending','288.0','2:5'),(7,2,2,'15/9/2023','2:25','pending','288.0','2:3'),(8,2,2,'15/9/2023','2:30','pending','288.0','2:3499999999999996'),(9,2,2,'15/9/2023','2:10','pending','288.0','2:15'),(10,2,2,'15/9/2023','4:00','pending','288.0','4:05'),(11,2,2,'15/9/2023','4:10','pending','324.0','4:159999999999999');

/*Table structure for table `charging_center` */

DROP TABLE IF EXISTS `charging_center`;

CREATE TABLE `charging_center` (
  `center_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `center_name` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `priceperunit` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`center_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `charging_center` */

insert  into `charging_center`(`center_id`,`login_id`,`center_name`,`phone`,`email`,`latitude`,`longitude`,`place`,`priceperunit`) values (1,12,'dfg','sdf','sdfg','9.977980240986346','76.28305435180664','sdfg','5'),(2,13,'meb','9874563120','meb@mail','9.988772182451712','76.28013617970528','meb','6');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`sender_id`,`complaint`,`reply`,`date`) values (1,3,'hdfgvhdf','aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','12/12/2022'),(2,2,'vbfbf','pending','12/12/2022'),(3,NULL,NULL,NULL,''),(4,4,'jcjgcgjckgcjg','pending','2023-04-11'),(5,4,'hdgghb','pending','2023-04-21'),(6,4,'qqqqqqqqq','pending','2023-04-21');

/*Table structure for table `faculty` */

DROP TABLE IF EXISTS `faculty`;

CREATE TABLE `faculty` (
  `faculty_id` int(11) NOT NULL AUTO_INCREMENT,
  `center_id` int(11) DEFAULT NULL,
  `fac_name` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`faculty_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Data for the table `faculty` */

insert  into `faculty`(`faculty_id`,`center_id`,`fac_name`,`description`) values (1,1,'faculty','jsdhnjdsfbdfhdjfkejfnkdsnfkejiuehfsfb'),(2,1,'hfjdbjsfsjhj','hjdvjhdvbjd'),(6,3,'devzzzzzz','djvjdjvdjfsjsdjvnsf'),(7,3,'mebin','kdsnsdnfedhcjd');

/*Table structure for table `faq` */

DROP TABLE IF EXISTS `faq`;

CREATE TABLE `faq` (
  `faq_id` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(100) DEFAULT NULL,
  `answer` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`faq_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `faq` */

insert  into `faq`(`faq_id`,`question`,`answer`) values (1,'questiooooooooon?','wieefnnfekcfnennnnsd'),(2,'ffifihifhihiddskj','hdhskjhjefiv');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `center_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`feedback`,`date`,`center_id`) values (1,2,'good','2023-04-12',1),(2,2,'hdhjsmsnd','2023-04-12',1),(3,2,'bdjsjsnsn','2023-04-21',2),(4,2,'hsjjsjdjdjjd','2023-04-21',2);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'bunk','bunk','bunk'),(4,'user','user','user'),(8,'bunk1','bunk1','bunk'),(9,'lay','lay','bunk'),(10,'bunk10','bunk10','bunk'),(11,'bunk15','bunk15','bunk'),(12,'abc','abc','bunk'),(13,'meb','meb','bunk');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `pay_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `pay_date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

/*Data for the table `payment` */

insert  into `payment`(`pay_id`,`booking_id`,`amount`,`pay_date`,`status`) values (1,1,'1500','2023-04-12','paid'),(2,2,'500','2023-04-13','paid'),(3,2,'500','2023-04-13','paid'),(4,3,'2000','2023-04-13','paid'),(5,3,'2000','2023-04-13','paid'),(6,4,'400','2023-04-13','paid'),(7,4,'400','2023-04-13','paid'),(8,4,'400','2023-04-13','paid'),(9,6,'3000','2023-04-13','paid'),(10,5,'1000','2023-04-21','paid');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`firstname`,`lastname`,`place`,`post`,`pin`,`gender`,`phone`,`email`) values (1,3,'useeeeeeeer','userd','fhgvdsjbnj','dfgd','dfgdf','male','1234567890','dfbdhs@hdgs'),(2,4,'user','userrrr','thrissur','thrissur','680683','male','9876543219','dbjsbhjbds');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
