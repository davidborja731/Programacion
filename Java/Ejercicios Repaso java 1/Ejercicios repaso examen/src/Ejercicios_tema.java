import java.util.Random;
import java.util.Arrays;
public class Ejercicios_tema {
    public static void main(String[] args) {
        // Instanciamos un objeto de la clase Random
        Random r = new Random();
        // Creamos un array de 16 bytes
        byte[] sequence = new byte[16];
        // Obtenemos una secuencia de 16 números aleatorios
        r.nextBytes(sequence);
        // Mostramos la secuencia obtenida
        System.out.println(Arrays.toString(sequence));
    }
}

