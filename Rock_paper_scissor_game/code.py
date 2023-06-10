import random
player1 = input("selecet Rock, Paper or Scissor ").lower()
player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()

print("Player2 selected " + player2)

if(player1 == "rock" and player2 == "paper"):
    print("player2 won")
elif(player1 == "peper" and player2 == "scissor"):
    print("player2 won")
elif(player1 == "scissor" and player2 == "rock"):
    print("player2 won")
elif(player1 ==  player2):
    print("Tie")
else:
    print("Player1 won")