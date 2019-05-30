import random


def main():
    number = random.randint(1, 9)
    guess_count = 0

    while True:
        guess = input('Guess a number between 1 and 9: ')

        if guess == 'exit':
            print('Goodbye')
            break

        guess = int(guess)
        guess_count += 1

        if guess < number:
            print('Guess was to low')
        elif guess > number:
            print('Guess was to high')
        elif guess is number:
            print('Guess was correct, after {} guesses'.format(guess_count))
            break


if __name__ == "__main__":
    main()
