# Exercício 1
class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

car = Car(model='Uno', color='Azul', year=2010)

# Exercício 2

class Restaurant:
    def __init__(self, name, category, active, capacity, rating_note):
        self.name = name
        self.category = category
        self.active = active
        self.capacity = capacity
        self.rating_note = rating_note

    def __str__(self):
        return f'{self.name} | {self.category}'

restaurant = Restaurant(name='Pizza Express', category='Italiano', active=False, capacity=1000, rating_note=5)
print(restaurant)

# Exercício 3

class Client:
    def __init__(self, name, lastname, age, address):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.address = address

client = Client(name='Rayana', lastname='Gonçalves', age=25, address='Rua Sem Nome')