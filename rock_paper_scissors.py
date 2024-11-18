import random

options=("rock","paper","scissors")
pscore=0
cscore=0
running=True

while running==True:
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("Enter your choice (rock/paper/scissors): " )
        if player not in options:
            print("enter valid option")
    
    print(f"\n{player} x {computer}\n")
    if player==computer:
        print("its a tie !\n")
    elif player == "paper" and computer == "rock":
        print("You won !!\n")
        pscore +=1    
    elif player == "scissors" and computer == "paper":
        print("You won !!\n")
        pscore +=1     
    elif player == "rock" and computer == "scissors":
        print("You won !!\n")
        pscore +=1
    else :
        print("you lose !\n")
        cscore+=1
    print(f"your score :{pscore}")
    print(f"computer score :{cscore}\n")
    choice= input("Do you want to play again(y/n) ?: ")
    if choice.lower() == "n":
        running = False

print("\nthanks for playing !\nsee you soon")