def main():
    input_number = int(input('enter a number to display all its divisors: '))

    list_divisors = []

    for i in range(1, input_number + 1):
        if input_number % i == 0:
            list_divisors.append(i)

    print('list of all divisors of {}: {}'.format(input_number, list_divisors))


if __name__ == "__main__":
    main()
