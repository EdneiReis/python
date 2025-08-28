#= Função que receba uma lista de números e retorne uma nova lista com apenas os números primos.

def numeros_primos(lista):
    lista_primos = []
    for numeros in lista:
        if numeros > 1:
            primo = True
            for divisor in range(2,numeros):
                if numeros % divisor == 0:
                    primo = False
                    break

            if primo:
                lista_primos.append(numeros)
    return lista_primos

numeros_primos(lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])