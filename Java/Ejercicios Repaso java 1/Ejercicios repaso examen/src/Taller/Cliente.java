package Taller;

import java.util.ArrayList;
import java.util.List;

public class Cliente extends Persona {
    private String telefono;
    private ArrayList<Vehiculos> vehiculos;

    public Cliente(String dni, String nombre, String primerApellido, String telefono) {
        super(dni, nombre, primerApellido);
        this.telefono = telefono;
        this.vehiculos = new ArrayList<>();
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public List<Vehiculos> getVehiculos() {
        return vehiculos;
    }

    public void setVehiculos(ArrayList<Vehiculos> vehiculos) {
        this.vehiculos = vehiculos;
    }

    @Override
    public String toString() {
        return "Cliente{" +
                "telefono='" + telefono + '\'' +
                ", vehiculos=" + vehiculos +
                ", dni='" + dni + '\'' +
                ", nombre='" + nombre + '\'' +
                ", primerApellido='" + primerApellido + '\'' +
                '}';
    }

    @Override
    public void identificarse() {
        System.out.println("DNI: " + dni + ", Nombre: " + nombre + ", Apellido: " + primerApellido + ", Teléfono: " + telefono);
    }

    public void agregarVehiculo(Vehiculos vehiculo) {
        this.vehiculos.add(vehiculo);
    }
}
