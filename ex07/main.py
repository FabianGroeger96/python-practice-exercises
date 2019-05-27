def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(a)
    b = [element for element in a if element % 2 == 0]
    print(b)


if __name__ == "__main__":
    main()
