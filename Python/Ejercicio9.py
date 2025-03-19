def fusionar_listas(lista1, lista2):
    lista_combinada = lista1 + lista2
    lista_ordenada = sorted(lista_combinada)
    return lista_ordenada

lista1 = [1,3,5,7]
lista2 = [2,4,6,8]
resultado = fusionar_listas(lista1, lista2)
print("Lista fusionada y ordenada: ", resultado)

print("Fin.")
