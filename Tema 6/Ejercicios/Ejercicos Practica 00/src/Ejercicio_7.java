import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.lang.Math;
public class Ejercicio_7 {
    public static void main(String[] args) {
        List<String> abecedario = new ArrayList<>();
        Collections.addAll(abecedario,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","W","X","Y","Z");
        int Numeros1 = (int)Math.floor(Math.random()*27);
        String letra = abecedario.get(Numeros1);
        System.out.println(letra);
        if ("A".equals(letra)) {
            System.out.println("Es una vocal");
            System.exit(1);
        }
        if ("E".equals(letra)) {
            System.out.println("Es una vocal");
            System.exit(1);
        }
        if ("I".equals(letra)) {
            System.out.println("Es una vocal");
            System.exit(1);
        }
        if ("O".equals(letra)) {
            System.out.println("Es una vocal");
            System.exit(1);
        }
        if ("U".equals(letra)) {
            System.out.println("Es una vocal");
            System.exit(1);
        }
        else {
            System.out.println("Es una consonante");
        }
    }
}
