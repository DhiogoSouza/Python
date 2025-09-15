from datetime import date

#variaveis
ano = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
anos_faltando = 18 - idade
anos_passados = idade - 18
print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual} ')

#calculo
if idade < 18:
    print(f'Você ainda vai se alistar no exército. Faltam {anos_faltando} ano/anos.')
elif idade == 18:
    print('Já está na hora de se alistar!!!')
elif idade > 18:
    print(f'Seu alistamento foi há {anos_passados} anos.')