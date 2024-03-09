import java.time.LocalDate;
import java.util.Scanner;

public class EJ_1 {
    private String director;
    private String titulo;
    private int año;

    public EJ_1(String director, String titulo, int año) {
        this.director = director;
        this.titulo = titulo;
        this.año = año;
    }

    public String getDirector() {
        return director;
    }

    public void setDirector(String director) {
        this.director = director;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public int getAño() {
        return año;
    }

    public void setAño(int año) {
        this.año = año;
    }

    public String infoPelicula() {
        return "Dirigida por " + director + " se llama " + titulo + " y se lanzo en " + año;
    }

    public boolean esantiguo() {
        return año < 2000;
    }

    public String actualizaDatos() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Dime el nuevo director ");
        String nuevodirector = scanner.next();
        System.out.println("Dime el nuevo titulo ");
        String nuevoTitulo = scanner.next();
        System.out.println("Dime el nuevo año ");
        int nuevoAño = scanner.nextInt();
        director = nuevodirector;
        titulo = nuevoTitulo;
        año = nuevoAño;
        return (" ");
    }
    public String calculoantiguedad() {
        LocalDate currentDate = LocalDate.now();
        int año = currentDate.getYear();
        int calculo = año - getAño();
        return "La pelicula tiene " + calculo + " años de antiguedad";
    }
    public void CompararPeliculas() {


    }
}


