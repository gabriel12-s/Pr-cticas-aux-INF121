class Ordenador:
    def __init__(self, codigo_serial, numero, ram, procesador, estado=True):
        self.codigo_serial = codigo_serial
        self.numero = numero
        self.ram = ram  
        self.procesador = procesador
        self.estado = estado 
    
    def mostrar_info(self):
        estado_str = "ACTIVO" if self.estado else "INACTIVO"
        print(f"  Ordenador {self.numero} - Serial: {self.codigo_serial}")
        print(f"     RAM: {self.ram} GB | Procesador: {self.procesador} | Estado: {estado_str}")

class Laboratorio:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.cantidad_ordenadores = 0
        self.ordenadores = []
        print(f"Laboratorio '{nombre}' creado - Capacidad: {capacidad} ordenadores")
    
    def agregar_ordenador(self, ordenador):
        if self.cantidad_ordenadores < self.capacidad:
            self.ordenadores.append(ordenador)
            self.cantidad_ordenadores += 1
            print(f"Ordenador {ordenador.numero} agregado a {self.nombre}")
            return True
        else:
            print(f"No hay espacio en {self.nombre} para mas ordenadores")
            return False
    
    def informacion(self, *args):
        if len(args) == 0:
            print(f"INFORMACION GENERAL - {self.nombre}:")
            print(f"   Capacidad: {self.capacidad} ordenadores")
            print(f"   Ordenadores actuales: {self.cantidad_ordenadores}")
            print(f"   Espacio disponible: {self.capacidad - self.cantidad_ordenadores}")
            
            if self.cantidad_ordenadores > 0:
                print("   Ordenadores en el laboratorio:")
                for ordenador in self.ordenadores:
                    ordenador.mostrar_info()
            else:
                print("   No hay ordenadores en este laboratorio")
                
        elif len(args) == 1:
            parametro = args[0]
            
            if isinstance(parametro, bool):
                estado_str = "ACTIVOS" if parametro else "INACTIVOS"
                print(f"ORDENADORES {estado_str} - {self.nombre}:")
                encontrados = False
                for ordenador in self.ordenadores:
                    if ordenador.estado == parametro:
                        ordenador.mostrar_info()
                        encontrados = True
                if not encontrados:
                    print(f"   No hay ordenadores {estado_str.lower()}")
                    
            elif isinstance(parametro, str):
                if parametro == self.nombre:
                    self.informacion()
                else:
                    print(f"   Este es el laboratorio {self.nombre}, no {parametro}")
                    
            elif isinstance(parametro, int):
                print(f"ORDENADORES CON MAS DE {parametro} GB RAM - {self.nombre}:")
                encontrados = False
                for ordenador in self.ordenadores:
                    if ordenador.ram > parametro:
                        ordenador.mostrar_info()
                        encontrados = True
                if not encontrados:
                    print(f"   No hay ordenadores con mas de {parametro} GB RAM")
    
    def trasladar_ordenadores(self, laboratorio_destino, cantidad):
        print(f"TRASLADANDO {cantidad} ORDENADORES:")
        print(f"   De: {self.nombre}")
        print(f"   A: {laboratorio_destino.nombre}")
        
        if cantidad > self.cantidad_ordenadores:
            print(f"No hay suficientes ordenadores en {self.nombre}")
            return False
        
        if cantidad > (laboratorio_destino.capacidad - laboratorio_destino.cantidad_ordenadores):
            print(f"No hay espacio suficiente en {laboratorio_destino.nombre}")
            return False
        
        print("ESTADO ANTES DEL TRASLADO:")
        print(f"   {self.nombre}: {self.cantidad_ordenadores} ordenadores")
        print(f"   {laboratorio_destino.nombre}: {laboratorio_destino.cantidad_ordenadores} ordenadores")
        
        ordenadores_trasladados = 0
        for i in range(cantidad):
            if self.ordenadores:
                ordenador = self.ordenadores.pop(0)  
                laboratorio_destino.agregar_ordenador(ordenador)
                self.cantidad_ordenadores -= 1
                ordenadores_trasladados += 1
        
        print("ESTADO DESPUES DEL TRASLADO:")
        print(f"   {self.nombre}: {self.cantidad_ordenadores} ordenadores")
        print(f"   {laboratorio_destino.nombre}: {laboratorio_destino.cantidad_ordenadores} ordenadores")
        print(f"Se trasladaron {ordenadores_trasladados} ordenadores exitosamente")
        
        return True

print(" SISTEMA LABORATORIOS LASIN ")

print("CREANDO LABORATORIOS")
lasin1 = Laboratorio("Lasin 1", 5) 
lasin2 = Laboratorio("Lasin 2", 6)  

print("CREANDO ORDENADORES")
ordenador1 = Ordenador("LAS001", 1, 8, "Intel i5", True)
ordenador2 = Ordenador("LAS002", 2, 16, "Intel i7", True)
ordenador3 = Ordenador("LAS003", 3, 4, "Intel i3", False)
ordenador4 = Ordenador("LAS004", 4, 32, "AMD Ryzen 7", True)
ordenador5 = Ordenador("LAS005", 5, 8, "Intel i5", True)
ordenador6 = Ordenador("LAS006", 6, 16, "AMD Ryzen 5", False)

print("ASIGNANDO ORDENADORES A LABORATORIOS")
lasin1.agregar_ordenador(ordenador1)
lasin1.agregar_ordenador(ordenador2)
lasin1.agregar_ordenador(ordenador3)
lasin1.agregar_ordenador(ordenador4)

lasin2.agregar_ordenador(ordenador5)
lasin2.agregar_ordenador(ordenador6)

print("PRUEBAS DEL METODO INFORMACION")

lasin1.informacion()
lasin2.informacion()

print("MOSTRAR POR ESTADO")
lasin1.informacion(True)  
lasin1.informacion(False)  

print("MOSTRAR POR LABORATORIO")
lasin1.informacion("Lasin 1")
lasin1.informacion("Lasin 2")  

print("MOSTRAR POR RAM MINIMA")
lasin1.informacion(8)   
lasin2.informacion(10)  

print("TRASLADO DE ORDENADORES")
lasin1.trasladar_ordenadores(lasin2, 2)

print("ESTADO FINAL")
lasin1.informacion()
lasin2.informacion()

print("MAS PRUEBAS")

lasin1.trasladar_ordenadores(lasin2, 5)

print("ORDENADORES POR RAM")
lasin1.informacion(0)  
lasin2.informacion(15)  

print("Sistema de laboratorios Lasin funcionando correctamente")