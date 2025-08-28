txt = input("Digite uma palavra:")
l = []

# Adiciona em uma lista
for i in txt:
    l.append(i)

# exibe as listas
print("Lista:",l)
print("Lista reversa:",l[::-1])

# Verifica se é um palindromo
if l == l[::-1]:
    print("Essa palavra é um palindromo")
else:
    print("Essa palavra não é um palindromo")
