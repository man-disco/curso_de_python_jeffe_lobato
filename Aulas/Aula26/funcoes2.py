def animais(especie="cachorro", nome='undefined'):
    especie = especie
    nome = nome
    print('Eu tenho um ' + especie + ' chamado ' + nome + '.')


animais('cachorro', 'pretinho')
animais('gato', 'lavado')
animais('lavado', 'gato')
animais("", 'Gobert')
animais(nome='Herbert')
animais(especie='mamute', nome='Gerson')


# --------------------------------------------------------------------------------------------------------------------
def nome_completo(primeiro_nome="", nome_do_meio="", ultimo_nome=""):
    primeiro_nome = primeiro_nome
    ultimo_nome = ultimo_nome
    nome_do_meio = nome_do_meio

    if nome_do_meio != "":
        print('O nome digitado foi ' + primeiro_nome.title() + " " + nome_do_meio.title() + " " + ultimo_nome.title())
    else:
        print('O nome digitado foi ' + primeiro_nome.title() + " " + ultimo_nome.title())


nome_completo('Henrique', 'Soares', 'silva')
nome_completo('Henrique', ultimo_nome='silva')
