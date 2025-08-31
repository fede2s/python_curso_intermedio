import sqlite3


class DbSqlite3():
    """
    Clase con...

    Atributos de instancia:
        nombre_base
        nombre_tabla
        campos

    Metodos de instancia privados:
        __crear_base()
        __crear_tabla()


    Metodos publicos:
        insertar_datos()
        borrar_registro()
        actualizar_registro()
        consultar_tabla()
        listar_tablas()
        obtener_columnas()
    """
    def __init__(
            self,
            nombre_base,
            nombre_tabla,
            campos):
        """
        El constructor define los atributos de instancia y los carga
        Ademas ejecuta los metodos privados: crear_base() y
        crear_tabla()
        """
        self.nombre_base = nombre_base
        self.nombre_tabla = nombre_tabla
        self.campos = campos
        self.__crear_base()
        self.__crear_tabla()

    def __crear_base(self):
        con = sqlite3.connect(self.nombre_base)
        con.commit()
        con.close()

    def __crear_tabla(self):
        campos = ', '.join(self.campos)
        sql = "CREATE TABLE if not exists " \
            + f"{self.nombre_tabla} ({self.campos});"
        try:
            con = sqlite3.connect(self.nombre_base)
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            print(f"Tabla '{self.nombre_tabla}' "
                  + " creada exitosamente.")
            con.close()
        except Exception as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            con.close()

    def insertar_datos(
            self,
            datos):
        con = sqlite3.connect(self.nombre_base)
        cursor = con.cursor()
        if len(datos) == 0:
            print("No hay datos para insertar.")
            con.commit()
            con.close()
            return

        """
        armo la cantidad de placeholders necesarios para la cantidad
        de datos
        """
        placeholders = ', '.join(['?'] * len(datos))
        print(datos)
        print(placeholders)
        sql = f"INSERT INTO {self.nombre_tabla} " \
            f"VALUES ({placeholders})"

        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def borrar_registro(self, id):
        sql = f"DELETE FROM {self.nombre_tabla} WHERE id = ?"
        data = (id,)
        con = sqlite3.connect(self.nombre_base)
        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()
        con.close()

    def actualizar_registro(
            self,
            id,
            nuevos_datos):
        """
        armo la cantidad de placeholders necesarios para la cantidad
        de campos
        """
        sql = f"UPDATE {self.nombre_tabla} SET "

        nombres_columnas = self.obtener_columnas()
        campos = nombres_columnas[1:]
        nombreid = nombres_columnas[0]
        for campo in campos:
            sql += f"{campo} = ?, "
        sql = sql[:-2]  # Elimino la última coma y espacio
        sql += " WHERE id = ?"
        data = tuple(nuevos_datos + (id,))
        con = sqlite3.connect(self.nombre_base)
        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()
        con.close()

    def consultar_tabla(self, id=None):
        if id is None:
            print("No se especificó un ID para consultar.")
            try:
                con = sqlite3.connect(self.nombre_base)
                cursor = con.cursor()
                sql = f"SELECT * FROM {self.nombre_tabla};"
                cursor.execute(sql)
                registros = cursor.fetchall()
                for registro in registros:
                    print(f"Registro leido: {registro}")
                con.commit()
                con.close()
                return registros
            except Exception as e:
                print(f"Error al consultar la tabla: {e}")
                con.commit()
                con.close()
                return None
        else:
            try:
                con = sqlite3.connect(self.nombre_base)
                cursor = con.cursor()
                sql = f"SELECT * FROM {self.nombre_tabla} WHERE id = ?;"
                data = (id,)
                cursor.execute(sql, data)
                registros = cursor.fetchall()
                for registro in registros:
                    print(f"Registro leido: {registro}")
                con.commit()
                con.close()
                return registros
            except Exception as e:
                print(f"Error al consultar la tabla: {e}")
                con.commit()
                con.close()
                return []

    def obtener_columnas(self):
        try:
            con = sqlite3.connect(self.nombre_base)
            cursor = con.cursor()
            cursor.execute(f"PRAGMA table_info({self.nombre_tabla});")
            columnas = cursor.fetchall()
            # Extraer solo los nombres de las columnas
            nombres_columnas = [columna[1] for columna in columnas]
            con.commit()
            con.close()
            return nombres_columnas
        except Exception as e:
            print("Error al obtener las columnas de la tabla "
                  + f"'{self.nombre_tabla}': {e}")
            con.commit()
            con.close()
            return []

    def listar_tablas(self):
        con = sqlite3.connect(self.nombre_base)
        cursor = con.cursor()
        # sql= "SHOW TABLES FROM base.db;"
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        cursor.execute(sql)
        tablas = cursor.fetchall()
        for tabla in tablas:
            print(f"Tabla: {tabla[0]}")
        con.commit()
        con.close()
        return tablas
