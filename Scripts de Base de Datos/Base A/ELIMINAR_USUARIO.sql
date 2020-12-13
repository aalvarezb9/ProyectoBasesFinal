DROP PROCEDURE IF EXISTS ELIMINAR_USUARIO;
DELIMITER $$
CREATE PROCEDURE ELIMINAR_USUARIO(IN ID INT, IN a INT) 
    BEGIN 
        SELECT @id_repositorio := Repositorio.id 
        FROM Repositorio 
        WHERE Repositorio.usuario_id = ID; 

        DELETE FROM Configuracion_Paleta WHERE Configuracion_Paleta.id_usuario = ID; 
        DELETE FROM Dibujo WHERE Dibujo.repositorio_id = @id_repositorio; 
        DELETE FROM Repositorio WHERE Repositorio.usuario_id = ID;
        DELETE FROM Usuario WHERE Usuario.id = ID; 

    END$$
DELIMITER ;