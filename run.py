import random
import sys
import colorama
from colorama import Fore, Back

import easyWords
import hardWords
import mediumWords
import drawing

all_easy_words = easyWords.easy_word_list
all_hard_words = hardWords.hard_word_list
all_medium_words = mediumWords.medium_word_list
hangman = drawing.drawing_dictionary

def game_start():
    """
    Prints logo and initialises game, asks player if they want to play
    """
    logo = (Fore.GREEN + """
    __  __                                      
   / / / /___ _____  ____ _____ ___  ____ _____ 
  / /_/ / __ `/ __ \/ __ `/ __ `__ \/ __ `/ __ \\
 / __  / /_/ / / / / /_/ / / / / / / /_/ / / / /
/_/ /_/\__,_/_/ /_/\__, /_/ /_/ /_/\__,_/_/ /_/ 
                  /____/                        
    """)
    print(logo)

    print(f"""{Fore.YELLOW}To start game press any key.
    Type exit key to close game.\n""")
    start = input('Start Game:').lower()
    if start == 'exit':
        print(f"Exiting...\n")
        sys.exit(-1)
    else:
        main()

class game():
    def __init__(self):
        """
        Define variables for class
        """
        print(f"""Please select your difficulty. 
        Press E for easy, m for medium or H for hard.\n""")

        self.word = self.set_word()
        self.secret = list(len(self.word)*'_')
        self.hangman = hangman
        self.guesses = []

        print(f"{Fore.YELLOW}Game starting...\n")

    def set_word(self):
        """
        Fucntion sets random words and difficulty level
        """
        self.difficulty = input("Difficulty select: ")

        if self.difficulty.lower() == 'e':
            self.lives = 8
            return random.choice(all_easy_words)
            
        elif self.difficulty.lower() == 'm':
            self.lives = 7
            return random.choice(all_medium_words)

        elif self.difficulty.lower() == 'h':
            self.lives = 6
            return random.choice(all_hard_words)
        else:
            print(f"""
            {Back.RED}You typed {self.difficulty.lower()}. Select difficulty again.{Back.RESET}
            """)
            game_start()
            
    def show_word(self):
        """
        Takes selected word to be hidden and replaces letters
        """
        joined_word = " ".join(self.secret)
        print(joined_word)
        print(self.word)
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
        if guess not in self.word.lower():

            self.guesses.append(guess)
            return self.guesses
        else:
            return self.guesses

    def is_valid_guess(self, guess):
        """
        Checks if guess is a valid
        """
        letter_guess = guess.lower()
        if letter_guess.isalpha() == False:
            print(f"""{Back.RED}{guess} is not a letter. Type a letter.
            {Back.RESET}\n
            """)
            self.update_letters()
            return False

        elif letter_guess in self.guesses or letter_guess in self.secret:
            print(f"""{Back.RED}You have already tried letter {letter_guess}.
            Please try another letter.{Back.RESET}\n""")
            self.update_letters()
            return False

        elif len(letter_guess) >= 2:
            length = len(letter_guess)
            print(f"""{Back.RED}Your tried to guess {length} letters.
             You can only type one at a time.{Back.RESET}\n""")
            self.update_letters()
            return False
        
        elif letter_guess.isalpha():
            return True

    def is_guess_in_word(self, guess):
        """
        Checks if guess matches a letter in the hidden word, 
        finds the index and reveals letter in secret word
        """
        if guess.lower() not in self.word.lower():
            self.lives -= 1
            print(f"{Fore.MAGENTA}Incorrect, you lost a life.{Fore.YELLOW}\n")
        else:
            print(f"""{Fore.GREEN}You guessed a
             letter correctly.{Fore.YELLOW}\n""")
            for i in range(0, len(self.word)):
                    letter = self.word[i]
                    if letter == guess:
                        self.secret[i] = guess               
        print("")

    def check_win(self, lives):
        if "_" not in self.secret:
            print(Fore.GREEN + """
             _      _______  __
            | | /| / /  _/ |/ /
            | |/ |/ // //    / 
            |__/|__/___/_/|_/  
                    
            """)
            print(f"""Congratulations, you have guessed the word with {lives} Lives left.
            The letter was {self.word}.{Fore.YELLOW}\n""")
            return False
        elif self.lives == 0:
            self.drawing(0)
            print(Fore.MAGENTA + """
               __   ____  ________
              / /  / __ \/ __/ __/
             / /__/ /_/ /\ \/ _/  
            /____/\____/___/___/  
            """)
            print(f'You lose!, the word was {self.word}{Fore.YELLOW}\n')
            return False
        
    def restart_game(self):
        """
        Asks if player wants to continue and allows restart if so
        """
        restart = input(f'do you want to play again: Y/N?\n').lower()
        if restart == 'n':
            print('Session ending - thanks for playing :)')
            game_start()
        elif restart == 'y':
            print("Restarting game...\n")
            main()
        else:
            print(f"{Back.RED}You need to type Y or N.{Back.RESET}\n")
            self.restart_game()

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
        play.drawing(lives)
        guess = input("Guess a letter: ")

        if play.is_valid_guess(guess) == True:
            letters = play.store_guesses(guess.lower())
            play.is_guess_in_word(guess.lower())
            if play.check_win(lives) == False:
                play.restart_game()
            
            play.update_letters()
game_start()