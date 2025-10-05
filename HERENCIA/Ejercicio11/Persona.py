class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre} {self.apellido}")

class Empleado:
    def __init__(self, sueldo, departamento):
        self.sueldo = sueldo
        self.departamento = departamento
    
    def mostrar_info(self):
        print(f"Sueldo: ${self.sueldo}")
        print(f"Departamento: {self.departamento}")

class Policia:
    def __init__(self, grado, placa):
        self.grado = grado
        self.placa = placa
    
    def mostrar_info(self):
        print(f"Grado: {self.grado}")
        print(f"Placa: {self.placa}")

class JefePolicia(Persona, Empleado, Policia):
    def __init__(self, nombre, apellido, sueldo, departamento, grado, placa, distrito, años_mando):

        Persona.__init__(self, nombre, apellido)
        Empleado.__init__(self, sueldo, departamento)
        Policia.__init__(self, grado, placa)
        
        self.distrito = distrito
        self.años_mando = años_mando
    
    def mostrar_info(self):
        print("=" * 40)
        Persona.mostrar_info(self)
        Empleado.mostrar_info(self)
        Policia.mostrar_info(self)
        print(f"Distrito: {self.distrito}")
        print(f"An~os de mando: {self.años_mando}")
        print("=" * 40)
    
    def get_sueldo(self):
        return self.sueldo
    
    def get_grado(self):
        return self.grado

def mostrar_mayor_sueldo(jefe1, jefe2):
    print("\n COMPARACION DE SUELDOS ")
    print(f"{jefe1.nombre}: ${jefe1.get_sueldo()}")
    print(f"{jefe2.nombre}: ${jefe2.get_sueldo()}")
    
    if jefe1.get_sueldo() > jefe2.get_sueldo():
        print(f"Mayor sueldo: {jefe1.nombre} {jefe1.apellido}")
    elif jefe2.get_sueldo() > jefe1.get_sueldo():
        print(f"Mayor sueldo: {jefe2.nombre} {jefe2.apellido}")
    else:
        print("Ambos tienen el mismo sueldo")

def comparar_grado(jefe1, jefe2):
    print("\n COMPARACION DE GRADOS ")
    print(f"{jefe1.nombre}: {jefe1.get_grado()}")
    print(f"{jefe2.nombre}: {jefe2.get_grado()}")
    
    if jefe1.get_grado() == jefe2.get_grado():
        print("Ambos tienen el mismo grado")
        return True
    else:
        print("Tienen grados diferentes")
        return False

print(" SISTEMA DE JEFES DE POLICIA ")

print("\n CREANDO JEFES DE POLICIA ")


print("\nJefe de Policia 1:")
jefe1 = JefePolicia(
    nombre="Carlos",
    apellido="Rodriguez",
    sueldo=75000,
    departamento="Narcoticos",
    grado="Coronel",
    placa="JEF-001",
    distrito="Centro",
    años_mando=8
)

print("\nJefe de Policia 2:")
jefe2 = JefePolicia(
    nombre="Ana",
    apellido="Martinez",
    sueldo=82000,
    departamento="Homicidios",
    grado="Coronel",
    placa="JEF-002",
    distrito="Norte",
    años_mando=12
)

print("\n DATOS DE LOS JEFES DE POLICIA ")

print("\nJEFE 1:")
jefe1.mostrar_info()

print("\nJEFE 2:")
jefe2.mostrar_info()

mostrar_mayor_sueldo(jefe1, jefe2)


mismo_grado = comparar_grado(jefe1, jefe2)

print("\n MAS JEFES DE POLICIA ")

jefe3 = JefePolicia(
    nombre="Luis",
    apellido="Garcia",
    sueldo=68000,
    departamento="Transito",
    grado="Teniente Coronel",
    placa="JEF-003",
    distrito="Sur",
    años_mando=5
)

jefe4 = JefePolicia(
    nombre="Maria",
    apellido="Lopez",
    sueldo=79000,
    departamento="Investigacion",
    grado="Coronel",
    placa="JEF-004",
    distrito="Este",
    años_mando=10
)

jefes = [jefe1, jefe2, jefe3, jefe4]

print("\n TODOS LOS JEFES DE POLICIA ")
for i, jefe in enumerate(jefes, 1):
    print(f"\nJefe {i}:")
    jefe.mostrar_info()

print("\nCOMPARACIONES ADICIONALES ")

print("\nCOMPARACION DE SUELDOS ENTRE TODOS:")
for i in range(len(jefes)):
    for j in range(i + 1, len(jefes)):
        print(f"\n{jefes[i].nombre} vs {jefes[j].nombre}:")
        mostrar_mayor_sueldo(jefes[i], jefes[j])

print("\nCOMPARACION DE GRADOS ENTRE TODOS:")
for i in range(len(jefes)):
    for j in range(i + 1, len(jefes)):
        print(f"\n{jefes[i].nombre} vs {jefes[j].nombre}:")
        comparar_grado(jefes[i], jefes[j])

print("\n RESUMEN FINAL ")
print("Jefes de Policia creados:")
for jefe in jefes:
    print(f"- {jefe.nombre} {jefe.apellido}: ${jefe.get_sueldo()} - {jefe.get_grado()}")