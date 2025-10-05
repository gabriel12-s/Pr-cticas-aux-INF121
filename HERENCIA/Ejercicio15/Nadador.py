class Nadador:
    def __init__(self, estiloNatacion):
        self.estiloNatacion = estiloNatacion
    
    def nadar(self):
        print(f"Nadando estilo {self.estiloNatacion}")

class Ciclista:
    def __init__(self, tipoBicicleta):
        self.tipoBicicleta = tipoBicicleta
    
    def pedalear(self):
        print(f"Pedaleando en bicicleta tipo {self.tipoBicicleta}")

class Corredor:
    def __init__(self, distanciaPreferida):
        self.distanciaPreferida = distanciaPreferida
    
    def correr(self):
        print(f"Corriendo una distancia de {self.distanciaPreferida} km")

class Triatleta(Nadador, Ciclista, Corredor):
    def __init__(self, nombre, edad, estiloNatacion, tipoBicicleta, distanciaPreferida):

        Nadador.__init__(self, estiloNatacion)
        Ciclista.__init__(self, tipoBicicleta)
        Corredor.__init__(self, distanciaPreferida)
        
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_info(self):
        print("=" * 40)
        print(f"TRIATLETA: {self.nombre}")
        print(f"Edad: {self.edad} an~os")
        print(f"Estilo de natacion: {self.estiloNatacion}")
        print(f"Tipo de bicicleta: {self.tipoBicicleta}")
        print(f"Distancia preferida en carrera: {self.distanciaPreferida} km")
        print("=" * 40)
    
    def entrenar(self):
        print(f"\n{self.nombre} esta entrenando:")
        print("-" * 20)
        self.nadar()
        self.pedalear()
        self.correr()
        print("Entrenamiento completado!")
print("SISTEMA DE TRIATLETAS ")
print("\n CREANDO TRIATLETA ")

triatleta1 = Triatleta(
    nombre="Carlos Rodriguez",
    edad=28,
    estiloNatacion="Crol",
    tipoBicicleta="Carretera",
    distanciaPreferida=10.5
)

print("\nINFORMACION DEL TRIATLETA ")
triatleta1.mostrar_info()

print("\n ACCIONES DEL TRIATLETA ")

print("\n1. Accion individual de natacion:")
triatleta1.nadar()

print("\n2. Accion individual de ciclismo:")
triatleta1.pedalear()

print("\n3. Accion individual de carrera:")
triatleta1.correr()

print("\n ENTRENAMIENTO COMPLETO ")
triatleta1.entrenar()

print("\n MAS TRIATLETAS ")

triatleta2 = Triatleta(
    nombre="Ana Martinez",
    edad=25,
    estiloNatacion="Mariposa",
    tipoBicicleta="Montana",
    distanciaPreferida=8.0
)

triatleta3 = Triatleta(
    nombre="Luis Garcia",
    edad=32,
    estiloNatacion="Espalda",
    tipoBicicleta="Triatlon",
    distanciaPreferida=15.0
)

triatletas = [triatleta1, triatleta2, triatleta3]

print("\n TODOS LOS TRIATLETAS ")
for i, triatleta in enumerate(triatletas, 1):
    print(f"\nTriatleta {i}:")
    triatleta.mostrar_info()

print("\n ENTRENAMIENTOS GRUPALES ")
for triatleta in triatletas:
    triatleta.entrenar()

print("\n VERIFICACION DE HERENCIA ")
print(f"Triatleta1 es Nadador? {isinstance(triatleta1, Nadador)}")
print(f"Triatleta1 es Ciclista? {isinstance(triatleta1, Ciclista)}")
print(f"Triatleta1 es Corredor? {isinstance(triatleta1, Corredor)}")
print(f"Triatleta1 es Triatleta? {isinstance(triatleta1, Triatleta)}")

print("\n METODOS ESPECIFICOS POR DEPORTE ")

print("\nNadadores:")
for triatleta in triatletas:
    print(f"{triatleta.nombre}: ", end="")
    triatleta.nadar()

print("\nCiclistas:")
for triatleta in triatletas:
    print(f"{triatleta.nombre}: ", end="")
    triatleta.pedalear()

print("\nCorredores:")
for triatleta in triatletas:
    print(f"{triatleta.nombre}: ", end="")
    triatleta.correr()

print("\n RESUMEN FINAL ")
print("Triatletas registrados:")
for triatleta in triatletas:
    print(f"- {triatleta.nombre} ({triatleta.edad} an~os)")
    print(f"  Natacion: {triatleta.estiloNatacion}")
    print(f"  Ciclismo: {triatleta.tipoBicicleta}")
    print(f"  Carrera: {triatleta.distanciaPreferida} km")
    print()