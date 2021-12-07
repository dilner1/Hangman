import random
import easyWords
import drawing

all_easy_words = easyWords.easy_word_list
word = random.choice(all_easy_words)
hangman = drawing.drawing_dictionary
lives = 9
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
    global word
    global letters_guessed
    while not done:
        for letter in word:
            if letter.lower() in letters_guessed:
                print(letter, end="")
            else:
                print("_",end="")
        print("")


def player_input():
    global word
    global letters_guessed
    global done
    global lives

    guess = input(f"Allowed error left {lives}. Next Guess:")
    letters_guessed.append(guess.lower())
    if guess.lower() not in word.lower():
        lives -= 1
        print(hangman[lives])
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
    player_input()


print(logo)
main()