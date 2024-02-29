import java.lang.Math;
import java.util.Scanner;

public class Ejercicio_3 {
    public static void main(String[] args) {
        Scanner numero = new Scanner(System.in);
        System.out.println("Dime el numero: ");
        int Numero = Integer.parseInt(numero.nextLine());
        System.out.println("La raiz cuadrada de el numero " +Numero+" es " +Math.sqrt(Numero));
    }
}
