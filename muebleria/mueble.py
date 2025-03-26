# clases relacionadas con los mueble
class Mueble:
    def __init__(self, precio, material):
        self._precio = precio
        self._material = material

    def calcula_precio(self):
        return self._precio  # Devuelve el precio del mueble

class Silla(Mueble):
    def __init__(self, precio, material, num_patas):
        super().__init__(precio, material)
        self._num_patas = num_patas
        self._precio_final = precio

    def __str__(self):
        return  f"Silla | Material: {self._material} | Precio: {self._precio} | Número de patas: {self._num_patas}"

# creamos la variable descuento, en caso de que sea cero el _precio_final seguira
# conservando el mismo _precio, pero si descuento es mayor que 0 entonces
# precio  hara su respectiva resta con descuento 
    def aplicar_descuento(self, descuento):
        """Aplica un descuento al precio de la silla"""
        if descuento > 0:
            self._precio_final = self._precio - descuento
        else:
            self._precio_final = self._precio

    def calcula_precio(self):
        return self._precio_final

class Mesa(Mueble):
    def __init__(self, precio, material, ancho, largo):
        super().__init__(precio, material)
        self._ancho = ancho
        self._largo = largo

    def __str__(self):
        return  f"Mesa | Material: {self._material} | Precio: {self._precio} | Tamaño: {self._ancho}x{self._largo} cm"

class Armario(Mueble):
    def __init__(self, precio, material, num_puertas):
        super().__init__(precio, material)
        self._num_puertas = num_puertas

    def __str__(self):
        return  f"Armario | Material: {self._material} | Precio: {self._precio} | Puertas: {self._num_puertas}"


