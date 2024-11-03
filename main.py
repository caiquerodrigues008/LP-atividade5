# Função para inverter as letras de cada palavra em uma frase
def inverter_palavras(frase):
    # Divide a frase em palavras, inverte cada uma, e junta-as novamente
    palavras_invertidas = [palavra[::-1] for palavra in frase.split()]
    nova_frase = " ".join(palavras_invertidas)
    return nova_frase

# Entrada do usuário
frase = input("Digite uma frase: ")

# Resultado com as palavras invertidas
nova_frase = inverter_palavras(frase)
print(f"Frase com palavras invertidas: {nova_frase}")
