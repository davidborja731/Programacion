import java.util.Random;
import java.util.Scanner;

public class random {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            int numero = (int) (Math.random()*100);
            System.out.println(numero);
            if (numero <= 50) {
                System.out.println("Dime algo");
                int numescan= scanner.nextInt();
            } else if (numero > 50) {
                System.out.println("Dime algo");
                String numescan= scanner.next();
            }
        }
    }
}
