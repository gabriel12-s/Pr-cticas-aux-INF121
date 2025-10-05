class MP4:
    def __init__(self, marca, capacidadGb):
        self.marca = marca
        self.capacidadGb = capacidadGb
        self.numCanciones = 0
        self.numVideos = 0
        self.canciones = [] 
        self.videos = []     
        
        self.espacioUsadoGb = 0
        
        print(f" MP4 '{marca}' creado - Capacidad: {capacidadGb} GB")
    
    def borrar_cancion(self, *args):
        """Sobrecarga para borrar por nombre, artista, o nombre y artista"""
        if len(args) == 1:
            nombre = args[0]
            for i, cancion in enumerate(self.canciones):
                if cancion[0] == nombre:
                    peso_kb = cancion[2]
                    self.canciones.pop(i)
                    self.numCanciones -= 1
                    self.espacioUsadoGb -= peso_kb / 1024 / 1024  
                    print(f" Cancion '{nombre}' borrada")
                    return True
            print(f"Cancion '{nombre}' no encontrada")
            return False
            
        elif len(args) == 2:
            if isinstance(args[1], str):
                nombre, artista = args
                for i, cancion in enumerate(self.canciones):
                    if cancion[0] == nombre and cancion[1] == artista:
                        peso_kb = cancion[2]
                        self.canciones.pop(i)
                        self.numCanciones -= 1
                        self.espacioUsadoGb -= peso_kb / 1024 / 1024
                        print(f" Cancion '{nombre}' de {artista} borrada")
                        return True
                print(f" Cancion '{nombre}' de {artista} no encontrada")
                return False
            else:
                artista = args[0]
                canciones_borradas = 0
                for i in range(len(self.canciones)-1, -1, -1):
                    if self.canciones[i][1] == artista:
                        peso_kb = self.canciones[i][2]
                        self.canciones.pop(i)
                        self.numCanciones -= 1
                        self.espacioUsadoGb -= peso_kb / 1024 / 1024
                        canciones_borradas += 1
                if canciones_borradas > 0:
                    print(f" {canciones_borradas} canciones de {artista} borradas")
                    return True
                else:
                    print(f" No se encontraron canciones de {artista}")
                    return False
    
    def __add__(self, cancion):
        """Sobrecarga + para anadir cancion si no existe y hay espacio"""
        nombre, artista, pesoKb = cancion
        
        for cancion_existente in self.canciones:
            if cancion_existente[0] == nombre and cancion_existente[1] == artista:
                print(f" La cancion '{nombre}' de {artista} ya existe")
                return self
        
        espacio_necesario = pesoKb / 1024 / 1024  # KB a GB
        if self.espacioUsadoGb + espacio_necesario <= self.capacidadGb:
            self.canciones.append([nombre, artista, pesoKb])
            self.numCanciones += 1
            self.espacioUsadoGb += espacio_necesario
            print(f" Cancion '{nombre}' de {artista} anadida")
        else:
            print(f" No hay espacio para anadir '{nombre}'")
        
        return self
    
    def __sub__(self, video):
        """Sobrecarga - para anadir video si no existe y hay espacio"""
        nombre, artista, pesoMb = video
        
        for video_existente in self.videos:
            if video_existente[0] == nombre and video_existente[1] == artista:
                print(f" El video '{nombre}' de {artista} ya existe")
                return self
        
        espacio_necesario = pesoMb / 1024  
        if self.espacioUsadoGb + espacio_necesario <= self.capacidadGb:
            self.videos.append([nombre, artista, pesoMb])
            self.numVideos += 1
            self.espacioUsadoGb += espacio_necesario
            print(f" Video '{nombre}' de {artista} anadido")
        else:
            print(f" No hay espacio para anadir '{nombre}'")
        
        return self
    
    def mostrar_capacidad(self):
        capacidad_disponible = self.capacidadGb - self.espacioUsadoGb
        print(f"\n CAPACIDAD DEL MP4 '{self.marca}':")
        print(f"   Capacidad total: {self.capacidadGb:.2f} GB")
        print(f"   Espacio usado: {self.espacioUsadoGb:.2f} GB")
        print(f"   Espacio disponible: {capacidad_disponible:.2f} GB")
        print(f"   Canciones: {self.numCanciones}")
        print(f"   Videos: {self.numVideos}")
    
    def mostrar_info(self):
        print(f"\n INFORMACION DEL MP4 '{self.marca}':")
        
        print("\n    CANCIONES:")
        if self.numCanciones == 0:
            print("      No hay canciones")
        else:
            for i, cancion in enumerate(self.canciones, 1):
                print(f"      {i}. '{cancion[0]}' - {cancion[1]} ({cancion[2]} KB)")
        
        print("\n    VIDEOS:")
        if self.numVideos == 0:
            print("      No hay videos")
        else:
            for i, video in enumerate(self.videos, 1):
                print(f"      {i}. '{video[0]}' - {video[1]} ({video[2]} MB)")
        
        self.mostrar_capacidad()

print(" SISTEMA REPRODUCTOR MP4 ")

mi_mp4 = MP4("Sony Walkman", 2.0) 

print("\n--- Agregando contenido inicial ---")

mi_mp4 + ["Back To Black", "Amy Winehouse", 100]
mi_mp4 + ["Lost On You", "LP", 150]
mi_mp4 + ["Rolling in the Deep", "Adele", 120]

mi_mp4 - ["Heathens", "twenty one pilots", 50]
mi_mp4 - ["Harmonica Andromeda", "KSHMR", 70]
mi_mp4 - ["Without Me", "Halsey", 30]

mi_mp4.mostrar_info()

print("\n PROBANDO BORRAR CANCIONES ")

print("\n1. Borrando por nombre 'Lost On You':")
mi_mp4.borrar_cancion("Lost On You")

print("\n2. Borrando todas las canciones de 'Amy Winehouse':")
mi_mp4.borrar_cancion("Amy Winehouse")

print("\n3. Borrando por nombre y artista:")
mi_mp4 + ["Shape of You", "Ed Sheeran", 110] 
mi_mp4.borrar_cancion("Shape of You", "Ed Sheeran")

mi_mp4.mostrar_info()

print("\n INTENTANDO AGREGAR CONTENIDO EXISTENTE ")
mi_mp4 + ["Rolling in the Deep", "Adele", 120]  
mi_mp4 - ["Heathens", "twenty one pilots", 50]   

print("\n PROBANDO LIMITE DE CAPACIDAD ")
mi_mp4 - ["Video Gigante", "Artista X", 3000]  


print("\n ESTADO FINAL ")
mi_mp4.mostrar_info()

print("\n AGREGANDO MAS CONTENIDO ")
mi_mp4 + ["Blinding Lights", "The Weeknd", 95]
mi_mp4 + ["Dance Monkey", "Tones and I", 105]
mi_mp4 - ["Bad Guy", "Billie Eilish", 45]


mi_mp4.mostrar_info()