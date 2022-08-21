class Carros:
    """Uma tentativa simples de representar um carro."""

    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos que descrevem um carro."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0
        self.combustivel = 100

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

    def tanque_gasolina(self):
        """Exibe a quantidade de gasolina do tanque."""
        print('O tanque de gasolina está com ' + str(self.combustivel) + '% de combustível. ')


Carro1 = Carros('Honda', 'Civic', 2015)


class CarrosEletricos(Carros):
    """Representa os aspectos de um carro específico, no caso, de um carro elétrico."""
    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos da classe pai 'Carros' """
        super().__init__(fabricante, modelo, ano)
        self.bateria = Bateria()

    def tanque_gasolina(self):
        """Carros elétricos não usam gasolina."""
        print('Carros elétricos não usam gasolina.')


class Bateria:
    """Uma tentativa simples de criar uma bateria."""
    def __init__(self, bateria=100):
        """Inicializa a bateria."""
        self.bateria = bateria

    def altera_bateria(self, novo_valor):
        """Altera o valor da bateria."""
        self.bateria = novo_valor

    def mostra_bateria(self):
        print('A bateria do carro está com ' + str(self.bateria) + '% de carga. ')


