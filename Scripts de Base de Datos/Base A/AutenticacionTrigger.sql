DELIMITER $$

CREATE TRIGGER Autenticacion AFTER UPDATE ON Usuario
FOR EACH ROW 
	BEGIN
		IF new.bit_estado = 1 THEN
	    	INSERT INTO Bitacora (id_user, descripcion) VALUES (new.id, "Se inició sesión");
	    ELSE
			INSERT INTO Bitacora (id_user, descripcion) VALUES (new.id, "Se cerró sesión");
		END IF ;
	END$$

DELIMITER ;