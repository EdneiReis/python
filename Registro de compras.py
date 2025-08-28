#Sistema de registro de compras. Peça ao usuário 3 produtos e suas quantidades compradas. Depois, pergunte
# os preços unitarios de cada grupo. 
# Calcule e imprima o valor total de cada produto (Quantidade * Preço Unitário) e o valor total da compra.

compras = {}
for i in range(3):
    produto = input(f"Digite o nome do produto {i+1}: ")
    quantidade = int(input(f"Digite a quantidade do produto {produto}: "))
    preco_unitario = float(input(f"Digite o preço unitário do produto {produto}: "))
    
    compras[produto] = {
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
        "valor_total": quantidade * preco_unitario
    }

print("\nResumo da compra:")
for produto, info in compras.items():
    print(f"Produto: {produto}, Quantidade: {info['quantidade']}, Preço Unitário: R${info['preco_unitario']:.2f}, Valor Total: R${info['valor_total']:.2f}")
total_compra = sum(info['valor_total'] for info in compras.values())
print(f"\nValor total da compra: R${total_compra:.2f}")
