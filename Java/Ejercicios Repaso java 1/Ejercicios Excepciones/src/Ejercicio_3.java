public class Ejercicio_3 {
    public static void main(String[] args) {
        try {
            throw new Laexcepcion("CASI");
        } catch (Laexcepcion e) {
            System.out.println(e.getMessage());
        }
    }

    public static class Laexcepcion extends Exception {
        public Laexcepcion(String mensaje) {
            super(mensaje);
        }
    }
}
