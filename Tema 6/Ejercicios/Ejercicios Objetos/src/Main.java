// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        Persona p1 = new Persona("Antonio","Recio","45678543H");
        Persona p2= new Persona();
        p2.setApellidos("Perez");
        p2.setDNI("213454667J");
        p2.setNombre("Juan");
        System.out.println(p1.toString());
        System.out.println(p1.toString());
    }
}
