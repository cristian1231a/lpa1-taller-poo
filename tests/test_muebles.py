# pruebas unitarias utilizando pytest


from muebleria.mueble import Silla, Mesa, Armario  # Importar desde el paquete muebleriap

#Prueba 1: Verificar el precio inicial de una silla
def test_precio_silla():
    silla = Silla(5000, "Madera", 4)
    assert silla.calcula_precio() == 5000  #Esperamos que el precio sea 5000

#Prueba 2: Aplicar descuento y verificar precio final
def test_descuento_silla():
    silla = Silla(5000, "Madera", 4)
    silla.aplicar_descuento(1000)
    assert silla._precio_final == 4000  #Esperamos que el precio final sea 4000

#Prueba 3: Crear un armario y verificar sus atributos
def test_armario():
    armario = Armario(12000, "Roble", 3)
    assert armario._num_puertas == 3  # Esperamos que tenga 3 puertas
    assert armario.calcula_precio() == 12000  #Esperamos que el precio sea 12000

#el 'assert' se usa para verificar que una condición sea verdadera. Si la condición es falsa

#Prueba 4: Crear una mesa y vericar atributos
def test_mesa():
    mesa = Mesa(9000,"Roble", 40, 20)
    assert mesa._largo == 20
    assert mesa._ancho == 40

def test_agregar_mueble():
    silla = Silla(500, "Pino", 5)
    assert silla._material == "Pino"