def calculadora(expressao):
    expressao_com_espacos = expressao.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
    print(expressao_com_espacos)
    tokens = expressao_com_espacos.split()
    print(tokens)

    i = 0
    while i < len(tokens):
      if tokens[i] == '*' or tokens[i] == '/':
          operador = tokens[i]
          num_anterior = float(tokens[i-1])
          num_seguinte = float(tokens[i+1])

          if operador == '*':
              resultado_parcial = num_anterior * num_seguinte
              print(resultado_parcial)
          else:
              if num_seguinte == 0:
                print("Erro: Divisão por zero!")
                return
              resultado_parcial = num_anterior / num_seguinte
              print(resultado_parcial)

          del tokens[i-1:i+2]
          print(tokens)
          tokens.insert(i-1, str(resultado_parcial))
          i = 0
      else:
        i += 1

    resultado_final = float(tokens[0])

    i = 1
    while i < len(tokens):
        operador = tokens[i]
        proximo_numero = float(tokens[i+1])

        if operador == '+':
            resultado_final += proximo_numero
        elif operador == '-':
            resultado_final -= proximo_numero

        i += 2

    return resultado_final

# Exemplo de uso
expressao_para_calcular = "5 + 2 * 3 - 8 / 4"
resultado = calculadora(expressao_para_calcular)

print(f"A expressão '{expressao_para_calcular}' resulta em: {resultado}")