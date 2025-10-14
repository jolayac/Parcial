from usuarios import Usuario
from libros import Libro


class Biblioteca:
    def __init__(self, nombre):
        self.nombre_bibliotecario = nombre
        self.lista_usuarios = []
        self.lista_libros = []

    def registrar_usuario(self):
        nombre = input("\nNombre del usuario:\n> ").strip(
        ).title()   # Pide nombre
        documento = input("\nNúmero de documento:\n> ").strip(
        ).title()   # Pide número de documento
        usuario = Usuario(nombre, documento)    # Crea el usuario
        self.lista_usuarios.append(usuario)
        print(
            f"\n{'-' * 30}\nUsuario creado.\n - Nombre: {usuario.nombre}\n - Documento: {usuario.documento}\n")

    def registrar_libro(self):
        # Pedir el título:
        titulo = input("\nTítulo del libro:\n> ").strip().title()
        # Pedir el autor
        autor = input("\nAutor del libro:\n> ").strip().title()
        # Para verificar la categoria:
        categoria_input = input(
            "Escriba la caegoría del libro. Las opciones son:\n1. Romance\n2. Comedia\n3. Historia\n> ")
        while True:
            # Transforma el resultado del usuario en minusculas
            categoria = categoria_input.strip().lower()
            if categoria == "terror" or categoria == "1":
                categoria_valida = "Terror"
                break
            elif categoria == "comedia" or categoria == "2":
                categoria_valida = "Comedia"
                break
            elif categoria == "historia" or categoria == "3":
                categoria_valida = "Historia"
                break  # Dependiendo de la opción, se categoriza el libro
            else:
                categoria_input = input(  # Señala que la opción elegida por el usuario es incorrecta o inexistente
                    f"\n\"{categoria_input}\" No es una opción válida.\nIntente de nuevo.\n> ")
        libro = Libro(titulo, autor, categoria_valida)
        self.lista_libros.append(libro)
        print(
            f"{'-' * 30}\nLibro creado\nTítulo: {libro.titulo}\nAutor: {libro.autor}\nCategoría: {libro.categoria}\n")

    def mostrar_usuarios(self):
        for usu in self.lista_usuarios:
            print(f"\nNombre: {usu.nombre}\nDocumento: {usu.documento}\n")

    def mostrar_libros(self):
        for lib in self.lista_libros:
            print(
                f"\nTítulo: {lib.titulo}\nAutor: {lib.autor}\nCategoría: {lib.categoria}\n")

    def mostrar_menu(self):
        while True:
            seleccion = input(
                "\nSeleccione lo que quiere hacer (escriba el número de la opción que quiere seleccionar):\n1. Registrar un nuevo usuario.\n2. Registrar un libro.\n3. Mostrar usuarios.\n4. Mostrar libros.\n> ").strip()
            if seleccion == "1":    # Registrar un nuevo usuario.
                self.registrar_usuario()
            elif seleccion == "2":  # Registrar un libro.
                self.registrar_libro()
            elif seleccion == "3":  # Mostrar usuarios.
                self.mostrar_usuarios()
            elif seleccion == "4":  # Mostrar libros.
                self.mostrar_libros()
            else:
                print(
                    f"\n\"{seleccion}\" no está entre las opciones (1, 2, 3 y 4).\nIntente de nuevo.\n")


def registrar_bibliotecario():
    nombre = input("\nIngrese su nombre\n> ").strip().title()
    bibliotecario = Biblioteca(nombre)
    return bibliotecario


def main():
    bibliotecario = registrar_bibliotecario()
    bibliotecario.mostrar_menu()


if __name__ == "__main__":
    main()
