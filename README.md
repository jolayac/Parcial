# Parcial
__Juan Sebastián Olaya Castañeda__
>Súplica: Sé que el README se hizo después de las 6:30pm. Nada que hacer. El código funciona como debe.


## Código principal
Despliega un menú de opciones que puede:
Registrar un nuevo usuario,
Registrar un libro,
Mostrar usuarios,
Mostrar libros,

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


## Opción 1: añadir un nuevo usuario

Al seleccionar esta opción, se puede crear un nuevo usuario en base al input que se hace de nombre y documento. Después, se guarda ese usuario a una lista ``usuarios_lista````
### Código
```
python
def nuevo_usuario():
    usuario = usuarios.registrar_usuario()
    usuarios_lista.append({usuario.nombre: usuario.documento})
```
### Resultado en la terminal
        Seleccione lo que quiere hacer (escriba el número de la opción que quiere seleccionar):
        1. Registrar un nuevo usuario.
        2. Registrar un libro.
        3. Mostrar usuarios.
        4. Mostrar libros.
        >1

        Ingrese su nombre:
        >Juancho

        Ingrese su número de documento:
        >123456789


## Opción 2: añadir un nuevo libro

Al seleccionar esta opción, se puede crear un nuevo libro en base al input que se hace de nombre y documento. Después, se guarda ese usuario a una lista ``libros_lista``.

### Código

        def nuevo_libro():
            libro = libros.registrar_libro()
            libros_lista.append({libro.titulo: libro.autor})

### Resultado en la terminal

        Seleccione lo que quiere hacer (escriba el número de la opción que quiere seleccionar):
        1. Registrar un nuevo usuario.
        2. Registrar un libro.
        3. Mostrar usuarios.
        4. Mostrar libros.
        >2

        Título del libro:
        >Cien años de soledad

        Autor del libro:
        >Gabriel 
        Escriba la caegoría del libro. Las opciones son:
        1. Romance
        2. Comedia
        3. Historia
        >1

## Opción 3: mostrar usuarios

Imprime una tupla con los datos del usuario (nombre y documento).

### Código

        def mostrrar_usuarios():
            for usu in usuarios_lista:
                print(f"\n{usu}\n")


### Resultado en la terminal

        Seleccione lo que quiere hacer (escriba el número de la opción que quiere seleccionar):
        1. Registrar un nuevo usuario.
        2. Registrar un libro.
        3. Mostrar usuarios.
        4. Mostrar libros.
        >3

        {'Juancho': '123456789'}


        {'Mateo': '123467865'}


## Opción 3: mostrar libros

Imprime una tupla con el nombre y el autor de los libros agregados

### Código

        def mostrar_libros():
            for lib in libros_lista:
                print(f"\n{lib}\n")



### Resultado en la terminal

        Seleccione lo que quiere hacer (escriba el número de la opción que quiere seleccionar):
            1. Registrar un nuevo usuario.
            2. Registrar un libro.
            3. Mostrar usuarios.
            4. Mostrar libros.
            >4

            {'Cien Años De Soledad': 'Gabriel'}


            {'La Peste': 'Albert'}





