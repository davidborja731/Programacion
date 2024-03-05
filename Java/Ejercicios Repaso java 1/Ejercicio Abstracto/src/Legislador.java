public abstract class Legislador extends Persona {
    String ProvinciaQueRepresenta;
    String partidopolitico;
    public abstract String getcamaraenlaqueTrabaja();

    public String getProvinciaQueRepresenta() {
        return ProvinciaQueRepresenta;
    }

    public void setProvinciaQueRepresenta(String provinciaQueRepresenta) {
        ProvinciaQueRepresenta = provinciaQueRepresenta;
    }

    public String getPartidopolitico() {
        return partidopolitico;
    }

    public void setPartidopolitico(String partidopolitico) {
        this.partidopolitico = partidopolitico;
    }

    @Override
    public String toString() {
        return "Legislador{" +
                "ProvinciaQueRepresenta='" + ProvinciaQueRepresenta + '\'' +
                ", partidopolitico='" + partidopolitico + '\'' +
                ", dni='" + dni + '\'' +
                ", nombre='" + nombre + '\'' +
                '}';
    }
}
