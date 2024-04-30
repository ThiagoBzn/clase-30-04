# e) Un fabricante de cámaras de acción indica en sus publicidades la duración de la batería de sus productos utilizando como unidades segundos. Por ejemplo, el modelo “Pro 4K” tiene una batería cuya duración es, según el manual, de 8000 segundos. Realiza un programa que pida una cantidad de segundos y que escriba cuántas horas, minutos y segundos son.
def convertir_segundos(segundos):
    horas = segundos // 3600
    segundos_restantes = segundos % 3600
    minutos = segundos_restantes // 60
    segundos_finales = segundos_restantes % 60
    return horas, minutos, segundos_finales

def main():
    segundos_totales = int(input("Ingrese la cantidad de segundos: "))

    horas, minutos, segundos = convertir_segundos(segundos_totales)

    print("Equivalente en:")
    print("Horas:", horas)
    print("Minutos:", minutos)
    print("Segundos:", segundos)

if __name__ == "__main__":
    main()
