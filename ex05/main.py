import numpy as np


def main():
    a_arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # set, doesn't contain duplicates
    equal_set = set()

    for a in a_arr:
        for b in b_arr:
            if a == b:
                equal_set.add(a)

    print('a: {}'.format(a_arr))
    print('b: {}'.format(b_arr))
    print('Equal numbers: {}'.format(equal_set))

    a_arr = np.random.randint(10, size=(np.random.randint(1, 10)))
    b_arr = np.random.randint(10, size=(np.random.randint(1, 10)))

    equal_set = set()

    for a in a_arr:
        for b in b_arr:
            if a == b:
                equal_set.add(a)

    print('a: {}'.format(a_arr))
    print('b: {}'.format(b_arr))
    print('Equal numbers: {}'.format(equal_set))

    equal_set = set(a_arr) & set(b_arr)
    print('Equal numbers (one line of code): {}'.format(equal_set))


if __name__ == "__main__":
    main()
