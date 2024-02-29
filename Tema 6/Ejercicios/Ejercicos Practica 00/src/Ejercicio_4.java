import java.util.Scanner;
public class Ejercicio_4 {
    public static void main(String[] args) {
        Scanner numero = new Scanner(System.in);
        System.out.print("Dime el numero: ");
        int Numero = Integer.parseInt(numero.nextLine());
        Scanner numero1 = new Scanner(System.in);
        System.out.print("Dime el numero: ");
        int Numero1 = Integer.parseInt(numero1.nextLine());
        int Numeros1 = (int)Math.floor(Math.random()*((Numero-Numero1)+1)+Numero1);
        int Numeros2 = (int)Math.floor(Math.random()*((Numero-Numero1)+1)+Numero1);
        int Numeros3 = (int)Math.floor(Math.random()*((Numero-Numero1)+1)+Numero1);
        System.out.println(Numeros1);
        System.out.println(Numeros2);
        System.out.println(Numeros3);
        }


}



