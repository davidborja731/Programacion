package Taller;

public class motos extends Vehiculos {
    private boolean llevaLimitador;

    public motos(String matricula, String marca, String modelo, boolean llevaLimitador) {
        super(matricula, marca, modelo);
        this.llevaLimitador = llevaLimitador;
    }

    public boolean isLlevaLimitador() {
        return llevaLimitador;
    }

    public void setLlevaLimitador(boolean llevaLimitador) {
        this.llevaLimitador = llevaLimitador;
    }

    @Override
    public String toString() {
        return "Moto{" +
                "llevaLimitador=" + llevaLimitador +
                ", matricula='" + matricula + '\'' +
                ", marca='" + marca + '\'' +
                ", modelo='" + modelo + '\'' +
                '}';
    }

    @Override
    public void identificarse() {
        System.out.println("Matrícula: " + matricula + ", Marca: " + marca + ", Modelo: " + modelo + ", Lleva limitador: " + (llevaLimitador ? "Sí" : "No"));
    }
}
