import java.util.Scanner;

public class Ejercicio_8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduce el precio de la vivienda: ");
        float precio = scanner.nextFloat();
        System.out.print("Introduce la superficie de la vivienda: ");
        float superfifcie = scanner.nextFloat();
        System.out.print("Introduce si la vivienda tiene garaje: ");
        boolean garaje = scanner.nextBoolean();
        if (precio <150000 && superfifcie>80 && garaje){
            System.out.println("Me interesa");
        }
        else {
            System.out.println("No me interesa");
        }

    }
}


