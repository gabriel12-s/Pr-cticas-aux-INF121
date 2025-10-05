
public class Vehiculo {
    private String marca;
    private String modelo;
    private int velocidadActual;
    public Vehiculo(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
        this.velocidadActual = 0; 
    }
    public String getMarca() {
        return marca;
    }
    public String getModelo() {
        return modelo;
    }
    
    public int getVelocidadActual() {
        return velocidadActual;
    }
    

    public void acelerar(int incremento) {
        if (incremento > 0) {
            velocidadActual += incremento;
            System.out.println(marca + " " + modelo + " acelero " + incremento + 
                             " km/h. Velocidad actual: " + velocidadActual + " km/h");
        }
    }
    
   
    public void frenar(int decremento) {
        if (decremento > 0) {
            int nuevaVelocidad = velocidadActual - decremento;
            if (nuevaVelocidad < 0) {
                nuevaVelocidad = 0;
            }
            velocidadActual = nuevaVelocidad;
            System.out.println(marca + " " + modelo + " freno " + decremento + 
                             " km/h. Velocidad actual: " + velocidadActual + " km/h");
        }
    }
    
    @Override
    public String toString() {
        return "Vehiculo: " + marca + " " + modelo + " - Velocidad: " + velocidadActual + " km/h";
    }
    
    public static void main(String[] args) {
        System.out.println(" SIMULACION DE CARRERA ");
        
        // Crear 2 objetos Vehículo
        Vehiculo coche1 = new Vehiculo("Toyota", "Corolla");
        Vehiculo coche2 = new Vehiculo("Honda", "Civic");
        
        System.out.println("\n INICIO DE LA CARRERA ");
        System.out.println(coche1);
        System.out.println(coche2);
        
        System.out.println("\n PRIMERA ACELERACION ");
        coche1.acelerar(50);
        coche2.acelerar(40);
        
        System.out.println("\n SEGUNDA ACELERACION ");
        coche1.acelerar(30);
        coche2.acelerar(35);
        
        System.out.println("\n PRIMER FRENADO ");
        coche1.frenar(20);
        coche2.frenar(15);
        
        System.out.println("\n TERCERA ACELERACION ");
        coche1.acelerar(25);
        coche2.acelerar(30);
        
        System.out.println("\n FRENADO FUERTE ");
        coche1.frenar(60);
        coche2.frenar(70); 
        
        System.out.println("\n ACELERACION FINAL ");
        coche1.acelerar(80);
        coche2.acelerar(75);
        
        System.out.println("\n RESULTADO FINAL ");
        System.out.println(coche1);
        System.out.println(coche2);
        
        
        if (coche1.getVelocidadActual() > coche2.getVelocidadActual()) {
            System.out.println("\n GANADOR: " + coche1.getMarca() + " " + coche1.getModelo());
        } else if (coche2.getVelocidadActual() > coche1.getVelocidadActual()) {
            System.out.println("\n GANADOR: " + coche2.getMarca() + " " + coche2.getModelo());
        } else {
            System.out.println("\n EMPATE");
        }
    }
}