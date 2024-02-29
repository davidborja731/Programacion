import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Ejercicio_2 {
    public static void main(String[] args) {
        File archivo = new File("..\\xd.txt");
        BufferedWriter bufferedWriter = null;
        try {
            bufferedWriter = new BufferedWriter(new FileWriter(archivo));
            bufferedWriter.write("Hola");
            bufferedWriter.flush();
            System.out.println("Correcto");
        } catch (IOException e) {
            throw new RuntimeException(e);
        } finally {
            if (bufferedWriter != null) {
                try {
                    bufferedWriter.close();
                } catch (IOException e) {
                    System.out.println("ERROR 404");
                }
            }
        }
    }
}

