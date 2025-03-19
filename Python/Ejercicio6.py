def contar_subcadena(cadena, subcadena):
    ocurrencias = cadena.lower().count(subcadena.lower())
    return ocurrencias

cadena = "Hola, Hola Mundo"
subcadena = "Hola"

print(contar_subcadena(cadena, subcadena))

print("Fin.")