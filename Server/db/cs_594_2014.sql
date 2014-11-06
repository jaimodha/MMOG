-- phpMyAdmin SQL Dump
-- version 3.5.8.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 06, 2014 at 09:27 AM
-- Server version: 5.6.14
-- PHP Version: 5.3.27

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `cs_594_2014`
--

-- --------------------------------------------------------

--
-- Table structure for table `characters`
--

CREATE TABLE IF NOT EXISTS `characters` (
  `char_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `char_name` varchar(255) DEFAULT NULL,
  `char_type` varchar(255) DEFAULT NULL,
  `char_x_pos` float DEFAULT NULL,
  `char_y_pos` float DEFAULT NULL,
  `char_z_pos` float DEFAULT NULL,
  `char_h_pos` float DEFAULT NULL,
  `char_p_pos` float DEFAULT NULL,
  `char_r_pos` float DEFAULT NULL,
  `is_moving` tinyint(1) DEFAULT NULL,
  `attack_id` int(11) DEFAULT NULL,
  `health_change` int(11) DEFAULT NULL,
  `c_level` int(11) DEFAULT NULL,
  `u_id` int(11) NOT NULL,
  PRIMARY KEY (`char_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `controlpoints`
--

CREATE TABLE IF NOT EXISTS `controlpoints` (
  `cp_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `cp_state` int(11) DEFAULT NULL,
  `cp_location` int(11) DEFAULT NULL,
  PRIMARY KEY (`cp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `games`
--

CREATE TABLE IF NOT EXISTS `games` (
  `game_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `t_id` int(11) NOT NULL,
  `cp_id` int(11) NOT NULL,
  PRIMARY KEY (`game_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE IF NOT EXISTS `messages` (
  `msg_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `message` varchar(255) DEFAULT NULL,
  `u_id` int(11) NOT NULL,
  PRIMARY KEY (`msg_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `npc`
--

CREATE TABLE IF NOT EXISTS `npc` (
  `npc_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `c_id` int(11) NOT NULL,
  `npc_name` varchar(255) DEFAULT NULL,
  `npc_type` varchar(255) DEFAULT NULL,
  `char_x_pos` float DEFAULT NULL,
  `char_y_pos` float DEFAULT NULL,
  `char_z_pos` float DEFAULT NULL,
  `char_h_pos` float DEFAULT NULL,
  `char_p_pos` float DEFAULT NULL,
  `char_r_pos` float DEFAULT NULL,
  `isGolemPiece` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`npc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `skills`
--

CREATE TABLE IF NOT EXISTS `skills` (
  `s_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `skill_name` varchar(255) DEFAULT NULL,
  `skill_type` varchar(255) DEFAULT NULL,
  `speed` int(11) DEFAULT NULL,
  `s_range` int(11) DEFAULT NULL,
  `s_cooldown` int(11) DEFAULT NULL,
  `s_casttime` int(11) DEFAULT NULL,
  `c_id` int(11) NOT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `teams`
--

CREATE TABLE IF NOT EXISTS `teams` (
  `team_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `team_name` varchar(40) NOT NULL,
  PRIMARY KEY (`team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `teams_controlpoints`
--

CREATE TABLE IF NOT EXISTS `teams_controlpoints` (
  `t_id` int(11) NOT NULL,
  `cp_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(40) NOT NULL,
  `email` varchar(80) NOT NULL,
  `t_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
