# Crie um programa para elaborar uma lista de convidados de uma festa, o programa irá perguntar o nome do convidado,
# você digitará o nome e ao terminar a lista, o programa irá exibir a lista em ordem alfabética. Insira até 10 nomes.
lista_convidados = []
print("Quando terminar digite FIM\n")

while True:
    convidado = input('Digite o nome do convidado ou digite FIM: ')

    if convidado.lower() == 'fim':
        break

    else:
        lista_convidados.append(convidado.title())

lista_convidados.sort()

print("\n############ LISTA DE CONVIDADOS ###############\n")

for convidado in lista_convidados:
    print(">>>>>>>>>> " + convidado)
