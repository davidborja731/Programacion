package Taller;

public class Propietario extends Persona {
    private String direccion;

    public Propietario(String dni, String nombre, String primerApellido, String direccion) {
        super(dni, nombre, primerApellido);
        this.direccion = direccion;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    @Override
    public String toString() {
        return "Propietario{" +
                "direccion='" + direccion + '\'' +
                ", dni='" + dni + '\'' +
                ", nombre='" + nombre + '\'' +
                ", primerApellido='" + primerApellido + '\'' +
                '}';
    }

    @Override
    public void identificarse() {
        System.out.println("DNI: " + dni + ", Nombre: " + nombre + ", Apellido: " + primerApellido + ", Dirección: " + direccion);
    }
}

