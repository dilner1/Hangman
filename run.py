import random


def generate_the_word():
    """
    Opens easyWords.txt file and selects a word at random
    """
    word_file = open("easyWords.txt", "r")
    random_word = random.choice(word_file.read().split('\n'))
    word_file.close()
    print(random_word.lower()) 

       

def main():
    """
    Calls all functions
    """
    print("Welcome to Hangman, let's begin")

    generate_the_word()
    print("A word has been selected, type a letter.")

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