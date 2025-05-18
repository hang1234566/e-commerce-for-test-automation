# my_new_script.py

import datetime

def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width

def greet_user(name):
    """Returns a greeting message."""
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"Hello, {name}! Current time is {current_time}."

if __name__ == "__main__":
    print("Starting my new Python script...")

    # Example 1: Calculate rectangle area
    side1 = 10
    side2 = 5
    area = calculate_area(side1, side2)
    print(f"The area of a rectangle with sides {side1} and {side2} is: {area}")

    # Example 2: Greet a user
    user_name = "Gemini AI"
    greeting = greet_user(user_name)
    print(greeting)

    print("Script finished.")