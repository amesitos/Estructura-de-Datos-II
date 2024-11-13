
class AgendaContactos {
    private Nodo primero;
    private Nodo ultimo;

    public AgendaContactos() {
        this.primero = null;
        this.ultimo = null;
    }

    public boolean agendaVacia() {
        return primero == null;
    }

    public void ingresarContacto(String nombre, String apellido, String telefono) {
        Nodo nuevoNodo = new Nodo(nombre, apellido, telefono);
        if (agendaVacia()) {
            primero = ultimo = nuevoNodo;
        } else {
            ultimo.siguiente = nuevoNodo;
            ultimo = nuevoNodo;
        }
        System.out.println("El contacto " + nombre + " " + apellido + " con número " + telefono + " ha sido registrado.\n");
    }

    public void eliminarContacto(String telefono) {
        if (agendaVacia()) {
            System.out.println("La agenda está vacía.");
            return;
        }

        Nodo auxiliar = primero;
        Nodo anterior = null;

        while (auxiliar != null) {
            if (auxiliar.telefono.equals(telefono)) {
                if (anterior == null) {
                    primero = auxiliar.siguiente;
                } else {
                    anterior.siguiente = auxiliar.siguiente;
                }
                if (auxiliar == ultimo) {
                    ultimo = anterior;
                }
                System.out.println("Contacto con número " + telefono + " ha sido eliminado.");
                return;
            }
            anterior = auxiliar;
            auxiliar = auxiliar.siguiente;
        }
        System.out.println("Número no encontrado en la agenda.");
    }

    public void mostrarAgenda() {
        if (agendaVacia()) {
            System.out.println("La agenda está vacía.");
            return;
        }


        int indice = 0;
        Nodo contactos = primero;

        System.out.println("\n------------------------------------------------");
        System.out.println("|\t         | AGENDA DE CONTACTOS |\t       |");
        System.out.println("|----------------------------------------------|");
        System.out.printf("| %-7s | %-18s | %-13s |\n", "ÍNDICE", "NOMBRE", "TELÉFONO");
        System.out.println("|----------------------------------------------|");

        while (contactos != null) {
            System.out.printf("| %-7d | %-18s | %-13s |\n", indice, contactos.nombre + " " + contactos.apellido, contactos.telefono);
            contactos = contactos.siguiente;
            indice++;
        }
        System.out.println("|----------------------------------------------|");
    }
}