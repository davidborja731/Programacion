import java.util.*;

public class Ejercicio_conteo_numeros {
    public static void main(String[] args) {
        Random rand = new Random();
        int[] numeros = new int[40];
        for (int i = 0; i < 40; i++) {
            numeros[i] = rand.nextInt(49); // Genera números aleatorios entre 0 y 99
        }

        // Crea un HashMap para almacenar cada número y su frecuencia
        HashMap<Integer, Integer> frecuencias = new HashMap<>();
        for (int numero : numeros) {
            frecuencias.put(numero, frecuencias.getOrDefault(numero, 0) + 1);
        }

        // Ordena el HashMap en función de sus valores (frecuencias)
        List<Map.Entry<Integer, Integer>> lista = new ArrayList<>(frecuencias.entrySet());
        lista.sort(Map.Entry.comparingByValue());

        // Invierte el orden de la lista para que esté de mayor a menor
        Collections.reverse(lista);
        // Imprime cada número y su frecuencia
        for (Map.Entry<Integer, Integer> entrada : lista) {
            System.out.println("Número: " + entrada.getKey() + ", Frecuencia: " + entrada.getValue());
        }
    }
}


