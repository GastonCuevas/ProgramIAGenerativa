print("Hola, mundo!")

from datetime import datetime

def calculateDaysBeetweenDates(date1, date2):
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

days = calculateDaysBeetweenDates("2023-01-01", "2023-01-31")
print(f"{days} días entre las dos fechas.")

#Escribir una función que 
#Reciba un número entero positivo 
# calcule el factorial de un número dado.
#devuelve el resultado con un print y la cadena "El factorial de {n} es {resultado}"
def calcular_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_factorial(n-1)

numero = 5
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es {resultado}")

#Escribir una función que
#reciba por parámetro el precio de un producto y la tasa de interés anual (en porcentaje).
#calcula el interes a un precio
#donde la tasa de interés un número por la cantidad de años
#devuelve el resultado con un print y la cadena "El interés sobre un producto de {precio} con una tasa de interés anual de {tasa}% es {interes}"
def calcular_interes(precio, tasa, montoFijoAdicional, years=1):
    interes = precio * (tasa / 100) * years + montoFijoAdicional
    print(f"El interés sobre un producto de {precio} con una tasa de interés anual de {tasa}% es {interes}")
    return interes

#ejecutar calcular_interes con un precio de 1000 y la tasa de interés siendo el factorial de 5
calcular_interes(1000, calcular_factorial(5), 50, 2)
