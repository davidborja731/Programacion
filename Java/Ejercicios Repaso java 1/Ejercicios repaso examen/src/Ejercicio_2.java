import java.io.*;
import java.util.Scanner;

public class Ejercicio_2 {
    public static void main(String[] args) {
        File carpeta = new File("F:\\Grado Superior\\Programacion\\Java\\Ejercicios Repaso java 1\\Ejercicios repaso examen\\data");
        File[] archivos = carpeta.listFiles();
        File salida = new File("salida_EJ2.txt");
        try {
            BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(salida));
            for (File archivo : archivos) {
                if (archivo.isFile() && archivo.getName().endsWith(".txt")) {
                    Scanner scanner = new Scanner(archivo);
                    while (scanner.hasNextLine()) {
                        String line = scanner.nextLine();
                        String[] palabras = line.split(" ");
                        bufferedWriter.write(line);
                    }
                }
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
