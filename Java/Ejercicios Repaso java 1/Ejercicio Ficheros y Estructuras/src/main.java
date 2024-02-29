import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        File carpeta = new File("E:\\Grado Superior\\Programacion\\Java\\Ejercicios Repaso java 1\\Ejercicio Ficheros y Estructuras\\Equipos txt");
        HashMap<Ciclista, String> ciclista = new HashMap<>();
        HashMap<String, Integer> equipo = new HashMap<>();
        if (carpeta.exists() && carpeta.isDirectory()) {
            File[] archivos = carpeta.listFiles();
            for (File archivo : archivos) {
                try (FileReader fr = new FileReader(archivo);
                     BufferedReader br = new BufferedReader(fr)) {
                    String linea;
                    int numero = 1;
                    while ((linea = br.readLine()) != null) {
                        String[] nombre = linea.split("\\|".trim());
                        String nombre1 = nombre[0].trim();
                        String pais = nombre[1].trim();
                        int edad = Integer.parseInt(nombre[2].split(" ")[1]);
                        ciclista.put(new Ciclista(nombre1, pais, edad), archivo.getName().split("\\.txt")[0]);
                        equipo.put(archivo.getName().split("\\.txt")[0], numero++);
                    }
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
        }
        //pregunta 1 y 2=
        String equipomaximo = null;
        String equipominimo = null;
        Integer valor = null;
        int maxvalor = Integer.MIN_VALUE;
        int minvalor = Integer.MAX_VALUE;

        for (Map.Entry<String, Integer> entry : equipo.entrySet()) {
            valor = entry.getValue();
            if (valor > maxvalor) {
                maxvalor = valor;
                equipomaximo = entry.getKey();
            }
            if (valor < minvalor) {
                minvalor = valor;
                equipominimo = entry.getKey();
            }
        }
        System.out.println("El equipo mas grande es " + equipomaximo + " con " + maxvalor);
        System.out.println("El equipo mas pequeño es " + equipominimo + " con " + minvalor);
        //pregunta 3=
        String corredor = "Jonas Vingegaard";
        for (Map.Entry<Ciclista, String> entry : ciclista.entrySet()) {
            if (entry.getKey().getNombre().toLowerCase().contains(corredor.toLowerCase())) {
                System.out.println("El equipo es " + entry.getValue());
            }
        }
        //pregunta extra buscar corredor =
        Scanner scanner = new Scanner(System.in);
        System.out.println("Dime el numero de ciclistas que vas a buscar: ");
        int numerociclistas = scanner.nextInt();
        int numeroinicial = 0;
        while (numeroinicial < numerociclistas) {
            System.out.println("Dime el ciclista a buscar ");
            String ciclista1 = scanner.next().trim();
            boolean encontrado = false;
            for (Map.Entry<Ciclista, String> entry : ciclista.entrySet()) {
                if (entry.getKey().getNombre().toLowerCase().startsWith(ciclista1.toLowerCase())) {
                    System.out.println("El equipo es " + entry);
                    encontrado = true;
                }
            }
            if (!encontrado) {
                System.out.println("no existe");
            }
            numeroinicial = numeroinicial + 1;
        }
        //equipo con menor media de edad entre sus corredores Pregunta 4=
        HashMap<String, Integer> sumEdadEquipo = new HashMap<>();
        HashMap<String, Integer> numCorredoresEquipo = new HashMap<>();
        for (Map.Entry<Ciclista, String> entry : ciclista.entrySet()) {
            String equipos = entry.getValue();
            int edad = entry.getKey().getEdad();
            sumEdadEquipo.put(equipos, sumEdadEquipo.getOrDefault(equipos, 0) + edad);
            numCorredoresEquipo.put(equipos, numCorredoresEquipo.getOrDefault(equipos, 0) + 1);
        }
        String equipoEdadMediaMasBaja = null;
        double minEdadMedia = Double.MAX_VALUE;
        for (String equipos : sumEdadEquipo.keySet()) {
            double edadMedia = (double) sumEdadEquipo.get(equipos) / numCorredoresEquipo.get(equipos);
            if (edadMedia < minEdadMedia) {
                equipoEdadMediaMasBaja = equipos;
                minEdadMedia = edadMedia;
            }
        }
        System.out.println("El equipo con la edad media de sus corredores más baja es " + equipoEdadMediaMasBaja + " con una edad media de " + minEdadMedia);
        //equipo con mayor media de edad entre sus corredores Pregunta = 5
        String equipoEdadMediaMasAlta = null;
        double maxEdadMedia = Double.MIN_VALUE;
        for (String equipos : sumEdadEquipo.keySet()) {
            double edadMedia = (double) sumEdadEquipo.get(equipos) / numCorredoresEquipo.get(equipos);
            if (edadMedia > maxEdadMedia) {
                equipoEdadMediaMasAlta = equipos;
                maxEdadMedia = edadMedia;
            }
        }
        System.out.println("El equipo con la edad media de sus corredores más alta es " + equipoEdadMediaMasAlta + " con una edad media de " + maxEdadMedia);
    }
}






