/*
 Navicat Premium Data Transfer

 Source Server         : full-stack
 Source Server Type    : MySQL
 Source Server Version : 50725
 Source Host           : localhost
 Source Database       : albumdb

 Target Server Type    : MySQL
 Target Server Version : 50725
 File Encoding         : utf-8

 Date: 03/13/2019 10:15:39 AM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `myweb_pic`
-- ----------------------------
DROP TABLE IF EXISTS `myweb_pic`;
CREATE TABLE `myweb_pic` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `picname` varchar(32) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `myweb_pic`
-- ----------------------------
BEGIN;
INSERT INTO `myweb_pic` VALUES ('1', 't', '1529675674.372393.jpg', '2018-06-22 21:54:34'), ('2', 'ss', '1529676288.7063906.jpg', '2018-06-22 22:04:48'), ('3', 'df', '1529668273.1352413.jpg', '2018-07-25 19:20:17'), ('4', 'dsf', '1542203820.9065607.jpg', '2018-09-06 21:55:03'), ('5', 'uy', '1552397288.6633084.jpg', '2019-03-12 21:28:08'), ('6', 'jh', '1552398049.7624578.jpg', '2019-03-12 21:35:38');
COMMIT;

-- ----------------------------
--  Table structure for `stu`
-- ----------------------------
DROP TABLE IF EXISTS `stu`;
CREATE TABLE `stu` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(16) NOT NULL,
  `age` tinyint(3) unsigned NOT NULL DEFAULT '20',
  `sex` enum('w','m') NOT NULL DEFAULT 'm',
  `classid` char(8) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `NewIndex1` (`age`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `stu`
-- ----------------------------
BEGIN;
INSERT INTO `stu` VALUES ('1', 'zhangsan', '22', 'm', 'python03'), ('2', 'lisi', '25', 'w', 'python04'), ('3', 'wangwu', '22', 'm', 'python03'), ('4', 'zhaoliu', '19', 'w', 'python04'), ('5', 'qq01', '20', 'm', 'python03'), ('6', 'qqmn', '21', 'w', 'python04'), ('7', 'uu02', '20', 'm', 'python05'), ('8', 'uu01', '21', 'w', 'python04'), ('9', 'test', '50', 'm', 'python05');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
