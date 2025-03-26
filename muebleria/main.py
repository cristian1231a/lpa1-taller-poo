# ejecutar el programa y probar las clases

from mueble import Silla, Mesa, Armario  # Importamos las clases de mueble.py
from rich.console import Console #rich es la libreria para que aparezca la tabla en la consola
from rich.table import Table

from inventario import Inventario  # Importa la clase Inventario

def main():
    console = Console()

    # 📌 Instanciando objetos de las subclases
    silla1 = Silla(5000, "Pino", 2)
    silla2 = Silla(10000, "Pino", 3)
    mesa = Mesa(10000, "Pino", 2, 3)
    armario = Armario(8000, "Roble", 4)

    # Aplicando descuento a silla1
    silla1.aplicar_descuento(0)

    #https://rich.readthedocs.io/en/stable/introduction.html
    # 📌 Creando una tabla para mostrar la información con Rich
    table = Table(title="Información de Muebles")
    table.add_column("Tipo", style="cyan")
    table.add_column("Material", style="magenta")
    table.add_column("Precio", justify="right", style="green")
    table.add_column("Detalles", style="yellow")

    # Agregar filas con la información de cada mueble
    table.add_row("Silla", silla1._material, f"${silla1.calcula_precio()}", f"Nº patas: {silla1._num_patas}")
    table.add_row("Silla", silla2._material, f"${silla2.calcula_precio()}", f"Nº patas: {silla2._num_patas}")
    table.add_row("Mesa", mesa._material, f"${mesa.calcula_precio()}", f"Dimensiones: {mesa._ancho}CM x {mesa._largo}CM")
    table.add_row("Armario", armario._material, f"${armario.calcula_precio()}", f"Puertas: {armario._num_puertas}")

    # 📌 Mostrar la tabla en la consola
    console.print(table)


    # Crear el inventario
    inventario = Inventario()

    # Crear muebles
    crearSilla = Silla(1000, "Pino", 4)

    # Agregar muebles al inventario
    inventario.agregar_mueble(crearSilla)

    # Listar muebles en inventario
    print("\n--- Muebles en inventario ---")
    print(inventario)



#permite que un archivo se pueda ejecutar tanto como un script independiente como un módulo importado en otro programa.
if __name__ == "__main__":
    main()


