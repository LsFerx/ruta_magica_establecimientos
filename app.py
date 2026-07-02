from dao.establecimiento_dao import EstablecimientoDAO
from models.establecimiento import Establecimiento  

def ver_establecimientos():
    try:
        establecimiento_dao = EstablecimientoDAO()
        establecimiento = establecimiento_dao.obtener_todo()

        if len(establecimiento) == 0:
            print("No hay elementos en la lista")
        else: 
            for establecimiento in establecimiento:
                print(f"{establecimiento.id} {establecimiento.nombre} {establecimiento.propietario} {establecimiento.categoria} {establecimiento.telefono}")
        print("\n Conexion exitosa con la base")
    except Exception as e:
        print("Error", e)

def insertar_establecimiento():
    print("Insertar un nuevo establecimiento ")
    nombre = input("Escribe el Nombre: ")
    propietario = input("Escribe el Nombre Del Propietario: ")
    categoria = int(input("Escriba la categoria: "))
    telefono = input("Escribe el telefono: ")

    try:
        establecimiento_dao = EstablecimientoDAO()
        ultimo_id = establecimiento_dao.obtener_ultimo_id() + 1
        establecimiento = Establecimiento(ultimo_id, nombre, propietario, categoria, telefono)
        establecimiento_dao.insertar(establecimiento)
        print("Insercion Exitosa")
    except Exception as e:
        print("Error al insertar el Establecimiento")
        print(e)

def actualizar_establecimiento():
    try:
        establecimiento_dao = EstablecimientoDAO()
        print("Lista de Establecimientos Disponibles")
        ver_establecimientos()
        id = int(input("Seleccione el id del establecimiento a actualizar"))
        nombre = input("Escribe el Nombre")
        propietario = input("Escribe el Nombre del Propietario:")
        categoria = int(input("Escribe la Categoria"))
        telefono = input("Escribe el telefono")
        establecimiento = Establecimiento(id, nombre, propietario, categoria, telefono)
        establecimiento_dao.actualizar(establecimiento)
        print("El establecimiento fue actualizado con exito")
    except Exception as e:
        print("Error al actualizar", e)

def eliminar_establecimiento():
    try:
        establecimiento_dao = EstablecimientoDAO()
        print("Lista de Establecimientos Disponibles:")
        establecimiento_dao.obtener_todo()
        id = int(input("escriba el id del Establecimiento a eliminar: "))
        establecimiento_dao.eliminar(id)
        print(f"Eliminado con exito", e)
    except Exception as e:
        print(f"Error al eliminar el Establecimiento", e)

        

def main():
    print("=== BIBLIOTECA UNIVERSITARIA ===")
    print("1. Ver todos los Establecimientos")
    print("2. Insertar un nuevo Establecimiento")
    print("3. Actualizar un Establecimiento existente")
    print("4. Eliminar un  Establecimiento existente")
    opcion = int(input("Selecciona una opcion del 1-4:"))
    match opcion:
        case 1:
            ver_establecimientos()
        case 2:
            insertar_establecimiento()
        case 3:
            actualizar_establecimiento() 
        case 4: 
            eliminar_establecimiento()

    print(" Saliendo de Ruta Magica... :) ")
    

if __name__ == "__main__":
    main()
    