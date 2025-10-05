class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.dinero = 0
        self.precio_pasaje = 1.50
    
    def subir_pasajeros(self, cantidad):

        if self.pasajeros + cantidad <= self.capacidad:
            self.pasajeros += cantidad
            print(f"Subieron {cantidad} pasajeros")
            return True
        else:
            espacio = self.capacidad - self.pasajeros
            print(f"Solo hay espacio para {espacio} pasajeros mas")
            return False
    
    def cobrar_pasaje(self):
        total = self.pasajeros * self.precio_pasaje
        self.dinero += total
        print(f"Se cobro {total} bs por {self.pasajeros} pasajeros")
    
    def asientos_disponibles(self):
        disponibles = self.capacidad - self.pasajeros
        print(f"Quedan {disponibles} asientos disponibles")
        return disponibles
    
    def mostrar_estado(self):
        print(f"Pasajeros: {self.pasajeros}")
        print(f"Dinero recaudado: {self.dinero} bs")
        print(f"Asientos libres: {self.asientos_disponibles()}")


print(" SISTEMA DE BUS ")

mi_bus = Bus(20)
print("\nEstado inicial:")
mi_bus.mostrar_estado()

print("\n Subiendo pasajeros ")
mi_bus.subir_pasajeros(5)
mi_bus.subir_pasajeros(8)
print("\n Cobrando pasaje ")
mi_bus.cobrar_pasaje()
print("\n Asientos disponibles ")
mi_bus.asientos_disponibles()
print("\n Subiendo mas pasajeros ")
mi_bus.subir_pasajeros(10)
print("\n Cobrando pasaje otra vez ")
mi_bus.cobrar_pasaje()
print("\n Estado final ")
mi_bus.mostrar_estado()