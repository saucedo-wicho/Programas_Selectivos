celsius = float(input("Ingrese la temperatura en grados celsius: "))
opcion = int(input("Ingrese la opción a convertir 1(farenheit), 2(kelvin): "))

match opcion:
    case 1:
        resultado = celsius * 1.8 + 32
        unidad = "F"
    case 2:
        resultado = celsius + 273.15
        unidad = "K"
    case _:
        resultado = None
        print("Ingrese una opción válida")
        
if resultado is not None: 
    print(f"La conversión de {celsius}° celsius es igual a {resultado} {unidad}")
