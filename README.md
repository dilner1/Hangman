# Hangman

# Features

# Features

## Features Left to Implement

# Testing

## Validator Testing

## Implementation

Implementation: What I am implementing

Test: How I tested it

Result: What happened

Verdict: did it work?

## bugs
Problem: When guessing a letter lives would be taken off depending on number of letters in word. This would happen even if one letter was guessed correctly.
Cause: Was checking each letter in word if it matched with the guess using 'for letter in word: if guess == letter:'
Resolution: Change function to check if guess was in word rather than checked every letter

Problem: Lives would reach zero but still allow user to play
Cause: Code written to catch zero lives would only come into effect after -1 lives had already occured
Resolution: Moved break on zero lives after lives = play.lives inside main() function

Problem: Letters would show in the order they were guesses when correct, not their actual place in the word
Cause: Did not have index for hidden word values
Resolution: used range() and len() to find index

Problem: Letters would show in the order they were guesses when correct, not their actual place in the word
Cause: f"{joined_word}\n" believe the \n
Resolution: removed formating and \n

Problem: Sometimes extra '_' appears on the hidden word
Cause: If there is _ left at the end of a game they are added onto the next game's word
Resolution: Problem only occured when providing a fixed word to guess, which I did in testing, when I changed this to randome each time as it should be the problem dissapeared

Problem: try / except error handling not catching incorrect values
Cause:
Resolution:

How I tested how user can break game - give user feedback that tells them what to do

Test with users see what they thought of it



## Unfixed Bugs

# Deployment

if you want to play this locally:
Cloning project and run locally

copy clone link, go to terminal or commanand line of choice, have git installed and copy URL

when project runs 

no need for pip install

python3 run.py

Deploy to Herokou:


# Credits

## Content

## Media