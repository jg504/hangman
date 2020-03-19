from random import randint

def selectWord():
    words = ['Hello', 'How', 'Are', 'You', 'Simple', 'Words', 'Nothing', 'Fancy']
    return words[randint(0, 7)]

def checkGuess(guess, characters, display):
    correctGuess = 0

    for i in range(len(characters)):
        if(characters[i] == guess):
            display[i] = guess
            correctGuess = 1
    
    if(correctGuess):
        return 0
    
    else:
        return 1

def guessInput(display):
    while(True):
        guess = input("Enter a single character as your guess: ").lower()

        alreadyGuessed = 0

        if(guess.isdigit()):
            print("\nThe guess cannot be a digit. Try again.\n\n")
            continue

        elif(len(guess) == 1):
            for i in range(len(display)):
                if(display[i] == guess):
                    print("\nYou have already guessed this character. Try again.")
                    alreadyGuessed = 1
            
            if(alreadyGuessed):
                continue
            
            return guess
        
        else:
            print("\nGuess cannot be multiple characters. Try again.\n")

def joinList(display):
    str = ""
    return(str.join(display))


def guessesLeftInput():
    while(True):
        temp = input("\nSet the number of incorrect guesses allowed: ")

        if(temp.isdigit()):
            return int(temp)
        
        else:
            print("\nIt has to be an integer. Try again.")

def checkFinished(display):
    temp = 1

    for i in range(len(display)):
        if(display[i] == "*"):
            temp = 0
    
    if(temp):
        return 1
    
    else:
        return 0

# __main__
while(True):
    choice = input("\nInput Yes to guess a word. Input No to exit. ").lower()
    
    if(choice == "yes"):

        print("\nYou have chosen to guess a new word.")

        actualWord = selectWord().lower()

        characters = list(actualWord)
        
        display = ['*']*len(characters)

        guessesLeft = guessesLeftInput()

        guessed = joinList(display)
        print("\nThe word is " + guessed + "\nNumber of incorrect guesses left are: " + str(guessesLeft) + "\n")

        guess = guessInput(display)
        while(guessesLeft > 0):
            incorrectGuess = checkGuess(guess, characters, display)
            
            if(incorrectGuess):
                guessesLeft -= 1
            
            guessed = joinList(display)

            finished = checkFinished(display)

            if(finished):
                print("\nCongratulations! You guessed the word. The word is " + guessed)
                break

            elif((guessesLeft == 0)):
                print("\nGuesses elapsed. Better luck next time!")

            else:
                print("\nThe word is " + guessed + "\nNumber of incorrect guesses left are: " + str(guessesLeft) + "\n")
                guess = guessInput(display)
    
    elif(choice == "no"):
        print("\nThank you for playing.\n")
        break

    else:
        print("\nInvalid choice. Try again.")