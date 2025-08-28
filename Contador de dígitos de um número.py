num = int(input("Digite um numero: "))
while (num > 0 and num < 999):
    if(num >= 100):
        centena = num // 100
        dezena = (num // 10) % 10
        unidade = num % 10
        print(centena, dezena, unidade)
        break
    elif (num > 0 or num < 100):
        dezena = (num // 10) % 10
        unidade = num % 10
        print(dezena, unidade)
        break
if (num < 0 or num > 999):
    print("Valor invalido")