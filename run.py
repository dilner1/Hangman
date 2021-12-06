import random

lives = 8
letters_guessed = []
difficulty = ""

logo = ("""
    __  __                                      
   / / / /___ _____  ____ _____ ___  ____ _____ 
  / /_/ / __ `/ __ \/ __ `/ __ `__ \/ __ `/ __ \\
 / __  / /_/ / / / / /_/ / / / / / / /_/ / / / /
/_/ /_/\__,_/_/ /_/\__, /_/ /_/ /_/\__,_/_/ /_/ 
                  /____/                        
    """)

def difficulty_select():
    """
    Takes input from user to select difficulty
    """
    
    global difficulty
    difficulty_question = input("Please select difficulty,\n Type easy, medium or hard: ")
    difficulty += difficulty_question.lower()
    diff = difficulty.replace(" ", "")

    print(f"You selected {diff}.")


def generate_the_word():
    """
    Opens easyWords.txt file and selects a word at random
    """
    print(difficulty)
    word_file = open("easyWords.txt", "r")
    random_word = random.choice(word_file.read().split('\n'))
    word_file.close()
    print(random_word.lower()) 

def player_turn():
    """
    Takes player guess
    """
    letters_guessed 
    player_guess = input("Please choose a letter:\n").lower()
    if not player_guess.isalpha():
        return "Only letters are allowed, try again!"
    else:
        print(f'You selected the letter {player_guess}')
        letters_guessed.append(player_guess)
        print(letters_guessed)
        
def main():
    """
    Calls all functions
    """
    print("Welcome to Hangman, let's begin!")
    difficulty_select()
    generate_the_word()
    print("A word has been selected.")
    player_turn()

print(logo)
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