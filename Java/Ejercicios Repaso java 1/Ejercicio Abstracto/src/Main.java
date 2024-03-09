import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Legislador> Lista1 = new ArrayList<>();
        Diputado diputado1 = new Diputado();
        diputado1.setNombre("Joaquin");
        diputado1.setDni("30123456L");
        diputado1.setProvinciaQueRepresenta("valencia");
        diputado1.setPartidopolitico("PSOE");

        Senador senador1 = new Senador();
        senador1.setNombre("Pedro Manuel Rollan Ojeda");
        senador1.setDni("98765321P");
        senador1.setProvinciaQueRepresenta("No se");
        senador1.setPartidopolitico("PP");

        Diputado diputado2 = new Diputado();
        diputado2.setNombre("Antonia");
        diputado2.setDni("85693214Ñ");
        diputado2.setProvinciaQueRepresenta("La rioja");
        diputado2.setPartidopolitico("Podemos");

        Diputado diputado3 = new Diputado();
        diputado3.setNombre("Pepa");
        diputado3.setDni("85632140K");
        diputado3.setProvinciaQueRepresenta("Sevilla");
        diputado3.setPartidopolitico("Sumar");
        Lista1.add(diputado1);
        Lista1.add(senador1);
        Lista1.add(diputado2);
        Lista1.add(diputado3);

        //recorro la lista
        System.out.println(Lista1);
        //añado al archivo.txt
        try {
            BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("Ladrones.txt"));
            for (Legislador legislador : Lista1) {
                bufferedWriter.write(legislador.toString());
                bufferedWriter.newLine();
                bufferedWriter.flush();
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        //Ejercicio 3

    }
}

