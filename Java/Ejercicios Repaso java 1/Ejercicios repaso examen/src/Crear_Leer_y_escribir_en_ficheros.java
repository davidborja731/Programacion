import java.io.*;
import java.util.Scanner;

public class Crear_Leer_y_escribir_en_ficheros {
    public static void main(String[] args) {
        System.out.println("Creo el archivo");
        boolean comprobar = true;
        Scanner scanner = new Scanner(System.in);
        while (comprobar) {
            System.out.println("Como quieres que se llame el archivo: ");
            String archivo = scanner.next();
            String ruta = archivo + ".txt";
            File archivo1 = new File(ruta);
            if (!archivo1.exists()) {
                try {
                    archivo1.createNewFile();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            } else {
                System.out.println("El archivo ya existe");
            }
            System.out.println("¿Quieres crear otro archivo?(si o no) ");
            String pregunta = scanner.next().toLowerCase();
            comprobar = pregunta.equals("si");
        }
        System.out.println("Leo el archivo");
        boolean comprobar2 = true;
        while (comprobar2) {
            System.out.println("Dime que archivo quieres leer: ");
            String archivobuscar = scanner.next();
            File archivoleer=new File(archivobuscar);
            if (archivoleer.exists()) {
                try {
                    BufferedReader modificar = new BufferedReader(new FileReader(archivoleer));
                    String linea;
                    while ((linea = modificar.readLine()) != null) {
                        System.out.println(linea);
                    }
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }else {
                System.out.println("El archivo no existe");
            }
            System.out.println("¿Quieres leer otro archivo?(si o no) ");
            String pregunta1 = scanner.next().toLowerCase();
            comprobar2 = pregunta1.equals("si");
        }
        System.out.println("Escribo en el archivo");
        System.out.println("Dime en que archivo quieres escribir: ");
        scanner.nextLine();
        String archivobuscar1 = scanner.nextLine();
        File archivoescribir = new File(archivobuscar1);
        boolean comprobar3 = true;
        while (comprobar3==true){
            if (archivoescribir.exists()) {
                try {
                    BufferedWriter escribir = new BufferedWriter(new FileWriter(archivobuscar1, true));
                    System.out.println("Dime que quieres escribir: ");
                    String añadir = scanner.nextLine();
                    escribir.write(añadir);
                    escribir.newLine();
                    escribir.close();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }else {
                System.out.println("El archivo no existe");
            }
            System.out.println("¿Quieres escribir en otro archivo? ");
            String pregunta3= scanner.next().toLowerCase();
            if (pregunta3=="si"){
                comprobar3=true;
            }else {
                comprobar3=false;
            }
        }

    }
}

