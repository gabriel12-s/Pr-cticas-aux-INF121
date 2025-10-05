class Crucero {
    String nombre;
    String paisOrigen;
    String paisDestino;
    int nroPasajeros;
    ArrayList<Pasajero> pasajeros;
    
    public Crucero(String nombre, String paisOrigen, String paisDestino) {
        this.nombre = nombre;
        this.paisOrigen = paisOrigen;
        this.paisDestino = paisDestino;
        this.nroPasajeros = 0;
        this.pasajeros = new ArrayList<>();
    }
    
    public void agregarPasajero(Pasajero p) {
        pasajeros.add(p);
        nroPasajeros++;
    }
    
    public void leer() {
        System.out.println("Leyendo crucero: " + nombre);
        System.out.println("  Ruta: " + paisOrigen + " → " + paisDestino);
    }
    
    public void mostrar() {
        System.out.println("CRUCERO: " + nombre);
        System.out.println("  Ruta: " + paisOrigen + " → " + paisDestino);
        System.out.println("  Pasajeros: " + nroPasajeros);
        System.out.println("  Pasajeros a bordo:");
        for (Pasajero p : pasajeros) {
            System.out.println("    - " + p);
        }
        System.out.println("  =============================");
    }
    
    public void compararCostos(Crucero otro) {
        double total1 = 0;
        double total2 = 0;
        
        for (Pasajero p : this.pasajeros) {
            total1 += p.costoPasaje;
        }
        
        for (Pasajero p : otro.pasajeros) {
            total2 += p.costoPasaje;
        }
        
        System.out.println("COSTO TOTAL DE PASAJES:");
        System.out.println("  " + this.nombre + ": $" + total1);
        System.out.println("  " + otro.nombre + ": $" + total2);
        System.out.println("  Mismo costo total? " + (total1 == total2));
    }
    
    public void compararPasajeros(Crucero otro) {
        boolean mismaCantidad = this.nroPasajeros == otro.nroPasajeros;
        
        System.out.println("COMPARACION DE PASAJEROS:");
        System.out.println("  " + this.nombre + ": " + this.nroPasajeros + " pasajeros");
        System.out.println("  " + otro.nombre + ": " + otro.nroPasajeros + " pasajeros");
        System.out.println("  Tienen misma cantidad? " + (mismaCantidad ? "SI" : "NO"));
    }
    
    public void mostrarDistribucionGenero() {
        int hombres = 0;
        int mujeres = 0;
        
        for (Pasajero p : this.pasajeros) {
            if (p.genero.equalsIgnoreCase("masculino")) {
                hombres++;
            } else if (p.genero.equalsIgnoreCase("femenino")) {
                mujeres++;
            }
        }
        
        System.out.println("DISTRIBUCION POR GENERO - " + this.nombre + ":");
        System.out.println("  Hombres: " + hombres);
        System.out.println("  Mujeres: " + mujeres);
        System.out.println("  Total: " + (hombres + mujeres));
    }
    
    public String toString() {
        return nombre + " (" + paisOrigen + " → " + paisDestino + ")";
    }
}