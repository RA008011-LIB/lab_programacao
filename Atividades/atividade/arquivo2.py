vetor = []

print("Digite 5 valores:")

for i in range(5):
    valor = int(input(f"Valor {i+1}: "))
    vetor.append(valor)

x = int(input("Digite o valor que deseja buscar: "))

posicao = -1

for i in range(len(vetor)):
    if vetor[i] == x:
        posicao = i
        break

print("Posição:", posicao)
