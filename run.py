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

class game():
    def __init__(self):
        """
        Define variables for class
        """
        self.word = word
        self.secret = list(len(word)*'_')
        self.lives = 8
        self.hangman = hangman
        self.guesses = []

        print("Game starting...\n")

    def show_word(self):
        """
        Takes selected word to be hidden and replaces letters
        """

        joined_word = " ".join(self.secret)
        print(joined_word)
        print(word)
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
        guessed_words = self.guesses
        word = self.word
        if guess not in word.lower():
            guessed_words.append(guess)
            incorrect_guesses_list = " ".join(guessed_words)
            return incorrect_guesses_list
        else:
            incorrect_guesses_list = " ".join(guessed_words)
            return incorrect_guesses_list

    def is_valid_guess(self, guess):
        """
        Checks if guess is a valid
        """

        letter_guess = guess.lower()
        if letter_guess.isalpha() == False:
            print(f"{guess} is not a letter. You must type a letter.")
            return False

        elif letter_guess in self.guesses or letter_guess in self.secret:
            print(f'You have already tried letter {letter_guess}, please try another letter')
            return False

        elif len(letter_guess) >= 2:
            length = len(letter_guess)
            print(f'Your tried to guess {length} letters. You can only type one at a time.')
            return False
        
        elif letter_guess.isalpha():
            return True

    def is_guess_in_word(self, guess, word):
        """
        Checks if guess matches a letter in the hidden word, finds the index and reveals letter in secret word
        """
        if guess.lower() not in word.lower():
            self.lives -= 1
            print("Incorrect, you lost a life.\n")
        else:
            print("You guessed a letter correctly.\n")
            for i in range(0, len(word)):
                    letter = word[i]
                    if letter == guess:
                        self.secret[i] = guess
                        
        print("")
    def check_win(self, word, lives):
        if "_" not in self.secret:
            print(f"Congratulations, you have guessed the word with {lives} lives left.\nThe letter was {word}")
            return False
    
    def restart_game(self):
        restart = input('do you want to play again: Y/N?')
        if restart == 'N':
            return False
        elif restart == 'Y':
            main()


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
            play.is_guess_in_word(guess.lower(), word)
            if play.check_win(word, lives) == False:
                if play.restart_game() == False:
                    break
            print(f"so far you have guessed: {letters}\n")
        
print(logo)
main()