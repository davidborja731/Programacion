import java.util.Scanner;

public class Ejercicio_1 {
    public static void main(String[] args) {
        Scanner base = new Scanner(System.in);
        System.out.println("Dime la base: ");
        int Base = Integer.parseInt(base.nextLine());
        Scanner altura = new Scanner(System.in);
        System.out.println("Dime la base: ");
        int Altura = Integer.parseInt(altura.nextLine());
        System.out.println("Resultado Area " + Base*Altura);
    }
}

