from datetime import datetime

def calculate_duration(start_date_str, end_date_str):
    """
    Calculates the duration between two dates given as strings.

    Args:
        start_date_str (str): The starting date and time string
                              (e.g., "5/22/25, 9:54:05 AM").
        end_date_str (str): The ending date and time string
                            (e.g., "5/22/25, 1:06:07 PM").

    Returns:
        str: A string representing the duration, or an error message if parsing fails.
    """
    # Define the format of the input date strings
    date_format = "%m/%d/%y, %I:%M:%S %p"

    try:
        # Convert the date strings to datetime objects
        start_date = datetime.strptime(start_date_str, date_format)
        end_date = datetime.strptime(end_date_str, date_format)

        # Ensure start_date is before or equal to end_date for a positive duration
        if start_date > end_date:
            start_date, end_date = end_date, start_date # Swap them if out of order

        # Calculate the difference between the two datetime objects
        duration = end_date - start_date

        # Extract components for a more readable output
        total_seconds = int(duration.total_seconds())
        days = duration.days
        hours = total_seconds // 3600 % 24
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        # Construct the result string
        result_parts = []
        if days > 0:
            result_parts.append(f"{days} day{'s' if days != 1 else ''}")
        if hours > 0:
            result_parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes > 0:
            result_parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
        if seconds > 0 or not result_parts: # Include seconds even if 0 if no other parts
            result_parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")

        return f"The duration is: {', '.join(result_parts)}"

    except ValueError as e:
        return f"Error parsing dates. Please ensure the format is 'MM/DD/YY, HH:MM:SS AM/PM'. Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# --- Interactive Usage ---
if __name__ == "__main__":
    print("Welcome to the Date Duration Calculator!")
    print("Please enter dates in the format: MM/DD/YY, HH:MM:SS AM/PM (e.g., 5/22/25, 9:54:05 AM)")

    while True:
        start_date_input = input("Enter the START date and time: ")
        end_date_input = input("Enter the END date and time: ")

        result = calculate_duration(start_date_input, end_date_input)
        print(result)

        another_calculation = input("\nDo you want to calculate another duration? (yes/no): ").lower()
        if another_calculation != 'yes':
            break

    print("Thank you for using the calculator!")
