class Persona:
    def __init__(self, nombre, paterno, materno, edad):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
    
    def mostrar(self):
        print(f"Persona: {self.nombre} {self.paterno} {self.materno}")
        print(f"Edad: {self.edad} an~os")
    
    def get_edad(self):
        return self.edad

class Docente(Persona):
    def __init__(self, nombre, paterno, materno, edad, sueldo, regProfesional):
        super().__init__(nombre, paterno, materno, edad)
        self.sueldo = sueldo
        self.regProfesional = regProfesional
    
    def mostrar(self):
        print(f"Docente: {self.nombre} {self.paterno} {self.materno}")
        print(f"Edad: {self.edad} an~os")
        print(f"Sueldo: {self.sueldo} Bs")
        print(f"Registro Profesional: {self.regProfesional}")

class Estudiante(Persona):
    def __init__(self, nombre, paterno, materno, edad, ru, matricula):
        super().__init__(nombre, paterno, materno, edad)
        self.ru = ru
        self.matricula = matricula
    
    def mostrar(self):
        print(f"Estudiante: {self.nombre} {self.paterno} {self.materno}")
        print(f"Edad: {self.edad} an~os")
        print(f"RU: {self.ru}")
        print(f"Matricula: {self.matricula} Bs")
    
    def modificar_edad(self, nueva_edad):
        print(f"Cambiando edad de {self.edad} a {nueva_edad} an~os")
        self.edad = nueva_edad

def promedio_edad_estudiantes(estudiantes):
    if not estudiantes:
        return 0
    total_edad = sum(estudiante.get_edad() for estudiante in estudiantes)
    return total_edad / len(estudiantes)

def misma_edad_estudiante_docente(estudiante, docente):
    return estudiante.get_edad() == docente.get_edad()

print(" SISTEMA DE PERSONAS ")

print("\n Creando personas ")

estudiante1 = Estudiante("Juan", "Perez", "Gomez", 20, "123456", 1500)
estudiante2 = Estudiante("Maria", "Lopez", "Rodriguez", 22, "789012", 1600)
docente1 = Docente("Carlos", "Garcia", "Mendez", 35, 5000, "DOC-001")

print("\n Informacion de las personas ")

print("\nEstudiante 1:")
estudiante1.mostrar()

print("\nEstudiante 2:")
estudiante2.mostrar()

print("\nDocente:")
docente1.mostrar()

print("\n Promedio de edad de estudiantes ")
estudiantes = [estudiante1, estudiante2]
promedio = promedio_edad_estudiantes(estudiantes)
print(f"Promedio de edad de los estudiantes: {promedio} años")

print("\n Modificando edad de estudiante ")
print("Antes de modificar:")
estudiante1.mostrar()

estudiante1.modificar_edad(21)

print("\nDespues de modificar:")
estudiante1.mostrar()


print("\n Nuevo promedio despues del cambio ")
nuevo_promedio = promedio_edad_estudiantes(estudiantes)
print(f"Nuevo promedio de edad: {nuevo_promedio} an~os")


print("\n Verificando edades iguales ")

misma_edad1 = misma_edad_estudiante_docente(estudiante1, docente1)
misma_edad2 = misma_edad_estudiante_docente(estudiante2, docente1)

print(f"Estudiante 1 tiene misma edad que docente? {misma_edad1}")
print(f"Estudiante 2 tiene misma edad que docente? {misma_edad2}")

print("\n Mas personas ")

estudiante3 = Estudiante("Ana", "Martinez", "Silva", 19, "345678", 1400)
docente2 = Docente("Laura", "Fernandez", "Castro", 22, 4500, "DOC-002")

print("\nNuevo Estudiante:")
estudiante3.mostrar()

print("\nNuevo Docente:")
docente2.mostrar()

print("\n Verificando con nuevo docente ")
misma_edad3 = misma_edad_estudiante_docente(estudiante2, docente2)
print(f"Estudiante 2 tiene misma edad que docente 2? {misma_edad3}")

print("\n Todos los estudiantes ")
todos_estudiantes = [estudiante1, estudiante2, estudiante3]
for i, estudiante in enumerate(todos_estudiantes, 1):
    print(f"Estudiante {i}: {estudiante.nombre} {estudiante.paterno} - Edad: {estudiante.edad}")

print("\n Promedio final de todos los estudiantes ")
promedio_final = promedio_edad_estudiantes(todos_estudiantes)
print(f"Promedio final de edad: {promedio_final:.2f} an~os")