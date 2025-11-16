def main():
    try:
        number = int(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Please enter a whole number (integer).")
        return

    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    main()