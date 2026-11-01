#Rock-Paper-Scissors. Write a program where user plays R, P, or S, then the system selects R, P, or S for the computer and display who wins. 
#first step is to import the random module to generate random values.
import random
#second step is to create a list of choices for the computer.
choices = ["R", "P", "S"]   
#third step is to ask the user to give their choice and store it in a variable.
user_choice = input("Please enter your choice (R, P, or S): ").upper()  
#fourth step is to generate a random choice for the computer and store it in a variable.
computer_choice = random.choice(choices)
#fifth step is to display the choices of the user and the computer.
print(f"User choice: {user_choice}")
print(f"Computer choice: {computer_choice}")
#sixth step is to determine the winner based on the choices of the user and the computer
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "R" and computer_choice == "S") or (user_choice == "P" and computer_choice == "R") or (user_choice == "S" and computer_choice == "P"):
    print("User wins!")
else:
    print("Computer wins!") 
#Improve the previous program to keep the score and ask the user if the want to play again. Each time display the current score.
#first step is to initialize the score variables for the user and the computer.
user_score = 0
computer_score = 0
#second step is to create a loop that continues until the user decides to stop playing.
while True:
    # Ask the user for their choice
    user_choice = input("Please enter your choice (R, P, or S): ").upper()
    
    # Validate user input
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    
    # Generate a random choice for the computer
    computer_choice = random.choice(choices)
    
    # Display the choices of the user and the computer
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    
    # Determine the winner and update scores
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "R" and computer_choice == "S") or (user_choice == "P" and computer_choice == "R") or (user_choice == "S" and computer_choice == "P"):
        print("User wins!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    
    # Display current scores
    print(f"Current Score - User: {user_score}, Computer: {computer_score}")
    
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again != 'Y':
        break