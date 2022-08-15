def soma(num1, num2):
    sum1 = num1
    sum2 = num2
    soma_total = num1 + num2
    return soma_total


def sub(num1, num2):
    sub1 = num1
    sub2 = num2
    sub_total = num1 - num2
    return sub_total


def mult(num1, num2):
    mult1 = num1
    mult2 = num2
    mult_total = mult1 * mult2
    return mult_total


def div(num1, num2):
    div1 = num1
    div2 = num2
    div_total = div1 // div2
    return div_total


def par_impar(num1, num2):
    num1 = num1
    num2 = num2
    soma_n = num1 + num2
    sobra = soma_n % 2

    if sobra == 0:
        par_impar = 'PAR'
    else:
        par_impar = 'IMPAR'

    return par_impar

