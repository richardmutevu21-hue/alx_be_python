def main():
    try:
        size = int(input("Enter the size of the pattern: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if size <= 0:
        print("Please enter a positive integer.")
        return

    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()  # newline after finishing the row
        row += 1

if __name__ == "__main__":
    main()