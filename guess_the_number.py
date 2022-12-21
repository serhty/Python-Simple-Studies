# We will keep a number between 1 and 100. The user has 7 guesses, each guess we will tell whether the number is up or down. if he wins we will print "congratulations", if he loses we will ask him if he wants to play again.

from random import randint
gameState = True
while gameState:
    randomNumber = randint(1,100)
    guessRight = 7
    while True:
        if guessRight > 0:
            guess = int(input("Guess a number between 1 and 100: "))
        else:
            print("You couldn't guess the number, the number = {} ".format(randomNumber))
            break
        
        if guess != randomNumber:
            guessRight -= 1
            if guess > randomNumber:
                print("Number smaller, remaining guess {} ".format(guessRight))
            elif guess < randomNumber:
                print("The larger the number, the remaining your guess {} ".format(guessRight))
        else:
            print("Congratulations. You found the number.")
    
    control = input("Do you want to continue? Enter 'Y' to continue, 'N' to exit.")
    if control == "Y":
        gameState = True
    else:
        gameState = False