# Exercício 01
person = {'name': 'Rayana', 'age': 25, 'city': 'Recife'}

# Exercício 02
person['age'] = 24
person['profession'] = 'Developer'
del person['city']
print(person)

# Exercício 03
square_numbers = { 'x': x**2 for x in range(1, 6)}
print(square_numbers)

# Exercício 04
if 'teste' in person:
    print(f'A chave existe no dicionário!')
else:
    print(f'A chave não existe no dicionário!')

# Exercício 05
sentence = 'Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos anos'
count_words = {}
words = sentence.split()
for word in words: 
    count_words[word] = count_words.get(word, 0) + 1
print(count_words)