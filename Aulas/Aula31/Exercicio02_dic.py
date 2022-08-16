# 2- Crie um dicionário, você irá inserir palavras e significados para estas palavras, ao executar o programa,
# o usuário será perguntado qual palavra ele sabe o significado. Caso a palavra esteja no dicionário, ela apre
# sentará o significado da palavra na tela, caso não esteja, ele irá exibir uma mensagem, dizendo que não possui
# a palavra em seu dicionário.

dicio = {}

dicio['lugubre'] = '\nSignificado de lugubre;\n\nAdjetivo\nQue pode estar relacionado à morte;\nQue faz lembrar a ' \
                   'morte ' \
                   'ou os ' \
                   'funerais;\n[Por Extensão] Que provoca medo, pavor; que é medonho; sinistro.\nSubstantivo ' \
                   'masculino Que contém ou apresenta lugubridade; que está ou se encontra de luto.\nEtimologia (' \
                   'origem da palavra lúgubre). Do latim lugubris.e. '

dicio['itinerário'] = '\nSignificado de Itinerário;\n\nSubstantivo masculino\nRoteiro de viagem ou o percurso que se ' \
                      'pretende seguir ou que será feito de um local a outro.\n' \
                      'Estações que fazem parte do caminho percorrido pelo trem; trajeto percorrido pelo trem.\n' \
                      'Oração ou desejo de quem pretende viajar.\n' \
                      'adjetivo Que se pode referir às estradas ou aos caminhos.\n' \
                      'Que designa o caminho percorrido entre um local e outro.\n' \
                      'Etimologia (origem da palavra itinerário). Do latim itinerarius.a.um.\n'
continuar = ""
while True:

    continuar = input('\nVocê deseja saber significado de alguma palavra? s/n ')
    if continuar.lower() == "n":
        break
    elif continuar.lower() == "s":
        palavra = input('Digite uma palavra: ')
        if palavra.lower() in dicio:
            print(dicio[palavra.lower()])
        else:
            print('\nEsta palavra não está no banco de dados, tente novamente.')

print('\nObrigado por ter utilizado o dicionário do Jefferson Lobato, volte sempre!')
