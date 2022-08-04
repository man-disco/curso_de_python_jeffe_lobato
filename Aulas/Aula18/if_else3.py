ingredientes = ["mostarda", "pimentão", "queijo extra"]
pedido = ["mostarda", "pimentão", "queijo extra", "banana", "chocolate"]

for ingrediente in pedido:
    if ingrediente in ingredientes:
        print("Adicionando " + ingrediente + " a sua pizza.")
    else:
        print("Sinto muito, não temos " + ingrediente + ".")
