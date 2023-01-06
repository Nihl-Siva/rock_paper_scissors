import random

rps_list=['rock', 'paper', 'scissors']

# Basic RPS function that meets all requirements
def rps_player():
    while True:
        cp_choice=random.choice(rps_list)
        user_choice=input("Choose: Rock, Paper, Scissors or Quit ")
        
        if user_choice.lower() == 'rock':
            print("Computer chose:",cp_choice.title() )
            if cp_choice == 'rock':
                print("Game Tied!")
            elif cp_choice == 'paper':
                print("You Lose!")
            else:
                print("You Win!")

        elif user_choice.lower() == 'paper':
            print("Computer chose:",cp_choice.title() )
            if cp_choice == 'paper':
                print("Game Tied!")
            elif cp_choice == 'scissors':
                print("You Lose!")
            else:
                print("You Win!")

        elif user_choice.lower() == 'scissors':
            print("Computer chose:",cp_choice.title() )
            if cp_choice == 'scissors':
                print("Game Tied!")
            elif cp_choice == 'rock':
                print("You Lose!")
            else:
                print("You Win!")

        elif user_choice.lower() == 'quit':
            print("Thank you for playing!")
            break

        else: # if player enter anything other than 'rock', 'paper', 'scissors', and 'quit', throw invalid input message
            print("Invalid input. Please try again.")

# More complex RPS function
# Player can now bet money
# Player inputs the total amount of money they want to gamble
# Each round, player can bet some or all of their money in their total amount
def rps_player_2():
    player_pot = float(input("How much money will you be playing with today? $"))
    win_count = 0 # win count is used so if the player is winning a lot, they are set up to lose their next round >:D

    while True:
        print(f"Current player pot: ${player_pot}")

        if player_pot == 0:
            print("You are out of funds. Thank you for playing!")
            break
        
        # loop used to make sure player does not bet over their total amount
        while True:
            bet_amount = float(input("How much do you want to bet this round? $"))
            if bet_amount > player_pot:
                print("Can't bet more than what you have. Please enter a bet amount less than or equal to your total pot.")
            else:
                break

        cp_choice=random.choice(rps_list)
        user_choice=input("Choose: Rock, Paper, Scissors or Quit ")        
        
        # if the player won 3 in a row, computer will automatically win the next round. "The house always wins!" >:D
        if user_choice.lower() == 'rock' and win_count == 3:
            print("Computer chose: Paper")
            print("You Lose!")
            player_pot -= bet_amount
            win_count = 0
        
        elif user_choice.lower() == 'paper' and win_count == 3:
            print("Computer chose: Scissors")
            print("You Lose!")
            player_pot -= bet_amount
            win_count = 0

        elif user_choice.lower() == 'scissors' and win_count == 3:
            print("Computer chose: Rock")
            print("You Lose!")
            player_pot -= bet_amount
            win_count = 0
        
        # if the player wins, increase the player's pot by the player's bet amount and increment win count by 1
        # if the player loses, decrease the player's pot by the player's bet amount and reset the win count to 0
        elif user_choice.lower() == 'rock':
            print("Computer chose:",cp_choice.title() )
            if cp_choice == 'rock':
                print("Game Tied!")
            elif cp_choice == 'paper':
                print("You Lose!")
                player_pot -= bet_amount
                win_count = 0
            else:
                print("You Win!")
                player_pot += bet_amount
                win_count += 1

        elif user_choice.lower() == 'paper':
            print("Computer chose:",cp_choice.title() )
            if cp_choice == 'paper':
                print("Game Tied!")
            elif cp_choice == 'scissors':
                print("You Lose!")
                player_pot -= bet_amount
                win_count = 0
            else:
                print("You Win!")
                player_pot += bet_amount
                win_count += 1

        elif user_choice.lower() == 'scissors':
            print("Computer chose:",cp_choice.title() )
            if cp_choice == 'scissors':
                print("Game Tied!")
            elif cp_choice == 'rock':
                print("You Lose!")
                player_pot -= bet_amount
                win_count = 0
            else:
                print("You Win!")
                player_pot += bet_amount
                win_count += 1

        elif user_choice.lower() == 'quit':
            print("Thank you for playing!")
            break

        else:
            print("Invalid input. Please try again.")
                

rps_player_2()
