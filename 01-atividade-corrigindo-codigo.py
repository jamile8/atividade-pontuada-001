import os
os.system ("cls || clear")


Quantidade_de_numeros = 5
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = 0
menor_numero = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0


for i in range(Quantidade_de_numeros):
        numero = int(input(f"Digite o {i+1}º número: "))


# Processando cada número
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

maior_numero = max(maior_numero, numero)
menor_numero = min(menor_numero, numero)

soma_geral += numero

# Calculando as médias
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares > 0 else 0
media_geral = soma_geral / 5

# Mostrando números na ordem inversa
numero_invertidos = [numero]

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"\nQuantidade de pares: {quantidade_pares}")
print(f"\nQuantidade de ímpares: {quantidade_impares}")
print(f"\nQuantidade de positivos: {quantidade_positivos}")
print(f"\nQuantidade de negativos: {quantidade_negativos}")
print(f"\nMaior número: {maior_numero}")
print(f"\nMenor número: {menor_numero}")
print(f"\nMédia dos números pares: {media_pares:.2f}")
print(f"\nMédia dos números ímpares: {media_impares:.2f}")
print(f"\nMédia de todos os números: {media_geral:.2f}")
print(f"\nNúmeros na ordem inversa: {numero_invertidos}")
print(f"Média de todos os números: {media_geral:.2f}")
print(f"Números na ordem inversa: {numeros_invertidos}")
