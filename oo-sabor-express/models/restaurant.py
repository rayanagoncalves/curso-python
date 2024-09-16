class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False
        Restaurant.restaurants.append(self)


    def __str__(self):
        return f'{self.name} | {self.category}'

    def list_restaurants():
        for restaurant in Restaurant.restaurants:
            print(f'{restaurant.name} | {restaurant.category} | {restaurant.active}')

restaurant_praca = Restaurant('Praça', 'Gourmet')
restaurant_pizza = Restaurant('Pizza Express', 'Italiana')
# restaurant_praca.name = 'Praça'
# restaurant_praca.category = 'Italiana'

# restaurants = [restaurant_praca]

# print(vars(restaurant_praca))

# print(f'Nome: {restaurant_praca.name}')

# print('Ativo') if restaurant_praca.active else print('Desativado')

# category = Restaurant.category
# Restaurant.name = 'Bistrô'

# restaurant_pizza = Restaurant()
# restaurant_pizza.name = 'Pizza Place'
# restaurant_pizza.category = 'Fast Food'

# if restaurant_pizza.category == 'Fast Food':
#     print(f'Categoria do restaurante {restaurant_pizza.name} é Fast Food!')

# restaurant_pizza.active = True

# print(f'Nome: {restaurant_praca.name} - Categoria: {restaurant_praca.category}')

# print(restaurant_praca)
# print(restaurant_pizza)

Restaurant.list_restaurants()