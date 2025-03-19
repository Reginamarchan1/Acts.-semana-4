def ordenar_palabras(lista_palabras):
    return sorted(lista_palabras, key=len)

palabras = ["gato","elefante","ratón","león","zorro"]
resultado = ordenar_palabras(palabras) 
print(resultado)

print("Fin.")