import java.util.TreeMap;

public class Ejercicio_5 {
    public static void main(String[] args) {
        TreeMap<String, Integer> lista = new TreeMap<>();
        lista.put("uno", 1);
        lista.put("dos", 2);
        lista.put("tres", 3);
        lista.put("cuatro", 4);
        lista.put("cinco", 5);
        System.out.println(lista.get("cuatro"));
        lista.remove("dos");
        System.out.println(lista);
    }
}
