#
# Problem 19 - Counting Sundays.
#
# Knowing that 1 January 1900 was a Monday, how many Sundays fell on the first
# day of the month between 1 January 1901 and 31 December 2000?
#

MONTHS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    """Determine if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def day_number(day, month, year):
    """Calculate the day number relative to 1 January 1900 (which is day 1)"""
    leap_years = sum(1 if is_leap_year(y) else 0 for y in range(1900, year))
    if is_leap_year(year) and month > 2:
        leap_years += 1

    return sum(MONTHS) * (year - 1900) + sum(MONTHS[:month - 1]) + day


def is_sunday(day, month, year):
    """Determine if a particular date is a Sunday."""
    return day_number(day, month, year) % 7 == 0


def main():
    # I'm going to do this without using the datetime module because other
    # languages do not have such a convenience.

    count = 0  # The count of Sundays.

    # Start on 1 January 1901.
    day = 1
    month = 1
    year = 1901

    # Locate the first Sunday.
    for n in range(7):
        if is_sunday(day + n, month, year):
            day = day + n
            break

    # From the first Sunday, increment the date by 1 week at a time and count
    # how often the first of each month occurs.
    while year < 2001:
        if day == 1:
            count += 1

        if day + 7 > MONTHS[month]:
            day = (day + 7) % MONTHS[month]

            if month + 1 > len(MONTHS) - 1:
                month = 1
                year += 1
            else:
                month += 1
        else:
            day += 7

    print(count)


if __name__ == "__main__":
    main()
