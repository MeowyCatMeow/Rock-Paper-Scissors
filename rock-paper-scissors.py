"""
rock paper scissors
https://hyperskill.org/projects/78?track=2
https://imgur.com/a/usDCkUw
"""
import random

def game(user_move):
    global user_score
    global value_win
    global choices
    pc_move = random.choice(list(value_win.keys()))
    if value_win[user_move] == pc_move or pc_move in value_win[user_move]:    
        print(f"Sorry, but the computer chose {pc_move}")    
    elif user_move == pc_move:
        print(f"There is a draw ({pc_move})")
        user_score += 50
    elif value_win[user_move] != pc_move or pc_move not in value_win:    
        print(f"Well done. The computer chose {pc_move} and failed")
        user_score += 100

def get_win(x, li):
    newli = []
    # copy = li.copy()
    # copy.remove(x)
    # return copy[len(choices) // 2:]
    # return random.sample(copy, len(copy) // 2 )
    distance = int(len(li) // 2 - li.index(x))
    # print(distance)
    newli = (li[-distance:] + li[:-distance])
    return newli[len(newli) // 2:]
    
def get_score():
    global user_name
    file = open("rating.txt", "r")
    for line in file:
        name, score = line.split()
        names[name] = score
    if user_name in names:
        return int(names[user_name])
    else:
        return 0
    file.close()

def greetings():

    global value_win
    global user_name
    global choices
    print("Enter your name:", end=" ")
    user_name = input()
    print("Hello,", user_name)
    li = input()
    print("Okay, let's start")
    if len(li) != 0:
        choices = li.split(",")
        for x in choices:
            value_win[x] = get_win(x, choices)
    else:
        choices = ["rock", "paper", "scissors"]
        value_win = {"rock": "paper", "scissors" : "rock", "paper" : "scissors"}  

    
value_win = {}
names = {}
greetings()
user_score = get_score()

while True:
    command = input()    
    if command == "!exit":
        print("Bye!")
        quit()
    elif command == "!rating":
        print("Your rating:", user_score)
    elif command in choices:
        game(command)
    else:
        print("Invalid input")
