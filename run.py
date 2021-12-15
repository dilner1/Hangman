import random
import colorama
from colorama import Fore, Back

import easyWords
import drawing

all_easy_words = easyWords.easy_word_list
hangman = drawing.drawing_dictionary


done = False

# difficulty = ""

logo = (Fore.YELLOW + """
    __  __                                      
   / / / /___ _____  ____ _____ ___  ____ _____ 
  / /_/ / __ `/ __ \/ __ `/ __ `__ \/ __ `/ __ \\
 / __  / /_/ / / / / /_/ / / / / / / /_/ / / / /
/_/ /_/\__,_/_/ /_/\__, /_/ /_/ /_/\__,_/_/ /_/ 
                  /____/                        
    """)

class game():
    def __init__(self):
        """
        Define variables for class
        """
        self.word = self.set_word()
        self.secret = list(len(self.word)*'_')
        self.lives = 8
        self.hangman = hangman
        self.guesses = []
        self.incorrect_guesses_list = " ".join(self.guesses)

        print("Game starting...\n")

    def set_word(self):
        return random.choice(all_easy_words)

    def show_word(self):
        """
        Takes selected word to be hidden and replaces letters
        """

        joined_word = " ".join(self.secret)
        print(joined_word)
        print(f'You have {self.lives} lives remaining.')

    def drawing(self, lives):
        """
        Takes the players lives and prints out connected picture
        """
        print(hangman[lives])

    def store_guesses(self, guess):
        """
        Takes guessed letter, if incorrect it is stored for user to view
        """
        # self.guesses = self.guesses
        # self.incorrect_guesses_list = " ".join(self.guesses)
        if guess not in self.word.lower():

            self.guesses.append(guess)
            return self.incorrect_guesses_list
        else:
            # self.incorrect_guesses_list = " ".join(self.guesses)
            return self.incorrect_guesses_list

    def is_valid_guess(self, guess):
        """
        Checks if guess is a valid
        """

        letter_guess = guess.lower()
        if letter_guess.isalpha() == False:
            print(f"{Back.RED}{guess} is not a letter. You must type a letter.{Back.RESET}\n")
            self.update_letters()
            return False

        elif letter_guess in self.guesses or letter_guess in self.secret:
            print(f"{Back.RED}You have already tried letter {letter_guess}, please try another letter.{Back.RESET}\n")
            self.update_letters()
            return False

        elif len(letter_guess) >= 2:
            length = len(letter_guess)
            print(f"{Back.RED}Your tried to guess {length} letters. You can only type one at a time.{Back.RESET}\n")
            self.update_letters()
            return False
        
        elif letter_guess.isalpha():
            return True

    def is_guess_in_word(self, guess):
        """
        Checks if guess matches a letter in the hidden word, finds the index and reveals letter in secret word
        """
        if guess.lower() not in self.word.lower():
            self.lives -= 1
            print(f"{Fore.MAGENTA}Incorrect, you lost a life.{Fore.YELLOW}\n")
        else:
            print(f"{Fore.GREEN}You guessed a letter correctly.{Fore.YELLOW}\n")
            for i in range(0, len(self.word)):
                    letter = self.word[i]
                    if letter == guess:
                        self.secret[i] = guess
                        
        print("")
    def check_win(self, lives):
        if "_" not in self.secret:
            print(f"Congratulations, you have guessed the word with {lives} lives left.\nThe letter was {self.word}")
            return False
    
    def restart_game(self):
        """
        Asks if player wants to continue and allows restart if so
        """
        restart = input('do you want to play again: Y/N?').lower()
        if restart == 'n':
            print('Game ending - thanks for playing :)')
            return False
        elif restart == 'y':
            print("Restarting game...\n")
            return True

    def update_letters(self):
        print(f"so far you have guessed: {self.guesses} \n")

def main():
    """
    Prints all functions
    """
    play = game()
    word = play.word
    print("A word has been selected.\n")
    lives = play.lives
    guesses = play.guesses

    while True:
        play.show_word()
        lives = play.lives
        if lives == 0:
            print(f'You lose, loser!, the word was {word}')
            break
        play.drawing(lives)
        guess = input("Guess a letter: ")

        if play.is_valid_guess(guess) == True:
            letters = play.store_guesses(guess.lower())
            play.is_guess_in_word(guess.lower())
            if play.check_win(lives) == False:
                if play.restart_game() == False:
                    break
                else:
                    exec(open("./run.py").read())
            play.update_letters()
        
print(logo)
main()