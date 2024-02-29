public class Ej13  {
    public static void main(String[] args) {
        int segundos = 9500;

            int horas = (segundos/3600);
            int minutos=(segundos/60%60);
            int segundo=(segundos%60);
            System.out.println(""+horas +""+ minutos+""+ segundo);
    }
}
