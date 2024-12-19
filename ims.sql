-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 19, 2024 at 06:10 AM
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
-- Database: `ims`
--

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `Id` int(11) NOT NULL,
  `Item` varchar(255) NOT NULL,
  `Price` decimal(10,2) NOT NULL,
  `Stock` int(11) NOT NULL,
  `Category` enum('Computers','Laptops','Desktops','All-in-One PCs','Computer Accessories','Monitors','Keyboards','Mice','Headsets','Speakers','Webcams','Printers','Scanners','Projectors','Storage Devices','Networking','Office Electronics','Copiers','Fax Machines','Calculators','Office Supplies','Paper','Pens','Binders','Stationery','Furniture','Chairs','Desks','Cabinets','Misc') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`Id`, `Item`, `Price`, `Stock`, `Category`) VALUES
(5, 'Laptop i3', 17000.00, 8, 'Laptops'),
(6, 'Plastic Chair Small', 80.00, 24, 'Chairs'),
(7, 'Lays', 10.00, 20, 'Misc'),
(8, 'Gaming Laptop RTX 3060', 95000.00, 5, 'Laptops'),
(9, 'Desktop PC Core i7', 65000.00, 10, 'Desktops'),
(10, 'Wireless Keyboard', 1500.00, 15, 'Keyboards'),
(11, 'Curved Monitor 27 inch', 25000.00, 12, 'Monitors'),
(12, 'Bluetooth Headphones', 3000.00, 50, 'Headsets'),
(13, 'LED Projector', 12000.00, 8, 'Projectors'),
(14, '4TB External Hard Drive', 7500.00, 30, 'Storage Devices'),
(15, 'Office Desk', 4500.00, 18, 'Furniture'),
(16, 'Laser Printer', 11000.00, 20, 'Printers'),
(17, 'HP Officejet Pro', 9000.00, 13, 'Printers'),
(18, 'Ergonomic Office Chair', 3500.00, 25, 'Chairs'),
(19, 'Wireless Mouse', 800.00, 40, 'Mice'),
(20, 'Paper Clips Box', 50.00, 100, 'Office Supplies'),
(21, 'Projector Screen', 5000.00, 10, 'Projectors'),
(22, 'Mechanical Keyboard', 5000.00, 12, 'Keyboards'),
(23, 'Webcam 1080p', 2500.00, 35, 'Webcams'),
(24, 'Fax Machine', 7000.00, 7, 'Fax Machines'),
(25, 'Binders Pack', 200.00, 50, 'Binders'),
(26, 'Desk Lamp', 1200.00, 15, 'Furniture'),
(27, 'HP Calculator', 500.00, 60, 'Calculators'),
(28, 'HP Office Chair', 4000.00, 20, 'Chairs'),
(29, 'Standing Desk', 12000.00, 10, 'Furniture'),
(30, 'USB Keyboard', 1000.00, 10, 'Keyboards');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
