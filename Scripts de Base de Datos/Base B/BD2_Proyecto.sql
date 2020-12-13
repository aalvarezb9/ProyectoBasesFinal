CREATE DATABASE IF NOT EXISTS ProgramaDeDibujoBD2;
 USE ProgramaDeDibujoBD2;

 CREATE TABLE IF NOT EXISTS Dibujo2(
id INT NOT NULL,
var_nombre VARCHAR(255) NOT NULL, 
blo_dibujo BLOB NOT NULL,
tim_creacion TIMESTAMP DEFAULT NOW(),
repositorio_id INT NOT NULL
 ) CHARACTER SET utf8;