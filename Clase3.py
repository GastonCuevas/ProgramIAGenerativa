from datetime import datetime, date
from typing import Union


def calcularDiasEntreFechas(fecha1: Union[str, date, datetime], fecha2: Union[str, date, datetime], formato: str = "%Y-%m-%d") -> int:
    """
    Calcula la cantidad absoluta de días entre dos fechas.

    Parámetros:
    - fecha1, fecha2: pueden ser str (con el formato indicado), datetime.date o datetime.datetime
    - formato: formato a usar si las fechas son cadenas (por defecto "%Y-%m-%d").

    Retorna:
    - Número entero de días entre ambas fechas (valor absoluto).
    """
    def _to_datetime(value: Union[str, date, datetime]) -> datetime:
        if isinstance(value, datetime):
            return value
        if isinstance(value, date):
            return datetime.combine(value, datetime.min.time())
        if isinstance(value, str):
            try:
                return datetime.strptime(value, formato)
            except ValueError as e:
                raise ValueError(f"Fecha inválida '{value}' para el formato '{formato}'") from e
        raise TypeError(f"Tipo no soportado: {type(value).__name__}")

    d1 = _to_datetime(fecha1)
    d2 = _to_datetime(fecha2)
    return abs((d2 - d1).days)


#Escribir una función que 
#Reciba un número entero positivo 
# calcule el factorial de un número dado.
#devuelve el resultado con un print y la cadena "El factorial de {n} es {resultado}"

def calcularFactorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcularFactorial(numero - 1)


#Escribir una función que
#reciba por parámetro el precio de un producto y la tasa de interés anual (en porcentaje).
#calcula el interes a un precio
#donde la tasa de interés un número por la cantidad de años
#devuelve el resultado con un print y la cadena "El interés sobre un producto de {precio} con una tasa de interés anual de {tasa}% es {interes}"

def calcularInteresSimple(precio, tasaAnual, montoFijoAdicional, anios=1):
    interes = precio * (tasaAnual / 100) * anios + montoFijoAdicional
    print(f"El interés sobre un producto de {precio} con una tasa de interés anual de {tasaAnual}% es {interes}")
    return interes


if __name__ == "__main__":
    print("Hola, mundo!")

    dias = calcularDiasEntreFechas("2023-01-01", "2023-01-31")
    print(f"{dias} días entre las dos fechas.")

    numero = 5
    resultado = calcularFactorial(numero)
    print(f"El factorial de {numero} es {resultado}")

    # ejecutar calcular_interes con un precio de 1000 y la tasa de interés siendo el factorial de 5
    calcularInteresSimple(1000, calcularFactorial(5), 50, 2)
