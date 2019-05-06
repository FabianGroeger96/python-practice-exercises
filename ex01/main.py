from datetime import datetime


def main():
    name = input('please enter your name: ')
    age = input('please enter your age: ')

    print('Hello {} with the age of {}'.format(name, age))

    age = int(age)
    year_turn_100 = int(datetime.today().year) + (100 - age)

    output_string = '{} will turn 100 in the year of {}'.format(name, year_turn_100)
    print(output_string)

    count_output = int(input('please enter how many time you`d like to see the message: '))

    print('{}\n'.format(output_string) * count_output)

    for i in range(0, count_output):
        print('count: {}, {}'.format((i+1), output_string))


if __name__ == "__main__":
    main()
