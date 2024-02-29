import java.io.File;
import java.io.FileInputStream;

public class Main {
    public static void main(String[] args) throws Exception {
        File file = new File("text.txt");
        FileInputStream inputStream = new FileInputStream(file);
        int contenido;
        while ((contenido = inputStream.read()) !=-1){
            System.out.println((char) contenido);
        }
    }
}