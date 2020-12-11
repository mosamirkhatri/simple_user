USE `user_schema`;
DROP procedure IF EXISTS `get_all_users`;

DELIMITER $$
USE `user_schema`$$
CREATE PROCEDURE `get_all_users` ()
BEGIN
SELECT \* From user;
END$$

DELIMITER ;