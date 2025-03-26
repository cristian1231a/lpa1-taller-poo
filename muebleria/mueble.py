# clases relacionadas con los mueble
class Mueble:
    def __init__(self, precio, material):
        self._precio = precio
        self._material = material



# Metodos
    def calcula_precio(self):
        return self._precio

    
    
    def __str__(self): 
        return f"{self._precio}"
    

    


class Silla(Mueble):
     def __init__(self, material, precio,num_patas):
        super().__init__(material, precio)
        self._num_patas = num_patas

        
        self._descuento = 0
        self._precio_final = 0

     
     
         
     def aplicar_descuento(self, descuento):
        
        if descuento > 0:
            self._precio_final = self._precio - descuento
        else: 
            self._precio_final = self._precio


     def __str__(self):
        return super().__str__() + f"""
        ---------SILLA-------
        Material: {self._material}
        Precio: {self._precio_final}
        Numero de patas: {self._num_patas}"""
        
        
            

class Mesa(Mueble):
     def __init__(self, precio, material, ancho,largo):
        super().__init__(precio, material)
        self._ancho = ancho
        self._largo = largo

     def __str__(self):
        return f"""
        ---------MESA-------
        Material: {self._material}
        Precio: {self._precio}
        Ancho: {self._ancho}CM x Largo: {self._largo}CM """


class Armario(Mueble):
     def __init__(self, precio, material, num_puertas):
        super().__init__(precio, material)
        self._num_puertas = num_puertas

     def __str__(self):
         return f"""
         -------Armario---------
         Material: {self._material} 
         Precio: {self._precio}
         Numero de puertas: {self._num_puertas} """
     

silla1 = Silla(5000,"Pino", 2)
silla2 = Silla(10000,"Pino", 3)

print(silla1)
print(silla2)

sillas = [silla1  , silla2]
precio_total = sum(Mueble.calcula_precio() for Mueble in sillas)
print(f"El precio total de las sillas:$ {precio_total}")
silla1.aplicar_descuento(2000)

mesa = Mesa(10000,"Pino", 2, 3)
armario = Armario(10000,"Pino", 2)




print(mesa)
print(armario)


# muebles = [silla2, mesa, armario]
# precio_total = sum(Mueble.calcula_precio_final() for Mueble in muebles)



    