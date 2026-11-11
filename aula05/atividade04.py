print('''
[código 1] - Sul
[código 2] - Norte
[código 3] - Leste
[código 4] - Oeste
[código 5 a 6] - Nordeste
[código 7 a 9] - Sudeste
[código 10] - Centro-Oeste
[código 11] - Noroeste
''')
opcao = int(input('Escolha uma opção: '))
match opcao:
    case 1:
        print('Sul')
    case 2:
            print('Norte')
    case 3:
            print('Leste')
    case 4:
            print('Oeste')
    case 5 | 6:
            print('Noroeste')
    case opcao if 7 <= opcao <= 9:
            print('Sudeste')
    case 10:
            print('Centro-Oeste')
    case 11:
            print('Noroeste')

    case _:
            print('Opção Inválida!!')
              

