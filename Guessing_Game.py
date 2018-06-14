def reverse_guessing_game(n):
    print("Think of a number between 0 and "+str(n))
    input("Hit enter when you have it.")
    guesses = 0  # counter for the number of guesses
    possibleNumbers = list(range(n+1))  # list of possible numbers
    while True:
        # keep looping until guessed right
        # will return when a correct guess is made
        guesses += 1  # increment the number of guesses
        # guess the middle possible number
        guessIndex = len(possibleNumbers)//2 
        computerGuess = possibleNumbers[guessIndex]
        print("I guess "+str(computerGuess))
        response = ''
        while response not in ['high','low','correct']:
            response = input("Is this high, low, or correct? ")
        if response == 'high':
            possibleNumbers = possibleNumbers[:guessIndex]
        elif response == 'low':
            possibleNumbers = possibleNumbers[guessIndex+1:]
        else: # computer wins
            print("I knew it!")
            print("It took me "+str(guesses)+" guesses.")
            return guesses
        if len(possibleNumbers) == 0:  # no 'possible' numbers left
            print("I think you lied to me!!!")
            return guesses

# play the game
guesses = reverse_guessing_game(100)