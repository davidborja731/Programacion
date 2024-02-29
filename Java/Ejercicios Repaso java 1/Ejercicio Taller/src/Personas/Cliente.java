package Personas;

import java.util.ArrayList;

public class Cliente extends Persona{
    int telefono;
    ArrayList lista_vehiculos=new ArrayList<>();

    public Cliente(String dni, String nombre, String primer_apellido) {
        super(dni, nombre, primer_apellido);
    }

    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    public ArrayList getLista_vehiculos() {
        return lista_vehiculos;
    }

    public void setLista_vehiculos(ArrayList lista_vehiculos) {
        this.lista_vehiculos = lista_vehiculos;
    }
}
