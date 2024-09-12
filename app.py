import os

restaurants = [{'name': 'Praça', 'category': 'Japonesa', 'active': False},
               {'name': 'Pizza Suprema', 'category': 'Pizza', 'active': True},
               {'name': 'Cantina ', 'category': 'Italiano', 'active': False}]

def show_program_name():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)
def show_options(): 
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finish_app():
    show_subtitle('Encerrando o programa')

def back_to_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def invalid_option():
    print('Opção inválida!\n')
    back_to_menu()

def show_subtitle(text): 
    os.system('clear')
    line = '*' * len(text)
    print(line)
    print(text)
    print(line)
    print()

def register_restaurant():
    show_subtitle('Cadastro de novos restaurantes')
    restaurant_name = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurant_category = input(f'Digite o nome da categoria do restaurante {restaurant_name}: ')
    restaurant_data = {'name': restaurant_name, 'category': restaurant_category, 'active': False}
    restaurants.append(restaurant_data)
    print(f'O restaurante {restaurant_name} foi cadastrado com sucesso!')
    back_to_menu()

def list_restaurants():
    show_subtitle('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        restaurant_category = restaurant['category']
        restaurant_active = 'Ativo' if restaurant['active'] else 'Desativado'
        print(f' .{restaurant_name.ljust(20)} | {restaurant_category.ljust(20)} | {restaurant_active}')

    back_to_menu()

def change_restaurant_status():
    show_subtitle('Alterando estado do restaurante')
    restaurant_name = input('Digite o nome do restaurante que deseja alternar o estado: ')
    founded_restaurant = False

    for restaurant in restaurants:
        if restaurant_name == restaurant['name']:
            founded_restaurant = True 
            restaurant['active'] = not restaurant['active']
            message = f'O restaurante {restaurant_name} foi ativado com sucesso!' if restaurant['active'] else f'O restaurante {restaurant_name} foi desativado com sucesso!' 
            print(message)
    if not founded_restaurant:
            print('O restaurante não foi encontrado!')

    back_to_menu()

def choose_option():
    try:
        option = int(input('Escolha uma opção: '))
        # chosen_option = int(chosen_option)

        if option == 1:
            register_restaurant()
        elif option == 2:
            list_restaurants()
        elif option == 3:
            change_restaurant_status()
        elif option == 4:
            finish_app()
        else:
            invalid_option()
    except:
        invalid_option()

def main():
    os.system('clear')
    show_program_name()
    show_options()
    choose_option()

if __name__ == '__main__':
    main()