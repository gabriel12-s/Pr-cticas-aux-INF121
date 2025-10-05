
public class SistemaCruceros {
    public static void main(String[] args) {
        System.out.println(" SISTEMA DE CRUCEROS ");
        
        System.out.println("\n Creando cruceros y pasajeros ");
        
        Crucero crucero1 = new Crucero("Caribe Paradise", "Miami", "Bahamas");
        Crucero crucero2 = new Crucero("Mediterranean Dream", "Barcelona", "Italia");
        

        Pasajero pasajero1 = new Pasajero("Juan Vargas", 35, "masculino", 502, 500);
        Pasajero pasajero2 = new Pasajero("Martina Vasques", 28, "femenino", 603, 1000);
        Pasajero pasajero3 = new Pasajero("Wilmer Montero", 42, "masculino", 401, 925);
        Pasajero pasajero4 = new Pasajero("Ana Lopez", 31, "femenino", 305, 750);
        Pasajero pasajero5 = new Pasajero("Carlos Ruiz", 45, "masculino", 208, 850);
        
        crucero1.agregarPasajero(pasajero1);
        crucero1.agregarPasajero(pasajero2);
        crucero1.agregarPasajero(pasajero3);
        
        crucero2.agregarPasajero(pasajero4);
        crucero2.agregarPasajero(pasajero5);
        
        System.out.println(" Cruceros y pasajeros creados exitosamente");
        
        System.out.println("\n LEER Y MOSTRAR ");
        
        System.out.println("\nLEYENDO:");
        crucero1.leer();
        pasajero1.leer();
        
        System.out.println("\nMOSTRANDO:");
        crucero1.mostrar();
        pasajero1.mostrar();
        
        System.out.println("\n COMPARAR COSTOS (==) ");
        crucero1.compararCostos(crucero2);
        
        System.out.println("\n COMPARAR PASAJEROS (+) ");
        crucero1.compararPasajeros(crucero2);
        
        System.out.println("\n DISTRIBUCION POR GENERO (-) ");
        crucero1.mostrarDistribucionGenero();
        crucero2.mostrarDistribucionGenero();
        
        // Resumen final
        System.out.println("\n RESUMEN FINAL ");
        System.out.println("CRUCERO 1:");
        crucero1.mostrar();
        
        System.out.println("CRUCERO 2:");
        crucero2.mostrar();
        
        System.out.println(" Todas las operaciones completadas exitosamente");
    }
}
