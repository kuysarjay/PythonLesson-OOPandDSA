# ==========================
# datetime Module
# ==========================
# The datetime module is used to work with dates and times.
# It allows you to:
# - Get the current date and time.
# - Create specific dates and times.
# - Format dates and times.
# - Perform date and time calculations.

# Common methods:
# datetime.now()      -> Returns the current date and time.
# datetime.today()    -> Returns today's date and time.
# strftime()          -> Formats a date/time into a readable string.
# strptime()          -> Converts a string into a datetime object.


# ==========================
# calendar Module
# ==========================
# The calendar module is used to display and manipulate calendars.
# It allows you to:
# - Display monthly and yearly calendars.
# - Check if a year is a leap year.
# - Find the weekday of a specific date.

# Common methods:
# calendar.month()     -> Displays a calendar for a specific month.
# calendar.calendar()  -> Displays a calendar for the entire year.
# calendar.isleap()    -> Checks if a year is a leap year.
# calendar.weekday()   -> Returns the weekday of a given date.

import calendar
from datetime import datetime

while True:
    print("\n======= CALENDAR APP =======")
    print("1. Show Current Date and Time")
    print("2. Show Calendar")
    print("3. Exit")
    print("============================")
    choice = input("\nEnter your choice: ")

    if choice == "1":
        now = datetime.now()

        print("\nCurrent Date and Time")
        print("Date:", now.strftime("%B %d, %Y"))
        print("Time:", now.strftime("%I:%M:%S %p"))

    elif choice == "2":
        try:
            year = int(input("Enter year: "))
            month = int(input("Enter month (1-12): "))

            if month < 1 or month > 12:
                print("Invalid month! Please enter a value from 1 to 12.")
            else:
                print("\n", calendar.month(year, month))

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    elif choice == "3":
        print("Thank you for using the Calendar App!")
        break

    else:
        print("Invalid choice! Please try again.")