import random
import easyWords
import drawing

all_easy_words = easyWords.easy_word_list
word = random.choice(all_easy_words)
hangman = drawing.drawing_dictionary


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

def game():
    """
    Hides letters in word
    """
    global done
    # global word
    lives = 9
    letters_guessed = []
    while not done:
        for letter in word:
            if letter.lower() in letters_guessed:
                print(letter, end="")
            else:
                print("_",end="")
        print("")

        guess = input(f"You have {lives} lives left. Guess next letter:")
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
    game()
    
print(logo)
main()