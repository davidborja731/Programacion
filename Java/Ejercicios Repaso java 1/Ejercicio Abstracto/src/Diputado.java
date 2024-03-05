public class Diputado extends Legislador{
    @Override
    public String getcamaraenlaqueTrabaja() {
        return "Mensaje de ejemplo";
    }

    @Override
    public String toString() {
        return "Diputado{" +
                "ProvinciaQueRepresenta='" + ProvinciaQueRepresenta + '\'' +
                ", partidopolitico='" + partidopolitico + '\'' +
                ", dni='" + dni + '\'' +
                ", nombre='" + nombre + '\'' +
                '}';
    }
}
