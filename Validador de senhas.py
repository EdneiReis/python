'''
a. mínimo de 8 caracteres
b. ao menos 1 letra maiúscula
c. ao menos 1 letra minúscula
d. ao menos 1 número'''

def valida_senha(senha):
  # 1. Verifica o comprimento primeiro
  if len(senha) < 8:
    return False

  # 2. Inicializa as flags de verificação
  tem_numero = False
  tem_maiuscula = False
  tem_minuscula = False

  # 3. Percorre a senha uma única vez para verificar tudo
  for caractere in senha:
    if caractere.isnumeric():
      tem_numero = True
    elif caractere.isupper():
      tem_maiuscula = True
    elif caractere.islower():
      tem_minuscula = True

  # 4. Retorna True apenas se todas as condições forem atendidas
  return tem_numero and tem_maiuscula and tem_minuscula

senha = input("Digite uma senha: ")
if valida_senha(senha): # Valida se senha retorna True
  print("Senha válida")
else:
  print("Senha inválida!")