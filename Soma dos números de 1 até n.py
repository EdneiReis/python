def soma_rec(n):
    soma = 0
    if n == 0:
        return
    for i in range(n+1):
        soma+=i
        print(i,"+")
        print(soma)
    return soma

soma_rec(5)