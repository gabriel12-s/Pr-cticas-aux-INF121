public class Cafeteria {
    public static void main(String[] args) {
        System.out.println(" SISTEMA DE CAFETERIA ");
        
        System.out.println("\n Creando objetos ");
        
        Producto cafe = new Producto("Cafe Americano", 12.50);
        Producto pastel = new Producto("Pastel de Chocolate", 18.00);
        
        Pedido pedido1 = new Pedido(101);
        Pedido pedido2 = new Pedido(102);
        
        System.out.println("\n Informacion inicial ");
        cafe.mostrarInfo();
        pastel.mostrarInfo();
        pedido1.mostrarInfo();
        pedido2.mostrarInfo();
        
        System.out.println("\n Modificando valores ");
        cafe.setPrecio(13.00);
        pastel.setNombre("Pastel Especial de Chocolate");
        
        pedido1.setEstado("preparado");
        pedido2.setEstado("entregado");
        
        System.out.println("\n Informacion final ");
        cafe.mostrarInfo();
        pastel.mostrarInfo();
        pedido1.mostrarInfo();
        pedido2.mostrarInfo();
        
        System.out.println("\n--- Usando getters ---");
        System.out.println("Nombre del cafe: " + cafe.getNombre());
        System.out.println("Precio del pastel: " + pastel.getPrecio() + " bs");
        System.out.println("Numero del pedido 1: " + pedido1.getNumero());
        System.out.println("Estado del pedido 2: " + pedido2.getEstado());
        
        System.out.println("\n Fin del programa ");
        
        System.gc();
    }
}
