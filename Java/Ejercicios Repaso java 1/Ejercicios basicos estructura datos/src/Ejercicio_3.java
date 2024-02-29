import java.util.TreeSet;

public class Ejercicio_3 {
    public static void main(String[] args) {
        TreeSet<Integer> lista = new TreeSet<>();
        lista.add(7);
        lista.add(9);
        lista.add(2);
        lista.add(6);
        lista.add(8);
        System.out.println(lista);
        lista.remove(2);
        System.out.println(lista);
        boolean comprobar = lista.contains(5);
        System.out.println(comprobar);
    }
}
