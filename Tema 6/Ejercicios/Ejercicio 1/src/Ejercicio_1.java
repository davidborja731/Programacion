import java.io.File;

public class Ejercicio_1 {
    public static void main(String[] args) {
        String ruta = "F:\\Grado Superior\\Programacion\\Tema 6\\Ejercicios\\Ejercicios Regex\\Hola.txt";
        File archivo = new File(ruta);
        System.out.println(archivo.getAbsoluteFile());
        System.out.println(archivo.getParent());
        System.out.println(archivo.getName());
        System.out.println(archivo.getName().substring(archivo.getName().lastIndexOf(".") + 1));
        System.out.println(archivo.exists());
    }
}
