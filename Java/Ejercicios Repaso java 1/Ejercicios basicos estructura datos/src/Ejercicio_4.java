import java.util.HashMap;

public class Ejercicio_4 {
    public static void main(String[] args) {
        HashMap<String, Integer> lista = new HashMap<>();
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
