'''função que receba uma lista de nomes e retorne apenas os
nomes que começam com uma determinada letra.'''

def verifica_nome(lista_nomes,letra):
  resultado = []
  for i in lista_nomes:
    if i[0] == letra:
      resultado.append(i)

  return resultado

ll = ["ednei", "edcarlos","maria"]
letra = "a"
verifica_nome(ll,"e")