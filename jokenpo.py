from random import choice

npc = ['Pedra','Papel','Tesoura']

while True:
    change = choice(npc)
    print('=== Escolha entre Pedra, Papel ou Tesoura ===')
    user = input('Escolha entre Pedra, Papel ou Tesoura: ')

    if change == 'Pedra' and user == 'Papel':
        print(f'Máquina escolheu {change} e você {user}, você ganhou :-) \n')
    elif change == 'Papel' and user == 'Tesoura':
        print(f'Máquina escolheu {change} e você {user}, você ganhou :-) \n')
    elif change == 'Tesoura' and user == 'Pedra':
        print(f'Máquina escolheu {change} e você {user}, você ganhou :-) \n')
        
    elif change == user:
        print(f'Máquina escolheu {change} e você {user}, houve empate :-| \n')

    elif change == 'Papel' and user == 'Pedra':
        print(f'Máquina escolheu {change} e você {user}, você perdeu :-( \n')
    elif change == 'Tesoura' and user == 'Papel':
        print(f'Máquina escolheu {change} e você {user}, você perdeu :-( \n')
    elif change == 'Pedra' and user == 'Tesoura':
        print(f'Máquina escolheu {change} e você {user}, você perdeu :-( \n')

    elif user is not choice(npc):
        print('BYE BYE BYE ')
        break