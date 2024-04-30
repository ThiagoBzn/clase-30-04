# b) Ana ha encontrado en casa de su abuelo un antiguo termómetro, que está graduado en grados Fahrenheit. Luego de mirar con atención, ve que el termómetro indica una temperatura de 78°F. Ana no sabe si el termómetro está funcionando mal, o se trata de una lectura correcta. Vamos a intentar ayudarla. Escribe un programa que pida una temperatura en grados Celsius y que muestre esa temperatura en grados Fahrenheit. Y otro pida una temperatura en grados Fahrenheit y que escriba esa temperatura en grados Celsius. Pista: la relación entre grados Celsius (C) y grados Fahrenheit (F) F = 1.8 * C + 32, y la relación entre grados Celsius (C) y grados Fahrenheit (F) es C = (F - 32) / 1.8
def celsius_a_fahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

def main():
    print("¿Qué conversión deseas realizar?")
    print("1. Convertir de grados Celsius a grados Fahrenheit.")
    print("2. Convertir de grados Fahrenheit a grados Celsius.")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print("La temperatura en grados Fahrenheit es:", fahrenheit)
    elif opcion == "2":
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        celsius = fahrenheit_a_celsius(fahrenheit)
        print("La temperatura en grados Celsius es:", celsius)
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    main()

