public class Main_EJ_1 {
    public static void main(String[] args) {
        EJ_1 pelicula1 = new EJ_1("Santiago Segura", "Padre no hay mas que uno", 2020);
        EJ_1 pelicula2 = new EJ_1("Santiago Segura", "Padre no hay mas que uno 2", 2022);
        System.out.println(pelicula1.infoPelicula());
        System.out.println(pelicula1.esantiguo());
        System.out.println(pelicula2.calculoantiguedad());
    }
}