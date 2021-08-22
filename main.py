import random


# Generate a random integer between 1 and 100
random_number = random.randint(1, 100)

# Initialize guess count and user guess
guess_count = 0
user_guess = None

# Determining the number of guesses user took to correctly guess the generated integer number
while(user_guess != random_number):
    user_guess = int(input("Enter your guess between the number 1-100: "))
    guess_count += 1
    if (user_guess == random_number):
        print("You guessed it right!")
    else:
        if(user_guess > random_number):
            print("You guessed it wrong! Enter a smaller number.")
        elif(user_guess < random_number):
            print("You guessed it wrong! Enter a larger number.")

# Showing the result to the user
print(f"You guessed the number in {guess_count} guesses.")
