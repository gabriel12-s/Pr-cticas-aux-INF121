
class Animal {
    protected String nombre;
    protected int edad;
    
    public Animal(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
    
    public void desplazarse() {
        System.out.println(nombre + " se esta desplazando");
    }
    
    public String getNombre() {
        return nombre;
    }
    
    public int getEdad() {
        return edad;
    }
}

class Leon extends Animal {
    public Leon(String nombre, int edad) {
        super(nombre, edad);
    }
    
    @Override
    public void desplazarse() {
        System.out.println(nombre + " el leon camina majestuosamente");
    }
}

class Pinguino extends Animal {
    public Pinguino(String nombre, int edad) {
        super(nombre, edad);
    }
    
    @Override
    public void desplazarse() {
        System.out.println(nombre + " el pinguino nada y se desliza sobre el hielo");
    }
}

class Canguro extends Animal {
    public Canguro(String nombre, int edad) {
        super(nombre, edad);
    }
    
    @Override
    public void desplazarse() {
        System.out.println(nombre + " el canguro salta con sus patas traseras");
    }
}

public class AnimalTest {
    public static void main(String[] args) {
        System.out.println(" SISTEMA DE ANIMALES ");
        
        System.out.println("\n Creando animales ");
        
        Leon leon = new Leon("Simba", 5);
        Pinguino pinguino = new Pinguino("Pingu", 3);
        Canguro canguro = new Canguro("Saltarin", 4);
        
        System.out.println("\n Arreglo de animales ");
        Animal[] animales = {leon, pinguino, canguro};
        

        System.out.println("\n Informacion de los animales ");
        for (Animal animal : animales) {
            System.out.println("Animal: " + animal.getNombre() + ", Edad: " + animal.getEdad() + " an~os");
        }
        

        System.out.println("\n Los animales se desplazan ");
        for (Animal animal : animales) {
            animal.desplazarse();
        }
        

        System.out.println("\nMas animales ");
        
        Leon leona = new Leon("Nala", 4);
        Pinguino pinguina = new Pinguino("Lola", 2);
        Canguro canguro2 = new Canguro("Bouncy", 6);
        
        Animal[] masAnimales = {leona, pinguina, canguro2};
        
        for (Animal animal : masAnimales) {
            animal.desplazarse();
        }
        
    
        System.out.println("\n Demostracion de polimorfismo ");
        System.out.println("Todos los animales son del tipo Animal pero se comportan diferente:");
        
        for (Animal animal : animales) {
            System.out.print(animal.getNombre() + " -> ");
            animal.desplazarse();
        }
    }
}