DROP VIEW IF EXISTS DatosDibujo;

CREATE VIEW DatosDibujo AS (
    SELECT 
	Dibujo.id, Dibujo.var_nombre, Dibujo.tim_creacion, Usuario.id AS
	FROM Usuario INNER JOIN Repositorio ON Usuario.id = Repositorio.usuario_id
    INNER JOIN Dibujo ON Dibujo.repositorio_id = Repositorio.id
);  