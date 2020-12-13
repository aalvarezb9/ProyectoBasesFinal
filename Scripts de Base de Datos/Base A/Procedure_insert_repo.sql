DELIMITER $$
CREATE PROCEDURE Irepositorio(IN id INT) 

BEGIN 
    INSERT INTO Repositorio(usuario_id) VALUES (id);
END$$
DELIMITER ;