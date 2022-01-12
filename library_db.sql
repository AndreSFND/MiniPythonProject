-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           10.4.21-MariaDB - mariadb.org binary distribution
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para library_db
CREATE DATABASE IF NOT EXISTS `library_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `library_db`;

-- Copiando estrutura para tabela library_db.books
CREATE TABLE IF NOT EXISTS `books` (
  `BID` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL DEFAULT '0',
  `author` varchar(255) NOT NULL DEFAULT '0',
  PRIMARY KEY (`BID`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela library_db.books: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` (`BID`, `title`, `author`) VALUES
	(1, 'Harry Potter 1', 'J K Rowling'),
	(2, 'Harry Potter 3', 'J K Rowling'),
	(5, 'Harry Potter 4', 'Dialog'),
	(6, 'New book', 'Andre'),
	(7, 'New book', 'Andre');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;

-- Copiando estrutura para tabela library_db.book_issues
CREATE TABLE IF NOT EXISTS `book_issues` (
  `issue_id` int(11) NOT NULL AUTO_INCREMENT,
  `bid` int(11) NOT NULL,
  `issue_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `return_date` datetime NOT NULL,
  `returned_date` datetime DEFAULT NULL,
  PRIMARY KEY (`issue_id`),
  KEY `FK1_book_issues_books` (`bid`),
  CONSTRAINT `FK1_book_issues_books` FOREIGN KEY (`bid`) REFERENCES `books` (`BID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela library_db.book_issues: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `book_issues` DISABLE KEYS */;
INSERT INTO `book_issues` (`issue_id`, `bid`, `issue_date`, `return_date`, `returned_date`) VALUES
	(1, 1, '2022-01-11 22:04:31', '2022-01-18 22:04:33', '2022-01-18 22:04:33'),
	(2, 2, '2022-01-11 22:04:56', '2022-01-18 22:04:57', '2022-01-12 01:26:05'),
	(3, 1, '2022-01-12 01:15:28', '2022-01-19 01:15:28', '2022-01-18 22:04:33'),
	(4, 1, '2022-01-12 01:28:45', '2022-01-19 01:28:45', '2022-01-12 01:38:16'),
	(6, 2, '2022-01-12 01:38:22', '2022-01-19 01:38:22', '2022-01-12 01:48:51'),
	(7, 2, '2022-01-12 04:11:41', '2022-01-19 04:11:41', '2022-01-12 04:15:31'),
	(8, 1, '2022-01-12 04:13:14', '2022-01-19 04:13:14', '2022-01-12 04:15:33'),
	(9, 1, '2022-01-12 04:17:27', '2022-01-19 04:17:27', '2022-01-12 04:17:38'),
	(10, 1, '2022-01-12 04:18:39', '2022-01-19 04:18:39', '2022-01-12 04:19:44'),
	(27, 1, '2022-01-12 09:44:10', '2022-01-19 09:44:10', '2022-01-12 09:44:43');
/*!40000 ALTER TABLE `book_issues` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
