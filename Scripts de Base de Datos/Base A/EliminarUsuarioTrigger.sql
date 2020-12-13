DELIMITER $$

CREATE TRIGGER EliminarUsuario BEFORE DELETE ON Usuario
FOR EACH ROW 
	BEGIN
	    INSERT INTO Bitacora (id_user, descripcion) VALUES (OLD.id, "Se eliminó un usuario");
	END$$

DELIMITER ;
