# Rock Paper And Scissor  Game Created By Sanaan Wani
from random import randint
print("Type '1' to end game")
print("Can you beat me human?")
keep_playing = "true"
while keep_playing == "true":
    player = input('Rock(r),Paper(p) or Scissors(s)?')
    if player == "1":
        print("Nice to meet you! GG!")
        break
    print(player, 'vs', end=' ')
    chosen = randint(1, 3)
    # print(chosen)
    if chosen == 1:
        computer = 'r'
    elif chosen == 2:
        computer = 'p'
    else:
        computer = 's'
    print(computer)
    if player == computer:
        print("We are connected! Its a Draw -_-")
    elif player == "r" and computer == "s":
        print('You Won!')
    elif player == "s" and computer == "r":
        print('LOL! Try again ;)')
    elif player == "s" and computer == "p":
        print('You Won!')
    elif player == "p" and computer == "s":
        print('LOL! Try again ;)')
    elif player == "p" and computer == "r":
        print('LOL! Try again ;)')
    elif player == "r" and computer == "p":
        print('LOL! Try again ;)')
    else:
        print("You can only choose r,p and s!")

