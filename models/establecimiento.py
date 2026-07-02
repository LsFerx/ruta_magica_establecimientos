class Establecimiento:
    
    #Constructor
    def __init__(self, id, nombre, propietario, categoria, telefono):
        self.id = id
        self.nombre = nombre
        self.propietario = propietario
        self.categoria = categoria
        self.telefono = telefono

    def mostrar_info(self):
        return f"ID:  {self.id}, Nombre: {self.nombre}, Propietario: {self.propietario}, Categoria: {self.categoria}, telefono: {self.telefono}"