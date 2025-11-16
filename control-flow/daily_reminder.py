def main():
    task = input("Enter your task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return

    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            base = f"Reminder: '{task}' is a high priority task"
        case "medium":
            base = f"Reminder: '{task}' is a medium priority task"
        case "low":
            base = f"Note: '{task}' is a low priority task"
        case _:
            base = f"Reminder: '{task}' has an unspecified priority"

    if time_bound == "yes":
        # for high/medium/low we want the immediate-attention wording
        print(f"{base} that requires immediate attention today!")
    elif time_bound == "no":
        if priority == "low":
            print(f"{base}. Consider completing it when you have free time.")
        else:
            print(f"{base}. Schedule it for today or soon based on your availability.")
    else:
        print(f"{base}. (Time-bound response unclear — please answer yes or no next time.)")

if __name__ == "__main__":
    main()