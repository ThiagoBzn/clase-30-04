# c) Aldo quiere comprobar si con las tres notas que tiene en Historia está aprobado o no. Para ayudarlo, escribe un programa que le solicite los tres valores, y que luego muestre el promedio de sus notas.
def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

def main():
    print("Bienvenido, Aldo. Espero valores lo que hago, aparentemente en matemáticas eres peor que yo.")
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    promedio = calcular_promedio(nota1, nota2, nota3)
    print("El promedio de tus notas es:", promedio)

    if promedio >= 6.0:
        print("¡Felicidades! Estás aprobado.")
    else:
        print("Si te digo que lo siento es mentira. Nos vemos en marzo, a estudiar!")

if __name__ == "__main__":
    main()

