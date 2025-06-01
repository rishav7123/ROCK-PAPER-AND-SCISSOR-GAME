import random
print("________WELCOME TO YOU FOR JOINING THIS GAME_________")

items = ["rock", "paper", "scissor"]

user_choice = input("Enter your choice: 'rock', 'paper', 'scissor'\n")
computer_choice = random.choice(items)
print(f"Computer choice is {computer_choice}")

if user_choice == computer_choice:
    print("Match tie!")

else:
    if user_choice == "rock":
           if computer_choice == "paper":
                
                print("Paper covers rock")
                print("Computer wins")
           else:    
                print("Rock breaks scissor")
                print("User wins")    

    if user_choice == "paper":
           if computer_choice == "rock":
                
                print("Paper covers rock")
                print("User wins")
           else:    
                print("Scissor cuts paper")
                print("Computer wins")  

    if user_choice == "scissor":
           if computer_choice == "paper":
               
                print("Scissor cuts paper")
                print("User wins")
           else:    
                print("Rock breaks scissor")
                print("Computer wins")    
                        
