class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False # _ indica que o atributo é protegido
        Restaurant.restaurants.append(self)


    def __str__(self):
        return f'{self._name} | {self._category}'

    @classmethod
    def list_restaurants(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | Status')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {restaurant.active}')

    @property
    def active(self):
        return '☒' if self._active else '☐'
    
    def change_status(self):
        self._active = not self._active

restaurant_praca = Restaurant('praça', 'Gourmet')
restaurant_praca.change_status()
restaurant_pizza = Restaurant('pizza Express', 'Italiana')

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