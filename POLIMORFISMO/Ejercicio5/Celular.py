class Celular:
    def __init__(self, nroTel, dueño, espacio, ram, nroApp):
        self.nroTel = nroTel
        self.dueño = dueño
        self.espacio = espacio  # en GB
        self.ram = ram  # en GB
        self.nroApp = nroApp
    
    def __iadd__(self, incremento):
        """Sobrecarga del operador += para aumentar nroApp en 10"""
        if incremento == 1:  
            self.nroApp += 10
        else:
            self.nroApp += incremento
        return self
    
    def __isub__(self, decremento):
        """Sobrecarga del operador -= para disminuir espacio en 5 GB"""
        if decremento == 1: 
            self.espacio -= 5
        else:
            self.espacio -= decremento
        return self
    
    def mostrar_datos(self):
        """Muestra todos los datos del celular"""
        print(f" Numero: {self.nroTel}")
        print(f" Dueno: {self.dueño}")
        print(f" Espacio: {self.espacio} GB")
        print(f" RAM: {self.ram} GB")
        print(f" Numero de Apps: {self.nroApp}")
        print("-" * 30)
    
    def __str__(self):
        return f"Celular de {self.dueño} - Tel: {self.nroTel}"

print(" SISTEMA DE CELULARES ")
print("\n Creando celulares ")
celular1 = Celular("77712345", "Juan Perez", 64, 4, 15)
celular2 = Celular("77767890", "Maria Garcia", 128, 6, 25)

print("\n DATOS ANTES DE LOS OPERADORES ")
print("Celular 1:")
celular1.mostrar_datos()

print("Celular 2:")
celular2.mostrar_datos()

print("\n APLICANDO OPERADORES ")

print("Aplicando ++ a celular1 (aumenta apps en 10):")
celular1 += 1 
print("Aplicando -- a celular2 (disminuye espacio en 5 GB):")
celular2 -= 1  


print("\nAplicando mas operaciones:")
celular1 += 1  
celular2 -= 1  

print("\nAplicando incremento personalizado:")
celular1 += 5  

print("Aplicando decremento personalizado:")
celular2 -= 3 

print("\n DATOS DESPUES DE LOS OPERADORES ")
print("Celular 1:")
celular1.mostrar_datos()

print("Celular 2:")
celular2.mostrar_datos()

print("\n DEMOSTRACIoN ADICIONAL ")
celular3 = Celular("77711111", "Carlos Lopez", 256, 8, 10)

print("Celular 3 antes:")
celular3.mostrar_datos()

celular3 += 1  # ++
celular3 += 1  # ++
celular3 -= 1  # --
celular3 -= 1  # --

print("Celular 3 despues de ++, ++, --, --:")
celular3.mostrar_datos()

print("\n RESUMEN FINAL ")
print(f"Celular 1: {celular1.dueño} -> Apps: {celular1.nroApp}, Espacio: {celular1.espacio}GB")
print(f"Celular 2: {celular2.dueño} -> Apps: {celular2.nroApp}, Espacio: {celular2.espacio}GB")
print(f"Celular 3: {celular3.dueño} -> Apps: {celular3.nroApp}, Espacio: {celular3.espacio}GB")