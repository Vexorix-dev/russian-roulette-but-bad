# Imports for later
import random
# Pre-game setup/Menu
playing=False
player_turn=False
dealer_turn=False
print("Buckshot Roulette: Python Version")
print("Press 'Y' to play")
# Main Game logic
if input()=="y":
    print("The game has begun!")
    playing=True
else:
    print("Maybe next time.")

if playing:
    player_turn=True
    print("The round has begun. Prepare yourself.")
while player_turn:
    print("Choose who to shoot. Click 'S' to shoot your self. Click 'D' to shoot the dealer. Be aware that shooting yourself skips the dealers turn.")
    choice=input()
    if choice.lower()=="d":
        shot=random.randint(1,6)
        if shot==1:
            print("The dealer has died. You win!")
            playing=False
            player_turn=False
            dealer_turn=False
        else:
            print("The shot was a blank. It is the dealer's turn.")
            dealer_turn=True
    elif choice.lower()=="s":
        shot=random.randint(1,6)
        if shot==1:
            print("You died!")
            playing=False
        else:
            print("Whew! You survived. You skipped the dealer's turn.")
        while dealer_turn:
            print("The dealer made a decision.")
            dealer_choice=random.randint(1,2)
            if dealer_choice==1:
                print("The dealer shoots himself.")
                shot=random.randint(1,6)
                if shot==1:
                    print("The dealer has died! You won!")
                    playing=False
                    player_turn=False
                    dealer_turn=False
                else:
                    print("The dealer survived. He chooses again.")
            else:
                print("The dealer shoots you!")
                shot=random.randint(1,6)
                if shot==1:
                    print("You died! Game over.")
                    playing=False
                    player_turn=False
                    dealer_turn=False
                else:
                    print("The shot was a blank! It is now your turn.")
                    playing=False
                    player_turn=True
                    dealer_turn=False
    
    
        
