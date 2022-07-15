import random


def again():
    question = input("Would you like to play again? Yes, or No?: ")
    if question.lower() == "yes":
        play()
    elif question.lower() == "no":
        print("Thanks for playing!")
    else:
        print('Incorrect response. Type "Yes or "No"')
        again()


def get_num(prompt):
    while True:
        answer = input(prompt)
        try:
            return float(answer)
        except ValueError:
            print(answer + " is not a number")


def play():
    magic_number = random.randint(1, 19) * 5
    guesses_left = 5
    no_guesses_left = False
    win = False
    print("The magic number is no more than 2 digits and a multiple of 5.")
    guess = get_num("Guesses Left: " + str(guesses_left) + " Guess a number: ")
    guesses_left -= 1
    if guess == magic_number:
        print("Way to go! You Win!")
        win = True
    elif guess > magic_number:
        print("Too high! Guess Lower!")
    else:
        print("Too low! Guess Higher!")
    while not no_guesses_left and not win:
        guess = get_num("Guesses Left: " + str(guesses_left) + " Wrong. Guess another number: ")
        guesses_left -= 1
        if guess == magic_number:
            print("Way to go! You Win!")
            win = True
        elif guess > magic_number:
            print("Too high! Guess Lower!")
        elif guess < magic_number:
            print("Too low! Guess Higher!")
        if win:
            again()
        if guesses_left < 0:
            no_guesses_left = True
    if no_guesses_left:
        print("You have no more guesses. You Lose.")
        again()


play()
