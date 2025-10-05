// Clase base Vehiculo
class Vehiculo {
    protected String conductor;
    protected String placa;
    protected int id;
    
    public Vehiculo(String conductor, String placa, int id) {
        this.conductor = conductor;
        this.placa = placa;
        this.id = id;
    }
    
    public void mostrarInfo() {
        System.out.println("Vehiculo ID: " + id);
        System.out.println("  Conductor: " + conductor);
        System.out.println("  Placa: " + placa);
    }
    
    public void cambiarConductor(String nuevoConductor) {
        System.out.println("Cambiando conductor de " + this.conductor + " a " + nuevoConductor);
        this.conductor = nuevoConductor;
    }
    
    public String getConductor() {
        return conductor;
    }
    
    public String getPlaca() {
        return placa;
    }
    
    public int getId() {
        return id;
    }
}

class Bus extends Vehiculo {
    private int capacidad;
    private String sindicato;
    
    public Bus(String conductor, String placa, int id, int capacidad, String sindicato) {
        super(conductor, placa, id);
        this.capacidad = capacidad;
        this.sindicato = sindicato;
    }
    
    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("  Tipo: Bus");
        System.out.println("  Capacidad: " + capacidad + " pasajeros");
        System.out.println("  Sindicato: " + sindicato);
    }
}

class Auto extends Vehiculo {
    private int caballosFuerza;
    private boolean descapotable;
    
    public Auto(String conductor, String placa, int id, int caballosFuerza, boolean descapotable) {
        super(conductor, placa, id);
        this.caballosFuerza = caballosFuerza;
        this.descapotable = descapotable;
    }
    
    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("  Tipo: Auto");
        System.out.println("  Caballos de Fuerza: " + caballosFuerza + " HP");
        System.out.println("  Descapotable: " + (descapotable ? "Si" : "No"));
    }
}

class Moto extends Vehiculo {
    private int cilindrada;
    private boolean casco;
    
    public Moto(String conductor, String placa, int id, int cilindrada, boolean casco) {
        super(conductor, placa, id);
        this.cilindrada = cilindrada;
        this.casco = casco;
    }
    
    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("  Tipo: Moto");
        System.out.println("  Cilindrada: " + cilindrada + " cc");
        System.out.println("  Casco incluido: " + (casco ? "si" : "No"));
    }
}

public class SistemaVehiculos {
    public static void main(String[] args) {
        System.out.println(" SISTEMA DE VEHICULOS ");
        
        System.out.println("\n Creando vehiculos ");
        
        Bus bus = new Bus("Juan Perez", "ABC-123", 1, 50, "Sindicato Transporte");
        Auto auto = new Auto("Maria Garcia", "XYZ-789", 2, 150, true);
        Moto moto = new Moto("Carlos Lopez", "DEF-456", 3, 250, true);
        
        System.out.println("\n Informacion de los vehiculos ");
        
        bus.mostrarInfo();
        System.out.println();
        
        auto.mostrarInfo();
        System.out.println();
        
        moto.mostrarInfo();
        System.out.println();
        
        System.out.println(" Solo placa y conductor ");
        System.out.println("Bus - Conductor: " + bus.getConductor() + ", Placa: " + bus.getPlaca());
        System.out.println("Auto - Conductor: " + auto.getConductor() + ", Placa: " + auto.getPlaca());
        System.out.println("Moto - Conductor: " + moto.getConductor() + ", Placa: " + moto.getPlaca());
        
        System.out.println("\n Cambiando conductores ");
        
        bus.cambiarConductor("Pedro Rodriguez");
        auto.cambiarConductor("Ana Martinez");
        moto.cambiarConductor("Luisa Fernandez");
        
        System.out.println("\n Informacion despues del cambio ");
        
        System.out.println("Bus - Conductor: " + bus.getConductor() + ", Placa: " + bus.getPlaca());
        System.out.println("Auto - Conductor: " + auto.getConductor() + ", Placa: " + auto.getPlaca());
        System.out.println("Moto - Conductor: " + moto.getConductor() + ", Placa: " + moto.getPlaca());
        
        System.out.println("\n Mas vehiculos ");
        
        Bus bus2 = new Bus("Roberto Silva", "GHI-789", 4, 40, "Sindicato Urbano");
        Auto auto2 = new Auto("Sofia Castro", "JKL-012", 5, 200, false);
        Moto moto2 = new Moto("Diego Rojas", "MNO-345", 6, 600, false);
        
        Vehiculo[] vehiculos = {bus2, auto2, moto2};
        
        for (Vehiculo vehiculo : vehiculos) {
            vehiculo.mostrarInfo();
            System.out.println();
        }
        

        for (Vehiculo vehiculo : vehiculos) {
            String nuevoConductor = "Conductor Nuevo " + vehiculo.getId();
            vehiculo.cambiarConductor(nuevoConductor);
        }
        
        // Verificar cambios
        System.out.println("\n Verificando cambios ");
        for (Vehiculo vehiculo : vehiculos) {
            System.out.println("Vehiculo " + vehiculo.getId() + 
                             " - Conductor: " + vehiculo.getConductor() + 
                             ", Placa: " + vehiculo.getPlaca());
        }
    }
}