frase = "Hola Mundo"

palabras = frase.split()

palabras_invertidas = [palabra[::-1] for palabra in palabras]

frase_invertida = ' '.join(palabras_invertidas)

print(f"La frase invertida es: {frase_invertida}")

print("Fin.")

