# 3 - Usuários: Crie uma classe chamada Usuário. Crie dois atributos de nomes primeiro_nome e ultimo_nome e, então crie
# vários outros atributos normalmente armazenados em um perfil de usuário. Escreva um método de nome descricao_usuario()
# que apresente um resumo das informações do usuário. Escreva outro método chamado saudacao_usuario(0 que mostre uma sau
# dação para cada usuário.
class Usuario:
    """Classe para definir um usuário."""

    def __init__(self, primeiro_nome, ultimo_nome, idade, sexo, cidade):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.idade = idade
        self.sexo = sexo
        self.cidade = cidade

    def descricao_usuario(self):
        print(self.primeiro_nome.title() + ' ' + self.ultimo_nome.title())
        print(str(self.idade) + ' anos')
        if self.sexo == 'feminino':
            print('Nascida em ' + self.cidade)
        else:
            print('Nascido em ' + self.cidade)
        print('Do sexo ' + self.sexo)

    def saudacao_usuario(self):
        print('Olá ' + self.primeiro_nome.title() + ' ' + self.ultimo_nome.title() + '!')


User1 = Usuario('pedro', 'LUcaS', 18, 'masculino', 'Uberaba')
User2 = Usuario('Luzia', 'alves', 47, 'feminino', 'Santa Catarina')
User3 = Usuario('Alfredo', 'goMES', 67, 'masculino', 'Piauí')

User1.descricao_usuario()
User1.saudacao_usuario()
print('')
User2.descricao_usuario()
User2.saudacao_usuario()
print('')
User3.descricao_usuario()
User3.saudacao_usuario()