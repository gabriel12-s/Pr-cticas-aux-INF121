public class Producto {
    private String nombre;
    private double precio;

    public Producto(String nombre, double precio) {
        this.nombre = nombre;
        this.precio = precio;
        System.out.println("Producto creado: " + nombre);
    }
    
    protected void finalize() {
        System.out.println("Producto eliminado: " + nombre);
    }
   
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public double getPrecio() {
        return precio;
    }
    public void setPrecio(double precio) {
        this.precio = precio;
    }
    public void mostrarInfo() {
        System.out.println("Producto: " + nombre + " - Precio: " + precio + " bs");
    }
}


