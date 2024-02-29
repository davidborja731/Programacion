package ClaseAbstracta;

import interf.Pintar;

import java.util.Scanner;

public class Bicicleta implements Pintar {
    private String Color;
    private Double precio;

    public Bicicleta(String color, Double precio) {
        Color = color;
        this.precio = precio;
    }

    @Override
    public String toString() {
        return "Bicicleta{" +
                "Color='" + Color + '\'' +
                ", precio=" + precio +
                '}';
    }

    public String getColor() {
        return Color;
    }

    public void setColor(String color) {
        Color = color;
    }

    public Double getPrecio() {
        return precio;
    }

    public void setPrecio(Double precio) {
        this.precio = precio;
    }


    @Override
    public Object pintar() {
        int precio_pintura=90;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Dime el nuevo color ");
        String nuevo = scanner.next();
        Color=nuevo;
        return null;
    }
}
