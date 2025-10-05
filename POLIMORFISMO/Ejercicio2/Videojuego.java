import java.util.Scanner;
public class Videojuego {

    private String nombre;
    private String plataforma;
    private int cantidadJugadores;
    
 
    public Videojuego() {
        this.nombre = "Sin nombre";
        this.plataforma = "Sin plataforma";
        this.cantidadJugadores = 0;
    }

    public Videojuego(String nombre) {
        this.nombre = nombre;
        this.plataforma = "Multiplataforma";
        this.cantidadJugadores = 1;
    }
    
    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }
    
    
    public void agregarJugador() {
        cantidadJugadores++;
        System.out.println("Se agrego 1 jugador a " + nombre);
        System.out.println("Total jugadores: " + cantidadJugadores);
    }
    
    public void agregarJugadores(int cantidad) {
        if (cantidad > 0) {
            cantidadJugadores += cantidad;
            System.out.println("Se agregaron " + cantidad + " jugadores a " + nombre);
            System.out.println("Total jugadores: " + cantidadJugadores);
        } else {
            System.out.println("La cantidad debe ser mayor a 0");
        }
    }
    
    public void mostrarInfo() {
        System.out.println("🎮 Videojuego: " + nombre);
        System.out.println("📱 Plataforma: " + plataforma);
        System.out.println("👥 Jugadores: " + cantidadJugadores);
        System.out.println("----------------------");
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println(" SISTEMA DE VIDEOJUEGOS ");
        
        System.out.println("\n Creando videojuegos ");
        
        Videojuego juego1 = new Videojuego("Mario Kart", "Nintendo Switch", 4);
        
        Videojuego juego2 = new Videojuego("FIFA 2024");
        
        Videojuego juego3 = new Videojuego();
        juego3.nombre = "Minecraft";
        juego3.plataforma = "PC";
        juego3.cantidadJugadores = 1;

        System.out.println("\n Informacion inicial ");
        juego1.mostrarInfo();
        juego2.mostrarInfo();
        juego3.mostrarInfo();
        
        System.out.println("\n Agregando jugadores ");
        
        System.out.println("Agregando 1 jugador:");
        juego1.agregarJugador();
        juego2.agregarJugador();
        juego3.agregarJugador();
        
        System.out.println("\n Agregando multiples jugadores ");
        
        System.out.print("Cuantos jugadores agregar a " + juego1.getNombre() + "? ");
        int cantidad1 = scanner.nextInt();
        juego1.agregarJugadores(cantidad1);
        
        System.out.print("Cuantos jugadores agregar a " + juego2.getNombre() + "? ");
        int cantidad2 = scanner.nextInt();
        juego2.agregarJugadores(cantidad2);
        
        System.out.print("Cuantos jugadores agregar a " + juego3.getNombre() + "? ");
        int cantidad3 = scanner.nextInt();
        juego3.agregarJugadores(cantidad3);
        
        System.out.println("\n--- Informacion final ---");
        juego1.mostrarInfo();
        juego2.mostrarInfo();
        juego3.mostrarInfo();
        
        scanner.close();
    }
    
    public String getNombre() {
        return nombre;
    }
    
    public String getPlataforma() {
        return plataforma;
    }
    
    public int getCantidadJugadores() {
        return cantidadJugadores;
    }
}