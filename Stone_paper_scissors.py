import random

map={'Stone':1, 'paper':0, 'Scissors':-1}
reverse_map = {v: k for k, v in map.items()}

while True:
 a = int(input("Enter Number (1=Stone, 0=Paper, -1=Scissors): "))
 computer=random.choice([1,0,-1])
 print("You chose:", reverse_map[a])
 print("Computer chose:", reverse_map[computer])



 if(a==computer): print("Draw")
 else:
    if(a==1 and computer==0): print("computer win")
    elif(a==1 and computer==-1): print("you win")
    elif(a==0 and computer==1): print("you win")
    elif(a==0 and computer==-1): print("you win")
    elif(a==-1 and computer==1): print("Computer wins")
    elif(a==-1 and computer==0): print("you win")
    elif(a==1 and computer==-1): print("you win")
    else: print("something went wrong")


    choice = input("Do you want to play again? (yes/no): ").lower()
    if choice != "yes":
        print("Game Over 👋")
        break
