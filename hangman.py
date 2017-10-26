# 345
from random import choice
from getpass import getpass
import turtle


class drawHangedMan():
    '''Class to define all the functions drawing the hanged man's body
    parts and a dictionary to easily call them based on guesses left'''

    def Base():
        turtle.speed(0)
        turtle.up()
        turtle.setpos(0, -200)
        turtle.down()
        turtle.bk(200)
        turtle.lt(90)
        turtle.fd(400)
        turtle.rt(90)
        turtle.speed(2)

    def Pole():
        turtle.fd(100)
        turtle.rt(90)
        # turtle.done()

    def Rope():
        turtle.fd(50)
        # turtle.done()

    def Head():
        turtle.circle(20, 450)
        turtle.rt(90)

    def Body():
        turtle.fd(150)
        turtle.bk(145)

    def LeftArm():
        turtle.rt(30)
        turtle.fd(80)
        turtle.bk(80)
        turtle.lt(30)

    def RightArm():
        turtle.lt(30)
        turtle.fd(80)
        turtle.bk(80)
        turtle.rt(30)

    def LeftLeg():
        turtle.fd(145)
        turtle.rt(30)
        turtle.fd(80)
        turtle.bk(80)
        turtle.lt(30)

    def RightLeg():
        turtle.lt(30)
        turtle.fd(80)
        turtle.bk(80)
        turtle.rt(30)

    actions = {8: Base,
               7: Pole,
               6: Rope,
               5: Head,
               4: Body,
               3: LeftArm,
               2: RightArm,
               1: LeftLeg,
               0: RightLeg}


def getSecretWord(file_name):
    f = open(file_name)
    print("Loading word list from file...")
    words = f.read().split(' ')
    f.close()
    print(f"{len(words)} words loaded.")
    secret = choice(words)

    return secret


def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            count += 1
    return count == len(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    output = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            output += letter
        else:
            output += '_'

    return output


def getAvailableLetters(lettersGuessed):
    output = [chr(a) for a in range(97, 123) if chr(a) not in lettersGuessed]
    return ' '.join(output)


def hangman(secretWord):
    gui = drawHangedMan()  # un-comment for next level graphics
    guesses = 8
    lettersGuessed = []

    gui.actions[guesses]()  # Draw the starting setup

    while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0:
        print(f"You have {guesses} guesse(s) left.")
        print(f"Available letters: {getAvailableLetters(lettersGuessed)}")

        attempt = input("Please guess a letter: ")

        if attempt in lettersGuessed:
            print("Oops! You've already guessed that letter: ", end="")
        elif attempt not in secretWord:
            lettersGuessed.append(attempt)
            print("Oops! That letter is not in my word: ", end="")
            guesses -= 1
            gui.actions[guesses]()  # Draw the hanged man
        else:
            lettersGuessed.append(attempt)
            print("Good guess: ", end="")

        print(getGuessedWord(secretWord, lettersGuessed))
        print("\n*************\n")

    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!\n")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secretWord}.\n")


print("\nWelcome to the game, Hangman!")

# un-comment for multiplayer
players = 0
while players != 1 and players != 2:
    players = int(input("1 or 2 players? "))

# players = 1  # comment out for multiplayer

secretWord = getSecretWord('words.txt') if players == 1\
    else getpass("Enter the secret word: ")

print(f"The secret word is {len(secretWord)} letters long.")
# print(f"It's {secretWord}")  # For testing purposes
print("*************\n")

hangman(secretWord)
