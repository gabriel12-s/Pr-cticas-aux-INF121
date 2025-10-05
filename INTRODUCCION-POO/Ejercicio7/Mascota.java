public class Mascota {
    
    String nombre;
    String tipo;
    int energia;
    
    
    public Mascota(String nombre, String tipo) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.energia = 50; 
    }
    
   
    public void alimentar() {
        energia = energia + 20;
        if (energia > 100) {
            energia = 100;
        }
        System.out.println(nombre + " fue alimentado. Energia: " + energia);
    }
    
    
    public void jugar() {
        if (energia >= 15) {
            energia = energia - 15;
            System.out.println(nombre + " jugo. Energia: " + energia);
        } else {
            System.out.println(nombre + " esta muy cansado para jugar. Energia: " + energia);
        }
    }
    
    public void mostrarEnergia() {
        System.out.println(nombre + " (" + tipo + ") - Energia: " + energia);
    }
    
    public static void main(String[] args) {
        System.out.println(" SISTEMA DE MASCOTAS ");
        
        
        System.out.println("\n Creando mascotas ");
        Mascota mascota1 = new Mascota("Firulais", "Perro");
        Mascota mascota2 = new Mascota("Mishi", "Gato");
        
    
        System.out.println("\n Energia inicial ");
        mascota1.mostrarEnergia();
        mascota2.mostrarEnergia();
        
        System.out.println("\n Alimentando mascotas ");
        mascota1.alimentar();
        mascota2.alimentar();
        
        System.out.println("\n Jugando con mascotas ");
        mascota1.jugar();
        mascota2.jugar();
        
        
        System.out.println("\n Alimentando otra vez ");
        mascota1.alimentar();
        mascota2.alimentar();
        
        System.out.println("\n Jugando mucho ");
        mascota1.jugar();
        mascota2.jugar();
        mascota1.jugar();
        mascota2.jugar();
        mascota1.jugar(); 
        mascota2.jugar(); 
        
        System.out.println("\n Energia final ");
        mascota1.mostrarEnergia();
        mascota2.mostrarEnergia();
    }
}
