#função que receba uma lista e retorne uma nova lista com os elementos sem repetição, mantendo a ordem original.

def elementos_sem_repeticao(*args):
    resultado = []
    for i in args:
        if i in resultado:
            continue
        else:
            resultado.append(i)
    return(resultado)

elementos_sem_repeticao(1,2,2,3,4,4,5,6,7,2,1,1,4,6,8,9)