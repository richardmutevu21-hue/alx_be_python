from datetime import datetime, timedelta

def display_current_datetime():
    """
    Gets the current date and time, stores it in current_date,
    and returns a formatted string "YYYY-MM-DD HH:MM:SS".
    """
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")
    return current_date  # return the datetime object if caller needs it

def calculate_future_date(days: int, from_date: datetime = None):
    """
    Calculates the date after adding `days` to from_date (or now if None).
    Saves it in future_date and returns a string "YYYY-MM-DD".
    """
    if from_date is None:
        from_date = datetime.now()
    future_date = from_date + timedelta(days=days)
    formatted = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted}")
    return future_date  # return datetime object (caller can format)

def main():
    display_current_datetime()
    while True:
        raw = input("Enter the number of days to add to the current date: ").strip()
        try:
            days = int(raw)
            future = calculate_future_date(days)
            # calculate_future_date already prints the result
            break
        except ValueError:
            print("Please enter a valid integer number of days.")

if __name__ == "__main__":
    main()