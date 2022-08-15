# 4 - Crie um joguinho de par ou ímpar, o programa irá perguntar ao primeiro jogador se ele quer par ou impar
# e vai pedir um número, logo pedirá o segundo jogador outro número, fará a soma, utilizando o mesmo módulo do
# exercício anterior, e dirá se o resultado é par ou ímpar, exibindo uma mensagem de parabéns ao vencedor daqu
# ela partida.
import Modulo_num


opc = ""
while True:
    opc = input('Você deseja jogar par ou impar? (s/n) \n')
    if opc.lower() == 'n':
        break
    elif opc.lower() == 's':
        jogador1 = input('Digite o nome do jogador 1: ')
        jogador2 = input('Digite o nome do jogador 2: ')
        par_ou_impar = input(jogador1.rstrip() + ' digite 1 para impar e 2 para par: \n')

        if par_ou_impar != '1' and par_ou_impar != '2':
            print('Você digitou uma opção invalida.')
            continue

        else:
            num_jog1 = int(input(jogador1 + ' digite um número qualquer: \n'))
            num_jog2 = int(input(jogador2 + ' digite um número qualquer: \n'))
            soma = Modulo_num.soma(num_jog1, num_jog2)
            resultado = Modulo_num.par_impar(num_jog1, num_jog2)
            print('\nO ' + jogador1 + ' escolheu ' + str(num_jog1) + ' e o ' + jogador2 + ' escolheu ' + str(num_jog2))
            print('\nE a soma da ' + str(soma) + ' que é ' + str(resultado))

            if resultado == 'PAR':
                if par_ou_impar == '1':
                    print('\nParabéns ' + jogador2 + ' você é o vencedor!')
                else:
                    print('\nParabéns ' + jogador1 + ' você é o vencedor!')
            if resultado == 'IMPAR':
                if par_ou_impar == '2':
                    print('\nParabéns ' + jogador1 + ' você é o vencedor!')
                else:
                    print('\nParabéns ' + jogador2 + ' você é o vencedor!')

            print('\nEspero que tenha se divertido\n ')

    else:
        print('\nValor incorreto, tente novamente.')

