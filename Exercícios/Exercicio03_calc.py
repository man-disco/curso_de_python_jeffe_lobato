# 3- Crie uma calculadora com 4 operações, div, sub, som, mult, que pergunte ao usuário qual operação ele dese
# ja fazer e peça os números que serão calculados, em seguida mostre o resultado da operação na tela, sendo que
# as funções utilizadas no programa estejam em um módulo separado do arquivo principal.
import Modulo_num

while True:
    print('\nCalculadora Python\nDigite "sair" para sair.\n')

    opc = input('Qual operação você deseja realizar? | soma, sub, mult ou div: ')
    if opc.lower() == 'soma':
        soma_total = Modulo_num.soma(int(input('Digite o primeiro número: ')), int(input('Digite o segundo numero: ')))
        print('O resultado da operação é: ' + str(soma_total))

    elif opc.lower() == 'sub':
        sub_total = Modulo_num.sub(int(input('Digite o primeiro número: ')), int(input('Digite o segundo numero: ')))
        print('O resultado da operação é: ' + str(sub_total))

    elif opc.lower() == 'mult':
        mult_total = Modulo_num.mult(int(input('Digite o primeiro número: ')), int(input('Digite o segundo numero: ')))
        print('O resultado da operação é: ' + str(mult_total))
# forma muito mais simples que o professor fez hahaha.
    elif opc.lower() == 'div':
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        print(Modulo_num.div(num1, num2))

    elif opc.lower() == 'sair':
        break

    else:
        print('Valor invalido, tente outro.')
