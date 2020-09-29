import random

choice = ["paper", "scissors", "rock"]
com = choice[random.randint(0, 2)]
input_correct = 1

while (input_correct):
    player = input(
        "請輸入下列其中一種: paper ,scissors, rock ")
    if (player in choice):
        input_correct = 0
    else:
        print("你的輸入有誤，請重新輸入")

print("你的選擇是:" + player + ", 電腦的選擇是:" + com)

if ((com == "rock" and player == "paper") or (com == "paper" and player == "scissors") or (com == "scissors" and player == "rock")):
    print("You win!")
elif (com == player):
    print("Tie")
else:
    print("You Lose")
