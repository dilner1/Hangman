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
        self.guess = 9
        self.hangman = hangman

    def show_word(self):
        """
        Test that word is fetched
        """
        print(word)
        joined_word = "".join(self.secret)
        print(joined_word)


def main():
    """
    Prints all functions
    """
    game()
    game().show_word()
    
print(logo)
main()