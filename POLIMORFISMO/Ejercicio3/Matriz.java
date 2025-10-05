public class Matriz {
    private float[][] matriz;
    private int filas;
    private int columnas;
    
    public Matriz() {
        this.filas = 3;
        this.columnas = 3;
        this.matriz = new float[filas][columnas];
        
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                if (i == j) {
                    matriz[i][j] = 1.0f; 
                } else {
                    matriz[i][j] = 0.0f; 
                }
            }
        }
        System.out.println("Matriz identidad 3x3 creada");
    }
    
    public Matriz(int filas, int columnas) {
        this.filas = filas;
        this.columnas = columnas;
        this.matriz = new float[filas][columnas];
        
        float valor = 1.0f;
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                matriz[i][j] = valor;
                valor += 1.0f;
            }
        }
        System.out.println("Matriz " + filas + "x" + columnas + " creada");
    }
    
    public Matriz(float[][] valores) {
        this.filas = valores.length;
        this.columnas = valores[0].length;
        this.matriz = valores;
        System.out.println("Matriz personalizada " + filas + "x" + columnas + " creada");
    }
    
    public Matriz sumar(Matriz otraMatriz) {
        if (this.filas != otraMatriz.filas || this.columnas != otraMatriz.columnas) {
            System.out.println("Error: Las matrices deben tener el mismo tamano para sumar");
            return null;
        }
        
        float[][] resultado = new float[filas][columnas];
        
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                resultado[i][j] = this.matriz[i][j] + otraMatriz.matriz[i][j];
            }
        }
        
        return new Matriz(resultado);
    }
    
    public Matriz restar(Matriz otraMatriz) {
        if (this.filas != otraMatriz.filas || this.columnas != otraMatriz.columnas) {
            System.out.println("Error: Las matrices deben tener el mismo tamano para restar");
            return null;
        }
        
        float[][] resultado = new float[filas][columnas];
        
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                resultado[i][j] = this.matriz[i][j] - otraMatriz.matriz[i][j];
            }
        }
        
        return new Matriz(resultado);
    }
    

    public boolean igual(Matriz otraMatriz) {
        if (this.filas != otraMatriz.filas || this.columnas != otraMatriz.columnas) {
            return false;
        }
        
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                if (this.matriz[i][j] != otraMatriz.matriz[i][j]) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    public void mostrarMatriz() {
        System.out.println("Matriz " + filas + "x" + columnas + ":");
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                System.out.print(matriz[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println();
    }
    
    public int getFilas() {
        return filas;
    }
    
    public int getColumnas() {
        return columnas;
    }
    
    public static void main(String[] args) {
        System.out.println(" SISTEMA DE MATRICES ");
        
        System.out.println("\n Matriz Identidad ");
        Matriz identidad = new Matriz();
        identidad.mostrarMatriz();
        
        System.out.println(" Matrices Personalizadas ");
        Matriz matrizA = new Matriz(2, 3);
        matrizA.mostrarMatriz();
        
        Matriz matrizB = new Matriz(2, 3);
        matrizB.mostrarMatriz();
        
        float[][] valores1 = {{1.0f, 2.0f}, {3.0f, 4.0f}};
        float[][] valores2 = {{5.0f, 6.0f}, {7.0f, 8.0f}};
        float[][] valores3 = {{1.0f, 2.0f}, {3.0f, 4.0f}};
        
        Matriz m1 = new Matriz(valores1);
        Matriz m2 = new Matriz(valores2);
        Matriz m3 = new Matriz(valores3);
        
        m1.mostrarMatriz();
        m2.mostrarMatriz();
        m3.mostrarMatriz();
        
        System.out.println(" Suma de Matrices ");
        Matriz suma = m1.sumar(m2);
        if (suma != null) {
            suma.mostrarMatriz();
        }
        
        System.out.println(" Resta de Matrices ");
        Matriz resta = m2.restar(m1);
        if (resta != null) {
            resta.mostrarMatriz();
        }
        
        System.out.println(" Comparacion de Matrices ");
        System.out.println("m1 es igual a m2: " + m1.igual(m2));
        System.out.println("m1 es igual a m3: " + m1.igual(m3));
        
        System.out.println("\n Operaciones con matrices de diferente tamano ");
        Matriz resultadoError = m1.sumar(identidad);
        if (resultadoError == null) {
            System.out.println("Correcto: No se pueden sumar matrices de diferente tamano");
        }
    }
}