import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Ejercicio_4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("¿Cuantos palabras quieres introducir? ");
        int introduccion = scanner.nextInt();
        ArrayList<String> lista = new ArrayList<>();
        for (int i = 0; i < introduccion; i++) {
            System.out.println("Dime la palabra ");
            String palabra = scanner.next();
            lista.add(palabra);
        }
        Collections.sort(lista);
        System.out.println("Lista ordenada" + lista);
        System.out.println("Dime la palabra a buscar ");
        String palabra = scanner.next();
        boolean comprobar = lista.contains(palabra);
        if (comprobar) {
            System.out.println("La posicion de la palabra es " + lista.indexOf(palabra));
        } else {
            System.out.println("La palabra no esta");
        }

    }
}
