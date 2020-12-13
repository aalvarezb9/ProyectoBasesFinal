DELIMITER $$

CREATE TRIGGER CrearDibujo AFTER INSERT ON Dibujo
FOR EACH ROW 
	BEGIN
	    INSERT INTO Bitacora (id_user, descripcion) VALUES (new.id, "Se creó un dibujo");
	END$$

DELIMITER ;