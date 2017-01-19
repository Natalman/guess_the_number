import random

correct = 'you guessed correctly!'

too_low = 'too low'
too_high = 'too high'




def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    while True:
        try:
            return int(input('Guess the secret number? '))

        except ValueError:
            print(" It has to be an integer")


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def max():
    while True:

        try:

            maxx = (input('Enter the max range number?'))
            maxx = int(maxx)

            if maxx <= 100:
                return maxx
            else:
                print('enter a number less the 100')

        except ValueError:
            print(" It has to be an integer")


def min(high):
    while True:

        try:

            minn = (input('Enter the min range number?'))
            minn = int(minn)

            if minn < high:
                return minn
            if minn <= 0:
                print('the min must not be less the 0')
            else:
                print('enter a number less the', high, '')

        except ValueError:
            print(" It has to be an integer")


def main():
    print('The range of the guessing game between 1- 100 ')

    high = max()
    low = min(high)
    secret = generate_secret(low, high)
    numberofguess = 0

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)
        numberofguess += 1

        if result == correct:
            print('you got it in ', numberofguess, 'Guesses')

            response = input("Do you want to play again? y for yes and anything else for no")

            if response == "y":
                return main()
            else:
                break


if __name__ == '__main__':
    main()
