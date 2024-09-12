# Exercicio 01
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Rayana', 'Jonathann', 'Analiete', 'Ronaldo']
years = [1999, 2024]

# Exercicio 02
for name in names:
    print(f'. {name}')

# Exercicio 03
print('\nSoma de todos os números ímpares de 1 a 10:')
result = 0
for i in range(1, 11):
    if(i % 2 != 0):
        result += i

print(result)

# Exercicio 04
print('\n1 a 10 de forma decrescente:')
for i in range(10, 0, -1):
    print(i)

# Exercício 05
print()
number = int(input('Informe um número: '))

for i in range(1, 11):
    result = number * i
    print(f'{number} x {i}: {result}')


# Exercício 06
print()
result = 0

try: 
    for number in numbers:
        result += number
    print(f'O resultado da soma é {result}')
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Exercício 07
print()
result = 0

try: 
    for number in numbers:
        result += number
    media = result/len(numbers)
    print(f'O resultado da média é {media}')
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

