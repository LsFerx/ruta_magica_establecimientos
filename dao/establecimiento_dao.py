from database.conexion import Conexion
from models.establecimiento import Establecimiento

class EstablecimientoDAO:
    #SELECT * FROM
    def obtener_todo(self, ):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM vista_establecimientos")

        registros = cursor.fetchall()

        establecimientos = []

        for registro in registros:
            establecimiento = Establecimiento(
                id = registro [0],
                nombre = registro [1],
                propietario = registro [2],
                categoria = registro [3],
                telefono = registro[4],
            )

            establecimientos.append(establecimiento)
        cursor.close()
        conexion.close()
        return establecimientos
    
    #INSERT
    def insertar(self, establecimiento):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO establecimientos(id, nombre, propietario, categoria, telefono)
        VALUES(%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            establecimiento.id,
            establecimiento.nombre,
            establecimiento.propietario,
            establecimiento.categoria,
            establecimiento.telefono,
        ))

        conexion.commit()
        cursor.close()
        conexion.close()
        
    #UPDATE
    def actualizar(self, establecimiento):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE establecimientos
        SET nombre = %s, propietario = %s, categoria = %s, telefono = %s
        WHERE id = %s
        """
        cursor.execute(sql, (
                      establecimiento.nombre,
                      establecimiento.propietario,
                      establecimiento.categoria,
                      establecimiento.telefono,
                      establecimiento.id,
                      ))

        conexion.commit()
        cursor.close()
        conexion.close()

    #DELETE
    def eliminar(Self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        
        cursor.execute("DELETE FROM establecimientos WHERE id = %s",(id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT MAX(id) FROM establecimientos")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None: 
            return 0 
        return resultado[0]