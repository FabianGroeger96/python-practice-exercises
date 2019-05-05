def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print('list: {}'.format(a))

    for number in a:
        if number < 5:
            print('{} is less than 5'.format(number))

    list_less = []
    for number in a:
        if number < 5:
            list_less.append(number)

    print('list of numbers less than 5: {}'.format(list_less))

    print('one line of code: {}'.format([number for number in a if number < 5]))

    input_number = int(input('please enter a number to display numbers smaller than it: '))
    print('numbers smaller than {}: {}'.format(input_number, [number for number in a if number < input_number]))


if __name__ == "__main__":
    main()
