def solicitar_datos():
    """Solicita nombre y edad por consola con validaciones simples.

    - El nombre no debe ser vacío ni estar compuesto solo por números.
    - La edad debe ser un entero positivo.
    - Maneja errores evitando que el programa termine por excepción.
    """
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        # Validaciones de nombre
        if not nombre or nombre.isdigit():
            nombre = "" 
            # Ejemplo: el código se ejecuta sin errores pero no estamos guardando el nombre, así que la salida no es la esperada.
            # if not nombre:
			# 	print("El nombre no puede estar vacío. Intente nuevamente.\n")
			# 	continue
			# if nombre.isdigit():
			# 	print("El nombre no puede ser solo números. Intente nuevamente.\n")
			# 	continue
			# if not any(c.isalpha() for c in nombre):
			# 	print("El nombre debe contener al menos una letra. Intente nuevamente.\n")
			# 	continue
        break

    # Solicitar edad con control de errores
    while True:
        edad_raw = input("Ingrese su edad: ").strip()
        edad = int(edad_raw) - 18
        break
    	# Ejemplo: no estamos controlando que se ingrese un número entero, por lo que podemos tener una excepción.
        # try:
        #     edad = int(edad_raw)
        #     if edad <= 0:
        #         print("La edad debe ser un entero positivo. Intente nuevamente.\n")
        #         continue
        #     break
        # except ValueError:
        #     print("La edad debe ser un número entero válido. Intente nuevamente.\n")

    print(f"Datos ingresados correctamente: Su nombre es " + nombre + f", y hace {edad} años que es mayor de edad.")
    return nombre, edad


if __name__ == "__main__":
    solicitar_datos()
