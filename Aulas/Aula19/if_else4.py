ingredientes = ["mostarda", "pimentão", "queijo extra"]
ingred_pedido = []
continuar = "s"
while continuar.lower() == "s":

    ing = input("Digite um ingrediente de sua preferencia: ")
    ingred_pedido.append(ing.lower())
    continuar = input("Deseja continuar? (s/n)")

for ingrediente in ingred_pedido:
    if ingrediente in ingredientes:
        print("Adicionando " + ingrediente + " a sua pizza.")
    else:
        print("Sinto muito, não temos " + ingrediente + ".")
