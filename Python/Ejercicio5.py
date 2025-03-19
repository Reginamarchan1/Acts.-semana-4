def cifrado_cesar(cadena, desplazamiento):
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto_minusculas = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    
    for caracter in cadena:
        if caracter in alfabeto_minusculas:
            indice = alfabeto_minusculas.index(caracter)
            nuevo_indice = (indice + desplazamiento) % 26
            resultado += alfabeto_minusculas[nuevo_indice]
        elif caracter in alfabeto_mayusculas:
            indice = alfabeto_mayusculas.index(caracter)
            nuevo_indice = (indice + desplazamiento) % 26
            resultado += alfabeto_mayusculas[nuevo_indice]
        else:
            resultado += caracter  
    
    return resultado

cadena = "Hola Mundo"
desplazamiento = 3
cadena_cifrada = cifrado_cesar(cadena, desplazamiento)
print(f"La cadena cifrada es: {cadena_cifrada}")
print("Fin.")
