# Exercicio 1
number = int(input('Insira um número: '))

if number % 2 == 0:
    print(f'{number} é par!')
else:
    print(f'{number} é ímpar!')

# Exercício 2
#age = int(input('Informe sua idade: '))

idade = int(input("Digite sua idade: "))
if 0 < idade <= 12:
    print("Criança")
elif 12 < idade < 18:
    print("Adolescente")
elif idade >= 18:
    print("Adulto")
else: 
    print("Valor inválido!")

# Exercício 3
user_name = input('Informe o nome do usuário: ')
password = input('Informe a senha: ')

if user_name == 'foo' and password == '123':
    print('Usuário logado')
else: 
    print('Login inválido')

# Exercício 4
x = int(input('Informe a coordenada x: '))
y = int(input('Informe a coordenada y: '))

if x > 0 and y > 0:
    print('Primeiro quadrante')
elif x < 0 and y > 0:
    print('Segundo quadrante')
elif x < 0 and y < 0:
    print('Terceiro quadrante')
elif x > 0 and y < 0:
    print('Quarto quadrante')
else:
    print('O ponto está localizado no eixo ou origem')

