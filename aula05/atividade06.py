valor_de_venda = float(input('Digite o valor da Venda: '))

match valor_de_venda:
    case valor_de_venda if valor_de_venda < 100:
        print('Pequena Venda')

    case valor_de_venda if 100 <= valor_de_venda <= 500:
        print('Pequena Média')   

    case valor_de_venda if valor_de_venda > 500:
        print('Pequena Grande')
    