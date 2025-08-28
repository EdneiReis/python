matriz_mult = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matriz_mult2 = [
    [10,11,12],
    [13,14,15],
    [16,17,18]
]

resultado_unitario = []
r = []
print("Matriz 1:")
for linha in matriz_mult:
    print(linha)

print("\nMatriz 2:")
for linha in matriz_mult2:
    print(linha)

print("\nResultado:")
for i in range(3):
    for j in range(3):
        for k in range(3):
            calculo = matriz_mult[j][k] * matriz_mult2[k][j]
            resultado_unitario.append(calculo)
            #print(f"{matriz_mult[j][k]} x {matriz_mult2[k][j]} = {resultado[i][k]}")

indice1 = 0
indice2 = 1
while(indice2 < len(resultado_unitario)):
    soma = resultado_unitario[indice1] + resultado_unitario[indice2]
    r.append(soma)
    indice1 +=2
    indice2 +=2

print(r)