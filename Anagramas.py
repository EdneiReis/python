"""função que verifique se duas palavras são anagramas
(mesmas letras em ordem diferente). Ex: amor – Roma = True; casa –
caro = False"""

def sao_anagramas(palavra1: str, palavra2: str) -> bool:

    str1_normalizada = palavra1.replace(" ", "").lower()
    str2_normalizada = palavra2.replace(" ", "").lower()

    if len(str1_normalizada) != len(str2_normalizada):
        return False

    return sorted(str1_normalizada) == sorted(str2_normalizada)

# --- Exemplos de Uso ---

# Exemplo 1: amor – Roma (deve retornar True)
print(f"'amor' e 'Roma' são anagramas? {sao_anagramas('amor', 'Roma')}")

# Exemplo 2: casa – caro (deve retornar False)
print(f"'casa' e 'caro' são anagramas? {sao_anagramas('casa', 'caro')}")

# Exemplo 3: I Love Code – Code Love I (deve retornar True)
print(f"'I Love Code' e 'Code Love I' são anagramas? {sao_anagramas('I Love Code', 'Code Love I')}")

# Exemplo 4: ator – rota (deve retornar True)
print(f"'ator' e 'rota' são anagramas? {sao_anagramas('ator', 'rota')}")

# Exemplo 5: banana – ananab (deve retornar False)
print(f"'banana' e 'ananab' são anagramas? {sao_anagramas('banana', 'ananab')}")
