import locale

texto = ''
while True:
    texto = input('Deseja continuar? S/N ')
    if texto.lower() != 's' and texto.lower() != 'n':
        print('Você digitou um valor incorreto.')
    else:
        if texto.lower() == 'n':
            break
        else:
            with open('texto.txt', 'a') as arquivo:
                diario = input('O que deseja escrever no seu diário? Digite: ')
                arquivo.write(diario + '\n')
