import java.util.HashSet;

public class Ejercicio_2 {
    public static void main(String[] args) {
        HashSet<String> lista = new HashSet<>();
        lista.add("hola");
        lista.add("que");
        lista.add("que");
        lista.add("estas");
        System.out.print(lista);
        lista.remove("estas");
        System.out.print(lista);
        boolean comprobar = lista.contains("patata");
        System.out.println(comprobar);

    }
}
