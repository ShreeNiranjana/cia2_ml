CREATE DATABASE IF NOT EXISTS `pythonlogin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `pythonlogin`;

CREATE TABLE IF NOT EXISTS `accounts` (
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `accounts` ( `password`, `email`) VALUES 
('Niru01', 'niranjana6503@gmail.com'),
('srik1*@','srikiruthika53@gmail.com'),
('SHRAVYA1310','shravyad@gmail.com'),
('blah2345','blah@gmail.com');
SELECT*FROM accounts;