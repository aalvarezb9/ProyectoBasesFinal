@author nohernandeza@unah.hn  @date 2020/12/07


# Descripción de la base de datos para la resolución del problema.


## Sobre esquemas/tablas y campos/atributos
----

Se hizo la creación de cinco (5) tablas, las cuales serán detalladas a continuación:


* **Usuario**: Debido a que el problema La función de la siguiente tabla radica en almacenar los datos de los usuarios registrados, cuenta con ocho (10) atributos que se detallan a continuación:

    1. id: Primary Key autoincremental de tipo *INT* para identificar de manera única a cada usuario registrado.
    2. p_nombre: Atributo de tipo *VARCHAR* con un límite de 200 carácteres para especificar el primer nombre del usuario a registrar.
    3. s_nombre: Atributo de tipo *VARCHAR* con un límite de 200 carácteres para especificar el segundo nombre del usuario a registrar.
    4. p_apellido: Atributo de tipo *VARCHAR* con un límite de 200 carácteres para especificar el primer apellido del usuario a registrar.
    5. s_apellido: Atributo de tipo *VARCHAR* con un límite de 200 carácteres para especificar el segundo apellido del usuario a registrar.
    6. username: Atributo de tipo *VARCHAR* con un límite de 200 carácteres para especificar el  username del usuario a registrar, es definido como un campo único.
    7. contraseña: Atributo de tipo *VARCHAR* con un límite de 200 carácteres para especificar la contraseña del usuario a registrar.
    8. tipo_usuario_id: Foreign Key de tipo *INT* que hace referencia al campo *id* de la tabla *Tipo_usuario*.
    9. f_color: Es el fill color que se escoge al momento de registrarse
    10. p_color: gual que el atributo anterior, se selecciona al iniciar el programa

* **Repositorio**: La función de la siguiente tabla es almacenar los dibujos e información de un usuario en específico, cuenta con dos (2) atributos que se detallan a continuación:

    1. id: Primary Key autoincremental de tipo *INT* para identificar de manera única cada repositorio.
    1. usuario_id: Foreign Key de tipo *INT* que hace referencia al campo *id* de la tabla *Usuario*.

* **Dibujo**: Su función radica en el almacenamiento del dibujo realizado por un usuario, cuenta con cuatro (5) atributos que se detallan a continuación:

    1. id: Primary Key autoincremental de tipo *INT* para identificar de manera única cada dibujo.
    2. var_nombre: El nombre que el usuario le da al dibujo
    3. jso_dibujo: Atributo de tipo *JSON* que almacenará un dibujo proveniente de un archivo tipo blob que será convertido a tipo json para poder ser almacenado.
    4. tim_creacion: Atributo de tipo *TIMESTAMP* que guardará la fecha completa de la creación de un dibujo.
    5. repositorio_id: Foreign Key de tpo *INT* que hace referecia al campo *id* de la tabla *Repositorio*.

* **Bitacora**: Cuenta con la función de almacenar las acciones realizadas por un usuario, cuenta con ocho (4) atributos que se detallan a continuación:

    1. id: Primary Key autoincremental de tipo *INT* para identificar de manera única cada bitácora.
    2. tim_accion: Es la hora a que se registró el suceso
    3. usuario_id: Foreign Key de tpo *INT* que hace referecia al campo *id* de la tabla *Usuario*.
    4. descripcion: Aquí se especifica la acción realizada

* **Configuración_Paleta**: Su función es almacenar los valores de colores, que serán gestionados solamente por el usuario administrador, cuenta con tres (4) atributos que se detallan a continuación:

    1. id: Primary Key autoincremental de tipo *INT* para identificar de manera única cada configuración de paleta.
    2. id_usuario: Se relaciona con los usuarios, para saber a quien le corresponde cada configuración.
    3. Pen_Color: Atributo de tipo *VARCHAR* con un límite de 200 carácteres que almacenará el color seleccionado para Pen_Color en formato hexadecimal.
    4. Fill_Color: Atributo de tipo *VARCHAR* con un límite de 200 carácteres que almacenará el color seleccionado para Fill_Color en formato hexadecimal.

Además, se creó una base de datos que respaldo con una tabla que almacena los dibujos de la tabla principal en formato BLOB.

## Componentes
---

Se hizo uso de los componentes vistos en clase para hacer este proyecto, como ser: 

* Consultas
* Sub-consultas
* Procedimientos almacenados
* Triggers
* Vistas
* Entre otros

Por otro lado, se usó el lenguaje de programación Python (3.x) en un sistema operativo basado en el kernel de Linux (uno de los que se especifican en la planificación académica).

## Tablas entidad-relación usadas
---

A continuación, se ejemplificará a través de las tablas ER el modelo de base de datos que se siguió para elaborar el proyecto:

![image](https://drive.google.com/uc?export=view&id=1jQ6-c1UOT0zhalcG4hZQuVaGfZx2zo6f)

## Otros componentes necesarios
---

* Conocimientos sobre programación orientada a objetos para evitar escribir código redundante
* Manejo de algunas estructuras de datos
* Uso sistemático de la lógica para resolver ciertos algoritmos
* Etc



