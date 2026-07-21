calificacion_num = int(input("Ingrese su calificación (0-100): "))
letra = ""

if calificacion_num < 0 or calificacion_num > 100:
    print("Ingrese valores válidos")
    calificacion_num = int(input("Ingrese su calificación (0-100): "))

    
if calificacion_num >= 90:
    letra = "A"
elif calificacion_num >= 80:
    letra = "B"
elif calificacion_num >= 70:
    letra = "C"
elif calificacion_num >= 60:
    letra = "D"
else:
     letra = "F"
    
print(f"La calificación {calificacion_num} corresponde a {letra}")