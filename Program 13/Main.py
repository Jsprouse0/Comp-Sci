'''
Author: Jacob Sprouse
Assignment title: Program 13
Assignment Description: Team Roster
Due Date: 05/12/2023
Date Created: 05/12/2023
Date Last Modified: 05/12/2023
'''

# def print_menu()
# *******************************************************************************************
# Description: prints the menu for the soccer team                                          *
# return: user input character                                                              *
# pre-condition: void function, will execute as long as user does not input 'q'             *
# post-condition: user input will determine the next function to execute or quit altogether *
#                                                                                           *
# *******************************************************************************************

# def add_player()
# *******************************************************************************************
# Description: will add a new player to the soccer_team dictionary                          *
# return: no return statement, only appends input to the dictionary                         *
# pre-condition: user chooses 'a' in the menu function                                      *
# post-condition: will add the new player into the dictionary with jersey num & rating      *
#                                                                                           *
# *******************************************************************************************

# def remove_player()
# *******************************************************************************************
# Description: will remove the player from the dictionary at the jersey number              *
# return: no return, only removes from the dictionary                                       *
# pre-condition: user chooses 'd' in the menu function to execute                           *
# post-condition: will remove the player from the dictionary                                *
#                                                                                           *
# *******************************************************************************************

# def update_player_ratings()
# *******************************************************************************************
# Description: updates the players rating to an existing player in the dictionary           *
# return: no return, will update an existing key within the dictionary                      *
# pre-condition: user chooses 'u' in the menu function to execute                           *
# post-condition: will update an existing players rating                                    *
#                                                                                           *
# *******************************************************************************************

# def output_players_above_ratings()
# *******************************************************************************************
# Description: will loop through the dictionary to print players above the input rating     *
# return: will print the jersey numbers and ratings for players above a certain rating      *
# pre-condition: user chooses 'r' in the menu function to execute                           *
# post-condition: outputs the players jersey and ratings above the users input              *
#                                                                                           *
# *******************************************************************************************

# def output_team_roster()
# ***********************************************************************************************
# Description: outputs the whole dictionary roster of all the jersey numbers with their players *
# return: all the dictionary contents with the players jersey number and rating                 *
# pre-condition: user chooses 'o' in the menu function to print                                 *
# post-condition: will print all the contents within the dictionary                             *
#                                                                                               *
# ***********************************************************************************************


def print_menu():
    print('\nMenu')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit\n')

    return input('Choose an option: \n').lower()


def add_player(soccer_team):
    jersey_number = int(input('Enter a new player\'s jersey number: \n'))
    player_rating = int(input('Enter the player\'s rating: \n'))
    soccer_team[jersey_number] = player_rating


def remove_player(soccer_team):
    jersey_number = int(input('Enter a jersey number: \n'))
    del soccer_team[jersey_number]


def update_player_ratings(soccer_team):
    jersey_number = int(input('Enter a jersey number: \n'))
    player_rating = int(input('Enter a new rating for player: \n'))
    soccer_team[jersey_number] = player_rating


def output_players_above_rating(soccer_team):
    player_rating = int(input('Enter a rating: \n'))
    list_jersey_numbers = sorted(list(soccer_team.keys()))

    print(f'ABOVE {player_rating}')
    for i in list_jersey_numbers:
        if soccer_team[i] > player_rating:
            print(f'Jersey Number: {i}, Rating: {soccer_team[i]}')


def output_team_roster(soccer_team):
    player_list = sorted(list(soccer_team.keys()))
    print('ROSTER')
    for i in player_list:
        print(f'Jersey number: {i}, Rating: {soccer_team[i]}')


soccer_team = dict()
menu = ''

while menu != 'q':
    menu = print_menu()

    if menu == 'a':
        add_player(soccer_team)

    elif menu == 'd':
        remove_player(soccer_team)

    elif menu == 'u':
        update_player_ratings(soccer_team)

    elif menu == 'r':
        output_players_above_rating(soccer_team)

    elif menu == 'o':
        output_team_roster(soccer_team)
