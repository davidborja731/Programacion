import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class Ejercicio_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Dime la primera frase: ");
        String frase1 = scanner.nextLine();
        String[] palabras1 = frase1.split(" ");
        System.out.println("Dime la segunda frase: ");
        String frase2 = scanner.nextLine();
        String[] palabras2 = frase2.split(" ");
        for (String palabra : palabras1) {
            for (String palabra2 : palabras2) {
                if(palabra.equals(palabra2)){
                    System.out.println("La palabra que coincide es "+palabra);
                    return;
                }
            }
        }
        System.out.println("No hay palabras en comun");
    }
}