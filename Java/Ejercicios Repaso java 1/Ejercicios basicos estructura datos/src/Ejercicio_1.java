import java.util.ArrayList;
import java.util.Scanner;

public class Ejercicio_1 {
    public static void main(String[] args) {
        ArrayList<String> lista = new ArrayList<>();
        lista.add("hola");
        lista.add("que");
        lista.add("tal");
        lista.add("estas");
        lista.add(4, "elemento4");
        for (int i = 0; i < lista.size(); i++) {
            System.out.println("Lista " + lista.get(i));
        }
        Scanner scanner = new Scanner(System.in);
        System.out.print("¿Que indice de la lista quieres borrar? ");
        String indice = scanner.next();
        lista.remove(lista.get(Integer.parseInt(indice)));
        System.out.println(lista);
        System.out.print("¿Que valor de la lista quieres borrar? ");
        String valor = scanner.next();
        lista.remove(valor);
        System.out.println(lista);

    }
}
