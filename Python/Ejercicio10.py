def eliminar_impares(lista):
    return [x for x in lista if x % 2 == 0]

mi_lista = [1,2,3,4,5]
resultado = eliminar_impares(mi_lista)
print("Lista sin impares: ", resultado)

print("Fin.")
    