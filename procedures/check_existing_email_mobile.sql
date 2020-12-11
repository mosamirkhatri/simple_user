USE `user_schema`;
DROP procedure IF EXISTS `check_existing_email_mobile`;

DELIMITER $$
USE `user_schema`$$
CREATE PROCEDURE `check_existing_email_mobile` (IN p_email VARCHAR(100), IN p_mobile CHAR(11))
BEGIN
SELECT user_id
FROM user
WHERE email = p_email OR mobile = p_mobile;
END$$

DELIMITER ;