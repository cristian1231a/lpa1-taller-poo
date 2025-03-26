from mueble import Silla, Mesa, Armario

# En esta clase inventario vamos a crear el CRUD con el que vamos a poder
# -agregar -eliminar -listar y calcular el precio total
class Inventario:
    def __init__(self):
        self.muebles = []  # Lista para almacenar los muebles

    def agregar_mueble(self, mueble):
        """Agrega un mueble al inventario."""
        self.muebles.append(mueble)

    def listar_muebles(self):
        """Lista todos los muebles en el inventario."""
        if not self.muebles:
            print("El inventario está vacío.")
        for mueble in self.muebles:
            print(mueble)

    def __str__(self):
        if not self.muebles:
            return "El inventario está vacío."
        return "\n".join(str(mueble) for mueble in self.muebles)  # Convierte cada mueble en string y los une con saltos de línea