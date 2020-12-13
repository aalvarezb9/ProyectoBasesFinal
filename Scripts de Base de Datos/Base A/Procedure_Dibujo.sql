DROP PROCEDURE IF EXISTS Dibujo;
DELIMITER $$
CREATE PROCEDURE Dibujo(IN nombre VARCHAR(255), IN dibujo JSON, IN idd INT, IN dibujo2 BLOB)

BEGIN
    SELECT @repo_id := id FROM Repositorio WHERE Repositorio.usuario_id = idd;

    INSERT INTO Dibujo (var_nombre, json_dibujo, repositorio_id) VALUES (nombre, dibujo, @repo_id);
    SELECT @dibujo_id := id FROM Dibujo WHERE var_nombre = nombre AND repositorio_id = @repo_id;

    INSERT INTO ProgramaDeDibujoBD2.Dibujo2 (id, var_nombre, blo_dibujo, repositorio_id) VALUES (@dibujo_id, nombre, dibujo2, @repo_id);
END$$
DELIMITER ;