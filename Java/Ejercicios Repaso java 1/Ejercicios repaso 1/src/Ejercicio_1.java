import java.util.Scanner;

public class Ejercicio_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Dime un numero: ");
        int numero1 = scanner.nextInt();
        System.out.print("Dime un numero: ");
        int numero2 = scanner.nextInt();
        System.out.print("Dime un numero: ");
        int numero3 = scanner.nextInt();
        System.out.print("Dime un numero: ");
        int numero4 = scanner.nextInt();
        int mayor = Math.max(numero1, numero2);
        int mayo2 = Math.max(numero3, numero4);
        int mayordefinitivo = Math.max(mayor, mayo2);
        if (numero1 == numero2 || numero1 == numero3 || numero1 == numero4) {
            System.out.println("Los numeros son iguales");
            System.exit(1);
        }
        if (numero2 == numero3 || numero2 == numero4) {
            System.out.println("Los numeros son iguales");
            System.exit(1);
        }
        if (numero3 == numero4) {
            System.out.println("Los numeros son iguales");
            System.exit(1);
        }
        if (numero4 == numero3) {
            System.out.println("Los numeros son iguales");
            System.exit(1);
        } else {
            System.out.println(mayordefinitivo);
        }
    }
}
