valor_da_compra = float(input('Informe o Valor da Compra: '))
fidelidade = input('Cliente cadastrado no programa de fidelidade ? [s/n]: ')

if valor_da_compra > 200 or fidelidade == 's':
    print(f'O valor do seu pedido é de R$ {valor_da_compra}')
    print('Você possui frete grátis!!')

else:
    frete = 25
    valor_final = valor_da_compra + frete
    print(f'O valor de seu frete é de R$ {frete}')
    print(f'O valor de seu pedido é de R$ {valor_final}')
