CREATE DATABASE IF NOT EXISTS ProgramaDeDibujoBD;
 USE ProgramaDeDibujoBD;

 
DROP TABLE IF EXISTS Usuario;
CREATE TABLE IF NOT EXISTS Usuario (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  p_nombre varchar(200) DEFAULT NULL,
  s_nombre varchar(200) DEFAULT NULL,
  p_apellido varchar(200) DEFAULT NULL,
  s_apellido varchar(200) DEFAULT NULL,
  username varchar(200) NOT NULL,
  contraseña varchar(200) NOT NULL,
  tipo_usuario_id int(11) NOT NULL,
  bit_estado bit(1) NOT NULL DEFAULT '0',
  p_color VARCHAR(250) NOT NULL,
  f_color VARCHAR(250) NOT NULL,
  UNIQUE KEY username (username)
) CHARACTER SET utf8;
 
CREATE TABLE IF NOT EXISTS Repositorio (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id)
) CHARACTER SET utf8;
 
DROP TABLE IF EXISTS Dibujo;
CREATE TABLE IF NOT EXISTS Dibujo(
id INT AUTO_INCREMENT PRIMARY KEY,
var_nombre VARCHAR(255) NOT NULL, 
json_dibujo JSON NOT NULL,
tim_creacion TIMESTAMP DEFAULT NOW(),
repositorio_id INT NOT NULL,
 FOREIGN KEY (repositorio_id) REFERENCES Repositorio(id)
 ) CHARACTER SET utf8;
 
DROP TABLE IF EXISTS Bitacora;
CREATE TABLE IF NOT EXISTS Bitacora (
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  tim_accion timestamp NOT NULL DEFAULT current_timestamp(),
  id_user int(11) DEFAULT NULL,
  descripcion varchar(250) DEFAULT NULL
) CHARACTER SET utf8;
 

 DROP TABLE IF EXISTS Configuracion_Paleta;
CREATE TABLE IF NOT EXISTS Configuracion_Paleta (
 id INT AUTO_INCREMENT PRIMARY KEY,
 id_usuario INT NOT NULL,
 Pen_Color VARCHAR(150),
 Fill_Color VARCHAR(150),
 FOREIGN KEY (id_usuario) REFERENCES Usuario(id)
 ) CHARACTER SET utf8;
 
 
 

 