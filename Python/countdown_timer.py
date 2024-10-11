import time

def countdown_timer(duration):
    print(f"Countdown started for {duration} seconds.")

    for remaining_time in range(duration, 0, -1):
        print(f"Time remaining: {remaining_time} seconds")
        time.sleep(1)

    print("Countdown reached zero! Time's up!")

def get_duration():
    while True:
        try:
            duration = int(input("Enter the duration of the countdown in seconds: "))
            if duration > 0:
                return duration
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    # Get user input for the duration of the countdown
    duration_input = get_duration()

    # Run the countdown timer
    countdown_timer(duration_input)
