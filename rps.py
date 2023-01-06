import random

rps_list=['rock', 'paper', 'scissors']

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

        else:
            print("Invalid input. Please try again.")
                

rps_player()
