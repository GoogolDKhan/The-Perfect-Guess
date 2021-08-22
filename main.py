import random


# Generate a random integer between 1 and 100
randNum = random.randint(1, 100)

# Initialize guess count and user guess
guesses = 0
userGuess = None

# Determining the number of guesses user took to correctly guess the generated integer number
while(userGuess != randNum):
    userGuess = int(input("Enter your guess between the number 1-100: "))
    guesses += 1
    if (userGuess == randNum):
        print("You guessed it right!")
    else:
        if(userGuess > randNum):
            print("You guessed it wrong! Enter a smaller number.")
        elif(userGuess < randNum):
            print("You guessed it wrong! Enter a larger number.")

# Showing the result to the user
print(f"You guessed the number in {guesses} guesses.")
