def main():
    number = int(input('please enter a number: '))

    if number % 4 == 0:
        print('{} is multiple of 4'.format(number))
    elif number % 2 == 0:
        print('{} is even'.format(number))
    else:
        print('{} is odd'.format(number))

    num = int(input('please enter a number to check: '))
    check = int(input('please enter a number to divide by: '))

    if num % check == 0:
        print('{} divides evenly by {}'.format(num, check))
    else:
        print('{} does not divide evenly by {}'.format(num, check))


if __name__ == "__main__":
    main()
