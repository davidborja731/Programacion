import java.util.Scanner;

public class Ejercicio_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Dime un numero ");
        int num1 = scanner.nextInt();
        System.out.println("Dime otro numero ");
        int num2 = scanner.nextInt();
        try {
            int operacion = num1 / num2;
            System.out.println(operacion);
        } catch (ArithmeticException arithmeticException) {
            System.out.println("Error");
        }
    }
}
