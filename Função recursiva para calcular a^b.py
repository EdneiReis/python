def numero_elevado(valor,expoente):
    if expoente > 0:
        a = 0
        return valor*numero_elevado(valor,expoente-1)
    else:
        return 1


numero_elevado(2,10)