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

        print("Game starting.\n")

    def show_word(self):
        """
        Test that word is fetched
        """
        joined_word = "".join(self.secret)
        print(f"{joined_word}\n")
        
        print(f'You have {self.lives} chances remaining.')

    def drawing(self, lives):
        """
        Prints takes the players lives and prints out connected picture
        """
        print(hangman[lives])

    def store_guesses(self, guess):
        guesses.append(guess)

def main():
    """
    Prints all functions
    """
    play = game()

    play.show_word()
    lives = play.lives
    play.drawing(lives)
    
print(logo)
main()