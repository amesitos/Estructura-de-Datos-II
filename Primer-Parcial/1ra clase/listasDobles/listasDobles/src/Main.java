import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ListaDoble lista = new ListaDoble();
        lista.agregarAlInicio(10);
        lista.agregarAlInicio(20);
        lista.agregarAlFinal(30);
        lista.agregarAlFinal(40);
        lista.agregarAlInicio(50);
        Scanner s = new Scanner(System.in);

        System.out.println("Mostrar lista hacia adelante:");
        lista.mostrarAdelante();

        System.out.println("Ingrese indice del dato a buscar");
        int indiceABuscar = s.nextInt();
        Nodo nodoEncontrado = lista.buscarPorIndice(indiceABuscar);
        if (nodoEncontrado != null) {
            System.out.println("Nodo en índice " + indiceABuscar + ": " + nodoEncontrado.dato);
        } else {
            System.out.println("No se encontró el nodo en el índice " + indiceABuscar);
        }

        System.out.println("Modificar por indice - inserte el indice");
        int indiBuscar = s.nextInt();
        System.out.println("valor a agregar?");
        int datoModi = s.nextInt();
        lista.modificarPorIndice(indiBuscar, datoModi);
        System.out.println("Lista después de modificar el índice "+indiBuscar+": ");
        lista.mostrarAdelante();

        System.out.println("Agregue indice a eliminar");
        int indiEli = s.nextInt();
        lista.eliminarPorIndice(indiEli);
        System.out.println("Lista después de eliminar el índice "+indiEli+": ");
        lista.mostrarAdelante();

        System.out.println("Lista lista hacia atras");
        lista.mostrarAtras();

    }
}