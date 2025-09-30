import usuarios
import libros

usuarios_lista = []
libros_lista = []


def nuevo_usuario():
    usuario = usuarios.registrar_usuario()
    usuarios_lista.append({usuario.nombre: usuario.documento})


def nuevo_libro():
    libro = libros.registrar_libro()
    libros_lista.append({libro.titulo: libro.autor})


def mostrrar_usuarios():
    for usu in usuarios_lista:
        print(f"\n{usu}\n")


def mostrar_libros():
    for lib in libros_lista:
        print(f"\n{lib}\n")


def main():
    while True:
        seleccion = input(
            "\nSeleccione lo que quiere hacer (escriba el número de la opción que quiere seleccionar):\n1. Registrar un nuevo usuario.\n2. Registrar un libro.\n3. Mostrar usuarios.\n4. Mostrar libros.\n>").strip()
        if seleccion == "1":    # Registrar un nuevo usuario.
            nuevo_usuario()
        elif seleccion == "2":  # Registrar un libro.
            nuevo_libro()
        elif seleccion == "3":  # Mostrar usuarios.
            mostrrar_usuarios()
        elif seleccion == "4":  # Mostrar libros.
            mostrar_libros()
        else:
            seleccion = input(
                f"\n\"{seleccion}\" no está entre las opciones (1 o 2).\nIntente de nuevo.\n>")


main()
