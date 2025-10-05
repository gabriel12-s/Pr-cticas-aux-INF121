public class Buzon {
    private String nro;
    private int nroC;
    private String[][] cartas;
    
    public Buzon(String nro) {
        this.nro = nro;
        this.nroC = 0;
        this.cartas = new String[50][3]; 
    }
    
    public void agregarCarta(String codigo, String remitente, String destinatario) {
        if (nroC < 50) {
            cartas[nroC][0] = codigo;
            cartas[nroC][1] = remitente;
            cartas[nroC][2] = destinatario;
            nroC++;
            System.out.println("Carta " + codigo + " agregada al buzon " + nro);
        } else {
            System.out.println("El buzon está lleno");
        }
    }
    
    public int contarCartasDestinatario(String destinatario) {
        int count = 0;
        for (int i = 0; i < nroC; i++) {
            if (cartas[i][2] != null && cartas[i][2].equalsIgnoreCase(destinatario)) {
                count++;
            }
        }
        return count;
    }
    
    public void eliminarCarta(String codigo) {
        for (int i = 0; i < nroC; i++) {
            if (cartas[i][0] != null && cartas[i][0].equals(codigo)) {
                for (int j = i; j < nroC - 1; j++) {
                    cartas[j][0] = cartas[j + 1][0];
                    cartas[j][1] = cartas[j + 1][1];
                    cartas[j][2] = cartas[j + 1][2];
                }
                cartas[nroC - 1][0] = null;
                cartas[nroC - 1][1] = null;
                cartas[nroC - 1][2] = null;
                nroC--;
                System.out.println("Carta " + codigo + " eliminada");
                return;
            }
        }
        System.out.println("Carta " + codigo + " no encontrada");
    }
    
    public String buscarRemitenteRecibio() {
        for (int i = 0; i < nroC; i++) {
            String remitente = cartas[i][1];
            for (int j = 0; j < nroC; j++) {
                if (cartas[j][2] != null && cartas[j][2].equals(remitente)) {
                    return remitente + " recibio carta de " + cartas[j][1];
                }
            }
        }
        return "Ningun remitente ha recibido carta";
    }
    
    public void buscarPalabra(String palabra, Carta[] todasCartas) {
        System.out.println("Buscando palabra: '" + palabra + "'");
        boolean encontrada = false;
        
        for (Carta carta : todasCartas) {
            if (carta != null && carta.getDescripcion().toLowerCase().contains(palabra.toLowerCase())) {

                for (int i = 0; i < nroC; i++) {
                    if (cartas[i][0] != null && cartas[i][0].equals(carta.getCodigo())) {
                        System.out.println("Codigo: " + carta.getCodigo() + 
                                         " | Remitente: " + cartas[i][1] + 
                                         " | Destinatario: " + cartas[i][2]);
                        encontrada = true;
                        break;
                    }
                }
            }
        }
        
        if (!encontrada) {
            System.out.println("Palabra no encontrada en ninguna carta");
        }
    }
    
    public void mostrarBuzon() {
        System.out.println("\n BUZON " + nro + "" );
        System.out.println("Total cartas: " + nroC);
        for (int i = 0; i < nroC; i++) {
            System.out.println((i + 1) + ". Codigo: " + cartas[i][0] + 
                             " | De: " + cartas[i][1] + 
                             " | Para: " + cartas[i][2]);
        }
        System.out.println("----------------------");
    }
    
    public static void main(String[] args) {
        System.out.println(" SISTEMA DE BUZONES Y CARTAS ");
        
        System.out.println("\n--- Creando cartas ---");
        Carta carta1 = new Carta("C123", "Querido amigo te escribo para decirte que ella no te ama .");
        Carta carta2 = new Carta("C456", "Hola, espero que estes bien. .");
        Carta carta3 = new Carta("C789", "Necesito charlar contigo ");
        Carta carta4 = new Carta("C101", "Hola xd.");
        Carta carta5 = new Carta("C202", " Reunion mañana a las 10 AM.");
        Carta carta6 = new Carta("C303", "F en el chat.");
        
        Carta[] todasCartas = {carta1, carta2, carta3, carta4, carta5, carta6};
        
        System.out.println("\n Creando buzones y agregando cartas ");
        
        Buzon buzon1 = new Buzon("001");
        buzon1.agregarCarta("C123", "Juan Alvarez", "Peter Chaves");
        buzon1.agregarCarta("C456", "Pepe Mujica", "Wilmer Perez");
        buzon1.agregarCarta("C789", "Paty Vasques", "Pepe Mujica");
        
        Buzon buzon2 = new Buzon("002");
        buzon2.agregarCarta("C101", "Maria Lopez", "Carlos Ruiz");
        buzon2.agregarCarta("C202", "Ana Garcia", "Pedro Martinez");
        buzon2.agregarCarta("C303", "Luis Torres", "Maria Lopez");
        
        Buzon buzon3 = new Buzon("003");
        buzon3.agregarCarta("C404", "Wilmer Pérez", "Juan Alvarez");
        buzon3.agregarCarta("C505", "Peter Chaves", "Ana Garcia");
        buzon3.agregarCarta("C606", "Carlos Ruiz", "Luis Torres");
        
        buzon1.mostrarBuzon();
        buzon2.mostrarBuzon();
        buzon3.mostrarBuzon();
        
        System.out.println("\n Cartas recibidas por destinatarios ");
        System.out.println("Pepe Mujica recibio: " + buzon1.contarCartasDestinatario("Pepe Mujica") + " cartas");
        System.out.println("Maria Lopez recibio: " + buzon2.contarCartasDestinatario("Maria Lopez") + " cartas");
        
        System.out.println("\n Eliminando carta ");
        buzon1.eliminarCarta("C456");
        buzon1.mostrarBuzon();
        
        System.out.println("\n Remitentes que recibieron cartas ");
        System.out.println("Buzon 1: " + buzon1.buscarRemitenteRecibio());
        System.out.println("Buzon 2: " + buzon2.buscarRemitenteRecibio());
        System.out.println("Buzon 3: " + buzon3.buscarRemitenteRecibio());
        
        System.out.println("\n Buscando palabra clave ");
        buzon1.buscarPalabra("hola", todasCartas);
        buzon2.buscarPalabra("hola", todasCartas);
        
        System.out.println("\n Buscando palabra clave -");
        buzon1.buscarPalabra("trabajo", todasCartas);
    }
}