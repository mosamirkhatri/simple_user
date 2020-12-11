USE `user_schema`;
DROP procedure IF EXISTS `create_user_table`;

DELIMITER $$
USE `user_schema`$$
CREATE DEFINER=`root`@`%` PROCEDURE `create_user_table`()
BEGIN
CREATE TABLE IF NOT EXISTS `user` (
`user_id` INT(11) NOT NULL AUTO_INCREMENT,
`name` VARCHAR(50) NOT NULL,
`email` VARCHAR(100),
`mobile` CHAR(11) NOT NULL,
`flat_number` VARCHAR(50) NOT NULL,
`address_line_one` VARCHAR(100),
`address_line_two` VARCHAR(100),
`city` VARCHAR(30) NOT NULL,
`state` VARCHAR(30) NOT NULL,
`pincode` CHAR(7) NOT NULL,
PRIMARY KEY (`user_id`)
);
END$$

DELIMITER ;