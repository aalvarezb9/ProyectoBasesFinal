DROP PROCEDURE IF EXISTS REGISTRAR_USUARIO;
DELIMITER $$
CREATE PROCEDURE REGISTRAR_USUARIO(IN P_NOMBRE VARCHAR(200), IN S_NOMBRE VARCHAR(200), IN P_APELLIDO VARCHAR(200), IN S_APELLIDO VARCHAR(200), 
                                     IN USERNAME VARCHAR(200), IN CONTRASEÑA VARCHAR(200), IN TIPO_USER INT(11),
					                IN PCOLOR VARCHAR(250), IN FCOLOR VARCHAR(250)) 

BEGIN 
    INSERT INTO Usuario(p_nombre, s_nombre, p_apellido, s_apellido, username, contraseña, tipo_usuario_id, p_color, f_color) 
    VALUES (P_NOMBRE, S_NOMBRE,P_APELLIDO,S_APELLIDO, USERNAME, CONTRASEÑA, TIPO_USER, PCOLOR, FCOLOR);

    SELECT @ID_USUARIO := id from Usuario ORDER BY id DESC LIMIT 1; 
    CALL IRepositorio(@ID_USUARIO);
    CALL IPaleta(PCOLOR, FCOLOR, @ID_USUARIO);

END$$
DELIMITER ;

CALL REGISTRAR_USUARIO("usuario2", "usuario2", "usuario2", "usuario2" ,"usuario2", "usuario2", 2, "#00FF00FF", "#FF00FF00");
CALL REGISTRAR_USUARIO("usuario3", "usuario3", "usuario3", "usuario3" ,"usuario3", "usuario3", 1, "#00FF00FF", "#FF00FF00");
