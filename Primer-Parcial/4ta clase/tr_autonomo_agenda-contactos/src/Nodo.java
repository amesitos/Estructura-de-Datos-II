
class Nodo {
    String nombre;
    String apellido;
    String telefono;
    Nodo siguiente;

    public Nodo(String nombre, String apellido, String telefono) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.telefono = telefono;
        this.siguiente = null;
    }
}