# randint function of the random library shall be used to select a random word from a list of words.
from random import randint

# Function to choose a random word.
def selectWord():

    # New words can be added without disturbing the code.
    words = ['Hello', 'How', 'Are', 'You', 'Simple', 'Words', 'Nothing', 'Fancy']
    return words[randint(0, len(words) - 1)]

# Function to check the player's guess.
def checkGuess(guess, characters, display):
    
    # correctGuess will be used to determine whether to decrement guessesLeft.
    correctGuess = 0

    # Check whether the guessed character is in the word.
    for i in range(len(characters)):
        if(characters[i] == guess):
            display[i] = guess
            correctGuess = 1
    
    # guessesLeft shall not be decremented.
    if(correctGuess):
        return 0
    
    # guessesLeft shall be decremented.
    else:
        return 1

# Function used to take the player's guess as input.
def guessInput(display):

    # The while loop shall make sure that the player inputs a valid guess.
    while(True):

        # guess will store the guess in lowercase form as the game is not case sensitive.
        guess = input("Enter a single character as your guess: ").lower()

        # alreadyGuessed will be used to check whether the character has already been guessed.
        alreadyGuessed = 0

        # The guess cannot be a digit.
        if(guess.isdigit()):
            print("\nThe guess cannot be a digit. Try again.\n\n")
            continue

        # Checks whether the guess is a single alphabet.
        elif(len(guess) == 1):

            # The loop shall check if the player has already guessed the character.
            for i in range(len(display)):
                if(display[i] == guess):
                    print("\nYou have already guessed this character. Try again.")
                    alreadyGuessed = 1
            
            # The flow of control is transferred back to the while so that a valid input can be obtained.
            if(alreadyGuessed):
                continue
            
            # The valid input is returned.
            return guess
        
        # The guess has to be a single character.
        else:
            print("\nGuess has to be a single character. Try again.\n")

# Function to convert a list of characters into a string.
def joinList(display):
    str = ""
    return(str.join(display))

# Function to set the number of incorrect guesses allowed.
def guessesLeftInput():

    # The loop shall make sure that an integer is inputted by the player.
    while(True):
        temp = input("\nSet the number of incorrect guesses allowed: ")

        # Checks whether an integer is received from the player.
        if(temp.isdigit()):
            return int(temp)
        
        # The loop shall continue.
        else:
            print("\nIt has to be an integer. Try again.")

# Function to check whether the entire word has been guessed correctly.
def checkFinished(display):
    temp = 1

    # The loop shall check whether the entire word has been guessed correctly.
    for i in range(len(display)):
        if(display[i] == "*"):
            temp = 0
    
    # The entire word has been guessed.
    if(temp):
        return 1
    
    # The entire word has not been guessed yet.
    else:
        return 0

# __main__
while(True):

    # choice shall determine whether the player wants to play the game.
    choice = input("\nInput Yes to guess a word. Input No to exit. ").lower()
    
    # Checks whether the player wants to continue.
    if(choice == "yes"):

        print("\nYou have chosen to guess a new word.")

        # actualWord shall store the randomly selected word to be guessed.
        actualWord = selectWord().lower()

        # characters shall store the characters of randomly selected word to be guessed.
        characters = list(actualWord)
        
        # display shall store the characters that have been guessed in the form of a list.
        # The characters that are yet to be guessed shall be stored as '*'.
        display = ['*']*len(characters)

        # guessesLeft shall store the number of incorrect guesses left.
        guessesLeft = guessesLeftInput()

        # guessed shall store the guessed characters as a string to be displayed for the player.
        guessed = joinList(display)
        print("\nThe word is " + guessed + "\nNumber of incorrect guesses left are: " + str(guessesLeft) + "\n")

        # guess shall store the player's guess.
        guess = guessInput(display)

        # The while loop shall run till either the guesses are finished or the word has been guessed correctly.
        while(guessesLeft > 0):

            # incorrectGuess shall be used to decrement the number of incorrect guesses left.
            incorrectGuess = checkGuess(guess, characters, display)
            
            # Checks whether the player's guess was incorrect.
            # If it was then decrements guessesLeft.
            if(incorrectGuess):
                guessesLeft -= 1
            
            # guessed shall store the guessed characters as a string to be displayed for the player.
            guessed = joinList(display)

            # finished shall check whether the entire word has been guessed correctly.
            finished = checkFinished(display)

            # If the player has guessed the entire word correctly then (s)he wins.
            if(finished):
                print("\nCongratulations! You guessed the word. The word is " + guessed)
                break

            # If the player has elapsed the number of incorrect guesses allowed then (s)he loses.
            elif((guessesLeft == 0)):
                print("\nGuesses elapsed. Better luck next time!")

            # If guesses are still left and the word is yet to be correctly guessed then the flow of control is transferred back to the while loop.
            else:
                print("\nThe word is " + guessed + "\nNumber of incorrect guesses left are: " + str(guessesLeft) + "\n")
                guess = guessInput(display)
    
    # Checks whether the player wants to quit.
    elif(choice == "no"):
        print("\nThank you for playing.\n")
        break
    
    # Invalid choice.
    else:
        print("\nInvalid choice. Try again.")