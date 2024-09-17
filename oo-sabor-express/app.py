from models.restaurant import Restaurant

restaurant_praca = Restaurant('praça', 'Gourmet')
restaurant_praca.receive_rating('Gui', 10)
restaurant_praca.receive_rating('Lais', 8)
restaurant_praca.receive_rating('Emy', 5)

def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()