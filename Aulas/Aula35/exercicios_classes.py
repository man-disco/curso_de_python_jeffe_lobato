# 1 - Crie uma classe chamada Restaurante. O método __init__() de Restaurante deve armazenar dois atributos:
# restaurante_nome e tipo_cozinha. Crie um método chamado restaurante_descricao() que mostre essas duas informações,
# e uim método de nome restaurante_aberto() que exiba uma mensagem informando que o restaurante está aberto. Crie uma
# instância chamada a partir da sua classe. Mostre os dois atributos individualmente e, em seguida, chame os dois mét
# odos.
#
# 2 - Três restaurantes: comece com a classe do exercício anterior. Crie três instancias diferentes da classe e chame
# restaurante_descricao() para cada instancia.
#
# 3 - Usuários: Crie uma classe chamada Usuário. Crie dois atributos de nomes primeiro_nome e ultimo_nome e, então crie
# vários outros atributos normalmente armazenados em um perfil de usuário. Escreva um método de nome descricao_usuario()
# que apresente um resumo das informações do usuário. Escreva outro método chamado saudacao_usuario() que mostre uma sau
# dação para cada usuário.

# 1

class Restaurante:
    """Classe para definir um restaurante."""

    def __init__(self, nome, tipo_cozinha):
        self.restaurante_nome = nome
        self.tipo_cozinha = tipo_cozinha

    def restaurante_descricao(self):
        print('\n * O restaurante se chama ' + self.restaurante_nome.title() + ' e sua especialidade é ' + self
              .tipo_cozinha + '.')

    def restaurante_aberto(self):
        print(' * O restaurante ' + self.restaurante_nome.title() + ' está aberto.')


restaurante1 = Restaurante('La casa do pastel', 'pastel')

print(restaurante1.restaurante_nome)
print(restaurante1.tipo_cozinha)
restaurante1.restaurante_descricao()
restaurante1.restaurante_aberto()

# 2
restaurante2 = Restaurante('Burger King', 'hamburger')
restaurante2.restaurante_descricao()
# ------------------------------------------------
restaurante3 = Restaurante('KFC', 'frango frito')
restaurante3.restaurante_descricao()
# ------------------------------------------------
restaurante4 = Restaurante('Girafas', 'comida tradicional')
restaurante4.restaurante_descricao()
print('')

