import random
import hangman_art
import hangman_words
import os

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
print(hangman_art.logo)

end_of_game = False

display = []
for letter in range(word_length):
    display += "_"

guesses = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    guesses.append(guess)

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    os.system('clear')
    print(f"You've guessed {guesses}\n")
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"Sorry, {guess} isn't in the word")
        if lives == 0:
            print("You lose.")
            print(f"The word was: {chosen_word}")
            end_of_game = True

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hangman_art.stages[lives])
