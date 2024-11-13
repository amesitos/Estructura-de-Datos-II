import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        AgendaContactos agenda = new AgendaContactos();
        Scanner sc = new Scanner(System.in);
        int opcion = 0;

        while (opcion != 4) {
            System.out.println("\n------------------------------------------");
            System.out.println("|\t      | AGENDA DE CONTACTOS |\t      |");
            System.out.println("|-----------------------------------------|");
            System.out.println("|\t1. Agregar nuevo contacto.            |");
            System.out.println("|\t2. Eliminar contacto por teléfono.    |");
            System.out.println("|\t3. Mostrar contactos.                 |");
            System.out.println("|\t4. Salir                              |");
            System.out.println("|-----------------------------------------|");
            System.out.print(" Seleccione una opción: ");

            try {
                opcion = Integer.parseInt(sc.nextLine());

                switch (opcion) {
                    case 1:
                        System.out.print("\nIngrese el nombre del contacto: ");
                        String nombre = sc.nextLine();
                        System.out.print("Ingrese los apellidos del contacto: ");
                        String apellido = sc.nextLine();
                        System.out.print("Ingrese el número de teléfono: ");
                        String telefono = sc.nextLine();
                        agenda.ingresarContacto(nombre, apellido, telefono);
                        break;
                    case 2:
                        System.out.print("Ingrese el número de teléfono del contacto a eliminar: ");
                        telefono = sc.nextLine();
                        agenda.eliminarContacto(telefono);
                        break;
                    case 3:
                        agenda.mostrarAgenda();
                        break;
                    case 4:
                        System.out.println("Saliendo de la agenda...");
                        break;
                    default:
                        System.out.println("Opción inválida.\n");
                }
            } catch (Exception e) {
                System.out.println("Error: " + e  +"\n");
            }
        }

        sc.close();
    }
}