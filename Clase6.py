def solicitar_datos():
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if nombre and not any(char.isdigit() for char in nombre):
            break
        print("El nombre no debe estar vacío ni contener números. Intente nuevamente.")

    while True:
        edad_raw = input("Ingrese su edad: ").strip()
        edad = int(edad_raw) - 18
        break

    print(f"Datos ingresados correctamente: Su nombre es {nombre}, y hace {edad} años que es mayor de edad.")
    return nombre, edad


if __name__ == "__main__":
    solicitar_datos()
