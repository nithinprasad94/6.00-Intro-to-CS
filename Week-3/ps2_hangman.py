# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

#My Helper Functions
def letterInWord(user_word,letter,goal_word):
    if (letter in goal_word):
        while (goal_word.rfind(letter) != -1):
            index = goal_word.rfind(letter)
            goal_word = goal_word[:index] + '#' + goal_word[index+1:]
            user_word = user_word[:index] + letter + user_word[index+1:]
    return user_word  

def updateAvailableLetters(char_string,letter):
    index = char_string.rfind(letter)
    return char_string[:index] + char_string[index+1:]

# your code begins here!
def hangman():

    #Print intro statement
    print "Welcome to the game, Hangman!"
    
    # actually load the dictionary of words and point to it with 
    # the wordlist variable so that it can be accessed from anywhere
    # in the program
    wordlist = load_words()

    #Obtain random word
    goal_word = choose_word(wordlist)
    goal_word_len = len(goal_word)

    #Determine number of guesses that user gets
    guesses_rem = 13

    #Initialize the user's word to all underscores
    user_word = "_"*goal_word_len
    guessed_correct = False #used to exit loop if user guesses correctly
    avail_letters = string.ascii_lowercase

    #Tell user how many letters you are thinking of ...
    print "I am thinking of a word that is",goal_word_len,"letters long."

    #Create a while loop to iterate through each guess
    while ((guesses_rem > 0) and (guessed_correct == False)):

        print "-"*13 #partitions guess cycle
        print "You have",guesses_rem,"guesses left."
        print "Available letters:",avail_letters
        letter = raw_input("Please guess a letter: ")

        #Determine if letter is in word and get new word
        word_before_guess = user_word
        #print word_before_guess
        user_word = letterInWord(user_word,letter,goal_word)
        #print user_word
        
        #Print appropriate message if word hasn't improved/has improved
        if (user_word == word_before_guess):
            print "Oops! That letter is not in my word:",user_word
        else:
            print "Good guess:",user_word

        #Update available letters
        avail_letters = updateAvailableLetters(avail_letters,letter)

        #Check if word = correct word
        if (user_word == goal_word):
            guessed_correct = True

        #Decrement number of guesses by 1        
        guesses_rem -= 1

    #Print win/loss
    if (guessed_correct == True):
        print "Congratulations, you won!"
    else:
        print "The word was",goal_word,"\nBetter luck next time!"

#Call Function
hangman()

    
    



