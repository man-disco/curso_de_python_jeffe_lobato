# A variavel lista sempre é dentro de colchetes.
# Uma lista sempre começa com 0 Ex: (0, 1,2)
carros = ['Ferrari', 'fusca', 'Civic']
print(carros)
print(carros[0])

# O ultimo elemento numa lista é representado pelo -1
print(carros[-1])

print('Eu gostaria de ter um ' + carros[1].title())


# Manipulando elementos de uma lista.

carros[1] = 'Mustang'
print(carros)

# Método append acrescenta valores ao final de uma lista.
carros.append('BMW')
print(carros)

# Insert acrescenta valores em uma posição definida de uma lista.
carros.insert(1, 'Jeep')
print(carros)

# Extend separa uma variável em vários elementos independentes em uma lista.
carros.extend('fusca')
print(carros)

# Del e pop deleta elementos de uma lista.
del carros[0]
print(carros)

carros.pop(2)
print(carros)

# Remove deleta elementos pelo valor da var.
carros.remove('BMW')
print(carros)
