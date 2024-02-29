import java.util.List;
import java.util.ArrayList;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        String[] cochesElectricos = {"Tesla","Nio","BYD","Rymac","Ribian"};
        List<String> coches = new ArrayList<String>();
        System.out.println(coches.isEmpty());
        coches.add("Audi");
        coches.add("Mercedes");
        coches.add("Seat");
        coches.add("Porsche");
        coches.add("Dacia");
        coches.addAll(List.of(cochesElectricos));
        System.out.println(coches.isEmpty());
        for (int i=0;i < coches.size();i++) {
            System.out.println(coches.get(i) + " ");
        }
        for (String coche : coches){
            System.out.println(coche + " ");
        }
    }
}