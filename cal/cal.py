import calendar
from datetime import datetime
import argparse


def month_to_number(month):
    """Convert month name or number to month number."""
    # English month names from calendar
    month_names_english = {m.lower(): i for i, m in enumerate(calendar.month_name) if m}
    # Portuguese month names mapping
    month_names_portuguese = {
        "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4,
        "maio": 5, "junho": 6, "julho": 7, "agosto": 8,
        "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12
    }

    try:
        # Try converting month using English names
        return int(month)
    except ValueError:
        # Handle month name in English or Portuguese
        month = month.lower()
        if month in month_names_english:
            return month_names_english[month]
        elif month in month_names_portuguese:
            return month_names_portuguese[month]
        else:
            raise KeyError("Invalid month name. Please specify a valid month name in English or Portuguese.")


def highlight_day(text, day):
    """Highlight the specific day in the calendar text with a background color."""
    day_str = f"{day:2}"
    return text.replace(day_str, f"\033[47;41m{day_str}\033[0m", 1)


def display_calendar(year, month=None):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    today = datetime.now()

    if month:
        calendar_output = cal.formatmonth(year, month)
        if month == today.month and year == today.year:
            calendar_output = highlight_day(calendar_output, today.day)
        print(calendar_output)
    else:
        calendar_output = cal.formatyear(year)
        print(calendar_output)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Display a calendar for a specific month and year, or the entire year, similar to Unix's cal command")
    parser.add_argument("-y", "--year", type=int, help="The year to display the calendar for")
    parser.add_argument("-m", "--month", help="The month to display the calendar for")

    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    # Use the current year and month if none are provided
    current_date = datetime.now()
    year = args.year if args.year is not None else current_date.year
    month = None
    if args.month:
        try:
            month = month_to_number(args.month)
        except KeyError as e:
            print(e)
            return
    elif args.year and not args.month:
        # If only year is provided, display the entire year
        display_calendar(year)
        return
    else:
        # Default to current month and year if nothing is provided
        month = current_date.month

    display_calendar(year, month)


if __name__ == "__main__":
    main()
