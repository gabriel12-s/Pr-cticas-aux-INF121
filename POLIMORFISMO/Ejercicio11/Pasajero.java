
class Pasajero {
    String nombre;
    int edad;
    String genero;
    int nroHabitacion;
    double costoPasaje;
    
    public Pasajero(String nombre, int edad, String genero, int nroHabitacion, double costoPasaje) {
        this.nombre = nombre;
        this.edad = edad;
        this.genero = genero;
        this.nroHabitacion = nroHabitacion;
        this.costoPasaje = costoPasaje;
    }
    
    public void leer() {
        System.out.println("Leyendo pasajero: " + nombre + ", Edad: " + edad + ", Genero: " + genero);
    }
    
    public void mostrar() {
        System.out.println("PASAJERO: " + nombre);
        System.out.println("  Edad: " + edad);
        System.out.println("  Genero: " + genero);
        System.out.println("  Habitacion: " + nroHabitacion);
        System.out.println("  Costo pasaje: $" + costoPasaje);
        System.out.println("  --------------------");
    }
    
    public String toString() {
        return nombre + " (Habitacion " + nroHabitacion + ")";
    }
}