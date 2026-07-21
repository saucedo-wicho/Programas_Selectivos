calificacion_parcial = float(input("Ingrese la calificación de su parcial (0 - 100): "))
proyecto = float(input("Ingrese la calificación de su proyecto (0 - 100): "))
examen = float(input("Ingrese la calificación de su examen (0-100): "))

if calificacion_parcial < 0 or calificacion_parcial > 100 or proyecto < 0 or proyecto > 100 or examen < 0 or examen > 100:
    print("Ingrese valores válidos")
    calificacion_parcial = float(input("Ingrese la calificación de su parcial (0 - 100): "))
    proyecto = float(input("Ingrese la calificación de su proyecto (0 - 100): "))
    examen = float(input("Ingrese la calificación de su examen (0-100): "))
    
calificacion_final = calificacion_parcial * 0.4 + proyecto * 0.3 + examen * 0.3
print(f"Tu calificación final es: {calificacion_final} ")