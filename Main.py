import random
def main():

    # Select a random number 1-10 and store random number into a variable
    random_number = random.randint(1, 10)

    # Give user initial number of attempts:
    attempts = 3

    while attempts != 0:
        # Ask user to guess a number
        guess = int(input("Please enter a number between 1-10: "))

        # Compare user's guess with the random number
        # Determine if guess is above or below random number
        # If guess is above random number, tell user to guess was above and try again
        # Remove 1 attempt from their total attempts
        if guess > random_number:
            attempts -= 1
            print(f"Your guess is above, you have {attempts} left")

        # If guess is below random number, tell them guess was below and try again
        # Remove 1 attempt from their total attempts
        elif guess < random_number:
            attempts -= 1
            print(f"Your guess is below, you have {attempts} left")

        # If guess is correct, tell user guess is correct, they win, end the game
        else:
            print("You guess was correct! You have won!")
            break

        # If attempt reaches 0, user has lost and program exits
        if attempts == 0:
            print("Game over! You have lost")


if __name__ == "__main__":
    main()
