nota01 = float(input('Informe a Nota da AV01: '))
nota02 = float(input('Informe a Nota da AV02: '))
nota03 = float(input('Informe a Nota da AV03: '))
nota04 = float(input('Informe a Nota da AV04: '))

media = (nota01 + nota02 + nota03 + nota04) / 4
print(f'Média das notas {media}') 

if media >= 7:
    print(f'Excelente!!! Você foi APROVADO!! Nos vemos ano que vem!!')

elif media < 5:
    print(f'Não tenho boas notícias. Você foi REPROVADO!!')

else:
    print(f'Foi por pouco!!! Você tem mais uma chance!! Você esta em RECUPERAÇÃO!!')

