# d) Un comerciante necesita ayuda para calcular el importe de una venta que acaba de realizar. Dispone del monto neto, y necesita agregar el porcentaje correspondiente al IVA, es decir, sumarle al importe que tiene un 21% más. Para ello, realizar un programa que solicite al usuario el monto neto y le sume el 21%, mostrando el resultado final en la pantalla. Reto 1: utiliza una sola variable.
def main():
    monto_neto = float(input("Ingrese el monto neto de la venta: "))

    # Calcular el monto total sumando el 21% de IVA
    monto_total = monto_neto * 1.21

    print(f"El monto neto de la venta es: $ARS{monto_neto:.2f}")
    print(f"El monto total con el 21% de IVA es: $ARS{monto_total:.2f}")

if __name__ == "__main__":
    main()

