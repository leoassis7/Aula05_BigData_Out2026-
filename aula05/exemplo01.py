valor_do_pedido = float(input('Digite o valor do pedido: '))
distancia = float(input('Digite distância: '))
frete = 8
if valor_do_pedido > 50 and distancia <= 3:
    valor_final = valor_do_pedido
    print('FRETE GRÁTIS')

else:
    valor_final = valor_do_pedido + frete
    print(f'O valor do seu frete é de R$ {frete}')
    print(f'Valor final: R$ {valor_final: .2f}')
    