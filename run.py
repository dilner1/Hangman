import random
import easyWords

thing = easyWords.easy_word_list
word = random.choice(thing)
lives = 8
letters_guessed = []
done = False

# difficulty = ""

logo = ("""
    __  __                                      
   / / / /___ _____  ____ _____ ___  ____ _____ 
  / /_/ / __ `/ __ \/ __ `/ __ `__ \/ __ `/ __ \\
 / __  / /_/ / / / / /_/ / / / / / / /_/ / / / /
/_/ /_/\__,_/_/ /_/\__, /_/ /_/ /_/\__,_/_/ /_/ 
                  /____/                        
    """)

#  def generate_the_word():
#     """
#     Opens easyWords.txt file and selects a word at random
#     """
#     # print(difficulty)
#     word_file = open("easyWords.txt", "r")
#     random_word = random.choice(word_file.read().split('\n'))
#     word_file.close()
#     print(random_word.lower()) 

def hide_word():
    global done
    global lives
    global word
    global letters_guessed
    while not done:
        for letter in word:
            if letter.lower() in letters_guessed:
                print(letter, end="")
            else:
                print("_",end="")
        print("")


        guess = input(f"Allowed error left {lives}. Next Guess:")
        letters_guessed.append(guess.lower())
        if guess.lower() not in word.lower():
            lives -= 1
            if lives == 0:
                break

        done = True
        for letter in word:
            if letter.lower() not in letters_guessed:
                done = False


    if done:
        print(f"You found the word, it was {word}")
    else: 
        print(f"You lost, the word was {word}")

def main():
    """
    Prints all functions
    """
    hide_word()


print(logo)
main()


# def difficulty_select():
#     """
#     Takes input from user to select difficulty
#     """
    
#     global difficulty
#     difficulty_question = input("Please select difficulty,\n Type easy, medium or hard: ")
#     difficulty += difficulty_question.lower()
#     diff = difficulty.replace(" ", "")

#     if validate_difficulty(diff):
#             print(f"You selected {diff}.")
            
#     # if diff != 'easy':
#     #     print('You need to type easy, medium or hard.')


#     # else:
#     #     print(f"You selected {diff}.")
        
# def validate_difficulty(value):
#     try:
#         value == 'easy'
#     except ValueError as e:
#         print(f"You typed the wrong thing, {e}")
#     except Exeption:
#         print('THIS IS WRONG')


# def generate_the_word():
#     """
#     Opens easyWords.txt file and selects a word at random
#     """
#     # print(difficulty)
#     word_file = open("easyWords.txt", "r")
#     random_word = random.choice(word_file.read().split('\n'))
#     word_file.close()
#     print(random_word.lower()) 

# def player_turn():
#     """
#     Takes player guess
#     """
#     letters_guessed 
#     player_guess = input("Please choose a letter:\n").lower()
#     if not player_guess.isalpha():
#         return "Only letters are allowed, try again!"
#     else:
#         print(f'You selected the letter {player_guess}')
#         letters_guessed.append(player_guess)
#         print(letters_guessed)
        
# def main():
#     """
#     Calls all functions
#     """
#     print("Welcome to Hangman, let's begin!")
#     difficulty_select()
#     generate_the_word()
#     print("A word has been selected.")
#     player_turn()

# print(logo)
# main()

    


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