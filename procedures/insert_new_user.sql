USE `user_schema`;
DROP procedure IF EXISTS `insert_new_user`;

DELIMITER $$
USE `user_schema`$$
CREATE DEFINER=`root`@`%` PROCEDURE `insert_new_user`(IN p_name VARCHAR(50), IN p_email VARCHAR(100), IN p_mobile CHAR(11), IN p_flat_number VARCHAR(50), IN p_address_line_one VARCHAR(100), IN p_address_line_two VARCHAR(100), IN p_city VARCHAR(30), IN p_state VARCHAR(30), IN p_pincode CHAR(6))
BEGIN
INSERT INTO
user
(name,email,mobile,flat_number,address_line_one,address_line_two,city,state,pincode)
values
(p_name,p_email,p_mobile,p_flat_number,p_address_line_one,p_address_line_two,p_city,p_state,p_pincode);

SELECT \* FROM user where user_id = (SELECT last_insert_id());
END$$

DELIMITER ;