#Rock Paper Cisors
import random

player_choice = int(input("Choose between 0 rock 1 paper 2 cisors :"))
if player_choice <= 2:
    ia_choice = random.randint(0,2)
    action = ["Rock", "Paper", "Cisors"]
    print(f"Player => {action[player_choice]} VS {action[ia_choice]} <= IA")

    if player_choice == ia_choice:
        print("Egalite")

    elif player_choice == 0 and player_choice < ia_choice and ia_choice != 2:
        print("IA Win")
    elif player_choice == 1 and player_choice < ia_choice:
        print("IA Win")
    elif player_choice == 2 and ia_choice == 0:
        print("IA Win")
    else:
        print("Player Win")
else:
    print("What ?")
