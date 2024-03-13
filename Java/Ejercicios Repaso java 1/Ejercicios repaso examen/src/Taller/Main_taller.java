package Taller;

public class Main_taller {
    public static void main(String[] args) {
        // Crear un propietario
        Propietario propietario = new Propietario("12345678A", "juan", "garcia", "Calle Falsa 123");

        // Crear un taller
        Taller taller = new Taller("taller juan", "Calle Real 456", propietario);

        // Crear un cliente
        Cliente cliente = new Cliente("87654321B", "cliente", "ApellidoCliente", "987654321");
        Cliente cliente1 = new Cliente("845455351B", "cliente1", "ApellidoCliente1", "987654321");
        // Crear un coche y una moto
        Coche coche = new Coche("1234ABC", "Ford", "puma", 180, 140);
        Coche coche2 = new Coche("144334ABC", "Seat", "panda", 156, 187);
        motos moto = new motos("5678DEF", "Yamaha", "h125", true);

        // Añadir los vehículos al cliente
        cliente.agregarVehiculo(coche);
        cliente1.agregarVehiculo(coche);
        cliente.agregarVehiculo(moto);
        cliente1.agregarVehiculo(coche2);

        // Añadir el cliente al taller
        taller.agregarCliente(cliente);

        // Identificar al propietario, al cliente y a los vehículos
        propietario.identificarse();
        cliente.identificarse();
        coche.identificarse();
        moto.identificarse();
        cliente1.identificarse();
        // Imprimir los datos de las clases usando toString
        System.out.println(propietario);
        System.out.println(cliente);
        System.out.println(coche);
        System.out.println(moto);
        System.out.println(taller);
    }
}

