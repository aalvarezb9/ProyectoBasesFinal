DROP TRIGGER IF EXISTS ActualizarUsuario;

DELIMITER $$

CREATE TRIGGER ActualizarUsuario BEFORE UPDATE ON Usuario
FOR EACH ROW 
	BEGIN
	    INSERT INTO Bitacora (id_user, descripcion) VALUES (new.id, "Se actualizó un usuario");
	END$$

DELIMITER ;