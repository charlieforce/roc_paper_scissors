import random

print('Hello and Welcome to the Rock, Paper, Scissors game!\n')
prompt_error = 'You did not select from the allowed options!'
game_is_active = True
 

while game_is_active:
    options = ['rock', 'paper', 'scissors']

    player_choice = input('Did you throw rock, paper, or scissors? ')
    computer_choice = options[random.randint(0,2)]

    #Get player to correctly choose option
    while player_choice not in options:
      print(prompt_error)
      player_choice = input('Did you throw rock, paper, or scissors? ')

    # What did the players select?
    print('The player\'s choice is', player_choice)
    print('The computer\'s choice is', computer_choice)

    # Comparisons
    if player_choice == computer_choice:
        print('\n~~Tic Game!~~\n')

    elif player_choice == 'rock':
        if computer_choice == 'paper':
            print('\n~~Computer Wins!~~\n')
        elif computer_choice == 'scissors':
              print('\n~~Player Wins!~~\n')

    elif player_choice == 'scissors':
        if computer_choice == 'rock':
            print('\n~~Computer Wins!~~\n')
        elif computer_choice == 'paper':
              print('\n~~Player Wins!~~\n')

    elif player_choice == 'paper':
        if computer_choice == 'rock':
            print('\n~~Player Wins!~~\n')
        elif computer_choice == 'scissors':
              print('\n~~Computer Wins!~~\n')


    #END OF GAME
    game_is_active = input('Would you like to keep playing? (Y/N) ')

    # Get player to correctly choose option
    while type(game_is_active) is not bool:
        if game_is_active == 'y' or game_is_active == 'yes' or game_is_active == 'Yes':
            pass
        elif game_is_active == 'n' or game_is_active == 'no' or game_is_active == 'No':
              game_is_active = False
        else:
            print(prompt_error)
            game_is_active = input('would you like to keep playing? (y/n) ')



