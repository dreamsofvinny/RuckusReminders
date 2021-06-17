from datetime import date, time

def convert(my_name):
    """
    Print a line about converting a notebook.
    Args:
        my_name (str): person's name
    Returns:
        None
    """

    print(f"I'll convert a notebook for you some day, {my_name}.")


class Event:

    def __init__(self, date_string, time_string, desc):
        self.date = to_date(date_string)
        self.time = to_time(time_string)
        self.desc = desc


    def to_date(date_string):
    """
    Converts "MM/DD/YYYY" string into a date type
    Args:
        date_string (str): a string to convert
    Returns:
        the_date (date): the date for this event
    """
    month, day, year = date_string.split("/")
    the_date = date(int(year), int(month), int(day))
    return the_date

    def to_time(time_string):
    """
    Converts "23:59" string into a time type
    Args:
        time_string (str): a string to convert
    Returns:
        the_time (time): the time for this event
    """
        hour, minute = time_string.split(":")
        the_time = time(int(hour), int(minute))
        return the_time


def main():
    to_date("05/29/1997")

if __name__ == '__main__':
    main()