import random

soma = 0
cont = 0
num = int(input("Digite um numero de 1 á 10: "))
rand = random.randint(1,10)
print(rand)
while num !=  rand:
 soma = soma + rand
 cont = cont + 1
 rand = random.randint(1,10)
 print(rand)
print("A soma é: ",soma)
print("tentativas", cont)
