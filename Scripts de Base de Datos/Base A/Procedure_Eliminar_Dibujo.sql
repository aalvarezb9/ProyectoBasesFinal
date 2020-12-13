DELIMITER $$
CREATE PROCEDURE EliminarDibujo(IN idd INT, IN A INT) 

BEGIN 
    DELETE FROM Dibujo WHERE id = idd;
    DELETE FROM ProgramaDeDibujoBD2.Dibujo2 WHERE ProgramaDeDibujoBD2.Dibujo2.id = idd;
END$$
DELIMITER ;