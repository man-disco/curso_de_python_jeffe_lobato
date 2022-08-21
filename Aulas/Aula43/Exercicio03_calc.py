import Modulo_num

while True:
    continuar = input('Você deseja calcular? S/N: ')
    if continuar.lower() == 'n':
        break
    if continuar.lower() != 's' and continuar.lower() != 'n':
        print('Você digitou um valor inválido.\n')
    else:
        print('\nCalculadora Python\nDigite "sair" para sair.\n')
        try:
            opc = input('Qual operação você deseja realizar? | soma, sub, mult ou div: ')
            if opc.lower() == 'soma':
                num1 = int(input('Digite o primeiro número: '))
                num2 = int(input('Digite o segundo número: '))
                print('O resultado da operação é: ' + Modulo_num.soma(num1, num2))

            elif opc.lower() == 'sub':
                num1 = int(input('Digite o primeiro número: '))
                num2 = int(input('Digite o segundo número: '))
                print('O resultado da operação é: ' + Modulo_num.sub(num1, num2))

            elif opc.lower() == 'mult':
                num1 = int(input('Digite o primeiro número: '))
                num2 = int(input('Digite o segundo número: '))
                print('O resultado da operação é: ' + Modulo_num.mult(num1, num2))

            elif opc.lower() == 'div':
                num1 = int(input('Digite o primeiro número: '))
                num2 = int(input('Digite o segundo número: '))
                print('O resultado da operação é: ' + Modulo_num.div(num1, num2))

            elif opc.lower() == 'sair':
                break
            else:
                print('\nValor invalido, tente outro.\n')
        except ZeroDivisionError:
            print('\nOcorreu ocorreu um erro inesperado na sua operação, verifique se não foi uma tentativa de divisão '
                  'por 0.\n')
        except TypeError:
            print('\nTente somar outro valor que não seja 0.\n')


print('\nObrigado por utilizar a calculadora, volte sempre!')
