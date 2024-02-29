import java.io.File;
import java.util.Arrays;
import java.util.Scanner;

public class Ejercicio_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Dime la ruta del archivo ");
        String ruta = scanner.nextLine();
        File archivo = new File(ruta);
        boolean cierto = archivo.exists();
        if (cierto) {
            System.out.println("El archivo existe");
            System.out.println(archivo.getParent());
            boolean file = archivo.isFile();
            boolean file1 = archivo.isDirectory();
            if (file) {
                System.out.println("Es un archivo");
            }
            if (file1) {
                System.out.println("Es un directorio");
                System.out.println(Arrays.toString(archivo.listFiles()));
                }
            } else {
                System.out.println("El archivo no existe");
            }
        }
    }
