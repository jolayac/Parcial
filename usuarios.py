class Usuario:
    def __init__(self, nombre: str, documento: str):
        self.nombre = nombre
        self.documento = documento


def registrar_usuario():
    nombre = input("\nIngrese su nombre:\n>").strip().title()
    documento = input("\nIngrese su número de documento:\n>").strip().title()
    usuario = Usuario(nombre, documento)
    return usuario
