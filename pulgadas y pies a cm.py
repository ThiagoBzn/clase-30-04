# a) Por motivos históricos, algunos países utilizan unidades de medida que pueden resultarnos
extrañas. Un ejemplo de ello son los pies y las pulgadas, utilizados para medir longitudes. Un pie
equivale a doce pulgadas y una pulgada son 2,54 cm. Escribir un programa que pida al usuario
una longitud expresada en pies y pulgadas y que escriba esa longitud en centímetros.
Pista: Tu programa necesita solicitar dos valores al usuario, uno para la cantidad de pies y otro
para la cantidad de pulgadas.
# Solicitar al usuario la cantidad de pies y pulgadas
pies = float(input("Ingresa la cantidad de pies: "))
pulgadas = float(input("Ingresa la cantidad de pulgadas: "))

# Convertir pies y pulgadas a centímetros
longitud_cm = pies * 30.48 + pulgadas * 2.54

# Mostrar la longitud en centímetros
print("La longitud es:", longitud_cm, "cm")
