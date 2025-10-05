
public class Fruta {
    private String nombre;
    private String tipo;
    private int nroVitaminas;
    private String[] vitaminas = new String[30];
    
    
    public Fruta() {
        this.nroVitaminas = 0;
    }
    
    public Fruta(String nombre, String tipo) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.nroVitaminas = 0;
    }
    
    public Fruta(String nombre, String tipo, String[] vitaminas) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.nroVitaminas = 0;
        for (int i = 0; i < vitaminas.length && i < 30; i++) {
            this.vitaminas[i] = vitaminas[i];
            this.nroVitaminas++;
        }
    }
    
    public String getNombre() {
        return nombre;
    }
    
    public String getTipo() {
        return tipo;
    }
    
    public int getNroVitaminas() {
        return nroVitaminas;
    }
    
    public String[] getVitaminas() {
        return vitaminas;
    }
    
    public void agregarVitamina(String vitamina) {
        if (nroVitaminas < 30) {
            vitaminas[nroVitaminas] = vitamina;
            nroVitaminas++;
        }
    }
    
    public void mostrarInfo() {
        System.out.println("Fruta: " + nombre);
        System.out.println("Tipo: " + tipo);
        System.out.println("Numero de vitaminas: " + nroVitaminas);
        System.out.print("Vitaminas: ");
        for (int i = 0; i < nroVitaminas; i++) {
            System.out.print(vitaminas[i] + " ");
        }
        System.out.println("\n----------------------");
    }
    
    public static void main(String[] args) {
        System.out.println("SISTEMA DE FRUTAS ");
        
        System.out.println("\n Creando frutas ");
        
        Fruta kiwi = new Fruta();
        kiwi.nombre = "Kiwi";
        kiwi.tipo = "subtropical";
        kiwi.agregarVitamina("K");
        kiwi.agregarVitamina("C");
        kiwi.agregarVitamina("E");
        
        Fruta naranja = new Fruta("Naranja", "citrica");
        naranja.agregarVitamina("C");
        naranja.agregarVitamina("A");
        naranja.agregarVitamina("B");
        
        String[] vitaminasFresa = {"C", "K", "B9"};
        Fruta fresa = new Fruta("Fresa", "bosque", vitaminasFresa);
        
        System.out.println("\n Informacion de todas las frutas ");
        kiwi.mostrarInfo();
        naranja.mostrarInfo();
        fresa.mostrarInfo();
        
        System.out.println("\n Fruta con mas vitaminas ");
        Fruta[] frutas = {kiwi, naranja, fresa};
        Fruta frutaMasVitaminas = frutas[0];
        
        for (int i = 1; i < frutas.length; i++) {
            if (frutas[i].getNroVitaminas() > frutaMasVitaminas.getNroVitaminas()) {
                frutaMasVitaminas = frutas[i];
            }
        }
        System.out.println("La fruta con mas vitaminas es: " + frutaMasVitaminas.getNombre() + 
                         " con " + frutaMasVitaminas.getNroVitaminas() + " vitaminas");
        
        System.out.println("\n--- Vitaminas del Kiwi ---");
        System.out.print("Vitaminas del Kiwi: ");
        String[] vitaminasKiwi = kiwi.getVitaminas();
        for (int i = 0; i < kiwi.getNroVitaminas(); i++) {
            System.out.print(vitaminasKiwi[i] + " ");
        }
        System.out.println();
        
        System.out.println("\n Frutas citricas ");
        int frutasCitricas = 0;
        for (Fruta fruta : frutas) {
            if (fruta.getTipo().equalsIgnoreCase("citrica")) {
                frutasCitricas++;
            }
        }
        System.out.println("Numero de frutas citricas: " + frutasCitricas);
        
        System.out.println("\n Ordenando frutas por primera vitamina ");
        for (int i = 0; i < frutas.length - 1; i++) {
            for (int j = i + 1; j < frutas.length; j++) {
                String vitaminaI = frutas[i].getVitaminas()[0];
                String vitaminaJ = frutas[j].getVitaminas()[0];
                
                if (vitaminaI.compareTo(vitaminaJ) > 0) {
                    Fruta temp = frutas[i];
                    frutas[i] = frutas[j];
                    frutas[j] = temp;
                }
            }
        }
        
        System.out.println("Frutas ordenadas por primera vitamina:");
        for (Fruta fruta : frutas) {
            System.out.println(fruta.getNombre() + " - Primera vitamina: " + fruta.getVitaminas()[0]);
        }
    }
}