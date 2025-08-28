# Questão 2

m = []

# Adiciona os valores 0 ou 1
for i in range(3):
    linha = []
    print(linha)
    for j in range(3):
        x = int(input("Preencha os valores com 0 ou 1"))
        linha.append(x)
    m.append(linha)

# Exibe mastriz
print("X igual a 1 e O igual a 0 \n")
for linha in m:
    print(linha)

# Calcula quantidade de 0
soma_0 = 0
for g in m:
    for r in g:
        if r == 0:
            soma_0 +=1
# Calcula quantidade de 1
soma_1 = 0
for g in m:
    for r in g:
        if r == 1:
            soma_1 +=1

# Verifica se é um jogo valido e se foi empate ou o 1 ou o 0 ganhou
while (soma_1 == soma_0 or soma_0 == (soma_1 -1) or soma_0 == (soma_1 +1)):
    if m[0][0] == m[1][0] and m[0][0] == m[2][0]:
        if m[0][0] == 1:
            print("O X ganhou")
            break
        else:
            print("O O ganhou")
            break

    if m[0][1] == m[1][1] and m[0][1] == m[2][1]:
        if m[0][1] == 1:
            print("O X ganhou")
            break
        else:
            print("O O ganhou")
            break

    if m[0][2] == m[1][2] and m[0][2] == m[2][2]:
        if m[0][2] == 1:
            print("O X ganhou")
            break
        else:
            print("O O ganhou")
            break

    if m[0][0] == m[0][1] and m[0][0] == m[0][2]:
        if m[0][0] == 1:
            print("O X ganhou")
            break
        else:
            print("O O ganhou")
            break

    if m[1][0] == m[1][1] and m[0][0] == m[1][2]:
        if m[1][0] == 1:
            print("O X ganhou")
            break
        else:
            print("O O ganhou")
            break

    if m[2][0] == m[2][1] and m[2][0] == m[2][2]:
        if m[2][0] == 1:
            print("O X ganhou")
            break
        else:
            print("O O ganhou")
            break

    if m[0][0] == m[1][1] and m[0][0] == m[2][2]:
        if m[0][0] == 1:
            print("O X ganhou")
            break
        else:
            print("O O ganhou")
            break
    else:
        print("Empate")
        break
else:
    print("Matriz invalida!")
