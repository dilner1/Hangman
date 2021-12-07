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


def hide_word():
    """
    Hides letters in chosen word from player
    """
    global word
    global letters_guessed
    while not done:
        for letter in word:
            if letter.lower() in letters_guessed:
                print(letter, end="")
            else:
                print("_",end="")
        print("")
        player_select_letter()

def player_select_letter():
    """
    Takes player input
    """
    global done
    global lives
    global word
    global letters_guessed
    guess = input(f"Allowed error left {lives}. Next Guess:")
    letters_guessed.append(guess.lower())
    if guess.lower() not in word.lower():
        lives -= 1
        print(hangman[lives])
        if lives == 0:
            win_check()

def win_check():
    """ 
    Checks if player wins or loses
    """
    global done
    global letters_guessed
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
    win_check()
    
print(logo)
main()