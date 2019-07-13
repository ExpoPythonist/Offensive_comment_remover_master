-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 06, 2019 at 03:30 PM
-- Server version: 10.3.14-MariaDB-1:10.3.14+maria~bionic-log
-- PHP Version: 7.2.17-0ubuntu0.19.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `elio_off_com_rem`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_details`
--

CREATE TABLE `app_details` (
  `id` int(11) NOT NULL,
  `keyname` varchar(500) NOT NULL,
  `value` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_details`
--

INSERT INTO `app_details` (`id`, `keyname`, `value`) VALUES
(1, 'client_id', '602026126981299'),
(2, 'client_secret', '6123f6442177e6b90d056eab5bf88fe9');

-- --------------------------------------------------------

--
-- Table structure for table `fbuser`
--

CREATE TABLE `fbuser` (
  `id` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `access_token` longtext NOT NULL,
  `image` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fbuser`
--

INSERT INTO `fbuser` (`id`, `uid`, `access_token`, `image`) VALUES
(1, 1, 'access_token', 'https://platform-lookaside.fbsbx.com/platform/profilepic/?asid=2187509174663547&height=50&width=50&ext=1559714637&hash=AeRW6y2im2AeYK9v');

-- --------------------------------------------------------

--
-- Table structure for table `page`
--

CREATE TABLE `page` (
  `id` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `page_id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `image` text NOT NULL,
  `access_token` longtext NOT NULL,
  `sentiment_analysis` tinyint(1) NOT NULL DEFAULT 1,
  `ad_only` tinyint(1) NOT NULL DEFAULT 0,
  `selected` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(500) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` longtext NOT NULL,
  `chk_facebook` tinyint(1) NOT NULL DEFAULT 0,
  `chk_pages` tinyint(1) NOT NULL DEFAULT 0,
  `chk_creditcard` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `password`, `chk_facebook`, `chk_pages`, `chk_creditcard`) VALUES
(1, 'E P SOORAJ', 'epsooraj4@gmail.com', 'b\'S8Eo/HfXXxEQ0yTBJruUZyZ7g3y4PjNyzlDPbiDHEnM=\'', 0, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_details`
--
ALTER TABLE `app_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `fbuser`
--
ALTER TABLE `fbuser`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `page`
--
ALTER TABLE `page`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `page_id` (`page_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app_details`
--
ALTER TABLE `app_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `fbuser`
--
ALTER TABLE `fbuser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `page`
--
ALTER TABLE `page`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
