package Taller;

public class Coche extends Vehiculos {
    private double anchura;
    private double altura;

    public Coche(String matricula, String marca, String modelo, double anchura, double altura) {
        super(matricula, marca, modelo);
        this.anchura = anchura;
        this.altura = altura;
    }

    public double getAnchura() {
        return anchura;
    }

    public void setAnchura(double anchura) {
        this.anchura = anchura;
    }

    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    @Override
    public String toString() {
        return "Coche{" +
                "anchura=" + anchura +
                ", altura=" + altura +
                ", matricula='" + matricula + '\'' +
                ", marca='" + marca + '\'' +
                ", modelo='" + modelo + '\'' +
                '}';
    }

    @Override
    public void identificarse() {
        System.out.println("Matrícula: " + matricula + ", Marca: " + marca + ", Modelo: " + modelo + ", Anchura: " + anchura + ", Altura: " + altura);
    }
}
