nota_final = float(input('Digite a Nota Final: '))
frequencia = float(input('Digite a Frequência: '))
mensalidade = float(input('Digite o valor da mensalidade: '))

if nota_final >= 7 and frequencia >= 75:
    desconto = mensalidade * 0.2
    mensalidade = mensalidade - desconto
    print(f'O valor do seu desconto é de R$ {desconto}')
    print(f'O valor da sua mensalidade é de R$ {mensalidade}')

else:
    print('Infelizmente você não possui desconto')
