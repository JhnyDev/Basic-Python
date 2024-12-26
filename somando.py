soma = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}º numero: '))
    if num%2 == 0:
        soma = num + soma
print(f'Resultado da soma de apenas numeros pares digitado: {soma}')