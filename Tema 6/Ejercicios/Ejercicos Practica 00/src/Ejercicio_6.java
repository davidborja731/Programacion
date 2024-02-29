import java.util.Scanner;

public class Ejercicio_6 {
    public static void main(String[] args) {
        Scanner numero = new Scanner(System.in);
        System.out.print("Dime el numero: ");
        int Numero = Integer.parseInt(numero.nextLine());
        Scanner numero1 = new Scanner(System.in);
        System.out.print("Dime el numero: ");
        int Numero1 = Integer.parseInt(numero1.nextLine());
        System.out.println(Math.pow(Numero,Numero1));
    }
}
