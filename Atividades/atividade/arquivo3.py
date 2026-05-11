import random

vetor = []
contador_6 = 0

for i in range(50):
    valor = random.randint(1, 6)
    vetor.append(valor)
    
    if valor == 6:
        contador_6 += 1

percentual = (contador_6 / 50) * 100

print("Lançamentos:", vetor)
print("Quantidade de vezes que saiu 6:", contador_6)
print(f"Percentual de 6: {percentual:.2f}%")
