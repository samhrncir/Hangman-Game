#!/usr/bin/env python2

from random import *

player_score = 0
computer_score = 0

def hangedman(handman):
    graphic = [
    """
        +----------+
        |           |
        |           O
        |
        |
        |
    ====================
    """
        ,
    """
        +----------+
        |           |
        |           O
        |           |
        |
        |
    ====================
    """
        ,
    """
        +----------+
        |           |
        |           O
        |          -|
        |
        |
    ====================
    """
        ,
    """
        +----------+
        |           |
        |           O
        |          -|-
        |
        |
    ====================
    """
        ,
    """
        +----------+
        |           |
        |           O
        |          -|-
        |          /
        |
    ====================
    """
        ,
    """
        +----------+
        |           |
        |           O
        |          -|-
        |          / \
        |
    ====================
    """
    ]


def start():
    print ("Let's play a game of Linux Hangman.")
    while game():
        pass
    scores()


def game():
    dictionary = ["gnu", "kernel", "linux", "mageia", "penguin", "ubuntu"]
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * ["-"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    while (letters_wrong != tries) and ("".join(clue) != word):
        letter=guess_letter()
        if len(letter)==1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print("You've already picked", letter)
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong +=1:
                    print("Sorry,", letter, "isn't what we're looking for.")
                else:
                    print("Congratulations,", letter, "is correct.")
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print ("Choose another.")

        hangedman(letters_wrong)
        print (" ".join(clue))
        print("Guesses: ", letters_tried)

        if letters_wrong == tries:
            print "Game Over."
            print("The word was", word)
            computer_score += 1
            break
        if "".join(clue) == word:
            print "You Win!"
            print("The word was", word)
            player_score += 1
            break
    return play_again()


def guess_letter():
    print
    letter = raw_input("Take a guess at our mystery word:")
    letter.strip()
    letter.lower()
    print
    return letter


def play_again():
    answer = raw_input("Would you like to play again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "Of course!"):
        return answer
    else:
        print("Thank you very much for playing our game. See you next time!")


def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player ", player_score)
    print("Computer: ", computer_score)

if __name__ == '__main__':
    start()
