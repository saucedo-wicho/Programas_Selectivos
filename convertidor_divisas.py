pesos = float(input("Ingrese la cantidad en pesos mexicanos (MXN): "))
print("Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
opcion = int(input("Ingrese la divisa a convertir: "))

match opcion:
    case 1:
        resultado = pesos / 16.5
        moneda = "USD"
    case 2:
        resultado = pesos / 18.0
        moneda = "EUR"
    case 3:
        resultado = pesos / 0.45
        moneda = "THB"
    case 4:
        resultado = pesos / 0.12
        moneda = "JPY"
    case 5:
        resultado = pesos / 0.013
        moneda = "KRW"
    case 6:
        resultado = pesos / 11.5 
        moneda = "AUD"
    case 7: 
        resultado = pesos / 2.8
        moneda = "PEN"
    case 8: 
        resultado = pesos / 8.2
        moneda = "CAD"
    case 9:
        resultado = pesos / 0.0023
        moneda = "VES"
    case 10: 
        resultado = pesos / 0.046
        moneda = "ARS"
    case _: 
        print("Opción no válida")
        resultado = 0
        moneda = ""
    
print(f"La conversión de {pesos} MXN a {moneda} es de: {resultado}")