class Carros:
    """Uma tentativa simples de representar um carro."""

    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos que descrevem um carro."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def descricacao_nome(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        nome_longo = str(self.ano) + " " + self.fabricante + " " + self.modelo
        return nome_longo.title()

    def leia_odometro(self):
        """Exibe uma frase que mostra a quilometragem do carro."""
        odm = "O carro tem " + str(self.odometro) + " KM rodados."
        print(odm)

    def altera_odometro(self, novo_odometro):
        """Alterar o odometro pelo valor passado como argumento."""
        self.odometro = novo_odometro

    def incrementa_odometro(self, novo_odometro):
        self.odometro += novo_odometro


Meu_carro = Carros('Toyota', 'auris', 2016)

print(Meu_carro.descricacao_nome())
Meu_carro.leia_odometro()
print("")
print("Mudando o odometro...")

Meu_carro.odometro = 5
Meu_carro.leia_odometro()

print("")
print("Mudando o odometro...")
Meu_carro.altera_odometro(10)
Meu_carro.leia_odometro()

print('')
print("Mudando o odometro...")
Meu_carro.incrementa_odometro(10)
Meu_carro.leia_odometro()

print('')
print("Mudando o odometro...")
Meu_carro.incrementa_odometro(3)
Meu_carro.leia_odometro()
print('')

if Meu_carro.odometro >= 23:
    print('Meu carro está cansado!')

meu_outro_carro = Carros('Ford', 'Mustang', 2019)
print("")
print("Mudando o odometro...")
meu_outro_carro.altera_odometro(10)
meu_outro_carro.leia_odometro()

print('')
print("Mudando o odometro...")
meu_outro_carro.incrementa_odometro(5)
meu_outro_carro.leia_odometro()

print('')
print("Mudando o odometro...")
meu_outro_carro.incrementa_odometro(19)
meu_outro_carro.leia_odometro()
print('')

