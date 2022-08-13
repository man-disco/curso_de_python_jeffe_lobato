# Programa de votação.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Menor de 16 anos não vota.
# Entre 16 e 17 anos e acima de 65 o voto é opcional.
# Entre 18 e 65, o voto é obrigatório.

if idade < 16:
    print(nome + ', você tem ' + str(idade) + " anos e você não pode votar.")

elif (16 >= idade <= 17) or (idade > 64):
    print(nome +', você tem ' + str(idade) + " anos e seu voto é opcional.")

elif idade > 64:
    print(nome + ', você tem ' + str(idade) + " anos e seu voto é opcional.")

else:
    print(nome + ', você tem ' + str(idade) + " anos e seu voto é obrigatório.")