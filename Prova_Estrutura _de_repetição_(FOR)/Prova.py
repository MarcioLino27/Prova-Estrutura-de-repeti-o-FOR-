inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))
soma = 0

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma += numero

else:
    if soma == 0:
        print("Não há números pares no intervalo.")
    else:
        print(f"A soma dos números pares no intervalo é: {soma}")
