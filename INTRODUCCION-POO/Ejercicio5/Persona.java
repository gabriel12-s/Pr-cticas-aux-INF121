public class Persona {
    String nombre;
    String paterno;
    String materno;
    int edad;
    String ci;
    
    public Persona(String nombre, String paterno, String materno, int edad, String ci) {
        this.nombre = nombre;
        this.paterno = paterno;
        this.materno = materno;
        this.edad = edad;
        this.ci = ci;
    }

    public void mostrarDatos() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Apellido Paterno: " + paterno);
        System.out.println("Apellido Materno: " + materno);
        System.out.println("Edad: " + edad + " an~os");
        System.out.println("CI: " + ci);
        System.out.println("-----------------+-----");
    }

    public boolean mayorDeEdad() {
        return edad >= 18;
    }

    public void modificarEdad(int nuevaEdad) {
        this.edad = nuevaEdad;
        System.out.println("Edad de " + nombre + " modificada a: " + nuevaEdad + " an~os");
    }
    

    public boolean mismoPaterno(Persona otraPersona) {
        return this.paterno.equals(otraPersona.paterno);
    }
    
    public static void main(String[] args) {
        System.out.println(" SISTEMA DE PERSONAS ");
        
     
        System.out.println("\n Creando personas ");
        Persona persona1 = new Persona("Juan", "Perez", "Gomez", 20, "1234567");
        Persona persona2 = new Persona("Maria", "Lopez", "Rodriguez", 16, "7654321");
        Persona persona3 = new Persona("Carlos", "Perez", "Sanchez", 25, "1111111");
        
      
        System.out.println("\n Datos de las personas ");
        persona1.mostrarDatos();
        persona2.mostrarDatos();
        persona3.mostrarDatos();
        

        System.out.println("\n Verificacion de mayoria de edad ");
        System.out.println(persona1.nombre + " es mayor de edad: " + persona1.mayorDeEdad());
        System.out.println(persona2.nombre + " es mayor de edad: " + persona2.mayorDeEdad());
        System.out.println(persona3.nombre + " es mayor de edad: " + persona3.mayorDeEdad());
        

        System.out.println("\n--- Modificando edad ---");
        persona2.modificarEdad(18);
        System.out.println(persona2.nombre + " es mayor de edad: " + persona2.mayorDeEdad());
        
   
        System.out.println("\n--- Comparando apellidos paternos ---");
        System.out.println(persona1.nombre + " y " + persona2.nombre + 
                         " tienen mismo paterno: " + persona1.mismoPaterno(persona2));
        System.out.println(persona1.nombre + " y " + persona3.nombre + 
                         " tienen mismo paterno: " + persona1.mismoPaterno(persona3));
        System.out.println(persona2.nombre + " y " + persona3.nombre + 
                         " tienen mismo paterno: " + persona2.mismoPaterno(persona3));
        
     
        System.out.println("\n Datos finales ");
        persona1.mostrarDatos();
        persona2.mostrarDatos();
        persona3.mostrarDatos();
    }
}