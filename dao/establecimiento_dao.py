from database.conexion import Conexion
from models.establecimiento import Establecimiento

class EstablecimientoDAO:
    #SELECT * FROM
    def obtener_todo(self, ):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM vista_establecimientos")

        registros = cursor.fetchall()

        stablecimientos = []
        for registro in registros:
            establecimiento = Establecimiento(
                id = registro [0],
                nombre = registro [1],
                propietario = registro [2],
                categoria = registro [3],
                telefono= = registro[4],
            )

            establecimiento.append(establecimiento)
        cursor.close()
        conexion.close()
        return establecimiento
    
    #INSERT
    def insertar(self, establecimiento):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO Establecimiento(id,nombre, propietario, categoria, telefono)
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
        UPDATE Establecimiento
        SET nombre = %s, propietario = %s, categoria = %s, telefono = %s
        WHERE id = %s
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

    #DELETE
    def eliminar(Self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        
        cursor.execute("DELETE FROM Establecimiento WHERE id_establecimiento = %s",(id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT MAX(id_establecimiento) FROM Establecimientos")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None: 
            return 0 
        return resultado[0]