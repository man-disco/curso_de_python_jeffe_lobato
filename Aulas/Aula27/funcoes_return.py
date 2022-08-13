def soma(num1, num2):
    soma1 = num1
    soma2 = num2
    soma_total = soma1 + soma2
    print(soma_total)
    return soma_total


def sub(num1, num2):
    sub1 = num1
    sub2 = num2
    sub_total = sub1 - sub2
    print(sub_total)
    return sub_total


def mult(num1, num2):
    mult1 = num1
    mult2 = num2
    mult_total = mult1 * mult2
    print(mult_total)
    return mult_total


def div(num1, num2):
    div1 = num1
    div2 = num2
    div_total = div1 / div2
    print(div_total)
    return div_total


mult = mult(4, 4)
div = div(20, 4)
sub = sub(3, 1)
soma = soma(2, 2)
print(sub)
conta_final = soma + sub
print('')
print(conta_final)
