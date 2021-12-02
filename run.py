import random


def generate_the_word():
    """
    Opens easyWords.txt file and selects a word at random
    """
    word_file = open("easyWords.txt", "r")
    random_word = random.choice(word_file.read().split('\n'))
    word_file.close()
    print(random_word.lower()) 

def player_turn():
    """
    Takes player guess
    """
    lives = 8
    player_guess = input("Please choose a letter:").lower()
    if not player_guess.isalpha():
        print("Only letters are allowed, try again!")
    else:
        print(f'You selected the letter {player_guess}')
        

def main():
    """
    Calls all functions
    """
    print("Welcome to Hangman, let's begin")

    generate_the_word()
    print("A word has been selected.")
    player_turn()

main()

    
# def hang_man_drawing(image):
#     """"
#     Stores the drawing states of the hangman
#     """
#     drawing = [
#         """
     
#     ========
#     """,
#     """
#       |
#       |
#       |
#       |
#       |
#     ========
#     """,
#     """
#      _________
#       |/
#       |
#       |
#       |
#       |
#     ========
#     """,
#     """
#      _________
#       |/     |
#       |      0
#       |
#       |
#       |
#     ========
#     """,
#     """
#      _________
#       |/     |
#       |      0
#       |      |
#       |
#       |
#     ========
#     """,
#     """
#      _________
#       |/     |
#       |      0
#       |      |\\
#       |
#       |
#     ========
#     """,
#     """
#      _________
#       |/     |
#       |      0
#       |     /|\\
#       |
#       |
#     ========
#     """,
#     """
#      _________
#       |/     |
#       |      0
#       |     /|\\
#       |     /
#       |
#     ========
#     """,
#     """
#      _________
#       |/     |
#       |      0
#       |     /|\\
#       |     / \\
#       |
#     ========
#     """
#     ]
#     return drawing(image)