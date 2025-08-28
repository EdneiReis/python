# Inicializa o dicionário de estoque
estoque = {}

# --- 1. Adicionar produtos ao estoque ---
print("--- Cadastro de Produtos ---")
for i in range(5):
  # Pede o nome do item e garante que não seja vazio
  item = ""
  while not item:
    item = input(f"Digite o nome do {i+1}º produto: ")
    quantidade = int(input(f"Digite a quantidade de '{item}': "))
    preco = float(input(f"Digite o preço de '{item}': "))

  # Armazena a quantidade e o preço em uma lista associada ao nome do item
  estoque[item] = [quantidade, preco]
  print("-" * 20)

# --- 2. Exibe o estoque inicial ---
print("\n✅ Estoque cadastrado com sucesso!")
print("--- Estoque Atual ---")
for item, valor in estoque.items():
  print(f"Produto: {item}, Quantidade: {valor[0]}, Preço: R$ {valor[1]:.2f}")
print("-" * 25)

# --- 3. Compra do cliente ---
carrinho = {}
print("\n--- Iniciar Compra ---")
print('(Digite "Sair" a qualquer momento para finalizar a compra)')

while True:
  produto_procurado = input("\nQual produto procura? ")

  # Condição para encerrar o loop de compras
  if produto_procurado == "Sair":
    break

  # Verifica se o produto procurado existe no estoque
  if produto_procurado in estoque:
    produto_em_estoque = estoque[produto_procurado]
    quantidade_disponivel = produto_em_estoque[0]

    print(f"Produto '{produto_procurado}' encontrado. Quantidade disponível: {quantidade_disponivel}")

    # Se não houver estoque, informa o usuário e continua o loop
    if quantidade_disponivel == 0:
        print("Produto esgotado!")
        continue

    quantidade_desejada = int(input("Qual a quantidade desejada? "))

    # Verifica se a quantidade desejada está disponível
    if 0 < quantidade_desejada <= quantidade_disponivel:
      # Atualiza a quantidade no estoque
      estoque[produto_procurado][0] -= quantidade_desejada

      # Adiciona o item ao carrinho
      preco_unitario = produto_em_estoque[1]
      carrinho[produto_procurado] = [quantidade_desejada, preco_unitario]
      print(f"✅ {quantidade_desejada} unidade(s) de '{produto_procurado}' adicionada(s) ao carrinho.")
    else:
      print("❌ Quantidade indisponível ou inválida.")
  else:
    print("❌ Produto não encontrado no estoque.")

# --- 4. Exibe o carrinho final e calcula o total ---
print("\n\n--- Resumo da Compra ---")

if not carrinho:
    print("O carrinho está vazio.")
else:
    total_compra = 0
    print("Itens no carrinho:")
    for item, valor in carrinho.items():
      quantidade_no_carrinho = valor[0]
      preco_unitario = valor[1]
      subtotal = quantidade_no_carrinho * preco_unitario
      total_compra += subtotal
      print(f"-> Produto: {item}, Quantidade: {quantidade_no_carrinho}, Preço Unit.: R$ {preco_unitario:.2f}, Subtotal: R$ {subtotal:.2f}")

    # --- 5. Exibe o resultado final ---
    print(f"\nO valor total da compra é: R$ {total_compra:.2f}")

    print("\n--- Estoque Atualizado ---")
    for item, valor in estoque.items():
        print(f"Produto: {item}, Quantidade: {valor[0]}, Preço: R$ {valor[1]:.2f}")