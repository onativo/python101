print('Digite uma sequência de números a serem somados.')
print('Digite 0 para encerrar a soma.')
soma = 0
valor = 1

while valor != 0:
    valor = int(input('Digite um valor a ser somado: '))
    soma = soma + valor
print(f'A soma dos valores digitados é igual a: {soma}')