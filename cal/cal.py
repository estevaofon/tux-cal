import calendar
from datetime import datetime
import argparse

def month_to_number(month):
    """Convert month name or number to month number."""
    try:
        # If input is a month number, return it directly
        return int(month)
    except ValueError:
        # Convert month name to number using calendar module
        month_names = {m.lower(): i for i, m in enumerate(calendar.month_name) if m}
        return month_names[month.lower()]

def display_calendar(year, month=None):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar(calendar.SUNDAY)  # Week starts on Sunday

    if month:
        # Generate and print the calendar for the specified month and year
        calendar_output = cal.formatmonth(year, month)
        print(calendar_output)
    else:
        # Generate and print the calendar for the entire year
        calendar_output = cal.formatyear(year)
        print(calendar_output)

def parse_args():
    parser = argparse.ArgumentParser(description="Display a calendar for a specific month and year, or the entire year, similar to Unix's cal command")
    parser.add_argument("-y", "--year", type=int, help="The year to display the calendar for (default is current year)")
    parser.add_argument("-m", "--month", help="The month to display the calendar for; if no year is specified, assumes the current year")

    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    
    # Use the current year if no year is provided
    if args.year is None:
        args.year = datetime.now().year

    # Convert month name to number if necessary
    month_number = None
    if args.month:
        try:
            month_number = month_to_number(args.month)
        except KeyError:
            print("Error: Invalid month name. Please specify a valid month name or number.")
            return

    display_calendar(args.year, month_number)

if __name__ == "__main__":
    main()
