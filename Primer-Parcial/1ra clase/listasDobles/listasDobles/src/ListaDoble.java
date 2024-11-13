class ListaDoble {
    Nodo cabeza;

    public ListaDoble() {
        cabeza = null;
    }

    public void agregarAlInicio(int dato) {
        Nodo nuevoNodo = new Nodo(dato);
        if (cabeza == null) {
            cabeza = nuevoNodo;
        } else {
            nuevoNodo.siguiente = cabeza;
            cabeza.anterior = nuevoNodo;
            cabeza = nuevoNodo;
        }
    }

    public void agregarAlFinal(int dato) {
        Nodo nuevoNodo = new Nodo(dato);
        if (cabeza == null) {
            cabeza = nuevoNodo;
        } else {
            Nodo temp = cabeza;
            while (temp.siguiente != null) {
                temp = temp.siguiente;
            }
            temp.siguiente = nuevoNodo;
            nuevoNodo.anterior = temp;
        }
    }

    public void mostrarAdelante() {
        Nodo temp = cabeza;
        while (temp != null) {
            System.out.print(temp.dato + " ");
            temp = temp.siguiente;
        }
        System.out.println();
    }

    public void mostrarAtras() {
        Nodo temp = cabeza;
        if (temp == null) return;

        while (temp.siguiente != null) {
            temp = temp.siguiente;
        }

        while (temp != null) {
            System.out.print(temp.dato + " ");
            temp = temp.anterior;
        }
        System.out.println();
    }

    public Nodo buscarPorIndice(int indice) {
        Nodo temp = cabeza;
        int contador = 0;
        while (temp != null) {
            if (contador == indice) {
                return temp;
            }
            temp = temp.siguiente;
            contador++;
        }
        return null;
    }

    public void eliminarPorIndice(int indice) {
        if (cabeza == null) return;
        Nodo temp = buscarPorIndice(indice);
        if (temp == null) return;

        if (temp == cabeza) {
            cabeza = temp.siguiente;
            if (cabeza != null) {
                cabeza.anterior = null;
            }
        } else {
            temp.anterior.siguiente = temp.siguiente;
            if (temp.siguiente != null) {
                temp.siguiente.anterior = temp.anterior;
            }
        }
    }

    public void modificarPorIndice(int indice, int nuevoDato) {
        Nodo temp = buscarPorIndice(indice);
        if (temp != null) {
            temp.dato = nuevoDato;
        }
    }
}
