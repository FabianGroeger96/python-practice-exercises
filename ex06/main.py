def main():
    word = str(input('Enter a word to check if its a palindrome: '))

    word_reverse = word[::-1]
    print('Reverse word: {}'.format(word_reverse))

    if word == word_reverse:
        print('{} is a palindrome'.format(word))
    else:
        print('{} is not a palindrome'.format(word))


def check_palindrome(word):
    # one line of code
    return word[::] == word[::-1]


if __name__ == "__main__":
    main()
