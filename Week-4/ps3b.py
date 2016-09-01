from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#

#Naive Greedy Algorithm - returns the first 'longest' word
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """

    n = HAND_SIZE
    perms = [] #Full list of permutations

    for i in range(1,n+1):
        sub_list = get_perms(hand,i)
        perms += sub_list

    #Go in reverse order and stop at the first good word
    perms.reverse()
    for perm in perms:
        if perm in word_list:
            return perm

    return None #Returned if no words found using given hand

#Smarter Greedy Algorithm - returns the best of the 'longest' words
def comp_choose_word_v2(hand,word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """

    k = HAND_SIZE

    return comp_recursive_choose_word(hand,k,word_list)
    

def comp_recursive_choose_word(hand,k,word_list):

    #Here, k represents the k letter permutations of the hand, starting with k = HAND_SIZE
    
    hand_len = calculate_handlen(hand)
    
    perms = get_perms(hand,k)
    
    best_word = ""
    best_word_score = 0

    for perm in perms:
        if perm in word_list:
            #print perm
            if get_word_score(perm,hand_len) > best_word_score:
                best_word = perm
                best_word_score = get_word_score(perm,hand_len)

    #Base Case: we're done if ...
    if (k == 1 or best_word_score > 0):
        if best_word == "":
            return None
        else:
            #print "there was a best word"
            return best_word
        
    #We want to choose the next largest word with highest possible weight
    else:
        return comp_recursive_choose_word(hand,k-1,word_list)

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_choose_word returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """

    hand_len = calculate_handlen(hand)
    word = ""
    total_score = 0

    while (hand_len > 0 and word != None):

        valid_word = False

        display_hand(hand)
        
        #Let computer choose word (function only chooses valid words)
        word = comp_choose_word(hand,word_list)

        if (word != None):
            print "Word chosen: " + word
            hand = update_hand(hand,word)
            hand_len = calculate_handlen(hand)
        
            score = get_word_score(word,HAND_SIZE)
            total_score += score
            
            print '"' + word + '" earned ' + str(score) + ' points. Total: ' + str(total_score)
            print
        else:
            print "No word synthesizable!"
        
    print "Total score: " + str(total_score) + " points."
    print

    return total_score

def comp_play_hand_v2(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_choose_word returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """

    hand_len = calculate_handlen(hand)
    word = ""
    total_score = 0

    while (hand_len > 0 and word != None):

        valid_word = False

        display_hand(hand)
        
        #Let computer choose word (function only chooses valid words)
        word = comp_choose_word_v2(hand,word_list)

        if (word != None):
            print "Word chosen: " + word
            hand = update_hand(hand,word)
            hand_len = calculate_handlen(hand)
        
            score = get_word_score(word,HAND_SIZE)
            total_score += score
            
            print '"' + word + '" earned ' + str(score) + ' points. Total: ' + str(total_score)
            print
        else:
            print "No word synthesizable!"
        
    print "Total score: " + str(total_score) + " points."
    print

    return total_score
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """

    done = False
    hand = {}

    while(not(done)):

        valid_choice = False
        choice = ""

        #Handle hand choice/game continuity
        
        #First time through, no choice for repeating previous hand
        if (hand == {}):
                
            while(not(valid_choice)):            

                choice = raw_input("Input an 'n' if you want to play a new hand,\n \
or an 'e' if you want to exit the game: ")

                valid_inputs = ['n','e']

                if (not(choice in valid_inputs)):
                    print "Invalid input. Please try again!"
                else:
                    valid_choice = True
                print

        #Otherwise, previous hand is an option
        else:
            
            while(not(valid_choice)):            

                choice = raw_input("Input an 'n' if a new hand should be dealt,\n \
an 'r' if the previous hand should be used, \n \
or an 'e' if you want to exit the game: ")

                valid_inputs = ['n','r','e']

                if (not(choice in valid_inputs)):
                    print "Invalid input. Please try again!"
                else:
                    valid_choice = True
                print

        #Handle user/computer choice (only if choice was 'n' or 'r')
        choice_2 = ""
                
        if (choice == 'n' or choice == 'r'):
            
            valid_choice = False
                    
            while(not(valid_choice)):            

                choice_2 = raw_input("Input a 'u' if you want to play the hand,\n \
or a 'c' if you want the computer to play the hand: ")

                valid_inputs = ['u','c']

                if (not(choice_2 in valid_inputs)):
                    print "Invalid input. Please try again!"
                else:
                    valid_choice = True
                print
                   
        #Handle choice
        if (choice == 'n'):
            hand = deal_hand(HAND_SIZE)

            if (choice_2 == 'u'):
                play_hand(hand,word_list)

            else:
                comp_play_hand(hand,word_list)

        elif (choice == 'r'):
            if (choice_2 == 'u'):
                play_hand(hand,word_list)

            else:
                comp_play_hand(hand,word_list)

        else:
            print "Thanks for playing!"
            done = True 

def play_game_comp_v_comp(word_list):

    num_iterations = 8
    i = 1

    comp1 = comp_play_hand
    comp2 = comp_play_hand_v2

    comp1_wins = 0
    comp2_wins = 0
    comp1_2_ties = 0

    while (i <= num_iterations):
        print "ITERATION: ", i
        #Deal hand
        hand = deal_hand(HAND_SIZE)

        print "<COMPUTER 1>: "
        comp1_score = comp1(hand,word_list)
        print "<COMPUTER 2>: "
        comp2_score = comp2(hand,word_list)

        if comp1_score > comp2_score:
            comp1_wins += 1
        elif comp1_score < comp2_score:
            comp2_wins += 1
        else:
            comp1_2_ties += 1

        i += 1
            
    print "Total iterations: ",num_iterations
    print "Computer 1 wins: ",comp1_wins
    print "Computer 2 wins: ",comp2_wins
    print "Computer 1/2 ties: ",comp1_2_ties
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    #play_game_comp_v_comp(word_list)
    play_game(word_list)

    
