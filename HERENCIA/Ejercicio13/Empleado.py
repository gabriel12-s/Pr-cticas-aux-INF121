class Empleado:
    def __init__(self, nombre, sueldomes):
        self.nombre = nombre
        self.sueldomes = sueldomes
    
    def mostrar_info(self):
        print(f"Empleado: {self.nombre}")
        print(f"Sueldo base: ${self.sueldomes}")
    
    def sueldo_total(self):
        return self.sueldomes

class Administrativo(Empleado):
    def __init__(self, nombre, sueldomes, cargo):
        super().__init__(nombre, sueldomes)
        self.cargo = cargo
    
    def mostrar_info(self):
        print(f"Administrativo: {self.nombre}")
        print(f"Cargo: {self.cargo}")
        print(f"Sueldo base: ${self.sueldomes}")

class Chef(Empleado):
    def __init__(self, nombre, sueldomes, tipo, sueldoHora, horaExtra):
        super().__init__(nombre, sueldomes)
        self.tipo = tipo
        self.sueldoHora = sueldoHora
        self.horaExtra = horaExtra
    
    def mostrar_info(self):
        print(f"Chef: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Sueldo base: ${self.sueldomes}")
        print(f"Sueldo por hora: ${self.sueldoHora}")
        print(f"Horas extra: {self.horaExtra}")
    
    def sueldo_total(self):
        total = self.sueldomes + (self.horaExtra * self.sueldoHora)
        return total

class Mesero(Empleado):
    def __init__(self, nombre, sueldomes, sueldoHora, horaExtra, propina):
        super().__init__(nombre, sueldomes)
        self.sueldoHora = sueldoHora
        self.horaExtra = horaExtra
        self.propina = propina
    
    def mostrar_info(self):
        print(f"Mesero: {self.nombre}")
        print(f"Sueldo base: ${self.sueldomes}")
        print(f"Sueldo por hora: ${self.sueldoHora}")
        print(f"Horas extra: {self.horaExtra}")
        print(f"Propina: ${self.propina}")
    
    def sueldo_total(self):
        total = self.sueldomes + (self.horaExtra * self.sueldoHora) + self.propina
        return total

def mostrar_empleados_sueldo_x(empleados, sueldo_x):
    print(f"\n EMPLEADOS CON SUELDO BASE ${sueldo_x} ")
    encontrados = False
    for empleado in empleados:
        if empleado.sueldomes == sueldo_x:
            empleado.mostrar_info()
            print(f"Sueldo total: ${empleado.sueldo_total()}")
            print("-" * 20)
            encontrados = True
    
    if not encontrados:
        print(f"No hay empleados con sueldo base ${sueldo_x}")

print(" RESTAURANTE RATATOUILLE ")

print("\n CREANDO EMPLEADOS ")

chef1 = Chef("Carlos Rodriguez", 3000, "Ejecutivo", 25, 10)

mesero1 = Mesero("Ana Martinez", 1500, 15, 8, 200)
mesero2 = Mesero("Luis Garcia", 1500, 15, 12, 350)

admin1 = Administrativo("Maria Lopez", 2000, "Gerente")
admin2 = Administrativo("Pedro Sanchez", 1800, "Contador")

empleados = [chef1, mesero1, mesero2, admin1, admin2]

print(f"Se crearon {len(empleados)} empleados:")

print("\n INFORMACION DE TODOS LOS EMPLEADOS ")
for empleado in empleados:
    empleado.mostrar_info()
    print(f"Sueldo total: ${empleado.sueldo_total()}")
    print("-" * 30)

print("\n BUSQUEDA POR SUELDO BASE ")

mostrar_empleados_sueldo_x(empleados, 1500)

mostrar_empleados_sueldo_x(empleados, 2000)

mostrar_empleados_sueldo_x(empleados, 2500)

print("\n SUELDOS TOTALES  ")
for empleado in empleados:
    print(f"{empleado.nombre}: ${empleado.sueldo_total()}")

print("\n COMPARACION DE SUELDOS ")
empleado_mayor_sueldo = empleados[0]
for empleado in empleados:
    if empleado.sueldo_total() > empleado_mayor_sueldo.sueldo_total():
        empleado_mayor_sueldo = empleado

print(f"Mayor sueldo total: {empleado_mayor_sueldo.nombre} - ${empleado_mayor_sueldo.sueldo_total()}")


print("\n MAS EMPLEADOS ")

chef2 = Chef("Roberto Silva", 3200, "Pastelero", 28, 15)
mesero3 = Mesero("Sofia Castro", 1600, 16, 10, 180)
admin3 = Administrativo("Laura Fernandez", 2200, "Supervisor")

nuevos_empleados = [chef2, mesero3, admin3]
todos_empleados = empleados + nuevos_empleados

print("Informacion de nuevos empleados:")
for empleado in nuevos_empleados:
    empleado.mostrar_info()
    print(f"Sueldo total: ${empleado.sueldo_total()}")
    print("-" * 30)

# Resumen final
print("\n RESUMEN FINAL ")
print("Total de empleados por tipo:")
chefs = [e for e in todos_empleados if isinstance(e, Chef)]
meseros = [e for e in todos_empleados if isinstance(e, Mesero)]
administrativos = [e for e in todos_empleados if isinstance(e, Administrativo)]

print(f"Chefs: {len(chefs)}")
print(f"Meseros: {len(meseros)}")
print(f"Administrativos: {len(administrativos)}")
print(f"Total: {len(todos_empleados)}")

print("\nSueldos totales:")
for empleado in todos_empleados:
    tipo = type(empleado).__name__
    print(f"- {empleado.nombre} ({tipo}): ${empleado.sueldo_total()}")