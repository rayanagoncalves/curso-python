import os

restaurants = ['Pizza', 'Sushi']

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
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finish_app():
    os.system('clear')
    print('Encerrando o programa\n')

def invalid_option():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def register_restaurant():
    os.system('clear') 
    print('Cadastro de novos restaurantes\n')
    restaurant_name = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurants.append(restaurant_name)
    print(f'O restaurante {restaurant_name} foi cadastrado com sucesso!\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def list_restaurants():
    os.system('clear') 
    print('Listando os restaurantes\n')

    for restaurant in restaurants:
        print(f' .{restaurant}')

    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def choose_option():
    try:
        option = int(input('Escolha uma opção: '))
        # chosen_option = int(chosen_option)

        if option == 1:
            register_restaurant()
        elif option == 2:
            list_restaurants()
        elif option == 3:
            print('Ativar restaurante')
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