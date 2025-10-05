class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            total = cantidad * self.precio
            print(f"Se vendieron {cantidad} {self.nombre}")
            print(f"Total: {total} bs")
            return True
        else:
            print(f"No hay suficiente stock de {self.nombre}")
            print(f"Stock disponible: {self.stock}")
            return False
    
    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Se agregaron {cantidad} {self.nombre}")
        print(f"Nuevo stock: {self.stock}")
    
    def mostrar_info(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: {self.precio} bs")
        print(f"Stock: {self.stock}")
        print("-" * 20)


print("TIENDA DE PRODUCTOS ")

print("\n Creando productos ")
producto1 = Producto("Leche", 8.50, 10)
producto2 = Producto("Pan", 2.00, 15)
producto3 = Producto("Arroz", 12.00, 5)

print("\n Productos disponibles ")
producto1.mostrar_info()
producto2.mostrar_info()
producto3.mostrar_info()

print("\n Realizando ventas ")
producto1.vender(3)
producto2.vender(5)
producto3.vender(10) 

print("\n Estado despues de ventas ")
producto1.mostrar_info()
producto2.mostrar_info()
producto3.mostrar_info()

print("\n Reabasteciendo productos ")
producto1.reabastecer(5)
producto3.reabastecer(10)

print("\n Estado final ")
producto1.mostrar_info()
producto2.mostrar_info()
producto3.mostrar_info()