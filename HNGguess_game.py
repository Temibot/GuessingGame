import random

level1=random.randint(1,10)
level2=random.randint(1,20)
level3=random.randint(1,50)

def game_level():
    level_dict = {
        1 : ["Easy",1,10, 6, level1],
        2 : ["Medium",1, 20, 4, level2],
        3 : ["Hard", 1, 50, 3, level3]
        }
    print("There are 3 game levels here: \n1. Easy\n2. Medium\n3. Hard")
    while True:

        try: 
            level_ans = int(input("Enter your level of choice: "))

            break
        except: 
            print("Invalid input")
       
    if level_ans == 1:
        return level_dict[1]
    elif level_ans == 2:
        return level_dict[2]
    elif level_ans == 3:
        return level_dict[3]
    else:
        print("Type a number 1, 2 or 3")
        guessGame() #jump back to the beginning if user doesnt type 1,2 or 3

def guessGame():
    level_item = game_level() #called the first function here
    print(f"You are in for the {level_item[0]} level; guess a number between {level_item[1]} - {level_item[2]} "
          f"and you have a maximum of {level_item[3]} chances to do so, Goodluck!")

    guessChance = 0

    while  guessChance < level_item[3]:
        while True:
            try:
                userGuess = int(input(f"Guess a number between {level_item[1]} - {level_item[2]}: "))
                break
            except:
                print("Type a number")

        guessChance+=1

        if userGuess == level_item[4]:
            print('You got it right!')
            quit()
        else:
            if level_item[3]-guessChance>0:
                print("That was wrong. You have", level_item[3]-guessChance, 'chance(s) left!')
    else:
        print('Game over!')



guessGame()
