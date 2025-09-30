# Juan Sebastián Olaya Castañeda

class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria


def registrar_libro():
    # Pedir el título:
    titulo = input("\nTítulo del libro:\n>").strip().title()
    # Pedir el autor
    autor = input("\nAutor del libro:\n>").strip().title()
    # Para verificar la categoria:
    categoria_input = input(
        "Escriba la caegoría del libro. Las opciones son:\n1. Romance\n2. Comedia\n3. Historia\n>")
    while True:
        categoria = categoria_input.strip().lower()
        if categoria == "terror" or categoria == "1":
            categoria_valida = "Terror"
            break
        elif categoria == "comedia" or categoria == "2":
            categoria_valida = "Comedia"
            break
        elif categoria == "historia" or categoria == "2":
            categoria_valida = "Historia"
            break
        else:
            categoria_input = input(
                f"\n\"{categoria_input}\" no es una opción válida.\nIntete de nuevo.\n>")

    libro = Libro(titulo, autor, categoria_valida)
    return libro
