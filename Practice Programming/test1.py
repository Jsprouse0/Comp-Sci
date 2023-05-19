def print_menu():
    print('\n   Menu')
    print('a - add new player')
    print('r - remove player')
    print('u - update players')
    print('d - show full roster')
    print('s - show player above a rating')
    print('q - Quit \n')

    return input("Choose an option: \n").lower()


def add_player(soccer_team):
    jersey_num = int(input('Enter a jersey number: \n'))
    player_rating = int(input('Enter a player rating: \n'))
    soccer_team[jersey_num] = player_rating


def remove_player(soccer_team):
    jersey_num = int(input('Enter a jersey number: \n'))
    del soccer_team[jersey_num]


def update_player(soccer_team):
    jersey_num = int(input('Enter a jersey number: \n'))
    updated_rating = int(input('Enter a new player rating: \n'))
    soccer_team[jersey_num] = updated_rating


def players_above_rating(soccer_team):
    player_rating = int(input('Enter a rating: \n'))
    players_rating_list = sorted(list(soccer_team.keys()))

    print(f'ABOVE {player_rating}')
    for i in players_rating_list:
        if soccer_team[i] > player_rating:
            print(f'Jersey Number: {i}, Rating: {soccer_team[i]}')


def roster(soccer_team):
    team_list = sorted(list(soccer_team.keys()))
    print('ROSTER')
    for i in team_list:
        print(f'Jersey Number: {i}, Rating: {soccer_team[i]}')


soccer_team = dict()
menu = ''

while menu != 'q':
    menu = print_menu()

    if menu == 'a':
        add_player(soccer_team)

    elif menu == 'r':
        remove_player(soccer_team)

    elif menu == 'd':
        roster(soccer_team)


