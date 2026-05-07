import math
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def encontrar_primo_depois_de(x: int):
    i = x + 1
    while not eh_primo(i):
        i += 1
    return i
numero = int(input('Digite um número: '))
if numero > 0:
    primo_atual = 2
    divisores = []
    while primo_atual <= numero:
        while not (numero / primo_atual).is_integer():
            primo_atual = encontrar_primo_depois_de(primo_atual)
        divisores.append(primo_atual)
        primo_atual += 1
    if sum(divisores) == numero:
        print(f'{numero} é perfeito')
    else:
        print(f'{numero} não é perfeito')