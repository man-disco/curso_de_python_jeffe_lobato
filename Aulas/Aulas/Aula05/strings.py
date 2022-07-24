# “Strings” são linhas de caracteres reconhecidas dentro de '' ou "".
nome1 = "vitor"
nome2 = 'alexandre'

# Variáveis podem ser concatenadas para gerar um resultado combinado.
nome_completo = " " + nome1 + " " + nome2 + " "
print(nome_completo)

# Métodos são funções e ferramentas diversas para variáveis.
# Ex: Método Title deixa somente as primeiras letras duma “string” maiúsculas.
print(nome_completo.title())

# Já o método upper deixa todos os caracteres maiúsculos.
nome_completo2 = nome_completo.upper()
print(nome_completo2)

# Exercício.
print("Olá " + nome_completo.title() + ", tudo bem?")

# Para inserir variáveis facilmente escreva %(inicial da variável) no print e variavéis em um parentesís.
numero = 2
print("Olá %s, %i tudo bem?" % (nome_completo, numero))
# Para concatenar uma variável int deve transforma-lá em str.
# Isso é devido ao fato do + tentar somar a variável já que é um operador aritmético.
print("Olá " + nome_completo + str(numero))
# Método “strip” remove espaços desnecessários na “string”.
print(nome_completo.strip())
# lstrip() para remover espaços na esquerda, rstrip() para direita.
print("Olá " + nome_completo.lstrip() + ", tudo bem?")
print("Olá " + nome_completo.rstrip() + ", tudo bem?")
# Para saltar linhas use \n na str
print("Olá " + nome_completo.strip() + ", Tudo bem? \n Como vai a família? \n Manda um abraço!")
