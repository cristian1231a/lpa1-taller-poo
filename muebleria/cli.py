from mueble import Silla, Mesa, Armario
from inventario import Inventario

def mostrar_menu():
    print("\n--- MENÚ DE LA MUEBLERÍA ---")
    print("1. Agregar Silla")
    print("2. Agregar Mesa")
    print("3. Agregar Armario")
    print("4. Mostrar Inventario")
    print("5. Salir")

def agregar_silla(inventario):
    precio = float(input("Ingrese el precio de la silla: "))
    material = input("Ingrese el material de la silla: ")
    num_patas = int(input("Ingrese el número de patas: "))
    silla = Silla(precio, material, num_patas)
    inventario.agregar_mueble(silla)
    print("Silla agregada con éxito.")

def agregar_mesa(inventario):
    precio = float(input("Ingrese el precio de la mesa: "))
    material = input("Ingrese el material de la mesa: ")
    ancho = float(input("Ingrese el ancho de la mesa: "))
    largo = float(input("Ingrese el largo de la mesa: "))
    mesa = Mesa(precio, material, ancho, largo)
    inventario.agregar_mueble(mesa)
    print("Mesa agregada con éxito.")

def agregar_armario(inventario):
    precio = float(input("Ingrese el precio del armario: "))
    material = input("Ingrese el material del armario: ")
    num_puertas = int(input("Ingrese el número de puertas: "))
    armario = Armario(precio, material, num_puertas)
    inventario.agregar_mueble(armario)
    print("Armario agregado con éxito.")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                agregar_silla(inventario)
            case "2":
                agregar_mesa(inventario)
            case "3":
                agregar_armario(inventario)
            case "4":
                print("\n--- Inventario ---")
                print(inventario)
            case "5":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()