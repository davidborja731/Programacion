package Clase;

import ClaseAbstracta.Bicicleta;

import java.util.Scanner;

public class BiciMontaña extends Bicicleta {
    private String tipo = "Montaña";

    public int getMarchas() {
        return Marchas;
    }

    public void setMarchas(int marchas) {
        Marchas = marchas;
    }

    private int Marchas;

    public BiciMontaña(String color, Double precio) {
        super(color, precio);
    }

    @Override
    public String toString() {
        return "BiciMontaña"+super.toString();
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    private int Marchas() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Dime el numero de marchas: ");
        int numeromar = scanner.nextInt();
        if (numeromar > 1 && numeromar < 6) {
            Marchas=numeromar;
        }else{
            System.out.println("Numero no valido");
        }
        return Integer.parseInt(null);
    }
}
