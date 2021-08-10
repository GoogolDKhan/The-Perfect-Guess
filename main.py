import random
randNum = random.randint(1, 100)
guesses = 0
userGuess = None
while(userGuess != randNum):
    userGuess = int(input("Enter your guess between 1-100: "))
    guesses += 1
    if (userGuess == randNum):
        print("You guessed it right!")
    else:
        if(userGuess > randNum):
            print("You guessed it wrong! Enter a smaller number.")
        elif(userGuess < randNum):
            print("You guessed it wrong! Enter a larger number.")

print(f"You guessed the number in {guesses} guesses.")
