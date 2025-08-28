def conta_palavras(frase):
  palavras = frase.split()
  contagem = {}
  for palavra in palavras:
    if palavra in contagem:
      contagem[palavra] += 1
    else:
      contagem[palavra] = 1
  return contagem

c = input("Digite uma frase: ")
print(conta_palavras(c))
