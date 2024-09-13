class Restaurant:
    name = ''
    category = ''
    active = False

restaurant_praca = Restaurant()
restaurant_praca.name = 'Praça'
restaurant_praca.category = 'Italiana'

restaurants = [restaurant_praca]

print(vars(restaurant_praca))

print(f'Nome: {restaurant_praca.name}')

print('Ativo') if restaurant_praca.active else print('Desativado')

category = Restaurant.category
Restaurant.name = 'Bistrô'

restaurant_pizza = Restaurant()
restaurant_pizza.name = 'Pizza Place'
restaurant_pizza.category = 'Fast Food'

if restaurant_pizza.category == 'Fast Food':
    print(f'Categoria do restaurante {restaurant_pizza.name} é Fast Food!')

restaurant_pizza.active = True

print(f'Nome: {restaurant_praca.name} - Categoria: {restaurant_praca.category}')