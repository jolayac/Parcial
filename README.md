# Parcial
__Juan Sebastián Olaya Castañeda__


## Código principal
Despliega un menú de opciones que puede:
Registrar un nuevo usuario,
Registrar un libro,
Mostrar usuarios,
Mostrar libros,

```python
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
```

### Opción 2: añadir un nuevo libre

Al seleccionar esta opción, se puede crear un nuevo usuario en base al input que se hace de nombre y documento. Después, se guarda ese usuario a una lista ``usuarios_lista````

```
python
def nuevo_usuario():
    usuario = usuarios.registrar_usuario()
    usuarios_lista.append({usuario.nombre: usuario.documento})
```

### Opción 3: añadir un nuevo libro

Al seleccionar esta opción, se puede crear un nuevo libro en base al input que se hace de nombre y documento. Después, se guarda ese usuario a una lista ``libros_lista``.

```
python
def nuevo_usuario():
    usuario = usuarios.registrar_usuario()
    usuarios_lista.append({usuario.nombre: usuario.documento})
```



## Resultados





