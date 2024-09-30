-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 30, 2024 at 04:16 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventory_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`id`, `username`, `password`, `name`) VALUES
(1, 'manager', 'manager123', 'manager kurt'),
(2, 'keziah', 'keziah123', ''),
(3, 'nikkie', 'nikkie123', ''),
(4, 'grio', 'grio123', ''),
(5, 'vann', 'vann1234', ''),
(6, 'lana', 'lana123', ''),
(7, 'john', 'john123', '');

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `id` int(11) NOT NULL,
  `activity` varchar(255) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `dateTime` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `history`
--

INSERT INTO `history` (`id`, `activity`, `product_name`, `quantity`, `dateTime`) VALUES
(1, 'Add Product', 'Sample Product 1', 123, '2024-09-30 21:48:08'),
(2, 'Add Product', 'Arwin', 20, '2024-09-30 21:55:58'),
(3, 'Updated Product', 'Mt dew Colo', 40, '2024-09-30 22:00:32'),
(4, 'Deleted Product', 'Mt dew Colo', 40, '2024-09-30 22:04:55');

-- --------------------------------------------------------

--
-- Table structure for table `inv`
--

CREATE TABLE `inv` (
  `product_ID` int(15) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `Qty` int(15) NOT NULL,
  `price` double(10,2) NOT NULL,
  `category` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inv`
--

INSERT INTO `inv` (`product_ID`, `product_name`, `Qty`, `price`, `category`) VALUES
(4, 'Coffee', 30, 20.00, NULL),
(5, 'Piattos', 70, 20.00, NULL),
(7, 'Snowbear', 40, 2.50, NULL),
(8, 'Bottled Water', 100, 23.50, NULL),
(9, 'bobot', 20, 1.00, NULL),
(16, 'biscuit', 20, 8.00, NULL),
(20, 'butter', 50, 50.50, 'Dairy Products'),
(21, 'ketchup', 70, 25.00, 'Condiments and Sauces'),
(22, 'zonrox', 50, 25.00, 'Household Items'),
(23, 'deodorant', 70, 60.00, 'Personal Care Products'),
(24, 'fita', 90, 7.00, 'Snacks'),
(26, 'oreo', 80, 12.00, 'Snacks'),
(28, 'vinegar', 30, 15.50, 'Condiments and Sauces'),
(29, 'milk', 50, 15.50, 'Dairy Products'),
(30, 'dishwashing liquid', 50, 45.00, 'Household Items'),
(42, 'skincare', 50, 10.50, 'Personal Care Products'),
(48, 'mountain dew', 50, 10.50, 'Drinks'),
(50, 'Sample Product', 270, 27.00, 'Dairy Products'),
(52, 'Sample Product 1', 123, 12.00, 'Drinks'),
(53, 'Arwin', 20, 150.00, 'Household Items');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `history`
--
ALTER TABLE `history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `inv`
--
ALTER TABLE `inv`
  ADD PRIMARY KEY (`product_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `history`
--
ALTER TABLE `history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `inv`
--
ALTER TABLE `inv`
  MODIFY `product_ID` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
