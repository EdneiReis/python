txt = input("Digite uma palavra:").lower()
contador = {}

lista = list(txt)
print(lista)
for letra in lista:
    lenta = letra.isalpha()  # Verifica se é uma letra
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1

contador.pop(" ")  # Remove espaços do contador

print("Contagem de letras:",contador)
