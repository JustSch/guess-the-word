import random
from pathlib import Path

lives = 9
GAME_WON = False

file_path = Path(__file__).with_name('word_list.txt')


list_file = open(file_path,'r')
word_list = list_file.read().splitlines()
list_file.close()


def run():
    ask_user()

def ask_user():
    answer = input('would you like to play guess the word? YES | NO ').upper()

    if answer == 'YES':
        choose_a_word()
    elif answer == 'NO':
        pass
    else:
        print('Please only write yes or no')
        run()
def still_have_lives():
    print('lives left: '+str(lives))
    return lives > 0 #fix this one

def choose_a_word():

    chosen_word = random.choice(word_list)
    letters_in_word = list(chosen_word)

    letters_guessed = []
    for i in range(0,len(letters_in_word)):
        letters_guessed.append('-')

    first_letter = random.choice(letters_in_word)
    reveal_letters(first_letter, letters_in_word, letters_guessed)

    while letters_guessed != letters_in_word:
        if still_have_lives(): #true if we still have lives
            choose_letters(letters_in_word,letters_guessed)
        else: 
             break 
    if (letters_guessed == letters_in_word):
        print('Congradulations You Have Correctly Guessed The Word: '+ chosen_word)
    else:
        print("You have lost. please try again")


    

def choose_letters(letters_in_word,letters_guessed):

    print(''.join(letters_guessed))

    letter = input('Please Guess A Letter: ')

    reveal_letters(letter, letters_in_word, letters_guessed)


def reveal_letters(letter_to_reveal, letters_in_word, letters_guessed):
    global lives
    if letter_to_reveal in letters_in_word:
        letter_location = 0
        while letter_location < len(letters_in_word):
            if letter_to_reveal == letters_in_word[letter_location]:
                letters_guessed[letter_location] = letters_in_word[letter_location]
            letter_location +=1
    else:
        lives -=1
        print('That letter was incorrect. Please try again!')



run()
