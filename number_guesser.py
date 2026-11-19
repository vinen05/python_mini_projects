import random

top_of_range = input("Type a number: ")
guess_limit = input("Type a guess limit number:")

if guess_limit.isdigit():
    guess_limit = int(guess_limit)
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print("Sorry, the number is less than or equal to zero.")
            quit()
    else:
        print("Sorry, the number is less than or equal to zero.")
        quit()

    random_number = random.randint(0, top_of_range)
    print(random_number)
    guesses = 0

    while True:
        guesses += 1
        user_guess = input("Guess a number: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Sorry, the number is less than zero.")
            continue

        if user_guess == random_number:
            print("Correct!")
            break
        elif user_guess > random_number:
            print("The random number is less than", user_guess)
        elif user_guess < random_number:
            print("The random number is greater than",user_guess)
        else:
            print("The random number is less than", user_guess)

        if guesses == guess_limit:
            print("Sorry, Your guessing limit is done.\nTry Again Next Time!")
            quit()

    print("You got it in", guesses, "guesses!")
else:
    print("Sorry, the number is less than or equal to zero.")
    quit()

