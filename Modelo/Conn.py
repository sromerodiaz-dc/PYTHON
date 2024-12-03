import sqlite3


class DatabaseConnection:
    #Clase que esrtablece la conexion con una base de datos SQLite y la crea si no existe
    def __init__(self):
        self.conexion = sqlite3.connect("base_datos.db")
        self.cursor = self.conexion.cursor() #Creamos un cursor para ejecutar las consultas
        self.crear_tabla("personas", "nome TEXT, dni TEXT, genero TEXT, fallecido BOOLEAN") #Creamos la tabla personas si no existe

    def crear_tabla(self, nombre_tabla, campos):
        #Metodo que crea una tabla en la base de datos si no existe
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {nombre_tabla} ({campos})")
        self.conexion.commit()

    def insertar(self, nombre_tabla, nombre, dni, genero, fallecido):
        self.cursor.execute(
            f"INSERT INTO {nombre_tabla} VALUES (?, ?, ?, ?)",
            (nombre, dni, genero, fallecido)
        )
        self.conexion.commit()

    def leer(self, nombre_tabla):
        self.cursor.execute(f"SELECT * FROM {nombre_tabla}")
        return self.cursor.fetchall()

    def delete_item(self, nombre_tabla, dni):
        self.cursor.execute(
            f"DELETE FROM {nombre_tabla} WHERE dni = ?",
            (dni,)
        )
        self.conexion.commit()

    def update_item(self, nombre_tabla, nombre, dni, genero, fallecido):
        self.cursor.execute(
            f"UPDATE {nombre_tabla} SET nome = ?, genero = ?, fallecido = ? WHERE dni = ?",
            (nombre, genero, fallecido, dni)
        )
        self.conexion.commit()