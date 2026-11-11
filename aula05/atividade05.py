num = float(input("Digite um número: "))

match num:
    case num if 0 > num:
        print('Negativo')
    case num if 0 < num:
        print('Positivo')
    case _:
        print('Zero')
