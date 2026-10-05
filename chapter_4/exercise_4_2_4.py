"""Campus IL self.py — exercise 4.2.4."""

import calendar

def main():
    date = input("Enter a date: ")
    day, month, year = int(date[:2]), int(date[3:5]), int(date[6:])
    print(calendar.day_name[calendar.weekday(year, month, day)])


if __name__ == "__main__":
    main()
