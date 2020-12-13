DROP PROCEDURE IF EXISTS Login;
DROP PROCEDURE IF EXISTS Logout;
DELIMITER $$
CREATE PROCEDURE Login(IN username VARCHAR(250), IN password VARCHAR(250), OUT status BIT, OUT idd INT)
BEGIN
		
        IF EXISTS(SELECT id FROM Usuario WHERE username = Usuario.username AND password = Usuario.contraseña) THEN	
        	SELECT @user := id FROM Usuario WHERE username LIKE Usuario.username AND password LIKE Usuario.contraseña;
            SELECT 1 INTO status;
            SELECT @user INTO idd;
            UPDATE Usuario SET bit_estado = 1 WHERE username = Usuario.username AND password = Usuario.contraseña;
        ELSE
        	SELECT 0 INTO status;       
        END IF;
    END$$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE Logout(IN id INT)
BEGIN
    	UPDATE Usuario SET bit_estado = 0 WHERE id = Usuario.id;
    END$$
DELIMITER ;