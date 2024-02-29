package Clase;

import ClaseAbstracta.Bicicleta;

public class Bicipaseo extends Bicicleta {
    private String tipo;

    public Bicipaseo(String color, Double precio) {
        super(color, precio);
    }

    @Override
    public String toString() {
        return "Bicipaseo"+super.toString();
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
}
