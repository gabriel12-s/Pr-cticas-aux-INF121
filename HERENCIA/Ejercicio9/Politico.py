class Politico:
    def __init__(self, profesion, añosExp):
        self.profesion = profesion
        self.añosExp = añosExp
    
    def mostrar_info(self):
        print(f"Profesion: {self.profesion}")
        print(f"An~os de experiencia: {self.añosExp}")

class Partido:
    def __init__(self, nombreP, rol):
        self.nombreP = nombreP
        self.rol = rol
    
    def mostrar_info(self):
        print(f"Partido: {self.nombreP}")
        print(f"Rol: {self.rol}")

class Presidente(Politico, Partido):
    def __init__(self, nombre, apellido, profesion, añosExp, nombreP, rol):
        Politico.__init__(self, profesion, añosExp)
        Partido.__init__(self, nombreP, rol)
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrar_info(self):
        print(f"Presidente: {self.nombre} {self.apellido}")
        Politico.mostrar_info(self)
        Partido.mostrar_info(self)
        print("-" * 30)

def buscar_presidente_por_nombre(presidentes, nombre_buscar):
    for presidente in presidentes:
        if presidente.nombre.lower() == nombre_buscar.lower():
            return presidente
    return None


print(" SISTEMA DE PRESIDENTES ")

print("\n Creando presidentes  ")

print("\nForma 1: Creacion directa")
presidente1 = Presidente("Juan", "Perez", "Abogado", 15, "Partido Liberal", "Lider")

print("Forma 2: Con variables")
nombre = "Maria"
apellido = "Garcia"
profesion = "Economista"
experiencia = 20
partido = "Partido Conservador"
rol = "Presidente"

presidente2 = Presidente(nombre, apellido, profesion, experiencia, partido, rol)

print("\n Informacion de presidentes creados ")
presidente1.mostrar_info()
presidente2.mostrar_info()

print("\n Creando vector de presidentes ")

presidente3 = Presidente("Carlos", "Lopez", "Ingeniero", 12, "Partido Verde", "Fundador")
presidente4 = Presidente("Ana", "Martinez", "Doctora", 18, "Partido Progresista", "Vicepresidente")
presidente5 = Presidente("Pedro", "Rodriguez", "Profesor", 10, "Partido Socialista", "Secretario")

presidentes = [presidente1, presidente2, presidente3, presidente4, presidente5]

print(f"Se crearon {len(presidentes)} presidentes")
print("\n Todos los presidentes ")
for i, presidente in enumerate(presidentes, 1):
    print(f"Presidente {i}: {presidente.nombre} {presidente.apellido}")

print("\n Busqueda de presidentes ")

nombre_buscar = "Maria"
presidente_encontrado = buscar_presidente_por_nombre(presidentes, nombre_buscar)

if presidente_encontrado:
    print(f"Presidente encontrado: {presidente_encontrado.nombre} {presidente_encontrado.apellido}")
    print(f"Partido politico: {presidente_encontrado.nombreP}")
    print(f"Profesión: {presidente_encontrado.profesion}")
else:
    print(f"No se encontro presidente con nombre: {nombre_buscar}")

print("\n Otra busqueda ")
nombre_buscar2 = "Carlos"
presidente_encontrado2 = buscar_presidente_por_nombre(presidentes, nombre_buscar2)

if presidente_encontrado2:
    print(f"Presidente encontrado: {presidente_encontrado2.nombre} {presidente_encontrado2.apellido}")
    print(f"Partido politico: {presidente_encontrado2.nombreP}")
    print(f"Profesion: {presidente_encontrado2.profesion}")
else:
    print(f"No se encontro presidente con nombre: {nombre_buscar2}")

print("\n Busqueda fallida ")
nombre_buscar3 = "Luis"
presidente_encontrado3 = buscar_presidente_por_nombre(presidentes, nombre_buscar3)

if presidente_encontrado3:
    print(f"Presidente encontrado: {presidente_encontrado3.nombre} {presidente_encontrado3.apellido}")
    print(f"Partido politico: {presidente_encontrado3.nombreP}")
    print(f"Profesion: {presidente_encontrado3.profesion}")
else:
    print(f"No se encontro presidente con nombre: {nombre_buscar3}")

print("\n Informacion completa de todos los presidentes ")
for presidente in presidentes:
    presidente.mostrar_info()

print("\n Resumen de presidentes ")
for i, presidente in enumerate(presidentes, 1):
    print(f"{i}. {presidente.nombre} {presidente.apellido} - {presidente.profesion} - {presidente.nombreP}")