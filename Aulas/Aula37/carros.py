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


Meu_carro = Carros('Toyota', 'auris', 2016)

print(Meu_carro.descricacao_nome())
Meu_carro.leia_odometro()
print("Mudando o odometro...")

Meu_carro.odometro = 5
Meu_carro.leia_odometro()
