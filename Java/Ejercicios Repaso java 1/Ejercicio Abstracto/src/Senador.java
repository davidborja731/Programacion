public class Senador extends Legislador{
    @Override
    public String getcamaraenlaqueTrabaja() {
        return "Soy un senador";
    }

    @Override
    public String toString() {
        return "Senador{" +
                "ProvinciaQueRepresenta='" + ProvinciaQueRepresenta + '\'' +
                ", partidopolitico='" + partidopolitico + '\'' +
                ", dni='" + dni + '\'' +
                ", nombre='" + nombre + '\'' +
                '}';
    }
}
