import random  # gives random things and 

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"] # the options that should be picked

while True: 
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower() # asking user for input making sure its lowercase desired condition
    if user_input == "q": #condition if user enters q then program will stop
        break  # this will stop the program if the condition is met 

    if user_input not in options: # so if the users input does not match anything in the list 
        continue

    random_number = random.randint(0, 2) 
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number] 
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":  # setting the conditions if you won the game 
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")  # the conditions if you lose anything 
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")





        
        

    

    


    

    





    





    

        




    
    




    

        
    

    
    
    

    


