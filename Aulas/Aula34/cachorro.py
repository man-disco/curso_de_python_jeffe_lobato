class Cachorro:
    """Uma tentativa simples de modelar um cachorro."""

    def __init__(self, nome, idade):
        """Inicializa os atributos nome e idade."""
        self.nome = nome
        self.idade = idade

    def sentar(self):
        """Simula um cachorro sentando em resposta a um comando."""
        print(self.nome.title() + " está sentando.")

    def rolar(self):
        """Simula um cachorro rolando."""
        print(self.nome.title() + " esta rolando.")


Meu_dog = Cachorro("Pretinho", 5)

Meu_dog.rolar()
Meu_dog.sentar()

Meu_outro_dog = Cachorro('Amora', 7)
Meu_outro_dog.rolar()
Meu_outro_dog.sentar()
