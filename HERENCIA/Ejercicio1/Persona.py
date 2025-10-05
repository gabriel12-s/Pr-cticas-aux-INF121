class Persona:
    def __init__(self, nombre, apellido, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
    
    def mostrar_info(self):
        print(f"Persona: {self.nombre} {self.apellido}")
        print(f"CI: {self.ci}")

class Cliente(Persona):
    def __init__(self, nombre, apellido, ci, mc_compra, id_cliente):
        super().__init__(nombre, apellido, ci)
        self.mc_compra = mc_compra
        self.id_cliente = id_cliente
    
    def mostrar_info(self):
        print(f"Cliente: {self.nombre} {self.apellido}")
        print(f"ID Cliente: {self.id_cliente}")
        print(f"MC Compra: {self.mc_compra}")
        print(f"CI: {self.ci}")

class Jefe(Persona):
    def __init__(self, nombre, apellido, ci, sucursal, tipo):
        super().__init__(nombre, apellido, ci)
        self.sucursal = sucursal
        self.tipo = tipo
    
    def mostrar_info(self):
        print(f"Jefe: {self.nombre} {self.apellido}")
        print(f"Sucursal: {self.sucursal}")
        print(f"Tipo: {self.tipo}")
        print(f"CI: {self.ci}")

print(" SISTEMA DE PERSONAS ")

print("\n--- Creando objetos ---")

persona1 = Persona("Juan", "Perez", "1234567")
cliente1 = Cliente("Maria", "Gonzalez", "7654321", "Electronicos", "CLI001")
jefe1 = Jefe("Carlos", "Lopez", "1111111", "Sucursal Central", "Gerente")

print("\n Informacion de los objetos ")

print("\nPersona:")
persona1.mostrar_info()

print("\nCliente:")
cliente1.mostrar_info()

print("\nJefe:")
jefe1.mostrar_info()

print("\n Probando herencia ")
print(f"Cliente es una Persona: {isinstance(cliente1, Persona)}")
print(f"Jefe es una Persona: {isinstance(jefe1, Persona)}")

print("\n Lista de todas las personas ")
personas = [persona1, cliente1, jefe1]

for persona in personas:
    persona.mostrar_info()
    print("---")