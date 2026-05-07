import random
repeticoes = int(input('Digite a quantidade de números aleatórios: '))
if repeticoes > 0:
    for i in range(repeticoes):
        numero_aleatorio = random.randint(1, 100)
        print(f'{i}° número aleatório: {numero_aleatorio}')