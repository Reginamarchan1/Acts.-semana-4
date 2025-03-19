def contar_vocales_y_consonantes(palabra):
    # Convertir la palabra a minúsculas para simplificar el conteo
    palabra = palabra.lower()
    
    # Definir los conjuntos de vocales y consonantes
    vocales = "aeiou"
    consonantes = "bcdfghjklmnpqrstvwxyz"
    
    # Inicializar contadores
    contador_vocales = 0
    contador_consonantes = 0
    
    # Contar vocales y consonantes
    for letra in palabra:
        if letra in vocales:
            contador_vocales += 1
        elif letra in consonantes:
            contador_consonantes += 1
    
    return contador_vocales, contador_consonantes

# Ejemplo de uso
palabra = "HolaMundo"
vocales, consonantes = contar_vocales_y_consonantes(palabra)
print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")
print("Fin.")
