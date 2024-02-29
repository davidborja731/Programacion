import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Ejercicio_3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("¿Cuantos numeros quieres introducir? ");
        int introduccion = scanner.nextInt();
        ArrayList<Integer> lista = new ArrayList<>();
        for (int i = 0; i < introduccion; i++) {
            System.out.println("Dime el numero ");
            int numero = scanner.nextInt();
            lista.add(numero);
        }
        Set nodupli = new HashSet<>(lista);
        lista.clear();
        lista.addAll(nodupli);
        System.out.println(lista);
    }
}

