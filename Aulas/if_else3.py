ingredientes = ['Mostarda', 'Pimentão', 'Queijo extra']
ingred_pedido = ['Mostarda', 'Pimentão', 'Queijo extra', 'Tomate']

for ingrediente in ingred_pedido:
	if ingrediente in ingredientes:
		print("Adicionando " + ingrediente + " a sua pizza.")
	else:
		print("Sinto muito, não temos " + ingrediente + ".")
print("\n Sua pizza está pronta!")
 
