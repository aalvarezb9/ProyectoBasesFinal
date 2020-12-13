DELIMITER $$

CREATE TRIGGER Registro AFTER INSERT ON Usuario
FOR EACH ROW 
	BEGIN
	    INSERT INTO Bitacora (id_user, descripcion) VALUES (new.id, "Se registró un usuario");
	END$$

DELIMITER ;