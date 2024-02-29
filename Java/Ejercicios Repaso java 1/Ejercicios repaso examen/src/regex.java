import java.util.regex.Pattern;

public class regex {
    private static String REGEX_CORREO = "^[A-Za-z0-9+_.-]+@(.+)$";

    public static boolean validar(String correo) {
        Pattern pattern = Pattern.compile(REGEX_CORREO);
        return pattern.matcher(correo).matches();
    }

    public static void main(String[] args) {
        String correo = "ejemplo@dominio.com";
        System.out.println("El correo " + correo + " es válido: " + validar(correo));
    }
}


