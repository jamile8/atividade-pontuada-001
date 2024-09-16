import os
os.system ("cls || clear")


Quantidade_de_numeros = 5
numeros = []

print("======= Solicitando Dados =======")

for i in range(Quantidade_de_numeros):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0
maior_numero = numeros[0]
menor_numero = numeros[0]

for numero in numeros:
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        soma_impares += numero

    if numero < 0:
        quantidade_negativos += 1
    elif numero > 0:
        quantidade_positivos += 1
        
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

soma_geral += numero

# Calculando as médias
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares > 0 else 0
media_geral = soma_geral / 5

numero_invertidos = list(reversed(numeros))


print("\n====== Estatísticas dos números =======")

print(f"\nQuantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Quantidade de números inseridos: {len(numeros)}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")
print(f"Números na ordem inversa: {numero_invertidos}")
