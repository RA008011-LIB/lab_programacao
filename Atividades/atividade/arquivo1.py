vetor = []

print("Digite 10 valores:")

for i in range(10):
    valor = int(input(f"Valor {i+1}: "))
    vetor.append(valor)

valores_diferentes = len(set(vetor))

print("Quantidade de valores diferentes:", valores_diferentes)
