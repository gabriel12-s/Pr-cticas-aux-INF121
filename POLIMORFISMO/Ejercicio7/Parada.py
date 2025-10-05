class Parada:
    def __init__(self, nombreP=None):
        if nombreP is None:
            self.nombreP = "Parada Sin Nombre"
        else:
            self.nombreP = nombreP

        self.admins = [""] * 10  
        self.autos = [["", "", ""] for _ in range(10)] 

        self.nroAdmins = 0
        self.nroAutos = 0
        
        print(f"Parada '{self.nombreP}' creada")
    
    def mostrar(self):
        print(f"\n PARADA: {self.nombreP} ")
        
        print("\n ADMINISTRADORES:")
        if self.nroAdmins == 0:
            print("  No hay administradores registrados")
        else:
            for i in range(self.nroAdmins):
                print(f"  {i+1}. {self.admins[i]}")
        
        print("\n AUTOS REGISTRADOS:")
        if self.nroAutos == 0:
            print("  No hay autos registrados")
        else:
            for i in range(self.nroAutos):
                print(f"  {i+1}. Modelo: {self.autos[i][0]}, Conductor: {self.autos[i][1]}, Placa: {self.autos[i][2]}")
        
        print("=" * 40)
    
    def adicionar(self, admin):
        if self.nroAdmins < 10:
            self.admins[self.nroAdmins] = admin
            self.nroAdmins += 1
            print(f" Administrador '{admin}' agregado")
            return True
        else:
            print(" No se pueden agregar mas administradores (llmite: 10)")
            return False
    
    def adicionar(self, modelo, conductor, placa):
        if self.nroAutos < 10:
            self.autos[self.nroAutos][0] = modelo
            self.autos[self.nroAutos][1] = conductor
            self.autos[self.nroAutos][2] = placa
            self.nroAutos += 1
            print(f" Auto '{modelo}' agregado - Conductor: {conductor}, Placa: {placa}")
            return True
        else:
            print(" No se pueden agregar mas autos (limite: 10)")
            return False

print(" SISTEMA DE PARADAS ")

print("\n Creando paradas ")

parada1 = Parada()

parada2 = Parada("Parada Central")
parada3 = Parada("Parada Norte")

print("\n Estado inicial de las paradas ")
parada1.mostrar()
parada2.mostrar()
parada3.mostrar()

print("\n Agregando administradores ")
parada1.adicionar("Juan Perez")
parada1.adicionar("Maria Garcia")

parada2.adicionar("Carlos Lopez")
parada2.adicionar("Ana Martinez")
parada2.adicionar("Pedro Rodriguez")

parada3.adicionar("Lucia Fernandez")

print("\n Agregando autos ")
parada1.adicionar("Toyota Corolla", "Roberto Silva", "ABC-123")
parada1.adicionar("Honda Civic", "Laura Mendoza", "XYZ-789")

parada2.adicionar("Nissan Sentra", "Miguel Torres", "DEF-456")
parada2.adicionar("Ford Focus", "Sofia Castro", "GHI-789")
parada2.adicionar("Chevrolet Spark", "Diego Rojas", "JKL-012")

parada3.adicionar("Kia Rio", "Elena Vargas", "MNO-345")
parada3.adicionar("Hyundai Accent", "Jorge Herrera", "PQR-678")

print("\n Estado despues de agregar datos ")
parada1.mostrar()
parada2.mostrar()
parada3.mostrar()

print("\n Probando limites ")
print("Intentando agregar mas de 10 administradores:")
for i in range(12):
    parada1.adicionar(f"Admin{i}")

print("\nIntentando agregar mas de 10 autos:")
for i in range(12):
    parada2.adicionar(f"Modelo{i}", f"Conductor{i}", f"PLACA-{i}")

print("\n Estado final ")
parada1.mostrar()
parada2.mostrar()
parada3.mostrar()

print("\n RESUMEN ")
print(f"Parada 1: {parada1.nroAdmins} admins, {parada1.nroAutos} autos")
print(f"Parada 2: {parada2.nroAdmins} admins, {parada2.nroAutos} autos")
print(f"Parada 3: {parada3.nroAdmins} admins, {parada3.nroAutos} autos")