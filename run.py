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
        self.word = "yes"
        #word
        self.secret = list(len(word)*'_')
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
            print('You lose, loser!')
            break
        play.drawing(lives)
        guess = input("Guess a letter:")
        play.store_guesses(guess.lower())

        play.is_guess_in_word(guess, word)
    
print(logo)
main()