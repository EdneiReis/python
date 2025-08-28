def gerador(limite):
  resultado = []
  for i in range(limite + 1):
    if i % 2 == 0:
      resultado.append(i)

  #Exibe lista
  def exibe_lista():
    for i in resultado:
      print(i)
  return exibe_lista()


gerador(10)