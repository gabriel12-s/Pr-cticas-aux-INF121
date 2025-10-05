
public class Pedido {
    private int numero;
    private String estado;

    public Pedido(int numero) {
        this.numero = numero;
        this.estado = "registrado";
        System.out.println("Pedido #" + numero + " creado");
    }
    
    protected void finalize() {
        System.out.println("Pedido #" + numero + " eliminado");
    }
    public int getNumero() {
        return numero;
    }
    public void setNumero(int numero) {
        this.numero = numero;
    }
    public String getEstado() {
        return estado;
    }
    public void setEstado(String estado) {
        this.estado = estado;
        System.out.println("Pedido #" + numero + " cambio a estado: " + estado);
    }
    public void mostrarInfo() {
        System.out.println("Pedido #" + numero + " - Estado: " + estado);
    }
}
