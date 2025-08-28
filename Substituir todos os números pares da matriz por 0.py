matriz_adb = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

resultado = [
    [],
    [],
    []
]

for i in range(len(matriz_adb)):
    for j in range(len(matriz_adb[i])):
        if matriz_adb[i][j] % 2 == 0:
            resultado[i].append(0)
        else:
            resultado[i].append(matriz_adb[i][j])

# Exibe resultado   
print("Matriz original:") 
for linha in matriz_adb:
    print(linha)

print("\nResultado:")
for linha in resultado:
    print(linha)