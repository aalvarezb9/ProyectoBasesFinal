DROP VIEW IF EXISTS DatosUser;

CREATE VIEW DatosUser AS (
    SELECT id, username, p_nombre, s_nombre, p_apellido, s_apellido 
    FROM Usuario ORDER BY id DESC
);