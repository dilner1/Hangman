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
        self.secret = ["_" for letter in self.word]
        self.lives = 8
        self.hangman = hangman
        self.guesses = []

        print("Game starting...\n")

    def show_word(self):
        """
        Fetch word and show on screen
        """

        joined_word = " ".join(self.secret)
        print(f"{joined_word}\n")
        
        print(f'You have {self.lives} lives remaining.')

    def drawing(self, lives):
        """
        Prints takes the players lives and prints out connected picture
        """
        print(hangman[lives])

    def store_guesses(self, guess):
        """
        Takes guessed letter and stores it
        """
        guessed_words = self.guesses
        guessed_words.append(guess)

        print(f"so far you have guessed{guessed_words}")

    def is_valid_guess(guess):
        """
        Checks if guess is a valid
        """

    def is_guess_in_word(self, guess, word):
        """
        Checks if guess matches a letter in the hidden word
        """
        for letter in word:
            if guess == letter:
                print("yes")
            else:
                self.lives -= 1
                print("Incorrect, you lost a life\n")

    def check_win(self, word, guesses):
        if self.guesses == word:
            print("You win!")
            return True

def main():
    """
    Prints all functions
    """
    play = game()
    word = play.word
    print("A word has been selected.\n")

    guesses = play.guesses
    while True:
        play.show_word()
        lives = play.lives
        play.drawing(lives)
        guess = input("Guess a letter: ")
        play.store_guesses(guess)
        # play.is_valid_guess(guess)
        # if play.is_valid_guess(guess) == True:
        #     play.is_guess_in_word(guess, word)
        play.is_guess_in_word(guess, word)

        if play.check_win(word, guesses):
            break
    
print(logo)
main()